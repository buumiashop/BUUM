# -*- coding: utf-8 -*-
"""BUUM OS — PANEL DE CALIDAD (los 4 filtros).
   Cada anuncio pasa por 3 críticos IA (Gemini visión) antes de llegar al dueño (el 4º filtro):
     1) Jefe de Marketing BUUM  (on-brand, engancha en 1 seg, ~95% visual, CTA, 'vale la pena')
     2) Director Creativo / CIO  (calidad técnica, composición, nada 'chafa', legible, sin defectos)
     3) Crítico 'marca mundial'  (¿Nike o Coca-Cola pagarían por publicar esto? nivel de las mejores)
   Solo lo que APRUEBAN los 3 pasa a 'por-aprobar/' (para el dueño). Lo demás va a 'rechazados/' con motivos.
   Uso:  python filtros_calidad.py <imagen.png>            (revisa una)
         python filtros_calidad.py --carpeta <carpeta>     (revisa todas las .png/.jpg)
"""
import os, sys, io, re, json, base64, shutil, urllib.request
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
MODEL = "gemini-2.5-flash"

def env(p):
    d = {}
    for l in io.open(p, encoding="utf-8"):
        l = l.strip()
        if l and not l.startswith("#") and "=" in l:
            k, v = l.split("=", 1); d[k.strip()] = v.strip()
    return d
GKEY = os.environ.get("GEMINI_API_KEY") or (env(os.path.join(ROOT,"config","config.local.env")).get("GEMINI_API_KEY") if os.path.exists(os.path.join(ROOT,"config","config.local.env")) else None)

CRITICOS = [
 ("Jefe de Marketing BUUM",
  "Eres el JEFE DE MARKETING de BUUM (tienda mexicana de iluminación/novedades). Filosofía de la marca: "
  "enganchar en 1 SEGUNDO, ~95% VISUAL (poco texto), BRILLANTE (es iluminación), colores de marca naranja #EA5003 y azul, "
  "vender que 'VALE LA PENA' (nunca 'barato/oferta'), wow superior. Evalúa SOLO si este anuncio cumple ESO."),
 ("Director Creativo / CIO",
  "Eres el DIRECTOR CREATIVO (CIO). Evalúa la CALIDAD TÉCNICA y estética: composición, jerarquía, tipografía legible, "
  "iluminación, que se vea PROFESIONAL y premium, SIN nada 'chafa', sin deformaciones, sin texto cortado ni artefactos, "
  "sin errores de IA. Sé exigente como en una agencia top."),
 ("Crítico marca mundial",
  "Eres un CRÍTICO PUBLICITARIO de clase mundial especializado en ANUNCIOS QUE VENDEN (e-commerce/DTC de élite: "
  "Govee, Anker, Ridge, las mejores campañas de performance del mundo). La pregunta clave: ¿este anuncio está al "
  "NIVEL DE LOS MEJORES ANUNCIOS DE PRODUCTO DEL MUNDO QUE DE VERDAD CONVIERTEN Y VENDEN? Debe: enganchar en 1 seg, "
  "comunicar el beneficio con claridad, verse PREMIUM y profesional, con marca coherente y limpia. Exige EXCELENCIA "
  "real y rechaza lo amateur, genérico, confuso o con marca mal integrada. Pero el objetivo es VENDER: NO exijas "
  "storytelling de cine ni de Super Bowl. Aprueba lo que un director de arte de una marca DTC líder publicaría con orgullo."),
]
# Críticos para CONTENIDO DE MARCA / MASCOTA / SOCIAL (su meta es ENGANCHE, no vender un producto)
CRITICOS_SOCIAL = [
 ("Jefe de Marketing BUUM",
  "Eres el JEFE DE MARKETING de BUUM. Evalúas contenido de MARCA/MASCOTA (gatito Kitsune) para redes, cuya meta es "
  "ENGANCHAR y dar a conocer la marca (likes, compartidas, guardados), NO vender un producto. ¿Es on-brand (colores, mascota), "
  "para en el scroll, es simpático/lindo/memorable y daría ganas de compartir? Colores naranja #EA5003 y azul."),
 ("Director Creativo / CIO",
  "Eres el DIRECTOR CREATIVO (CIO). Evalúa CALIDAD TÉCNICA y estética: composición, color, que se vea PROFESIONAL y pulido, "
  "sin defectos ni artefactos de IA, sin texto deforme. Exigente como agencia top."),
 ("Crítico viral mundial",
  "Eres un CRÍTICO de CONTENIDO SOCIAL de nivel mundial (memes, mascotas de marca, cuentas top). La pregunta: ¿este contenido "
  "PARARÍA EL SCROLL y ganaría likes/compartidas al nivel de las mejores cuentas del mundo? NO pidas que venda un producto — "
  "pide ENGANCHE, originalidad, gracia o belleza, y calidad. Si es genérico o aburrido, RECHAZA; si engancha de verdad, APRUEBA."),
]

FORMATO = ("\n\nResponde EXACTAMENTE en este formato (3 líneas):\n"
           "VEREDICTO: APRUEBA   (o RECHAZA)\n"
           "PUNTAJE: N   (0-10)\n"
           "MOTIVO: una frase corta y concreta.")

def critico(img_b64, rol, instr):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={GKEY}"
    body = {"contents": [{"parts": [{"inlineData": {"mimeType": "image/png", "data": img_b64}}, {"text": instr + FORMATO}]}]}
    try:
        req = urllib.request.Request(url, data=json.dumps(body).encode(), headers={"Content-Type": "application/json"})
        d = json.load(urllib.request.urlopen(req, timeout=120))
        txt = d["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        return {"rol": rol, "ok": None, "puntaje": None, "motivo": "error: " + str(e), "raw": ""}
    ver = re.search(r"VEREDICTO:\s*(APRUEBA|RECHAZA)", txt, re.I)
    pun = re.search(r"PUNTAJE:\s*(\d+(?:\.\d+)?)", txt)
    mot = re.search(r"MOTIVO:\s*(.+)", txt)
    ok = bool(ver and ver.group(1).upper() == "APRUEBA")
    return {"rol": rol, "ok": ok, "puntaje": float(pun.group(1)) if pun else None,
            "motivo": (mot.group(1).strip() if mot else txt.strip()[:140])}

def revisar(path, modo="producto"):
    b = base64.b64encode(open(path, "rb").read()).decode()
    crits = CRITICOS_SOCIAL if modo == "social" else CRITICOS
    print("\n==============================\n📢", os.path.basename(path), "[" + modo + "]")
    res = []
    for rol, instr in crits:
        r = critico(b, rol, instr); res.append(r)
        icon = "✅" if r["ok"] else ("❌" if r["ok"] is False else "⚠️")
        print(f"  {icon} {rol:24s} {('%.0f/10'%r['puntaje']) if r['puntaje'] is not None else '   '}  · {r['motivo']}")
    aprobado = all(r["ok"] for r in res)
    print("  →", "🏆 PASA (a revisión del dueño)" if aprobado else "🚫 NO pasa (se rehace)")
    return aprobado, res

def main():
    args = sys.argv[1:]
    if not args:
        print("Uso: python filtros_calidad.py <imagen>  |  --carpeta <carpeta>"); return
    if args[0] == "--carpeta":
        car = args[1]; apr = os.path.join(car, "por-aprobar"); rec = os.path.join(car, "rechazados")
        os.makedirs(apr, exist_ok=True); os.makedirs(rec, exist_ok=True); rep = {}
        for f in sorted(os.listdir(car)):
            if f.lower().endswith((".png", ".jpg", ".jpeg")):
                ok, res = revisar(os.path.join(car, f))
                shutil.copy(os.path.join(car, f), os.path.join(apr if ok else rec, f))
                rep[f] = {"aprobado": ok, "criticos": res}
        json.dump(rep, io.open(os.path.join(car, "_reporte_filtros.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        n = sum(1 for v in rep.values() if v["aprobado"])
        print(f"\nRESUMEN: {n}/{len(rep)} pasaron los 3 filtros → por-aprobar/")
    else:
        revisar(args[0])

if __name__ == "__main__":
    main()
