# -*- coding: utf-8 -*-
"""RONDA 3 — convierte las bases cinematográficas en ANUNCIOS (concepto + emoción + MARCA BUUM).
   Tipografía LIMPIA compuesta con PIL (no la IA). Salida: marketing/wow/ad_*.png"""
import os, sys, io
from PIL import Image, ImageDraw, ImageFont, ImageFilter
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
WOW = os.path.join(HERE, "wow")
LOGO = os.path.join(ROOT, "activos", "marca", "logo-oficial", "logo-buum-oficial.png")
ORANGE = (234, 80, 3)
F_BLACK = "C:/Windows/Fonts/ariblk.ttf"; F_BOLD = "C:/Windows/Fonts/arialbd.ttf"

def font(p, s): return ImageFont.truetype(p, s)

def wrap(draw, text, fnt, maxw):
    words = text.split(); lines = []; cur = ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= maxw: cur = t
        else: lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines

def compose(base, head, sub, out, logo=LOGO, logo_frac=0.30):
    im = Image.open(base).convert("RGB")
    W, H = im.size
    # scrim inferior para legibilidad
    scrim = Image.new("L", (W, H), 0); sd = ImageDraw.Draw(scrim)
    for y in range(H):
        a = 0 if y < H*0.42 else int(225 * ((y - H*0.42) / (H*0.58)))
        sd.line([(0, y), (W, y)], fill=min(a, 225))
    black = Image.new("RGB", (W, H), (0, 0, 0))
    im = Image.composite(black, im, scrim)
    d = ImageDraw.Draw(im)
    M = int(W*0.06)
    # headline
    hf = font(F_BLACK, int(W*0.072))
    lines = wrap(d, head.upper(), hf, W - 2*M)
    lh = int(W*0.084)
    total = len(lines)*lh
    sf = font(F_BOLD, int(W*0.032))
    y = H - M - total - int(W*0.06)
    # acento naranja
    d.rectangle([M, y - int(W*0.03), M + int(W*0.11), y - int(W*0.017)], fill=ORANGE)
    for ln in lines:
        d.text((M+2, y+2), ln, font=hf, fill=(0, 0, 0))       # sombra
        d.text((M, y), ln, font=hf, fill=(255, 255, 255))
        y += lh
    # subtitulo
    y += int(W*0.012)
    for ln in wrap(d, sub, sf, W - 2*M):
        d.text((M, y), ln, font=sf, fill=(232, 232, 236)); y += int(W*0.045)
    # logo arriba-izquierda (nitido, sin sombra que lo ensucie; resample de alta calidad)
    try:
        lg = Image.open(logo).convert("RGBA")
        lw = int(W*logo_frac); lg = lg.resize((lw, int(lg.height*lw/lg.width)), Image.LANCZOS)
        im = im.convert("RGBA"); im.alpha_composite(lg, (M, M)); im = im.convert("RGB")
    except Exception as e:
        print("  (logo:", str(e)[:60], ")")
    im.save(out); print("  OK", os.path.basename(out))

ADS = [
 ("w3.png", "Enciende tu casa con el sol", "Reflector solar recargable · se carga de día y alumbra toda la noche · $0 de recibo", "ad_1.png"),
 ("w5.png", "Que tu entrada nunca esté a oscuras", "Reflector solar recargable · luz potente, sin cables, sin electricista", "ad_2.png"),
 ("w2.png", "Luz de sobra. Gasto cero.", "Reflector solar recargable BUUM · el sol lo carga, tú solo disfrutas", "ad_3.png"),
]
if __name__ == "__main__":
    print("Ronda 3 — anuncios con concepto + marca...")
    for b, h, s, o in ADS:
        compose(os.path.join(WOW, b), h, s, os.path.join(WOW, o))
    print("LISTO.")
