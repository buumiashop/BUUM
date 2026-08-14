# -*- coding: utf-8 -*-
"""RUTINA DE GATITOS (práctica) — PROCESO completo, SIN PUBLICAR.
   Concepto creativo variado (arte/meme/realista/emocional, no genérico) -> genera -> 4 filtros ->
   lo aprobado va a 'por-autorizar/' para que el dueño lo autorice en el Centro de Mando.
   NADA se publica sin autorización. Uso: python rutina_gatitos.py --n 3
"""
import os, sys, io, json, base64, time, random, shutil, urllib.request, datetime
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import filtros_calidad as fc   # los 4 filtros (reutiliza y ya reconfigura stdout a utf-8)

GKEY = fc.GKEY
OUT = os.path.join(HERE, "gatitos", "lote"); os.makedirs(OUT, exist_ok=True)
APROB = os.path.join(HERE, "por-autorizar"); os.makedirs(APROB, exist_ok=True)
FBLACK = "C:/Windows/Fonts/ariblk.ttf"

MASCOTA = ("Mascota oficial BUUM: gato KITSUNE tierno chibi 3D, pelaje BLANCO con marcas de mascara de zorro japonesa en "
           "NARANJA #EA5003 y AZUL #102AC4, ojos grandes amigables, dije naranja de pausa. Consistente. ")
NEG = " Sin texto, sin letras, sin marcas de agua, sin foco antiguo de vidrio amarillo. Cuadro 1:1."

# BANCO DE CONCEPTOS creativos (variado, NO genérico)
BANCO = [
 {"id": "realista", "tipo": "Gato realista", "meme": None,
  "p": "Foto REALISTA y adorable de un gatito BLANCO esponjado con sutiles marcas naranja y azul cerca de los ojos (guiño a BUUM), "
       "en una sala acogedora iluminada de noche con luz blanca limpia y bonita, cinematografico, ternura premium tipo portada de revista." + NEG},
 {"id": "arte-pop", "tipo": "Arte / póster", "meme": None,
  "p": MASCOTA + "Ilustrada como POSTER ARTISTICO estilo POP-ART audaz (a lo Warhol), colores vivos de marca, composicion de galeria, premium y llamativo." + NEG},
 {"id": "arte-clasico", "tipo": "Arte / póster", "meme": None,
  "p": MASCOTA + "Retratada como una PINTURA CLASICA elegante (estilo renacentista/oleo) pero tierna, con marco de museo, sofisticada y divertida a la vez." + NEG},
 {"id": "epico", "tipo": "Épico", "meme": None,
  "p": MASCOTA + "En una escena EPICA y cinematografica: la mascota heroica sobre una loma al atardecer con un rayo de luz blanca, dramatico y aspiracional, tipo cartel de cine." + NEG},
 {"id": "meme-noche", "tipo": "Meme", "meme": ("YO A LAS 3 A.M.", "buscando el apagador"),
  "p": MASCOTA + "Con cara MUY graciosa y exagerada, medio dormido y despeinado, en un cuarto oscuro tanteando la pared, expresion comica. Estilo 3D limpio." + NEG},
 {"id": "meme-lunes", "tipo": "Meme", "meme": ("EL LUNES:", "yo:"),
  "p": MASCOTA + "Con cara comica de flojera absoluta, derretido sobre un sillon, super expresivo y gracioso. Estilo 3D limpio, fondo simple." + NEG},
]

def gen(prompt, out, tries=4):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-image:generateContent?key={GKEY}"
    body = {"contents": [{"parts": [{"text": prompt}]}], "generationConfig": {"responseModalities": ["TEXT", "IMAGE"]}}
    for t in range(tries):
        try:
            req = urllib.request.Request(url, data=json.dumps(body).encode(), headers={"Content-Type": "application/json"})
            d = json.load(urllib.request.urlopen(req, timeout=240))
            for p in d.get("candidates", [{}])[0].get("content", {}).get("parts", []):
                if "inlineData" in p:
                    open(out, "wb").write(base64.b64decode(p["inlineData"]["data"])); return True
        except Exception as e:
            print("   err:", str(e)[:140])
        time.sleep(2)
    return False

def meme(path, top, bottom):
    im = Image.open(path).convert("RGB"); W, H = im.size; d = ImageDraw.Draw(im)
    f = ImageFont.truetype(FBLACK, int(W*0.09))
    def txt(s, y):
        s = s.upper(); w = d.textlength(s, font=f); x = (W-w)/2
        for dx in (-3, 3):
            for dy in (-3, 3): d.text((x+dx, y+dy), s, font=f, fill=(0, 0, 0))
        d.text((x, y), s, font=f, fill=(255, 255, 255))
    if top: txt(top, int(H*0.03))
    if bottom: txt(bottom, int(H*0.86))
    im.save(path)

def main():
    a = sys.argv[1:]; n = 3
    if "--n" in a: n = int(a[a.index("--n")+1])
    if "--ids" in a:
        ids = a[a.index("--ids")+1].split(",")
        conceptos = [c for c in BANCO if c["id"] in ids]
    else:
        conceptos = random.sample(BANCO, min(n, len(BANCO)))
    print(f"🎬 Rutina de gatitos (SIN PUBLICAR) — {len(conceptos)} piezas creativas → 4 filtros → por-autorizar\n")
    aprob = 0
    for c in conceptos:
        f = os.path.join(OUT, c["id"] + ".png")
        print("🎨", c["tipo"], "·", c["id"])
        if not gen(c["p"], f): print("   (no se generó)"); continue
        if c["meme"]: meme(f, c["meme"][0], c["meme"][1])
        ok, res = fc.revisar(f, modo="social")
        if ok:
            shutil.copy(f, os.path.join(APROB, c["id"] + ".png")); aprob += 1
    print(f"\n✅ {aprob} pieza(s) pasaron QC → 'por-autorizar/'. NADA se publicó. Autorízalas en el Centro de Mando.")

if __name__ == "__main__":
    main()
