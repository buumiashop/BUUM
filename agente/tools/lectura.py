# -*- coding: utf-8 -*-
"""Herramientas v1 del agente BUUM — TODAS de solo lectura, validadas contra la allowlist."""
import os
import logging
from permissions.rutas import ruta_permitida, ALLOW, MAX_BYTES_LECTURA

log = logging.getLogger("buum.tools")

KB = "/opt/buum/KB"
LOG_AGENTE = "/var/log/buum/agente.log"

TOOLS = [
    {
        "name": "leer_kb",
        "description": (
            "Lee un documento de la Knowledge Base de BUUM (la fuente unica de verdad). "
            "Usala para consultar reglas, procesos, productos, decisiones y estado. "
            "Empieza siempre por ARRANQUE.md y ESTADO-ACTUAL.md si necesitas contexto general."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "ruta": {
                    "type": "string",
                    "description": "Ruta relativa dentro de la KB, p. ej. 'ARRANQUE.md' o '04-negocio/productos/reflector-solar/DOCUMENTO-MAESTRO.md'",
                }
            },
            "required": ["ruta"],
        },
    },
    {
        "name": "buscar_kb",
        "description": (
            "Busca un texto en toda la Knowledge Base y devuelve las coincidencias "
            "como 'archivo:linea: contenido'. Usala cuando no sepas en que documento esta algo."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "texto": {"type": "string", "description": "Texto a buscar (sin distincion de mayusculas)"}
            },
            "required": ["texto"],
        },
    },
    {
        "name": "leer_estado",
        "description": "Devuelve el estado actual de BUUM (KB/ESTADO-ACTUAL.md): punto exacto del proyecto, conexiones y pendientes.",
        "input_schema": {"type": "object", "properties": {}},
    },
    {
        "name": "leer_logs",
        "description": "Devuelve las ultimas lineas del log del propio agente (diagnostico).",
        "input_schema": {
            "type": "object",
            "properties": {
                "lineas": {"type": "integer", "description": "Cuantas lineas finales devolver (defecto 50, max 200)"}
            },
        },
    },
    {
        "name": "listar_proyecto",
        "description": (
            "Lista archivos y carpetas de las zonas permitidas del proyecto BUUM. "
            "Zonas: KB, agente, marketing, os, tienda, activos, datos y logs. "
            "Sin argumento, lista las zonas raiz disponibles."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "ruta": {"type": "string", "description": "Ruta absoluta dentro de las zonas permitidas, p. ej. '/opt/buum/KB/04-negocio'"}
            },
        },
    },
]

RECHAZO = (
    "RECHAZADO por politica de permisos: esa ruta esta fuera de las zonas de lectura "
    "permitidas del agente (v1 solo lectura). Los secretos y archivos del sistema nunca son accesibles."
)


def _leer_archivo(ruta_abs: str) -> str:
    if not ruta_permitida(ruta_abs):
        log.warning("permiso denegado: %s", ruta_abs)
        return RECHAZO
    if not os.path.isfile(ruta_abs):
        return f"No existe el archivo: {ruta_abs}"
    with open(ruta_abs, "r", encoding="utf-8", errors="replace") as f:
        contenido = f.read(MAX_BYTES_LECTURA)
    if os.path.getsize(ruta_abs) > MAX_BYTES_LECTURA:
        contenido += "\n[... archivo truncado por tamano ...]"
    return contenido


def _leer_kb(ruta: str) -> str:
    ruta = (ruta or "").lstrip("/").replace("..", "")
    return _leer_archivo(os.path.join(KB, ruta))


def _buscar_kb(texto: str) -> str:
    texto_l = (texto or "").lower()
    if len(texto_l) < 3:
        return "Texto de busqueda demasiado corto (minimo 3 caracteres)."
    hits = []
    for base, _dirs, files in os.walk(KB):
        for nombre in files:
            if not nombre.endswith((".md", ".txt", ".json")):
                continue
            ruta = os.path.join(base, nombre)
            if not ruta_permitida(ruta):
                continue
            try:
                with open(ruta, "r", encoding="utf-8", errors="replace") as f:
                    for num, linea in enumerate(f, 1):
                        if texto_l in linea.lower():
                            rel = os.path.relpath(ruta, KB)
                            hits.append(f"{rel}:{num}: {linea.strip()[:180]}")
                            if len(hits) >= 40:
                                return "\n".join(hits) + "\n[... mas resultados omitidos ...]"
            except OSError:
                continue
    return "\n".join(hits) if hits else f"Sin coincidencias para '{texto}' en la KB."


def _leer_estado() -> str:
    return _leer_archivo(os.path.join(KB, "ESTADO-ACTUAL.md"))


def _leer_logs(lineas) -> str:
    n = min(int(lineas or 50), 200)
    if not os.path.isfile(LOG_AGENTE):
        return "Aun no hay log del agente."
    with open(LOG_AGENTE, "r", encoding="utf-8", errors="replace") as f:
        return "".join(f.readlines()[-n:]) or "Log vacio."


def _listar(ruta) -> str:
    if not ruta:
        return "Zonas de lectura permitidas:\n" + "\n".join(ALLOW)
    if not ruta_permitida(ruta):
        return RECHAZO
    if not os.path.isdir(ruta):
        return f"No es una carpeta: {ruta}"
    filas = []
    for nombre in sorted(os.listdir(ruta)):
        completo = os.path.join(ruta, nombre)
        filas.append(("[dir]  " if os.path.isdir(completo) else "[arch] ") + nombre)
    return "\n".join(filas) if filas else "(carpeta vacia)"


def ejecutar_herramienta(nombre: str, entrada: dict) -> str:
    """Punto unico de ejecucion: valida permisos y despacha. Nunca lanza al bucle."""
    log.info("herramienta=%s entrada=%s", nombre, str(entrada)[:200])
    try:
        if nombre == "leer_kb":
            return _leer_kb(entrada.get("ruta", ""))
        if nombre == "buscar_kb":
            return _buscar_kb(entrada.get("texto", ""))
        if nombre == "leer_estado":
            return _leer_estado()
        if nombre == "leer_logs":
            return _leer_logs(entrada.get("lineas"))
        if nombre == "listar_proyecto":
            return _listar(entrada.get("ruta", ""))
        return f"Herramienta desconocida: {nombre}. En v1 no existen herramientas de escritura, shell ni publicacion."
    except Exception as e:  # noqa: BLE001 — el bucle debe seguir vivo
        log.error("error en herramienta %s: %s", nombre, e)
        return f"Error ejecutando {nombre}: {e}"
