#!/usr/bin/env python3
"""RUTINA DIARIA DE MARKETING (BUUM) v2 - CREATIVA.
   Un 'director creativo' (Gemini texto) INVENTA un concepto y ESTILO nuevo cada vez (caricatura, acuarela,
   vintage, futurista, etc.), sin repetir (historial). Luego: keyframes en ese estilo (Gemini imagen) ->
   animacion (Kling/Replicate) -> montaje (ffmpeg: grade suave, glow, overlays de marca, musica)
   -> revision/video_FECHA.mp4 (NO publica). Cada comercial es TOTALMENTE NUEVO."""
import sys, os, io, sys, json, time, base64, random, datetime, subprocess, urllib.request
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
VID  = os.path.join(HERE, "video")  # pendiente migrar videos
REV  = os.path.join(HERE, "revision"); os.makedirs(REV, exist_ok=True)
FF   = "C:/Users/playg/Tools/ffmpeg-8.1.1-essentials_build/bin"
FONT = "C:/Windows/Fonts/ARLRDBD.TTF"
FOCO = os.path.join(ROOT, "buumia-catalogo", "foco-led-60w", "fotos", "60w-1-clean.png")
LOGO = os.path.join(ROOT, "buumia-catalogo", "marca", "logo-buum-horizontal.png")
MUS  = os.path.join(VID, "musica.mp3")
HISTP = os.path.join(HERE, "historial.json")

def env(p):
    d = {}
    for l in io.open(p, encoding="utf-8"):
        l = l.strip()
        if l and not l.startswith("#") and "=" in l:
            k, v = l.split("=", 1); d[k.strip()] = v.strip()
    return d
K = {**(env(os.path.join(ROOT,"config","config.local.env")) if os.path.exists(os.path.join(ROOT,"config","config.local.env")) else {}), **os.environ}
GKEY = K["GEMINI_API_KEY"]; RTOK = K["REPLICATE_API_TOKEN"]
UA = {"User-Agent": "curl/8.4.0"}
FECHA = datetime.date.today().isoformat()

# ---------- 0) DIRECTOR CREATIVO (Gemini texto) ----------
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
    raise RuntimeError("gemini_text agotado")

# Respaldo de conceptos variados por si el director de IA esta limitado (429). Estilos distintos.
FALLBACK = [
    {"estilo": "caricatura 2D", "titulo": "Enciende la magia", "sub": "Foco LED 60W", "realista": False,
     "prompt_inicio": "Flat 2D cartoon illustration, vertical, a cozy little house room at night, dark, a cute hanging light bulb OFF, playful vector style, orange and blue palette",
     "prompt_fin": "same flat 2D cartoon room but the hanging bulb is ON, glowing bright, warm rays filling the whole room, cheerful",
     "movimiento": "the cartoon bulb switches on and light fills the room, gentle"},
    {"estilo": "acuarela", "titulo": "Luz que abraza", "sub": "Ilumina tu hogar", "realista": False,
     "prompt_inicio": "soft watercolor painting, vertical, a dim cozy interior at dusk with a single hanging bulb unlit, gentle washes, paper texture",
     "prompt_fin": "same watercolor interior but the bulb glows warm, light blooms softly over the scene",
     "movimiento": "the painted light turns on and glows softly"},
    {"estilo": "futurista neon", "titulo": "El futuro brilla", "sub": "Potencia 60W", "realista": False,
     "prompt_inicio": "sleek futuristic dark room, vertical, neon accents, a modern pendant LED bulb off, cyber aesthetic, blue tones",
     "prompt_fin": "same futuristic room, the LED bulb blasts on with brilliant white light, neon glow, high tech",
     "movimiento": "the futuristic bulb powers on with a burst of light"},
    {"estilo": "vintage retro 50s", "titulo": "Clasico que ilumina", "sub": "Luz de calidad", "realista": False,
     "prompt_inicio": "1950s vintage advertising poster style, vertical, retro living room, a bulb off, halftone print look, warm muted colors",
     "prompt_fin": "same retro poster, the bulb shines bright with starburst light rays, classic ad vibe",
     "movimiento": "retro light turns on with a starburst shine"},
    {"estilo": "realista cinematografico", "titulo": "Ilumina todo", "sub": "Mucha luz, gasta poco", "realista": True,
     "prompt_inicio": "photorealistic cinematic vertical shot of a cozy modern mexican room at night, the LED bulb hanging from the ceiling OFF, dark, talavera details",
     "prompt_fin": "same room, the LED bulb ON flooding everything with clean bright white light, cozy and cinematic",
     "movimiento": "the bulb turns on and floods the room with light"},
]

hist = json.load(open(HISTP, encoding="utf-8")) if os.path.exists(HISTP) else []
recientes = ", ".join([h.get("estilo", "") for h in hist[-8:]]) or "ninguno"
DIR = (f"Eres el director creativo de marketing de BUUM, marca mexicana de focos LED 60W (mascota: gato Kitsune; "
       f"colores naranja #EA5003 y azul #001866). Inventa UN concepto de comercial VERTICAL 9:16 TOTALMENTE NUEVO y "
       f"original para redes, pensado para retener, conseguir likes, crear comunidad y CONVENCER de comprar. "
       f"Elige un ESTILO visual sorprendente y variado (ej: caricatura 2D, acuarela, 3D estilo Pixar, vintage retro "
       f"anos 50, futurista neon, claymation, papercraft, comic, cine noir, stop-motion, realista cinematografico, "
       f"anime, vitral, etc.). NO repitas estos estilos recientes: {recientes}. El concepto SIEMPRE gira en torno a la "
       f"LUZ, el foco o iluminar. Devuelve UNICAMENTE un JSON valido (sin texto extra, sin markdown) con las claves: "
       f'"estilo", "titulo" (titular corto on-brand en espanol, max 4 palabras), "sub" (subtitulo corto en espanol), '
       f'"realista" (true solo si es foto-realista; false si es arte/estilizado), '
       f'"prompt_inicio" (prompt en INGLES para el PRIMER frame: describe la escena/personajes en ese estilo, vertical 9:16), '
       f'"prompt_fin" (prompt en INGLES para el ULTIMO frame: misma escena y estilo pero con un cambio atractivo, '
       f'normalmente la LUZ encendida iluminando todo), '
       f'"movimiento" (prompt corto en INGLES del movimiento, camara fija, para Kling).')
print(f"== RUTINA {FECHA} | director creativo... ==")
try:
    raw = gemini_text(DIR)
    js = raw[raw.find("{"): raw.rfind("}") + 1]
    c = json.loads(js)
except Exception as e:
    usados = [h.get("estilo", "") for h in hist[-len(FALLBACK):]]
    opts = [f for f in FALLBACK if f["estilo"] not in usados] or FALLBACK
    c = random.choice(opts)
    print("   (director limitado, uso respaldo):", str(e)[:50])
print("   estilo:", c["estilo"], "| titulo:", c["titulo"])

# ---------- 1) keyframes en ese estilo (Gemini imagen) ----------
from PIL import Image, ImageDraw, ImageFont
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
        time.sleep(2)
    return False

# lienzo 9:16 (fuerza formato vertical). Si es realista, pega el foco real arriba.
canvas = Image.new("RGB", (1080, 1920), (128, 128, 128))
if c.get("realista"):
    src = Image.open(FOCO).convert("RGB"); fh = 380; fw = int(src.width * fh / src.height)
    canvas.paste(src.resize((fw, fh)), ((1080 - fw) // 2, 240))
cpath = os.path.join(HERE, "_canvas.png"); canvas.save(cpath)
on_p = os.path.join(HERE, "_on.png"); off_p = os.path.join(HERE, "_off.png")
S = " Vertical 9:16, llena TODO el cuadro de forma coherente. NO texto, NO logos, NO marcas, NO letras."
if not gemini_img(cpath, c["prompt_inicio"] + S, off_p): sys.exit("FALLO inicio")
if not gemini_img(off_p, c["prompt_fin"] + " Mismo encuadre y MISMO estilo." + S, on_p): sys.exit("FALLO fin")
print("1/3 keyframes OK")

# ---------- 2) animacion (Kling) ----------
def datauri(p): return "data:image/png;base64," + base64.b64encode(open(p, "rb").read()).decode()
H = {"Authorization": "Bearer " + RTOK, "Content-Type": "application/json", **UA}
ver = json.load(urllib.request.urlopen(urllib.request.Request(
    "https://api.replicate.com/v1/models/kwaivgi/kling-v1.6-pro", headers=H), timeout=40))["latest_version"]["id"]
NEG = "zoom, push in, camera movement, pan, second lamp, duplicate, two of everything, text, watermark, flicker, distorted"
body = {"version": ver, "input": {"prompt": c["movimiento"] + " Locked static camera, no zoom, no pan.",
        "negative_prompt": NEG, "duration": 5, "cfg_scale": 0.5,
        "start_image": datauri(off_p), "end_image": datauri(on_p)}}
d = json.load(urllib.request.urlopen(urllib.request.Request(
    "https://api.replicate.com/v1/predictions", data=json.dumps(body).encode(), headers=H), timeout=60))
geturl = d["urls"]["get"]; print("2/3 Kling", d["id"], "...")
clip = os.path.join(HERE, "_clip.mp4"); out = None
for _ in range(150):
    time.sleep(5)
    s = json.load(urllib.request.urlopen(urllib.request.Request(geturl, headers=H), timeout=60))
    if s["status"] == "succeeded": out = s["output"]; break
    if s["status"] in ("failed", "canceled"): sys.exit("Kling FALLO: " + str(s.get("error")))
urllib.request.urlretrieve(out if isinstance(out, str) else out[0], clip)

# ---------- 3) overlays + montaje ----------
print("3/3 montaje...")
W, Hh = 1080, 1920
ov = Image.new("RGBA", (W, Hh), (0, 0, 0, 0)); od = ImageDraw.Draw(ov)
for y in range(Hh):
    t = max(0.0, (y - Hh * 0.62) / (Hh * 0.38)); od.line([(0, y), (W, y)], fill=(2, 8, 30, int(170 * t)))
big = ImageFont.truetype(FONT, 84); mid = ImageFont.truetype(FONT, 44)
od.text((70, Hh - 360), c["titulo"], font=big, fill=(255, 255, 255, 255))
od.ellipse([70, Hh - 232, 90, Hh - 212], fill=(234, 80, 3, 255))
od.text((104, Hh - 244), c["sub"], font=mid, fill=(255, 255, 255, 235))
ovp = os.path.join(HERE, "_ovtext.png"); ov.save(ovp)
logo = Image.open(LOGO).convert("RGBA"); lh = 64; lw = int(logo.width * lh / logo.height)
logo = logo.resize((lw, lh)); chip = Image.new("RGBA", (lw + 48, lh + 32), (0, 0, 0, 0))
ImageDraw.Draw(chip).rounded_rectangle([0, 0, chip.width - 1, chip.height - 1], radius=20, fill=(255, 255, 255, 240))
chip.alpha_composite(logo, (24, 16)); bdp = os.path.join(HERE, "_badge.png"); chip.save(bdp)

dur = float(subprocess.check_output([f"{FF}/ffprobe", "-v", "error", "-show_entries", "format=duration",
            "-of", "default=nk=1:nw=1", clip]).decode().strip())
SD = round(dur / 0.9, 2)
scene = os.path.join(HERE, "_scene.mp4")
filt = ("[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setpts=PTS/0.9,fps=24,"
        "eq=contrast=1.05:saturation=1.16,vibrance=intensity=0.18[g0];"
        "[g0]split[a][b];[b]gblur=sigma=16,eq=brightness=0.05[bl];[a][bl]blend=all_mode=screen:all_opacity=0.22[gl];"
        f"[1:v]fade=t=in:st=0.8:d=1.1:alpha=1,fade=t=out:st={SD-0.4}:d=0.35:alpha=1[txt];[gl][txt]overlay=0:0[v1];"
        "[2:v]fade=t=in:st=0.8:d=1.1:alpha=1[bdg];[v1][bdg]overlay=30:30[v2]")
subprocess.run([f"{FF}/ffmpeg", "-y", "-loglevel", "error", "-i", clip,
    "-framerate", "24", "-loop", "1", "-t", str(SD), "-i", ovp,
    "-framerate", "24", "-loop", "1", "-t", str(SD), "-i", bdp,
    "-filter_complex", filt, "-map", "[v2]", "-an", "-t", str(SD), "-r", "24",
    "-c:v", "libx264", "-crf", "19", "-pix_fmt", "yuv420p", scene], check=True)
outv = os.path.join(REV, f"video_{FECHA}.mp4")
fo = round(SD - 1.2, 2)
subprocess.run([f"{FF}/ffmpeg", "-y", "-loglevel", "error", "-i", scene, "-i", MUS,
    "-filter_complex", f"[1:a]afade=t=in:st=0:d=1.0,afade=t=out:st={fo}:d=1.2,volume=0.9[a]",
    "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", outv], check=True)

hist.append({"fecha": FECHA, "estilo": c["estilo"], "titulo": c["titulo"], "sub": c["sub"]})
json.dump(hist, open(HISTP, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
open(os.path.join(REV, f"video_{FECHA}_nota.txt"), "w", encoding="utf-8").write(
    f"Fecha: {FECHA}\nEstilo: {c['estilo']}\nTitular: {c['titulo']} / {c['sub']}\n"
    f"Concepto (inicio): {c['prompt_inicio']}\nFormato: 9:16. NO publicado (revision).\n"
    f"Feedback del dueno (que te gusto / que no): \n")
for f in (cpath, on_p, off_p, clip, ovp, bdp, scene):
    try: os.remove(f)
    except: pass
print("LISTO ->", outv, "| estilo:", c["estilo"])
