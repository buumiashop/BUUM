# -*- coding: utf-8 -*-
"""Anuncios FINALES A1/A2 con escenas de ChatGPT del Fundador + textos/logo/precio por codigo."""
import os, io, sys, shutil
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
KB   = os.path.join(ROOT, "activos", "productos", "R54W50")
ESC  = os.path.join(KB, "escenas"); os.makedirs(ESC, exist_ok=True)
OUT  = os.path.join(HERE, "contenido", "pro")
LOGO = os.path.join(ROOT, "tienda", "tema-vivo", "assets", "logo-buumia-original.png")
DL   = "C:/Users/playg/Downloads"

SRC_A1 = os.path.join(DL, "image-1786598667228.webp")   # patio antes/despues (con reflector)
SRC_A2 = os.path.join(DL, "image-1786598675575.webp")   # porton con silueta

# archivar en la biblioteca (nunca borrar las de Descargas)
A1_KB = os.path.join(ESC, "escena-a1-patio-chatgpt.png")
A2_KB = os.path.join(ESC, "escena-a2-porton-chatgpt.png")
if not os.path.exists(A1_KB): Image.open(SRC_A1).convert("RGB").save(A1_KB)
if not os.path.exists(A2_KB): Image.open(SRC_A2).convert("RGB").save(A2_KB)

W, H = 1080, 1920
ORANGE = (234, 80, 3); NAVY = (0, 24, 102); WHITE = (255, 255, 255); ORANGE_CL = (255, 138, 61)
F_BLACK = "C:/Windows/Fonts/seguibl.ttf"; F_SEMI = "C:/Windows/Fonts/seguisb.ttf"
def font(p, s): return ImageFont.truetype(p, s)

def fill_cover(img, w, h):
    r = max(w / img.width, h / img.height)
    img = img.resize((int(img.width * r) + 1, int(img.height * r) + 1), Image.LANCZOS)
    x = (img.width - w) // 2; y = (img.height - h) // 2
    return img.crop((x, y, x + w, y + h))

def rrect(d, xy, rad, **kw): d.rounded_rectangle(xy, radius=rad, **kw)

def text_shadow(d, xy, s, f, fill, off=5):
    d.text((xy[0] + off, xy[1] + off), s, font=f, fill=(0, 0, 0, 200))
    d.text(xy, s, font=f, fill=fill)

def chip(d, cx, y, s, f, fg, bg, pad=(26, 14)):
    bb = d.textbbox((0, 0), s, font=f); tw, th = bb[2] - bb[0], bb[3] - bb[1]
    rrect(d, (cx - tw / 2 - pad[0], y, cx + tw / 2 + pad[0], y + th + 2 * pad[1]), (th + 2 * pad[1]) / 2, fill=bg)
    d.text((cx - tw / 2 - bb[0], y + pad[1] - bb[1]), s, font=f, fill=fg)

def paste_logo(base, cx, y, wlogo=300):
    lg = Image.open(LOGO).convert("RGBA"); r = wlogo / lg.width
    lg = lg.resize((wlogo, int(lg.height * r)), Image.LANCZOS)
    pad = 22
    card = Image.new("RGBA", (lg.width + 2 * pad, lg.height + 2 * pad), (0, 0, 0, 0))
    rrect(ImageDraw.Draw(card), (0, 0, card.width - 1, card.height - 1), 34, fill=(255, 255, 255, 242))
    card.alpha_composite(lg, (pad, pad))
    sh = Image.new("RGBA", base.size, (0, 0, 0, 0))
    rrect(ImageDraw.Draw(sh), (cx - card.width // 2 + 6, y + 10, cx + card.width // 2 + 6, y + card.height + 10), 34, fill=(0, 0, 0, 110))
    base.alpha_composite(sh.filter(ImageFilter.GaussianBlur(12)))
    base.alpha_composite(card, (cx - card.width // 2, y))

def benefit_row(d, y, items, f):
    ws = []; total = 0
    for s in items:
        bb = d.textbbox((0, 0), s, font=f); w = bb[2] - bb[0] + 44; ws.append((s, w, bb)); total += w
    total += 18 * (len(items) - 1); x = (W - total) / 2
    for s, w, bb in ws:
        th = bb[3] - bb[1]
        rrect(d, (x, y, x + w, y + th + 26), (th + 26) / 2, fill=(255, 255, 255, 235))
        d.text((x + 22 - bb[0], y + 13 - bb[1]), s, font=f, fill=NAVY)
        x += w + 18

def price_cta(d, canvas):
    fpz = font(F_BLACK, 64); s = "2 x $1,299"
    bb = d.textbbox((0, 0), s, font=fpz); pw = bb[2] - bb[0] + 90
    rrect(d, ((W - pw) / 2, H - 262, (W + pw) / 2, H - 148), 30, fill=ORANGE + (255,))
    d.text(((W - (bb[2] - bb[0])) / 2 - bb[0], H - 262 + (114 - (bb[3] - bb[1])) / 2 - bb[1]), s, font=fpz, fill=WHITE)
    chip(d, W // 2, H - 120, "Envío gratis a todo México", font(F_SEMI, 38), WHITE, (10, 90, 60, 235))

def glow_at(base, cx, cy, rad, alpha=170):
    g = Image.new("RGBA", base.size, (0, 0, 0, 0))
    ImageDraw.Draw(g).ellipse((cx - rad, cy - rad * 0.7, cx + rad, cy + rad * 0.7), fill=(255, 255, 255, alpha))
    base.alpha_composite(g.filter(ImageFilter.GaussianBlur(rad * 0.45)))

# ============ A1 FINAL ============
def a1():
    canvas = fill_cover(Image.open(A1_KB).convert("RGB"), W, H).convert("RGBA")
    paste_logo(canvas, W // 2, 46, 290)
    d = ImageDraw.Draw(canvas)
    # titular a la IZQUIERDA (mitad negra), alineado a la izquierda
    f1 = font(F_BLACK, 96)
    text_shadow(d, (64, 300), "SIN", f1, WHITE)
    text_shadow(d, (64, 400), "CABLE.", f1, WHITE)
    text_shadow(d, (64, 540), "SIN", f1, ORANGE_CL)
    text_shadow(d, (64, 640), "RECIBO.", f1, ORANGE_CL)
    fs = font(F_SEMI, 42)
    text_shadow(d, (64, 790), "Se carga solo", fs, WHITE, off=3)
    text_shadow(d, (64, 845), "con el sol", fs, WHITE, off=3)
    # chips ANTES / DESPUÉS
    chip(d, 250, 1180, "ANTES", font(F_BLACK, 40), WHITE, (0, 0, 0, 175))
    chip(d, 800, 1180, "DESPUÉS", font(F_BLACK, 40), WHITE, ORANGE + (255,))
    benefit_row(d, H - 430, ["SOLAR", "ILUMINA COMO 500 W", "AGUANTA LLUVIA"], font(F_SEMI, 34))
    benefit_row(d, H - 352, ["CONTROL REMOTO", "HASTA 12 H DE LUZ"], font(F_SEMI, 34))
    price_cta(d, canvas)
    canvas.convert("RGB").save(os.path.join(OUT, "A1-FINAL.png"))
    print("A1 FINAL OK")

# ============ A2 FINAL ============
def a2():
    canvas = fill_cover(Image.open(A2_KB).convert("RGB"), W, H).convert("RGBA")
    paste_logo(canvas, W // 2, 46, 290)
    d = ImageDraw.Draw(canvas)
    f1 = font(F_BLACK, 104)
    for i, (t, c) in enumerate([("¿NO VES", WHITE), ("QUIÉN TOCA", ORANGE_CL), ("TU PUERTA?", WHITE)]):
        bb = d.textbbox((0, 0), t, font=f1)
        text_shadow(d, ((W - (bb[2] - bb[0])) / 2 - bb[0], 215 + i * 108), t, f1, c)
    fs = font(F_SEMI, 46)
    s = "Luz donde no llega el cable"
    bb = d.textbbox((0, 0), s, font=fs)
    text_shadow(d, ((W - (bb[2] - bb[0])) / 2 - bb[0], 575), s, fs, WHITE, off=3)
    # reflector REAL abajo-derecha, encendido
    p = Image.open(os.path.join(KB, "recortes", "principal.png")).convert("RGBA")
    r = 360 / p.height; p = p.resize((int(p.width * r), 360), Image.LANCZOS)
    px, py = W - p.width - 70, H - 640
    glow_at(canvas, px + p.width // 2, py + p.height // 2, 240, alpha=115)
    canvas.alpha_composite(p, (px, py))
    glow_at(canvas, px + p.width // 2, py + int(p.height * 0.55), 135, alpha=210)
    d = ImageDraw.Draw(canvas)
    benefit_row(d, H - 740, ["SOLAR", "ILUMINA COMO 500 W", "SIN CABLEADO"], font(F_SEMI, 30))
    price_cta(d, canvas)
    canvas.convert("RGB").save(os.path.join(OUT, "A2-FINAL.png"))
    print("A2 FINAL OK")

a1(); a2()
