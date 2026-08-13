# -*- coding: utf-8 -*-
"""Agente BUUM v1 — solo lectura, sobre Claude Code headless con token de suscripcion.

Sin costo variable: usa el plan de Claude del Fundador (CLAUDE_CODE_OAUTH_TOKEN).
Permisos de herramientas: agente/policies/permisos.json (solo Read/Grep/Glob en /opt/buum).

Uso (por SSH, como usuario buum):
    python3 /opt/buum/agente/core/main.py "tu pregunta"   (como usuario buum-agent)
    python3 /opt/buum/agente/core/main.py            # interactivo
"""
import io
import json
import logging
import os
import subprocess
import sys
import time

AGENTE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # /opt/buum/agente
RAIZ = os.path.dirname(AGENTE_DIR)                                        # /opt/buum
sys.path.insert(0, AGENTE_DIR)

from core.db import DB  # noqa: E402

ENV_FILE = "/etc/buum/agent.env"  # minimo privilegio: SOLO token de suscripcion + modelo
LOG_FILE = "/var/log/buum/agente.log"
CLAUDE_BIN = os.path.expanduser("~/.local/bin/claude")
TIMEOUT_S = 300


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


class Agente:
    def __init__(self):
        self.log = preparar_logging()
        env = cargar_env()
        if not env.get("CLAUDE_CODE_OAUTH_TOKEN"):
            sys.exit("Falta CLAUDE_CODE_OAUTH_TOKEN en /etc/buum/buum.env")
        self.modelo = env.get("BUUM_AGENT_MODEL", "sonnet").strip() or "sonnet"
        # el subproceso claude recibe SOLO el token, no el resto de secretos
        self.env_hijo = dict(os.environ)
        self.env_hijo["CLAUDE_CODE_OAUTH_TOKEN"] = env["CLAUDE_CODE_OAUTH_TOKEN"]
        with open(os.path.join(AGENTE_DIR, "policies", "SYSTEM.md"), encoding="utf-8") as f:
            self.system = f.read()
        self.db = DB()
        self.cid = self.db.nueva_conversacion()
        self.sesion_claude = None  # session_id de claude para hilar la conversacion
        self.log.info("conversacion iniciada id=%s modelo=%s", self.cid, self.modelo)

    def preguntar(self, msj: str) -> str:
        self.db.guardar_mensaje(self.cid, "user", msj, self.modelo)
        cmd = [
            CLAUDE_BIN, "-p", msj,
            "--model", self.modelo,
            "--output-format", "json",
            "--settings", os.path.join(AGENTE_DIR, "policies", "permisos.json"),
            "--append-system-prompt", self.system,
        ]
        if self.sesion_claude:
            cmd += ["--resume", self.sesion_claude]
        t0 = time.time()
        try:
            proc = subprocess.run(
                cmd, cwd=RAIZ, env=self.env_hijo, timeout=TIMEOUT_S,
                capture_output=True, text=True, encoding="utf-8", errors="replace",
            )
        except subprocess.TimeoutExpired:
            self.log.error("timeout de %ss", TIMEOUT_S)
            return "El agente tardó demasiado y se detuvo (tope de seguridad)."
        dur = time.time() - t0

        try:
            data = json.loads(proc.stdout)
        except json.JSONDecodeError:
            self.log.error("salida no-JSON rc=%s stderr=%s", proc.returncode, proc.stderr[:400])
            return f"Error del agente (rc={proc.returncode}). Revisa /var/log/buum/agente.log"

        self.sesion_claude = data.get("session_id") or self.sesion_claude
        u = data.get("usage", {})
        self.db.registrar_uso(
            self.cid, self.modelo,
            int(u.get("input_tokens", 0) or 0) + int(u.get("cache_read_input_tokens", 0) or 0),
            int(u.get("output_tokens", 0) or 0),
            0.0,  # suscripcion: sin costo variable; el equivalente API queda en el log
        )
        self.log.info(
            "llamada modelo=%s dur=%.1fs turnos=%s in=%s out=%s costo_equiv=$%.4f error=%s",
            self.modelo, dur, data.get("num_turns"), u.get("input_tokens"),
            u.get("output_tokens"), float(data.get("total_cost_usd", 0) or 0),
            data.get("is_error"),
        )
        salida = (data.get("result") or "").strip() or "(sin respuesta)"
        self.db.guardar_mensaje(self.cid, "assistant", salida, self.modelo)
        return salida


def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    agente = Agente()

    if len(sys.argv) > 1:
        print("\nBUUM> " + agente.preguntar(" ".join(sys.argv[1:])) + "\n")
        return

    print("Agente BUUM v1 (solo lectura, plan de suscripcion). Escribe 'salir' para terminar.")
    while True:
        try:
            msj = input("tú> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not msj:
            continue
        if msj.lower() in ("salir", "exit", "quit"):
            break
        print("\nBUUM> " + agente.preguntar(msj) + "\n")


if __name__ == "__main__":
    main()
