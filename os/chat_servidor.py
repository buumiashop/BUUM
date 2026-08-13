# -*- coding: utf-8 -*-
"""Bandeja de chat local del Centro de Mando BUUM.

SOLO escucha en 127.0.0.1:8131 (acceso via tunel SSH). Python estandar, cero
dependencias. Corre como buum-agent; reutiliza el wrapper del agente (main.py).

Uso:  sudo -H -u buum-agent python3 /opt/buum/os/chat_servidor.py
Tunel desde el PC:  ssh -N -L 8131:127.0.0.1:8131 buum@SERVIDOR
"""
import json
import logging
import os
import re
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

OS_DIR = os.path.dirname(os.path.abspath(__file__))          # /opt/buum/os
RAIZ = os.path.dirname(OS_DIR)                               # /opt/buum
sys.path.insert(0, os.path.join(RAIZ, "agente"))

from core.db import DB          # noqa: E402
from core.main import Agente    # noqa: E402

HOST, PUERTO = "127.0.0.1", 8131
MAX_MENSAJE = 4000
MAX_BODY = 16_000
RE_CID = re.compile(r"^[0-9a-f]{12}$")
MIME = {".html": "text/html; charset=utf-8", ".js": "text/javascript; charset=utf-8",
        ".css": "text/css; charset=utf-8", ".png": "image/png", ".jpg": "image/jpeg",
        ".svg": "image/svg+xml", ".json": "application/json; charset=utf-8",
        ".ico": "image/x-icon", ".webp": "image/webp", ".mp4": "video/mp4"}

logging.basicConfig(filename="/var/log/buum/chat.log", level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("buum.chat")

AGENTE = Agente()
CANDADO = threading.Lock()  # una llamada al agente a la vez (512MB RAM)


class Peticion(BaseHTTPRequestHandler):
    server_version = "BUUM/1"

    def log_message(self, fmt, *args):  # accesos al log, no a consola
        log.info("%s %s", self.address_string(), fmt % args)

    def _json(self, obj, codigo=200):
        cuerpo = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(codigo)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(cuerpo)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(cuerpo)

    def _error(self, codigo, msj):
        self._json({"error": msj}, codigo)

    def _cuerpo(self):
        n = int(self.headers.get("Content-Length", 0) or 0)
        if n <= 0 or n > MAX_BODY:
            return None
        try:
            return json.loads(self.rfile.read(n).decode("utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError):
            return None

    # ---------- GET ----------
    def do_GET(self):
        ruta = self.path.split("?", 1)[0]
        try:
            if ruta == "/api/chat/conversaciones":
                return self._json({"conversaciones": DB().listar_conversaciones()})
            if ruta == "/api/chat/mensajes":
                cid = (self.path.split("cid=", 1) + [""])[1][:12]
                if not RE_CID.match(cid):
                    return self._error(400, "conversacion invalida")
                return self._json({"mensajes": DB().mensajes_de(cid)})
            return self._estatico(ruta)
        except Exception:
            log.exception("GET %s", ruta)
            return self._error(500, "error interno")

    def _estatico(self, ruta):
        if ruta in ("/", "/index.html"):
            ruta = "/centro-de-mando.html"
        destino = os.path.realpath(os.path.join(OS_DIR, ruta.lstrip("/")))
        if not destino.startswith(OS_DIR + os.sep) or not os.path.isfile(destino):
            return self._error(404, "no existe")
        ext = os.path.splitext(destino)[1].lower()
        with open(destino, "rb") as f:
            datos = f.read()
        self.send_response(200)
        self.send_header("Content-Type", MIME.get(ext, "application/octet-stream"))
        self.send_header("Content-Length", str(len(datos)))
        self.end_headers()
        self.wfile.write(datos)

    # ---------- POST ----------
    def do_POST(self):
        try:
            if self.path == "/api/chat/nueva":
                cid = AGENTE.nueva_conversacion()
                return self._json({"id": cid})
            if self.path == "/api/chat/enviar":
                datos = self._cuerpo()
                if not isinstance(datos, dict):
                    return self._error(400, "cuerpo invalido")
                cid = str(datos.get("cid", ""))
                msj = str(datos.get("mensaje", "")).strip()
                if not RE_CID.match(cid) or not AGENTE.db.existe_conversacion(cid):
                    return self._error(400, "conversacion invalida")
                if not msj or len(msj) > MAX_MENSAJE:
                    return self._error(400, f"mensaje vacio o mayor a {MAX_MENSAJE} caracteres")
                with CANDADO:
                    respuesta = AGENTE.preguntar(cid, msj)
                return self._json({"respuesta": respuesta})
            return self._error(404, "no existe")
        except Exception:
            log.exception("POST %s", self.path)
            return self._error(500, "error interno")


def main():
    servidor = ThreadingHTTPServer((HOST, PUERTO), Peticion)
    log.info("bandeja escuchando en %s:%s", HOST, PUERTO)
    print(f"Bandeja BUUM en http://{HOST}:{PUERTO} (solo local; usa tunel SSH)")
    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
