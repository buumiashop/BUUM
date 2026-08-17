# -*- coding: utf-8 -*-
"""FASE 13D — Colector de realidad: META (SOLO LECTURA).

Lee metricas basicas reales de la pagina de Facebook y la cuenta de Instagram
de BUUM via Graph API (GET unicamente) y las guarda como snapshot verificable
en datos/snapshots/meta/YYYY-MM-DD/.

Reglas: solo GET; nada de publicar, editar ni configurar; sin secretos en el
snapshot; lo no disponible se declara NO_DISPONIBLE.
"""
import io
import json
import os
import sys
import urllib.request
import urllib.parse
import urllib.error
from datetime import datetime, timezone

VERSION = "1.0"
V = "v21.0"
AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))


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
    sys.exit("Sin archivo de credenciales")


def get(ruta, params, token):
    params = dict(params or {})
    params["access_token"] = token
    url = f"https://graph.facebook.com/{V}/{ruta}?" + urllib.parse.urlencode(params)
    try:
        with urllib.request.urlopen(url, timeout=30) as r:
            return json.load(r), None
    except urllib.error.HTTPError as e:
        try:
            det = json.load(e).get("error", {}).get("message", "")[:120]
        except Exception:
            det = ""
        return None, f"HTTP {e.code} en {ruta}: {det}"
    except Exception as e:
        return None, f"{type(e).__name__} en {ruta}"


def real(v):     return {"valor": v, "tipo": "REAL"}
def nodisp(por): return {"valor": None, "tipo": "NO_DISPONIBLE", "motivo": por}


def main():
    env = cargar_env()
    token = env.get("META_USER_TOKEN")
    if not token:
        sys.exit("Falta META_USER_TOKEN")

    ahora = datetime.now(timezone.utc)
    errores = []
    metricas = {}

    # ---- Pagina de Facebook (token de pagina derivado, patron oficial BUUM) ----
    cuentas, e = get("me/accounts", {"fields": "id,name,access_token,followers_count,fan_count"}, token)
    if e:
        errores.append(e)
        pagina = None
    else:
        datos = (cuentas or {}).get("data", [])
        pagina = datos[0] if datos else None
    if pagina:
        metricas["facebook_pagina"] = real(pagina.get("name"))
        metricas["facebook_seguidores"] = real(pagina.get("followers_count")) if pagina.get("followers_count") is not None else nodisp("campo no devuelto")
        metricas["facebook_me_gusta"] = real(pagina.get("fan_count")) if pagina.get("fan_count") is not None else nodisp("campo no devuelto")
        ptoken = pagina.get("access_token") or token

        # ---- Instagram business ----
        ig, e = get(pagina["id"], {"fields": "instagram_business_account{id,username,followers_count,media_count}"}, ptoken)
        if e:
            errores.append(e)
        cuenta_ig = ((ig or {}).get("instagram_business_account")) or {}
        if cuenta_ig:
            metricas["instagram_usuario"] = real(cuenta_ig.get("username"))
            metricas["instagram_seguidores"] = real(cuenta_ig.get("followers_count"))
            metricas["instagram_publicaciones"] = real(cuenta_ig.get("media_count"))
            alcance, e = get(f"{cuenta_ig['id']}/insights", {"metric": "reach", "period": "days_28"}, ptoken)
            if e:
                errores.append(e)
                metricas["instagram_alcance_28d"] = nodisp("insights no disponible: " + e)
            else:
                try:
                    valores = alcance["data"][0]["values"]
                    metricas["instagram_alcance_28d"] = real(valores[-1]["value"])
                except (KeyError, IndexError):
                    metricas["instagram_alcance_28d"] = nodisp("respuesta sin values")
        else:
            metricas["instagram_seguidores"] = nodisp("cuenta IG no vinculada o no devuelta")
    else:
        metricas["facebook_seguidores"] = nodisp("me/accounts sin resultados")

    snapshot = {
        "fuente": "meta",
        "version_colector": VERSION,
        "extraido_en": ahora.isoformat(),
        "periodo": {"nota": "estado actual; alcance IG = ultimos 28 dias"},
        "estado": "OK" if not errores else ("PARCIAL" if metricas else "FALLIDO"),
        "errores": errores,
        "metricas": metricas,
    }

    dia = ahora.strftime("%Y-%m-%d")
    destino = os.path.join(RAIZ, "datos", "snapshots", "meta", dia)
    os.makedirs(destino, exist_ok=True)
    with io.open(os.path.join(destino, "snapshot.json"), "w", encoding="utf-8") as f:
        json.dump(snapshot, f, ensure_ascii=False, indent=1)
    with io.open(os.path.join(destino, "metadata.json"), "w", encoding="utf-8") as f:
        json.dump({"fuente": "meta", "version_colector": VERSION, "extraido_en": ahora.isoformat(),
                   "estado": snapshot["estado"], "errores": errores}, f, ensure_ascii=False, indent=1)
    print(f"SNAPSHOT {snapshot['estado']} -> datos/snapshots/meta/{dia}/ | metricas: {len(metricas)} | errores: {len(errores)}")


if __name__ == "__main__":
    main()
