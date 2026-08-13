# -*- coding: utf-8 -*-
"""Agente BUUM v1 — solo lectura, MANUAL TOOL LOOP (sin tool_runner).

Uso (por SSH, como usuario buum):
    /opt/buum/.venv/bin/python /opt/buum/agente/core/main.py "tu pregunta"
    /opt/buum/.venv/bin/python /opt/buum/agente/core/main.py            # interactivo
"""
import io
import logging
import os
import sys
import time

AGENTE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # /opt/buum/agente
sys.path.insert(0, AGENTE_DIR)

from anthropic import Anthropic  # noqa: E402

from core.db import DB  # noqa: E402
from core.presupuesto import Presupuesto, costo_llamada  # noqa: E402
from tools.lectura import TOOLS, ejecutar_herramienta  # noqa: E402

ENV_FILE = "/etc/buum/buum.env"
LOG_FILE = "/var/log/buum/agente.log"
MAX_TOKENS = 4096
MAX_ITERACIONES = 12  # tope duro de vueltas del bucle por turno


def cargar_env() -> dict:
    d = {}
    try:
        with open(ENV_FILE, encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if linea and not linea.startswith("#") and "=" in linea:
                    k, v = linea.split("=", 1)
                    d[k.strip()] = v.strip()
    except (FileNotFoundError, PermissionError) as e:
        sys.exit(f"No pude leer {ENV_FILE}: {e}")
    return d


def preparar_logging():
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )
    return logging.getLogger("buum.agente")


def texto_de(respuesta) -> str:
    return "\n".join(b.text for b in respuesta.content if b.type == "text")


def turno(client, modelo, system, historial, db, cid, presupuesto, log) -> str:
    """Un turno completo del usuario: MANUAL TOOL LOOP hasta stop_reason != tool_use."""
    for _ in range(MAX_ITERACIONES):
        ok, motivo = presupuesto.permite(db)
        if not ok:
            log.warning("presupuesto: %s", motivo)
            return motivo

        t0 = time.time()
        respuesta = client.messages.create(
            model=modelo,
            max_tokens=MAX_TOKENS,
            output_config={"effort": "low"},
            system=[{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}],
            tools=TOOLS,
            messages=historial,
        )
        dur = time.time() - t0
        u = respuesta.usage
        costo = costo_llamada(modelo, u.input_tokens, u.output_tokens)
        db.registrar_uso(cid, modelo, u.input_tokens, u.output_tokens, costo)
        log.info(
            "llamada modelo=%s dur=%.1fs in=%d out=%d cache_read=%s costo=$%.5f stop=%s",
            modelo, dur, u.input_tokens, u.output_tokens,
            getattr(u, "cache_read_input_tokens", 0), costo, respuesta.stop_reason,
        )

        # el contenido del asistente (incluidos bloques de pensamiento y tool_use)
        # vuelve INTACTO al historial
        historial.append({"role": "assistant", "content": respuesta.content})

        if respuesta.stop_reason == "tool_use":
            resultados = []
            for bloque in respuesta.content:
                if bloque.type == "tool_use":
                    salida = ejecutar_herramienta(bloque.name, dict(bloque.input))
                    resultados.append(
                        {"type": "tool_result", "tool_use_id": bloque.id, "content": salida}
                    )
            historial.append({"role": "user", "content": resultados})
            continue

        if respuesta.stop_reason == "pause_turn":
            continue  # reenviar tal cual: el servidor retoma solo

        if respuesta.stop_reason == "refusal":
            log.warning("refusal del modelo")
            return "El modelo declinó responder esta petición (política de seguridad)."

        return texto_de(respuesta)

    log.error("tope de iteraciones alcanzado")
    return "Detuve el turno: demasiadas vueltas de herramientas (tope de seguridad)."


def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    log = preparar_logging()
    env = cargar_env()

    api_key = env.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        sys.exit("Falta ANTHROPIC_API_KEY en /etc/buum/buum.env")
    modelo = env.get("BUUM_AGENT_MODEL", "").strip()
    if not modelo:
        sys.exit("Falta BUUM_AGENT_MODEL en /etc/buum/buum.env")

    presupuesto = Presupuesto(env)
    db = DB()
    client = Anthropic(api_key=api_key)

    with open(os.path.join(AGENTE_DIR, "policies", "SYSTEM.md"), encoding="utf-8") as f:
        system = f.read()

    cid = db.nueva_conversacion()
    log.info("conversacion iniciada id=%s modelo=%s", cid, modelo)
    historial = []

    def preguntar(msj: str) -> None:
        db.guardar_mensaje(cid, "user", msj, modelo)
        historial.append({"role": "user", "content": msj})
        salida = turno(client, modelo, system, historial, db, cid, presupuesto, log)
        db.guardar_mensaje(cid, "assistant", salida, modelo)
        print("\nBUUM> " + salida + "\n")

    if len(sys.argv) > 1:
        preguntar(" ".join(sys.argv[1:]))
        return

    print("Agente BUUM v1 (solo lectura). Escribe 'salir' para terminar.")
    while True:
        try:
            msj = input("tú> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not msj:
            continue
        if msj.lower() in ("salir", "exit", "quit"):
            break
        preguntar(msj)


if __name__ == "__main__":
    main()
