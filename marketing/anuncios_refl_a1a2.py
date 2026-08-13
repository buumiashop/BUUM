# -*- coding: utf-8 -*-
"""A1 (antes/despues) y A2 (dolor porton) del Reflector Solar 50W — metodo rompecabezas.
   Producto REAL pegado, luz BLANCA, textos grandes con acentos correctos."""
import os, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
KB   = os.path.join(ROOT, "activos", "productos", "R54W50")
PRO  = os.path.join(HERE, "contenido", "pro")
OUT  = os.path.join(PRO); os.makedirs(OUT, exist_ok=True)
LOGO = os.path.join(ROOT, "tienda", "tema-vivo", "assets", "logo-buumia-original.png")

W, H = 1080, 1920
ORANGE = (234, 80, 3); NAVY = (0, 24, 102); GREEN = (22, 160, 111); WHITE = (255, 255, 255)

F_BLACK = "C:/Windows/Fonts/seguibl.ttf"
F_SEMI  = "C:/Windows/Fonts/seguisb.ttf"
def font(path, size): return ImageFont.truetype(path, size)

def fill_cover(img, w, h):
    r = max(w / img.width, h / img.height)
    img = img.resize((int(img.width * r) + 1, int(img.height * r) + 1), Image.LANCZOS)
    x = (img.width - w) // 2; y = (img.height - h) // 2
    return img.crop((x, y, x + w, y + h))

def rrect(d, xy, rad, fill=None, outline=None, width=1):
    d.rounded_rectangle(xy, radius=rad, fill=fill, outline=outline, width=width)

def text_shadow(d, xy, s, f, fill, sh=(0, 0, 0, 200), off=5):
    d.text((xy[0] + off, xy[1] + off), s, font=f, fill=sh)
    d.text(xy, s, font=f, fill=fill)

def chip(d, cx, y, s, f, fg, bg, pad=(26, 14)):
    bb = d.textbbox((0, 0), s, font=f)
    tw, th = bb[2] - bb[0], bb[3] - bb[1]
    x0 = cx - tw / 2 - pad[0]; x1 = cx + tw / 2 + pad[0]
    rrect(d, (x0, y, x1, y + th + 2 * pad[1]), (th + 2 * pad[1]) / 2, fill=bg)
    d.text((cx - tw / 2 - bb[0], y + pad[1] - bb[1]), s, font=f, fill=fg)
    return y + th + 2 * pad[1]

def paste_logo(base, cx, y, wlogo=300):
    lg = Image.open(LOGO).convert("RGBA")
    r = wlogo / lg.width
    lg = lg.resize((wlogo, int(lg.height * r)), Image.LANCZOS)
    # marco limpio: tarjeta blanca redondeada detras
    pad = 22
    card = Image.new("RGBA", (lg.width + pad * 2, lg.height + pad * 2), (0, 0, 0, 0))
    cd = ImageDraw.Draw(card)
    rrect(cd, (0, 0, card.width - 1, card.height - 1), 34, fill=(255, 255, 255, 242))
    card.alpha_composite(lg, (pad, pad))
    sh = Image.new("RGBA", base.size, (0, 0, 0, 0))
    sd = ImageDraw.Draw(sh)
    rrect(sd, (cx - card.width // 2 + 6, y + 10, cx + card.width // 2 + 6, y + card.height + 10), 34, fill=(0, 0, 0, 110))
    base.alpha_composite(sh.filter(ImageFilter.GaussianBlur(12)))
    base.alpha_composite(card, (cx - card.width // 2, y))
    return y + card.height

def product(hpx):
    p = Image.open(os.path.join(KB, "recortes", "principal.png")).convert("RGBA")
    r = hpx / p.height
    return p.resize((int(p.width * r), hpx), Image.LANCZOS)

def glow_at(base, cx, cy, rad, alpha=170, color=(255, 255, 255)):
    g = Image.new("RGBA", base.size, (0, 0, 0, 0))
    gd = ImageDraw.Draw(g)
    gd.ellipse((cx - rad, cy - rad * 0.7, cx + rad, cy + rad * 0.7), fill=color + (alpha,))
    base.alpha_composite(g.filter(ImageFilter.GaussianBlur(rad * 0.45)))

def beam(base, tip, p1, p2, alpha=95):
    b = Image.new("RGBA", base.size, (0, 0, 0, 0))
    bd = ImageDraw.Draw(b)
    bd.polygon([tip, p1, p2], fill=(255, 255, 255, alpha))
    base.alpha_composite(b.filter(ImageFilter.GaussianBlur(38)))

def benefit_row(d, y, items, f):
    total = 0; ws = []
    for s in items:
        bb = d.textbbox((0, 0), s, font=f); w = bb[2] - bb[0] + 44; ws.append((s, w, bb)); total += w
    gap = 18; total += gap * (len(items) - 1)
    x = (W - total) / 2
    for s, w, bb in ws:
        th = bb[3] - bb[1]
        rrect(d, (x, y, x + w, y + th + 26), (th + 26) / 2, fill=(255, 255, 255, 235))
        d.text((x + 22 - bb[0], y + 13 - bb[1]), s, font=f, fill=NAVY)
        x += w + gap
    return y

# ============ A1 — ANTES / DESPUÉS ============
def build_a1():
    bg = Image.open(os.path.join(PRO, "refl_a1_patio.png")).convert("RGB")
    bg = fill_cover(bg, W, H)
    left = bg.crop((0, 0, W // 2, H))
    right = bg.crop((W // 2, 0, W, H))
    # ANTES (izq): mas oscuro y frio
    left = ImageEnhance.Brightness(left).enhance(0.42)
    left = ImageEnhance.Color(left).enhance(0.45)
    # DESPUÉS (der): brillante, limpio y BLANCO (bajar lo amarillo)
    right = ImageEnhance.Brightness(right).enhance(1.28)
    right = ImageEnhance.Color(right).enhance(0.55)
    canvas = Image.new("RGBA", (W, H))
    canvas.paste(left, (0, 0)); canvas.paste(right, (W // 2, 0))

    # reflector real al centro-derecha, alumbrando su mitad con luz blanca
    p = product(320)
    px, py = W - p.width - 95, 580
    beam(canvas, (px + p.width // 2, py + p.height - 40), (W // 2 + 20, H - 500), (W + 170, H - 500), alpha=120)
    # charco de luz blanca en el piso del lado DESPUÉS
    glow_at(canvas, 3 * W // 4 + 30, H - 640, 330, alpha=95)
    glow_at(canvas, px + p.width // 2, py + p.height // 2, 210, alpha=120)
    canvas.alpha_composite(p, (px, py))
    glow_at(canvas, px + p.width // 2, py + int(p.height * 0.55), 130, alpha=205)

    d = ImageDraw.Draw(canvas)
    # divisor
    d.rectangle((W // 2 - 3, 620, W // 2 + 3, H - 480), fill=(255, 255, 255, 90))
    # chips ANTES / DESPUÉS (abajo del titular, sobre la escena)
    chip(d, W // 4, 950, "ANTES", font(F_BLACK, 40), WHITE, (0, 0, 0, 175))
    chip(d, 3 * W // 4, 950, "DESPUÉS", font(F_BLACK, 40), WHITE, ORANGE + (255,))

    # logo + titular
    paste_logo(canvas, W // 2, 60, 300)
    d = ImageDraw.Draw(canvas)
    f1 = font(F_BLACK, 128)
    t1, t2 = "SIN CABLE.", "SIN RECIBO."
    for i, (t, c) in enumerate([(t1, WHITE), (t2, (255, 138, 61))]):
        bb = d.textbbox((0, 0), t, font=f1)
        text_shadow(d, ((W - (bb[2] - bb[0])) / 2 - bb[0], 218 + i * 128), t, f1, c)
    fs = font(F_SEMI, 44)
    s = "Reflector solar: se carga solo con el sol"
    bb = d.textbbox((0, 0), s, font=fs)
    text_shadow(d, ((W - (bb[2] - bb[0])) / 2 - bb[0], 498), s, fs, WHITE, off=3)

    # fila de beneficios + precio + CTA
    benefit_row(d, H - 430, ["SOLAR", "ILUMINA COMO 500 W", "AGUANTA LLUVIA"], font(F_SEMI, 34))
    benefit_row(d, H - 352, ["CONTROL REMOTO", "HASTA 12 H DE LUZ"], font(F_SEMI, 34))
    fpz = font(F_BLACK, 64)
    s = "2 x $1,299"
    bb = d.textbbox((0, 0), s, font=fpz)
    pw = bb[2] - bb[0] + 90
    rrect(d, ((W - pw) / 2, H - 262, (W + pw) / 2, H - 148), 30, fill=ORANGE + (255,))
    d.text(((W - (bb[2] - bb[0])) / 2 - bb[0], H - 262 + (114 - (bb[3] - bb[1])) / 2 - bb[1]), s, font=fpz, fill=WHITE)
    chip(d, W // 2, H - 120, "Envío gratis a todo México", font(F_SEMI, 38), WHITE, (10, 90, 60, 235))
    canvas.convert("RGB").save(os.path.join(OUT, "A1-antes-despues.png"))
    print("A1 OK")

# ============ A2 — ¿NO VES QUIÉN TOCA TU PUERTA? ============
def build_a2():
    bg = Image.open(os.path.join(PRO, "refl_a2_porton.png")).convert("RGB")
    bg = fill_cover(bg, W, H)
    bg = ImageEnhance.Brightness(bg).enhance(0.92)
    canvas = bg.convert("RGBA")

    d = ImageDraw.Draw(canvas)
    paste_logo(canvas, W // 2, 60, 300)
    d = ImageDraw.Draw(canvas)
    f1 = font(F_BLACK, 104)
    lines = [("¿NO VES", WHITE), ("QUIÉN TOCA", (255, 138, 61)), ("TU PUERTA?", WHITE)]
    for i, (t, c) in enumerate(lines):
        bb = d.textbbox((0, 0), t, font=f1)
        text_shadow(d, ((W - (bb[2] - bb[0])) / 2 - bb[0], 225 + i * 108), t, f1, c)
    fs = font(F_SEMI, 46)
    s = "Luz donde no llega el cable"
    bb = d.textbbox((0, 0), s, font=fs)
    text_shadow(d, ((W - (bb[2] - bb[0])) / 2 - bb[0], 585), s, fs, WHITE, off=3)

    # reflector real abajo-derecha encendido
    p = product(360)
    px, py = W - p.width - 70, H - 640
    glow_at(canvas, px + p.width // 2, py + p.height // 2, 240, alpha=115)
    canvas.alpha_composite(p, (px, py))
    glow_at(canvas, px + p.width // 2, py + int(p.height * 0.55), 135, alpha=210)

    d = ImageDraw.Draw(canvas)
    benefit_row(d, H - 740, ["SOLAR", "ILUMINA COMO 500 W", "SIN CABLEADO"], font(F_SEMI, 30))
    fpz = font(F_BLACK, 64)
    s = "2 x $1,299"
    bb = d.textbbox((0, 0), s, font=fpz)
    pw = bb[2] - bb[0] + 90
    rrect(d, ((W - pw) / 2, H - 262, (W + pw) / 2, H - 148), 30, fill=ORANGE + (255,))
    d.text(((W - (bb[2] - bb[0])) / 2 - bb[0], H - 262 + (114 - (bb[3] - bb[1])) / 2 - bb[1]), s, font=fpz, fill=WHITE)
    chip(d, W // 2, H - 120, "Envío gratis a todo México", font(F_SEMI, 38), WHITE, (10, 90, 60, 235))
    canvas.convert("RGB").save(os.path.join(OUT, "A2-quien-toca.png"))
    print("A2 OK")

build_a1(); build_a2()
