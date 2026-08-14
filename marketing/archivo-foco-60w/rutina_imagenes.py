#!/usr/bin/env python3
"""RUTINA DIARIA DE IMAGENES (BUUM). Barata (solo Gemini, sin Kling).
   Director creativo inventa un POSTER/anuncio NUEVO cada vez (estilo variado, sin repetir) ->
   imagen 4:5 (Gemini) -> overlay de marca (logo + titular) -> revision_imagenes/imagen_FECHA.png.
   Cada imagen TOTALMENTE NUEVA. NO publica."""
import sys, os, io, sys, json, time, base64, random, datetime, urllib.request
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REV  = os.path.join(HERE, "revision_imagenes"); os.makedirs(REV, exist_ok=True)
FONT = "C:/Windows/Fonts/ARLRDBD.TTF"
FOCO = os.path.join(ROOT, "activos", "productos", "foco-60w", "60w-1-clean.png")  # pendiente migrar activo
LOGO = os.path.join(ROOT, "activos", "marca", "logo-buum-horizontal.png")
HISTP = os.path.join(HERE, "historial_img.json")

def env(p):
    d = {}
    for l in io.open(p, encoding="utf-8"):
        l = l.strip()
        if l and not l.startswith("#") and "=" in l:
            k, v = l.split("=", 1); d[k.strip()] = v.strip()
    return d
GKEY = os.environ.get("GEMINI_API_KEY") or (env(os.path.join(ROOT,"config","config.local.env")).get("GEMINI_API_KEY") if os.path.exists(os.path.join(ROOT,"config","config.local.env")) else None) or sys.exit("Falta GEMINI_API_KEY: variable de entorno o config/config.local.env")
FECHA = datetime.date.today().isoformat()

def gemini_text(prompt, model="gemini-2.5-flash", tries=4):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={GKEY}"
    body = {"contents": [{"parts": [{"text": prompt}]}]}
    for i in range(tries):
        try:
            r = urllib.request.Request(url, data=json.dumps(body).encode(), headers={"Content-Type": "application/json"})
            d = json.load(urllib.request.urlopen(r, timeout=120))
            return d["candidates"][0]["content"]["parts"][0]["text"]
        except Exception as e:
            print("   texto:", str(e)[:60]); time.sleep(8 * (i + 1))
    raise RuntimeError("texto agotado")

def gemini_img(img, prompt, out, tries=3):
    b = base64.b64encode(open(img, "rb").read()).decode()
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-image:generateContent?key={GKEY}"
    body = {"contents": [{"parts": [{"inlineData": {"mimeType": "image/png", "data": b}}, {"text": prompt}]}],
            "generationConfig": {"responseModalities": ["TEXT", "IMAGE"]}}
    for _ in range(tries):
        try:
            r = urllib.request.Request(url, data=json.dumps(body).encode(), headers={"Content-Type": "application/json"})
            d = json.load(urllib.request.urlopen(r, timeout=200))
            for p in d.get("candidates", [{}])[0].get("content", {}).get("parts", []):
                if "inlineData" in p:
                    open(out, "wb").write(base64.b64decode(p["inlineData"]["data"])); return True
        except Exception as e: print("   img:", e)
        time.sleep(3)
    return False

FALLBACK = [
    {"estilo": "caricatura 2D", "titulo": "Enciende la magia", "sub": "Foco LED 60W", "realista": False,
     "prompt_imagen": "flat 2D cartoon poster, a cute glowing light bulb as hero, cozy room, orange and blue palette, cheerful, vector style"},
    {"estilo": "acuarela", "titulo": "Luz que abraza", "sub": "Ilumina tu hogar", "realista": False,
     "prompt_imagen": "soft watercolor poster, a warm glowing bulb lighting a cozy interior, gentle washes, paper texture, inviting"},
    {"estilo": "futurista neon", "titulo": "El futuro brilla", "sub": "Potencia 60W", "realista": False,
     "prompt_imagen": "sleek futuristic neon poster, a high-tech LED bulb glowing brilliant white, cyber aesthetic, blue and orange neon"},
    {"estilo": "vintage retro 50s", "titulo": "Clasico que ilumina", "sub": "Luz de calidad", "realista": False,
     "prompt_imagen": "1950s retro advertising poster, a shining bulb with starburst rays, halftone print, warm muted classic ad look"},
    {"estilo": "realista", "titulo": "Ilumina todo", "sub": "Mucha luz, gasta poco", "realista": True,
     "prompt_imagen": "photorealistic cozy mexican room beautifully lit by a bright LED bulb hanging from the ceiling, warm cinematic, talavera details"},
]

hist = json.load(open(HISTP, encoding="utf-8")) if os.path.exists(HISTP) else []
recientes = ", ".join([h.get("estilo", "") for h in hist[-8:]]) or "ninguno"
DIR = (f"Eres el director creativo de BUUM (focos LED 60W, marca mexicana, mascota gato Kitsune, naranja #EA5003 y azul "
       f"#001866). Inventa UNA imagen-anuncio (poster) VERTICAL 4:5 TOTALMENTE NUEVA para redes, que enganche, consiga "
       f"likes y haga comprar. Estilo visual variado y sorprendente (caricatura, acuarela, 3D, vintage, futurista neon, "
       f"comic, claymation, papercraft, realista, etc.). NO repitas estos estilos recientes: {recientes}. Siempre sobre "
       f"la LUZ/el foco. Devuelve SOLO JSON valido sin markdown con claves: "
       f'"estilo", "titulo" (titular corto espanol, max 4 palabras), "sub" (subtitulo corto), '
       f'"realista" (true si foto-realista; false si arte), "prompt_imagen" (prompt en INGLES para generar el poster en ese estilo).')
print(f"== IMAGEN {FECHA} | director...")
try:
    raw = gemini_text(DIR); c = json.loads(raw[raw.find("{"): raw.rfind("}") + 1])
except Exception as e:
    usados = [h.get("estilo", "") for h in hist[-len(FALLBACK):]]
    c = random.choice([f for f in FALLBACK if f["estilo"] not in usados] or FALLBACK)
    print("   (respaldo):", str(e)[:40])
print("   estilo:", c["estilo"], "| titulo:", c["titulo"])

# lienzo 4:5 (fuerza formato). Si realista, pega el foco real.
W, Hh = 1080, 1350
canvas = Image.new("RGB", (W, Hh), (128, 128, 128))
if c.get("realista"):
    src = Image.open(FOCO).convert("RGB"); fh = 360; fw = int(src.width * fh / src.height)
    canvas.paste(src.resize((fw, fh)), ((W - fw) // 2, 170))
cpath = os.path.join(HERE, "_imgcanvas.png"); canvas.save(cpath)
base = os.path.join(HERE, "_img.png")
if not gemini_img(cpath, c["prompt_imagen"] + " Vertical 4:5, fills the whole frame, coherent. NO text, NO logos, NO letters.", base):
    sys.exit("FALLO imagen")

# overlay de marca (scrim + titular + sub + logo)
img = Image.open(base).convert("RGB").resize((W, Hh)).convert("RGBA")
ov = Image.new("RGBA", (W, Hh), (0, 0, 0, 0)); od = ImageDraw.Draw(ov)
for y in range(Hh):
    t = max(0.0, (y - Hh * 0.60) / (Hh * 0.40)); od.line([(0, y), (W, y)], fill=(2, 8, 30, int(175 * t)))
big = ImageFont.truetype(FONT, 82); mid = ImageFont.truetype(FONT, 42)
od.text((64, Hh - 250), c["titulo"], font=big, fill=(255, 255, 255, 255))
od.ellipse([64, Hh - 132, 84, Hh - 112], fill=(234, 80, 3, 255))
od.text((98, Hh - 144), c["sub"], font=mid, fill=(255, 255, 255, 235))
logo = Image.open(LOGO).convert("RGBA"); lh = 60; lw = int(logo.width * lh / logo.height)
logo = logo.resize((lw, lh)); chip = Image.new("RGBA", (lw + 44, lh + 30), (0, 0, 0, 0))
ImageDraw.Draw(chip).rounded_rectangle([0, 0, chip.width - 1, chip.height - 1], radius=18, fill=(255, 255, 255, 240))
chip.alpha_composite(logo, (22, 15))
img = Image.alpha_composite(img, ov); img.alpha_composite(chip, (28, 28))
outp = os.path.join(REV, f"imagen_{FECHA}.png"); img.convert("RGB").save(outp, quality=92)

hist.append({"fecha": FECHA, "estilo": c["estilo"], "titulo": c["titulo"]})
json.dump(hist, open(HISTP, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
open(os.path.join(REV, f"imagen_{FECHA}_nota.txt"), "w", encoding="utf-8").write(
    f"Fecha: {FECHA}\nEstilo: {c['estilo']}\nTitular: {c['titulo']} / {c['sub']}\nNO publicado.\nFeedback: \n")
for f in (cpath, base):
    try: os.remove(f)
    except: pass
print("LISTO ->", outp, "| estilo:", c["estilo"])
