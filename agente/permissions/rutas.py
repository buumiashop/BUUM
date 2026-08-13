# -*- coding: utf-8 -*-
"""Matriz de permisos de rutas del agente BUUM v1 (SOLO LECTURA).
   Las herramientas de archivos SOLO pueden leer dentro de ALLOW.
   Todo lo demas esta bloqueado — incluida /etc/buum (la API key jamas es accesible)."""
import os

ALLOW = [
    "/opt/buum/KB",
    "/opt/buum/agente",
    "/opt/buum/marketing",
    "/opt/buum/os",
    "/opt/buum/tienda",
    "/opt/buum/activos",
    "/var/lib/buum/data",
    "/var/log/buum",
]

# Bloqueos explicitos (defensa doble; la allowlist ya los excluye)
BLOCK = ["/etc", "/root", "/home", "/proc", "/sys", "/dev"]

MAX_BYTES_LECTURA = 60_000  # tope por archivo devuelto al modelo


def ruta_permitida(ruta: str) -> bool:
    """True solo si la ruta REAL (resueltos symlinks) cae dentro de ALLOW."""
    rp = os.path.realpath(ruta)
    for b in BLOCK:
        if rp == b or rp.startswith(b + "/"):
            return False
    return any(rp == a or rp.startswith(a + "/") for a in ALLOW)
