# -*- coding: utf-8 -*-
"""Lote de lanzamiento v2 — 6 FORMATOS DISTINTOS de la serie BUUM (escuela):
1 HEROE · 2 FICHA coleccionable · 3 EN TU ESPACIO (polaroid) · 4 DATO BUUM ·
5 ANTES/DESPUES · 6 MASCOTA. Rotacion de formatos, misma familia (paleta+logo+tipografia)."""
import os
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ESC = os.path.join(ROOT, "activos", "productos", "R54W50", "escenas", "lote-2")
MARCA = os.path.join(ROOT, "activos", "marca")
OUT = os.path.join(HERE, "contenido", "lote-lanzamiento")
os.makedirs(OUT, exist_ok=True)

W, H = 1080, 1350
NARANJA = (234, 80, 3); NAVY = (0, 24, 102); AZUL = (16, 42, 196)
BLANCO = (255, 255, 255); CREMA = (244, 241, 236)

def F(nombre, tam):
    return ImageFont.truetype(r"C:\Windows\Fonts\%s" % nombre, tam)

logo_claro = Image.open(os.path.join(MARCA, "logo-buum-marco.png")).convert("RGBA")
logo_oscuro = Image.open(os.path.join(MARCA, "logo-buum-marco-oscuro.png")).convert("RGBA")
def logo_en(im, oscuro=False, w=230, pos=(44, 44)):
    lg = (logo_oscuro if oscuro else logo_claro).copy()
    lg = lg.resize((w, int(w * lg.height / lg.width)), Image.LANCZOS)
    im.alpha_composite(lg, pos)

def fondo(src, foco_y=0.35):
    im = Image.open(os.path.join(ESC, src)).convert("RGB")
    r = max(W / im.width, H / im.height)
    im = im.resize((int(im.width * r) + 1, int(im.height * r) + 1), Image.LANCZOS)
    x = (im.width - W) // 2
    y = max(0, min(im.height - H, int(im.height * foco_y)))
    return im.crop((x, y, x + W, y + H)).convert("RGBA")

def sombra(d, xy, t, f, fill, s=4):
    d.text((xy[0]+s, xy[1]+s+1), t, font=f, fill=(0, 6, 26, 170)); d.text(xy, t, font=f, fill=fill)

# ---------- 1) HEROE (la aprobada, se queda) ----------
# 01-llego-buum.jpg ya existe del lote v1 — se conserva tal cual.

# ---------- 2) FICHA COLECCIONABLE (formato estrella) ----------
im = Image.new("RGBA", (W, H), NARANJA)
d = ImageDraw.Draw(im)
for yy in range(0, H, 8):  # textura sutil de lineas
    d.line([(0, yy), (W, yy)], fill=(255, 110, 40, 18))
card = [70, 150, W-70, H-90]
d.rounded_rectangle(card, 36, fill=BLANCO, outline=NAVY, width=8)
d.text((100, 180), "FICHA BUUM · No. 001", font=F("arialbd.ttf", 40), fill=NARANJA)
d.text((100, 235), "REFLECTOR SOLAR 50W", font=F("ariblk.ttf", 62), fill=NAVY)
prod = Image.open(os.path.join(ROOT, "tienda", "tema-pro", "assets", "refl-armado-tight.png")).convert("RGBA")
pw = 640; prod = prod.resize((pw, int(pw * prod.height / prod.width)), Image.LANCZOS)
im.alpha_composite(prod, ((W - pw)//2, 320))
y = 860
stats = [("BRILLO", "ilumina como 500W", 0.95), ("CARGA", "solar · gratis", 1.0), ("AGUANTE", "IP66 lluvia y polvo", 0.9), ("DURACIÓN", "hasta 12 h de luz", 0.85)]
for nom, txt, pct in stats:
    d.text((110, y), nom, font=F("arialbd.ttf", 34), fill=NAVY)
    d.rounded_rectangle([320, y+6, 660, y+30], 12, fill=(230, 234, 246))
    d.rounded_rectangle([320, y+6, 320 + int(340*pct), y+30], 12, fill=NARANJA)
    d.text((680, y), txt, font=F("arialbd.ttf", 30), fill=(90, 100, 130))
    y += 62
d.rounded_rectangle([100, y+16, 560, y+94], 22, fill=NARANJA)
d.text((124, y+32), "2 × $1,299 · envío gratis", font=F("arialbd.ttf", 38), fill=BLANCO)
d.text((600, y+34), "★★★★★", font=F("arialbd.ttf", 44), fill=(255, 196, 0))
logo_en(im, oscuro=True, w=200, pos=(W-260, 176))
im.convert("RGB").save(os.path.join(OUT, "02-ficha-buum.jpg"), "JPEG", quality=90)
print("OK 02 ficha")

# ---------- 3) EN TU ESPACIO (polaroid) ----------
im = Image.new("RGBA", (W, H), CREMA)
d = ImageDraw.Draw(im)
d.rectangle([0, 0, W, 14], fill=NARANJA)
foto = fondo("gen-06.png", 0.18).resize((904, 1000), Image.LANCZOS)
marco = Image.new("RGBA", (960, 1150), BLANCO)
marco.paste(foto, (28, 28))
marco = marco.rotate(-2, expand=True, fillcolor=(0,0,0,0), resample=Image.BICUBIC)
sh = Image.new("RGBA", im.size, (0,0,0,0)); sd = ImageDraw.Draw(sh)
sd.rounded_rectangle([70, 90, 70+marco.width-10, 90+marco.height-10], 18, fill=(120, 130, 160, 90))
im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(14)))
im.alpha_composite(marco, (55, 70))
d = ImageDraw.Draw(im)
d.text((90, 1165), "EN TU NEGOCIO", font=F("arialbd.ttf", 40), fill=NARANJA)
d.text((90, 1215), "El único abierto de la cuadra.", font=F("ariblk.ttf", 58), fill=NAVY)
logo_en(im, oscuro=True, w=190, pos=(W-240, H-160))
im.convert("RGB").save(os.path.join(OUT, "03-en-tu-negocio.jpg"), "JPEG", quality=90)
print("OK 03 polaroid")

# ---------- 4) DATO BUUM (educativo claro) ----------
im = Image.new("RGBA", (W, H), CREMA)
d = ImageDraw.Draw(im)
d.rectangle([0, 0, 16, H], fill=NARANJA)
d.text((80, 130), "DATO BUUM", font=F("arialbd.ttf", 46), fill=NARANJA)
d.text((70, 210), "12", font=F("ariblk.ttf", 380), fill=NAVY)
d.text((560, 400), "horas", font=F("ariblk.ttf", 110), fill=NAVY)
d.text((80, 640), "de luz con una sola carga de sol.", font=F("arialbd.ttf", 52), fill=(60, 70, 100))
d.text((80, 715), "Sin cables. Sin recibo. Sin pretextos.", font=F("arialbd.ttf", 44), fill=(120, 130, 155))
prod = Image.open(os.path.join(ROOT, "tienda", "tema-pro", "assets", "refl-armado-tight.png")).convert("RGBA")
pw = 560; prod = prod.resize((pw, int(pw * prod.height / prod.width)), Image.LANCZOS)
im.alpha_composite(prod, (W - pw - 60, H - int(pw * prod.height / prod.width) - 90))
d.rectangle([80, 800, 420, 812], fill=NARANJA)
logo_en(im, oscuro=True, w=210, pos=(64, H-150))
im.convert("RGB").save(os.path.join(OUT, "04-dato-12h.jpg"), "JPEG", quality=90)
print("OK 04 dato")

# ---------- 5) ANTES / DESPUES (pattern interrupt) ----------
base = fondo("gen-05.png", 0.30)
antes = ImageEnhance.Brightness(base.convert("RGB")).enhance(0.16)
antes = ImageEnhance.Color(antes).enhance(0.5).convert("RGBA")
im = base.copy()
mitad = W // 2
im.paste(antes.crop((0, 0, mitad, H)), (0, 0))
d = ImageDraw.Draw(im)
d.rectangle([mitad-7, 0, mitad+7, H], fill=NARANJA)
d.rounded_rectangle([50, 110, 320, 190], 16, fill=(0, 10, 30, 220))
d.text((84, 128), "ANTES", font=F("ariblk.ttf", 46), fill=(160, 170, 195))
d.rounded_rectangle([mitad+50, 110, mitad+430, 190], 16, fill=NARANJA)
d.text((mitad+84, 128), "CON BUUM", font=F("ariblk.ttf", 46), fill=BLANCO)
sc = Image.new("RGBA", (W, 330), (0, 8, 30, 0))
sd = ImageDraw.Draw(sc)
for yy in range(330):
    sd.line([(0, yy), (W, yy)], fill=(0, 8, 30, int(230 * (yy/330)**1.3)))
im.alpha_composite(sc, (0, H-330))
d = ImageDraw.Draw(im)
sombra(d, (56, H-268), "LA MISMA CASA.", F("ariblk.ttf", 74), BLANCO)
sombra(d, (56, H-178), "OTRA NOCHE.", F("ariblk.ttf", 74), NARANJA)
d.text((56, H-84), "Reflector solar 50W · se instala en minutos", font=F("arialbd.ttf", 40), fill=(230, 236, 255))
logo_en(im, w=220, pos=(W-270, 40))
im.convert("RGB").save(os.path.join(OUT, "05-antes-despues.jpg"), "JPEG", quality=90)
print("OK 05 antes/despues")

# ---------- 6) MASCOTA (Kitsune presenta) ----------
im = Image.new("RGBA", (W, H), NAVY)
d = ImageDraw.Draw(im)
for i, yy in enumerate(range(0, H, 90)):  # rayos diagonales sutiles
    d.line([(0, yy), (W, yy - 260)], fill=(20, 40, 130), width=34)
gato = Image.open(os.path.join(MARCA, "mascota-oficial.png")).convert("RGBA")
gw = 620; gato = gato.resize((gw, int(gw * gato.height / gato.width)), Image.LANCZOS)
im.alpha_composite(gato, ((W-gw)//2 - 140, H - gato.height - 40))
# globo de dialogo
d.rounded_rectangle([420, 240, W-56, 560], 40, fill=BLANCO)
d.polygon([(560, 560), (640, 560), (520, 660)], fill=BLANCO)
d.text((470, 285), "¡Ya abrimos!", font=F("ariblk.ttf", 74), fill=NARANJA)
d.text((470, 390), "Luz solar para tu casa", font=F("arialbd.ttf", 44), fill=NAVY)
d.text((470, 450), "o negocio, sin recibo.", font=F("arialbd.ttf", 44), fill=NAVY)
prod = Image.open(os.path.join(ROOT, "tienda", "tema-pro", "assets", "refl-armado-tight.png")).convert("RGBA")
pw = 470; prod = prod.resize((pw, int(pw * prod.height / prod.width)), Image.LANCZOS)
card = Image.new("RGBA", (pw+40, int(pw * prod.height / prod.width)+40), BLANCO)
card.paste(prod, (20, 20), prod)
im.alpha_composite(card, (W - pw - 90, 720))
d.rounded_rectangle([56, H-150, 620, H-64], 24, fill=NARANJA)
d.text((84, H-128), "Envío GRATIS a todo México", font=F("arialbd.ttf", 40), fill=BLANCO)
logo_en(im, w=230, pos=(44, 44))
im.convert("RGB").save(os.path.join(OUT, "06-mascota-ya-abrimos.jpg"), "JPEG", quality=90)
print("OK 06 mascota")
print("LOTE v2 COMPLETO")
