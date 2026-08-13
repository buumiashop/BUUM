# -*- coding: utf-8 -*-
"""Servidor del Centro de Mando: sirve el panel Y atiende /api/editar (edición por IA desde el panel).
   Así el botón 'Editar' funciona ahí mismo (sin copiar/pegar al chat).
   Uso: python servidor_panel.py [puerto]"""
import os, sys, json
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from functools import partial
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
MK = os.path.join(ROOT, "buumia-tienda", "marketing")
sys.path.insert(0, MK)
import editar_img  # motor de edición image-to-image

FOLDERS = [os.path.join(MK, "por-autorizar"), os.path.join(MK, "gatitos"), os.path.join(MK, "gatitos", "lote"),
           os.path.join(MK, "gatitos", "oficial"), os.path.join(MK, "aprobados"),
           os.path.join(ROOT, "buumia-catalogo", "marca", "logo-oficial")]

def find(basename):
    basename = os.path.basename(basename.split("?")[0])
    for f in FOLDERS:
        p = os.path.join(f, basename)
        if os.path.exists(p):
            return p
    return None

class H(SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass
    def _json(self, obj, code=200):
        b = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(code); self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(b))); self.end_headers(); self.wfile.write(b)
    def do_POST(self):
        if self.path.split("?")[0] == "/api/editar":
            try:
                n = int(self.headers.get("Content-Length", 0) or 0)
                data = json.loads(self.rfile.read(n) or b"{}")
                p = find(data.get("file", ""))
                obs = (data.get("obs") or "").strip()
                if not p:
                    return self._json({"ok": False, "error": "no encontré el archivo"})
                if not obs:
                    return self._json({"ok": False, "error": "sin instrucción"})
                tmp = p + ".tmp.png"
                if editar_img.editar(p, tmp, obs) and os.path.exists(tmp):
                    os.replace(tmp, p)
                    rel = os.path.relpath(p, ROOT).replace("\\", "/")
                    return self._json({"ok": True, "img": "/" + rel + "?v=" + str(int(os.path.getmtime(p)))})
                return self._json({"ok": False, "error": "la IA no generó imagen"})
            except Exception as e:
                return self._json({"ok": False, "error": str(e)[:200]})
        self.send_error(404)

if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8130
    srv = ThreadingHTTPServer(("127.0.0.1", port), partial(H, directory=ROOT))
    print("BUUM panel server (con editor IA) en http://127.0.0.1:%d" % port)
    srv.serve_forever()
