# -*- coding: utf-8 -*-
"""A1/A2 v2 — estandar PRO de la escuela: logo con marco (sin caja), scrim, titular pesado
   con clave amarilla + garabato, fila de iconos dibujados, rayos, sin look plantilla."""
import os, io, sys, math
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
KB   = os.path.join(ROOT, "activos", "productos", "R54W50")
OUT  = os.path.join(HERE, "contenido", "pro")
LOGO = os.path.join(ROOT, "activos", "marca", "logo-buum-marco.png")  # marco solido p/ fondo oscuro

W, H = 1080, 1920
ORANGE = (234, 80, 3); YELLOW = (255, 204, 0); WHITE = (255, 255, 255)
F_BLACK = "C:/Windows/Fonts/seguibl.ttf"; F_SEMI = "C:/Windows/Fonts/seguisb.ttf"
def font(p, s): return ImageFont.truetype(p, s)

def fill_cover(img, w, h):
    r = max(w / img.width, h / img.height)
    img = img.resize((int(img.width * r) + 1, int(img.height * r) + 1), Image.LANCZOS)
    x = (img.width - w) // 2; y = (img.height - h) // 2
    return img.crop((x, y, x + w, y + h))

def text_shadow(d, xy, s, f, fill, off=5):
    d.text((xy[0] + off, xy[1] + off), s, font=f, fill=(0, 0, 0, 210))
    d.text(xy, s, font=f, fill=fill)

def scrim(base, y0, y1, top_alpha, bottom_alpha):
    band = Image.new("L", (1, y1 - y0))
    for i in range(y1 - y0):
        band.putpixel((0, i), int(top_alpha + (bottom_alpha - top_alpha) * i / (y1 - y0)))
    band = band.resize((W, y1 - y0))
    black = Image.new("RGBA", (W, y1 - y0), (0, 0, 0, 255)); black.putalpha(band)
    base.alpha_composite(black, (0, y0))

def paste_logo(base, cx, y, wlogo=330):
    lg = Image.open(LOGO).convert("RGBA"); r = wlogo / lg.width
    lg = lg.resize((wlogo, int(lg.height * r)), Image.LANCZOS)
    sh = lg.copy().filter(ImageFilter.GaussianBlur(6))
    dark = Image.new("RGBA", lg.size, (0, 0, 0, 160)); sh = Image.composite(dark, Image.new("RGBA", lg.size, (0,0,0,0)), sh.split()[3])
    base.alpha_composite(sh, (cx - lg.width // 2 + 5, y + 7))
    base.alpha_composite(lg, (cx - lg.width // 2, y))
    return y + lg.height

def garabato(d, x0, x1, y, color=ORANGE, wdt=9):
    # subrayado a mano: dos trazos ondulados superpuestos
    for k, dy in [(0, 0), (1, 7)]:
        pts = []
        n = 14
        for i in range(n + 1):
            t = i / n
            pts.append((x0 + (x1 - x0) * t, y + dy + math.sin(t * math.pi * 2.2 + k) * 5))
        d.line(pts, fill=color + (255,), width=wdt, joint="curve")

def burst(d, cx, cy, r0, r1, n=7, color=YELLOW, wdt=7, a0=200, spread=360, start=0):
    for i in range(n):
        ang = math.radians(start + spread * i / n)
        d.line([(cx + r0 * math.cos(ang), cy + r0 * math.sin(ang)),
                (cx + r1 * math.cos(ang), cy + r1 * math.sin(ang))], fill=color + (a0,), width=wdt)

def rays(base, cx, cy, rad, n=12, alpha=60):
    g = Image.new("RGBA", base.size, (0, 0, 0, 0)); gd = ImageDraw.Draw(g)
    for i in range(n):
        ang = math.radians(360 * i / n + 11)
        gd.line([(cx, cy), (cx + rad * math.cos(ang), cy + rad * math.sin(ang))],
                fill=(255, 255, 255, alpha), width=16 if i % 2 else 8)
    base.alpha_composite(g.filter(ImageFilter.GaussianBlur(10)))

def glow_at(base, cx, cy, rad, alpha=170):
    g = Image.new("RGBA", base.size, (0, 0, 0, 0))
    ImageDraw.Draw(g).ellipse((cx - rad, cy - rad * 0.7, cx + rad, cy + rad * 0.7), fill=(255, 255, 255, alpha))
    base.alpha_composite(g.filter(ImageFilter.GaussianBlur(rad * 0.45)))

# ---- iconos dibujados (linea blanca, estilo limpio) ----
def icon_sol(d, cx, cy, s):
    d.ellipse((cx - s*0.32, cy - s*0.32, cx + s*0.32, cy + s*0.32), outline=WHITE, width=6)
    for i in range(8):
        a = math.radians(45 * i)
        d.line([(cx + s*0.45*math.cos(a), cy + s*0.45*math.sin(a)), (cx + s*0.62*math.cos(a), cy + s*0.62*math.sin(a))], fill=WHITE, width=6)
def icon_rayo(d, cx, cy, s):
    p = [(cx + s*0.12, cy - s*0.6), (cx - s*0.3, cy + s*0.1), (cx - s*0.02, cy + s*0.1), (cx - s*0.12, cy + s*0.6), (cx + s*0.3, cy - s*0.12), (cx + s*0.03, cy - s*0.12)]
    d.polygon(p, fill=WHITE)
def icon_lluvia(d, cx, cy, s):
    d.arc((cx - s*0.5, cy - s*0.55, cx + s*0.15, cy + 0), 180, 360, fill=WHITE, width=6)
    d.arc((cx - s*0.25, cy - s*0.7, cx + s*0.5, cy - s*0.05), 180, 20, fill=WHITE, width=6)
    d.line([(cx - s*0.5 + 3, cy - s*0.26), (cx + s*0.5 - 3, cy - s*0.26)], fill=WHITE, width=6)
    for k in (-1, 0, 1):
        d.line([(cx + k*s*0.28 + s*0.06, cy + s*0.05), (cx + k*s*0.28 - s*0.06, cy + s*0.45)], fill=WHITE, width=6)
def icon_control(d, cx, cy, s):
    d.rounded_rectangle((cx - s*0.22, cy - s*0.55, cx + s*0.22, cy + s*0.55), radius=int(s*0.16), outline=WHITE, width=6)
    d.ellipse((cx - s*0.09, cy - s*0.36, cx + s*0.09, cy - s*0.18), fill=WHITE)
    for yy in (0.02, 0.28):
        d.ellipse((cx - s*0.07, cy + s*yy, cx + s*0.07, cy + s*yy + s*0.14), outline=WHITE, width=4)
def icon_reloj(d, cx, cy, s):
    d.ellipse((cx - s*0.45, cy - s*0.45, cx + s*0.45, cy + s*0.45), outline=WHITE, width=6)
    d.line([(cx, cy), (cx, cy - s*0.28)], fill=WHITE, width=6)
    d.line([(cx, cy), (cx + s*0.2, cy + s*0.1)], fill=WHITE, width=6)

def icon_row(canvas, d, y, items):
    # items: [(draw_fn, "LINEA1", "LINEA2")]
    n = len(items); cell = (W - 120) / n
    fc = font(F_SEMI, 26)
    for i, (fn, l1, l2) in enumerate(items):
        cx = int(60 + cell * i + cell / 2)
        fn(d, cx, y, 64)
        for j, t in enumerate([l1, l2]):
            bb = d.textbbox((0, 0), t, font=fc)
            d.text((cx - (bb[2] - bb[0]) / 2 - bb[0], y + 52 + j * 30 - bb[1]), t, font=fc, fill=WHITE)

ICONS = [(icon_sol, "SE CARGA", "CON EL SOL"), (icon_rayo, "ILUMINA", "COMO 500 W"),
         (icon_lluvia, "AGUANTA", "LA LLUVIA"), (icon_control, "CONTROL", "REMOTO"),
         (icon_reloj, "HASTA 12 H", "DE LUZ")]

def price_cta(d, y):
    fpz = font(F_BLACK, 66); s = "2 x $1,299"
    bb = d.textbbox((0, 0), s, font=fpz); pw = bb[2] - bb[0] + 96
    d.rounded_rectangle(((W - pw) / 2, y, (W + pw) / 2, y + 118), radius=32, fill=ORANGE + (255,))
    d.text(((W - (bb[2] - bb[0])) / 2 - bb[0], y + (118 - (bb[3] - bb[1])) / 2 - bb[1]), s, font=fpz, fill=WHITE)
    fs = font(F_SEMI, 40); s2 = "Envío gratis a todo México"
    bb2 = d.textbbox((0, 0), s2, font=fs)
    text_shadow(d, ((W - (bb2[2] - bb2[0])) / 2 - bb2[0], y + 140), s2, fs, WHITE, off=3)

# ================= A1 =================
def a1():
    canvas = fill_cover(Image.open(os.path.join(KB, "escenas", "escena-a1-patio-chatgpt.png")).convert("RGB"), W, H).convert("RGBA")
    d = ImageDraw.Draw(canvas)
    paste_logo(canvas, W // 2, 44, 330)
    d = ImageDraw.Draw(canvas)
    # titular pesado en la mitad negra (clave amarilla + garabato)
    f1 = font(F_BLACK, 100)
    text_shadow(d, (64, 300), "SIN", f1, WHITE)
    text_shadow(d, (64, 402), "CABLE.", f1, WHITE)
    text_shadow(d, (64, 545), "SIN", f1, YELLOW)
    text_shadow(d, (64, 647), "RECIBO.", f1, YELLOW)
    bb = d.textbbox((64, 647), "RECIBO.", font=f1)
    garabato(d, 64, bb[2], 775)
    fs = font(F_SEMI, 42)
    text_shadow(d, (64, 830), "Se carga solo con el sol", fs, WHITE, off=3)
    # chispas junto al reflector de la escena (garabato de energia)
    burst(d, 700, 300, 60, 108, n=5, color=YELLOW, wdt=7, spread=170, start=150)
    # chips ANTES / DESPUES integrados (sin caja blanca)
    fch = font(F_BLACK, 42)
    text_shadow(d, (170, 1160), "ANTES", fch, (185, 185, 185), off=4)
    text_shadow(d, (700, 1160), "DESPUÉS", fch, YELLOW, off=4)
    bb = d.textbbox((700, 1160), "DESPUÉS", font=fch)
    garabato(d, 700, bb[2], 1222, color=ORANGE, wdt=7)
    # base: scrim + iconos + precio
    scrim(canvas, 1380, H, 0, 235)
    d = ImageDraw.Draw(canvas)
    icon_row(canvas, d, 1500, ICONS)
    price_cta(d, 1665)
    canvas.convert("RGB").save(os.path.join(OUT, "A1-PRO.png"))
    print("A1 PRO OK")

# ================= A2 =================
def a2():
    canvas = fill_cover(Image.open(os.path.join(KB, "escenas", "escena-a2-porton-chatgpt.png")).convert("RGB"), W, H).convert("RGBA")
    scrim(canvas, 0, 640, 200, 0)
    d = ImageDraw.Draw(canvas)
    paste_logo(canvas, W // 2, 44, 330)
    d = ImageDraw.Draw(canvas)
    f1 = font(F_BLACK, 106)
    for i, (t, c) in enumerate([("¿NO VES", WHITE), ("QUIÉN TOCA", YELLOW), ("TU PUERTA?", WHITE)]):
        bb = d.textbbox((0, 0), t, font=f1)
        text_shadow(d, ((W - (bb[2] - bb[0])) / 2 - bb[0], 218 + i * 110), t, f1, c)
    bb = d.textbbox((0, 0), "QUIÉN TOCA", font=f1)
    x0 = (W - (bb[2] - bb[0])) / 2
    garabato(d, x0, x0 + (bb[2] - bb[0]), 445, wdt=8)
    fs = font(F_SEMI, 46); s = "Luz donde no llega el cable"
    bb = d.textbbox((0, 0), s, font=fs)
    text_shadow(d, ((W - (bb[2] - bb[0])) / 2 - bb[0], 585), s, fs, WHITE, off=3)
    # reflector real con rayos variados + charco de luz (integrado, no pegado)
    p = Image.open(os.path.join(KB, "recortes", "principal.png")).convert("RGBA")
    r = 330 / p.height; p = p.resize((int(p.width * r), 330), Image.LANCZOS)
    px, py = W - p.width - 84, H - 855
    ccx, ccy = px + p.width // 2, py + p.height // 2
    rays(canvas, ccx, ccy, 300, n=14, alpha=52)
    glow_at(canvas, ccx, ccy, 250, alpha=130)
    canvas.alpha_composite(p, (px, py))
    glow_at(canvas, ccx, py + int(p.height * 0.55), 135, alpha=215)
    # charco de luz al piso
    glow_at(canvas, ccx - 60, H - 330, 280, alpha=65)
    d = ImageDraw.Draw(canvas)
    burst(d, px - 30, py + 40, 44, 86, n=4, color=YELLOW, wdt=6, spread=120, start=180)
    # base: scrim + iconos + precio
    scrim(canvas, 1380, H, 0, 235)
    d = ImageDraw.Draw(canvas)
    icon_row(canvas, d, 1500, ICONS)
    price_cta(d, 1665)
    canvas.convert("RGB").save(os.path.join(OUT, "A2-PRO.png"))
    print("A2 PRO OK")

a1(); a2()
