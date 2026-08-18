# -*- coding: utf-8 -*-
"""Lote de lanzamiento organico (6 piezas, 1080x1350 4:5) — FASE post-nucleo.
Identidad social BUUM: kicker MAYUSCULAS naranja + titular Arial Black grande +
acento naranja + logo oficial con marco blanco SIEMPRE en la misma esquina.
Publico: texto GRANDE (vista cansada), acentos correctos. Sin inventar promesas.
"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ESC = os.path.join(ROOT, "activos", "productos", "R54W50", "escenas", "lote-2")
LOGO = os.path.join(ROOT, "activos", "marca", "logo-buum-marco.png")
OUT = os.path.join(HERE, "contenido", "lote-lanzamiento")
os.makedirs(OUT, exist_ok=True)

W, H = 1080, 1350
NARANJA = (234, 80, 3)
BLANCO = (255, 255, 255)

F_KICK = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 46)
F_TIT = ImageFont.truetype(r"C:\Windows\Fonts\ariblk.ttf", 108)
F_TIT2 = ImageFont.truetype(r"C:\Windows\Fonts\ariblk.ttf", 88)
F_SUB = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 44)

PIEZAS = [
 ("01-llego-buum",      "gen-01.png", "YA ESTAMOS ABIERTOS",           ["LLEGÓ", "BUUM"],            "Iluminación solar · envío gratis a todo México", 0.30),
 ("02-sin-recibo",      "gen-04.png", "REFLECTOR SOLAR 50W",           ["SIN CABLE,", "SIN RECIBO"], "2 piezas $1,299 · envío gratis", 0.35),
 ("03-en-tu-negocio",   "gen-06.png", "EN TU NEGOCIO",                 ["ILUMINA", "COMO 500W"],     "Se carga solo con el sol", 0.42),
 ("04-en-tu-patio",     "gen-05.png", "EN TU PATIO",                   ["LA NOCHE", "ES TUYA"],      "Hasta 12 horas de luz", 0.30),
 ("05-hecho-para-mx",   "gen-17.png", "AGUANTA LLUVIA, SOL Y POLVO",   ["HECHO PARA", "MÉXICO"],     "Certificación NOM · protección IP66", 0.30),
 ("06-de-dia-carga",    "gen-20.png", "DE DÍA CARGA",                  ["DE NOCHE", "ILUMINA"],      "Con el sol. Gratis. Todos los días.", 0.30),
]

logo = Image.open(LOGO).convert("RGBA")
logo = logo.resize((240, int(240 * logo.height / logo.width)), Image.LANCZOS)

def fondo(src, foco_y):
    im = Image.open(os.path.join(ESC, src)).convert("RGB")
    r = max(W / im.width, H / im.height)
    im = im.resize((int(im.width * r) + 1, int(im.height * r) + 1), Image.LANCZOS)
    x = (im.width - W) // 2
    y = max(0, min(im.height - H, int(im.height * foco_y - H * 0.35)))
    return im.crop((x, y, x + W, y + H))

def sombra(d, xy, texto, fuente, fill):
    x, y = xy
    d.text((x + 4, y + 5), texto, font=fuente, fill=(0, 6, 26, 160))
    d.text((x, y), texto, font=fuente, fill=fill)

for nombre, src, kicker, titulo, sub, foco_y in PIEZAS:
    im = fondo(src, foco_y).convert("RGBA")
    # scrim inferior (legibilidad): degradado azul-noche
    sc = Image.new("L", (1, H), 0)
    for yy in range(H):
        t = max(0, (yy - int(H * 0.52)) / (H * 0.48))
        sc.putpixel((0, yy), int(210 * (t ** 1.4)))
    grad = Image.new("RGBA", (W, H), (0, 10, 40, 255))
    im = Image.composite(grad, im, sc.resize((W, H)))
    d = ImageDraw.Draw(im)
    # logo SIEMPRE arriba-izquierda
    im.alpha_composite(logo, (44, 44))
    # bloque de texto abajo-izquierda
    y = H - 210 - 118 * len(titulo)
    sombra(d, (56, y), kicker, F_KICK, NARANJA)
    y += 66
    ftit = F_TIT if max(d.textlength(t, font=F_TIT) for t in titulo) <= W - 112 else F_TIT2
    for linea in titulo:
        sombra(d, (52, y), linea, ftit, BLANCO)
        y += ftit.size + 10
    d.rectangle([56, y + 6, 56 + 210, y + 18], fill=NARANJA)  # acento naranja
    y += 40
    sombra(d, (56, y), sub, F_SUB, (235, 240, 255))
    im.convert("RGB").save(os.path.join(OUT, nombre + ".jpg"), "JPEG", quality=90, optimize=True)
    print("OK", nombre)
print("LOTE COMPLETO ->", OUT)
