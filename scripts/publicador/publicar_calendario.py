# -*- coding: utf-8 -*-
"""PUBLICADOR AUTOMATICO POR CALENDARIO (Departamento de Contenido BUUM).

Corre por cron cada 15 min en el servidor (como buum). Lee el calendario
(marketing/calendario-contenido.json, versionado en git) y publica en FB+IG las
piezas cuyo momento llego, SOLO si estado == "aprobado" (aprobacion del Fundador).
El estado de "ya publicado" vive en /var/lib/buum/data/publicados.json (local
del servidor; el clon usa deploy key de solo lectura y no puede hacer push).

Regla de seguridad: este script SOLO publica piezas aprobadas con fecha/hora;
jamas decide contenido. La imagen debe estar en una URL publica (CDN de la
tienda). Autorizado por el Fundador 2026-08-18 (publicacion automatica de
piezas YA aprobadas, unicamente).

Uso:  python3 scripts/publicador/publicar_calendario.py [--dry-run]
"""
import io
import json
import os
import sys
import urllib.request
import urllib.parse
from datetime import datetime, timezone

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
CAL = os.path.join(RAIZ, "marketing", "calendario-contenido.json")
ESTADO_DIR = "/var/lib/buum/data" if os.path.isdir("/var/lib/buum/data") else os.path.join(RAIZ, "datos")
ESTADO = os.path.join(ESTADO_DIR, "publicados.json")
V = "v21.0"
DRY = "--dry-run" in sys.argv


def cargar_env():
    for ruta in ("/etc/buum/buum.env", os.path.join(RAIZ, "config", "config.local.env")):
        if os.path.exists(ruta):
            d = {}
            for l in io.open(ruta, encoding="utf-8"):
                l = l.strip()
                if l and not l.startswith("#") and "=" in l:
                    k, v = l.split("=", 1)
                    d[k.strip()] = v.strip()
            return d
    sys.exit("Sin credenciales")


def api(metodo, ruta, params, token):
    params = dict(params)
    params["access_token"] = token
    datos = urllib.parse.urlencode(params).encode()
    url = f"https://graph.facebook.com/{V}/{ruta}"
    if metodo == "GET":
        req = urllib.request.Request(url + "?" + urllib.parse.urlencode(params))
    else:
        req = urllib.request.Request(url, data=datos)
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return json.load(r), None
    except urllib.error.HTTPError as e:
        try:
            det = json.load(e).get("error", {}).get("message", "")[:200]
        except Exception:
            det = ""
        return None, f"HTTP {e.code}: {det}"
    except Exception as e:
        return None, str(e)[:200]


def main():
    if not os.path.exists(CAL):
        print("sin calendario"); return
    cal = json.load(io.open(CAL, encoding="utf-8"))
    hechos = {}
    if os.path.exists(ESTADO):
        hechos = json.load(io.open(ESTADO, encoding="utf-8"))
    ahora = datetime.now(timezone.utc)

    pendientes = []
    for p in cal.get("piezas", []):
        if p.get("estado") != "aprobado" or p.get("id") in hechos:
            continue
        try:
            cuando = datetime.fromisoformat(p["cuando_utc"]).replace(tzinfo=timezone.utc)
        except Exception:
            continue
        if cuando <= ahora:
            pendientes.append(p)
    if not pendientes:
        print(f"{ahora.isoformat()} nada por publicar"); return

    env = cargar_env()
    token = env.get("META_USER_TOKEN") or sys.exit("Falta META_USER_TOKEN")
    cuentas, e = api("GET", "me/accounts", {"fields": "id,name,access_token,instagram_business_account"}, token)
    if e:
        print("ERROR cuentas:", e); return
    pagina = cuentas["data"][0]
    ptoken = pagina.get("access_token") or token
    ig_id = (pagina.get("instagram_business_account") or {}).get("id")
    if not ig_id:
        det, _ = api("GET", pagina["id"], {"fields": "instagram_business_account"}, ptoken)
        ig_id = ((det or {}).get("instagram_business_account") or {}).get("id")

    for p in pendientes:
        rid = p["id"]
        res = {"cuando": ahora.isoformat(), "fb": None, "ig": None}
        print(f"--> publicando {rid}: {p.get('titulo','')} [{','.join(p.get('canales', ['fb','ig']))}]")
        if DRY:
            print("    DRY-RUN: no se publica"); continue
        canales = p.get("canales", ["fb", "ig"])
        if "fb" in canales:
            r, e = api("POST", f"{pagina['id']}/photos", {"url": p["imagen_url"], "caption": p["caption"]}, ptoken)
            res["fb"] = r.get("post_id") or r.get("id") if r else "ERROR " + (e or "")
            print("    FB:", res["fb"])
        if "ig" in canales and ig_id:
            r, e = api("POST", f"{ig_id}/media", {"image_url": p["imagen_url"], "caption": p["caption"]}, ptoken)
            if r and r.get("id"):
                r2, e2 = api("POST", f"{ig_id}/media_publish", {"creation_id": r["id"]}, ptoken)
                res["ig"] = r2.get("id") if r2 else "ERROR " + (e2 or "")
            else:
                res["ig"] = "ERROR " + (e or "")
            print("    IG:", res["ig"])
        hechos[rid] = res
        os.makedirs(ESTADO_DIR, exist_ok=True)
        json.dump(hechos, io.open(ESTADO, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("hecho.")


if __name__ == "__main__":
    main()
