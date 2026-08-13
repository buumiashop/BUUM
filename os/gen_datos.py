# -*- coding: utf-8 -*-
"""Genera buumia-os/datos.js = TRABAJOS (galería de lo entregado, leído de carpetas) + RUTINAS + CONEXIONES.
   Para que el Centro de Mando muestre TODO sin entrar a carpetas sueltas."""
import os, io, json, datetime
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
MK = os.path.join(ROOT, "buumia-tienda", "marketing")

def rel(p):  # ruta relativa al html (buumia-os/) + versión anti-caché por fecha de archivo
    r = os.path.relpath(p, HERE).replace("\\", "/")
    try: return r + "?v=" + str(int(os.path.getmtime(p)))
    except: return r

def fecha(p):
    try: return datetime.date.fromtimestamp(os.path.getmtime(p)).isoformat()
    except: return ""

# Observaciones/advertencias por archivo (se muestran en la Galería del OS)
OBS = {
 "reflector-tus-noches.png": "⚠️ Práctica, NO publicar así. El reflector es genérico (aún no lo vendemos) y dice 'solar' pero no se ve celda solar (parece empotrado tomando luz de la casa). Aprobado solo por lo bonito (luz + logo).",
}

trabajos = []
# 1) Logo oficial
logo = os.path.join(ROOT, "buumia-catalogo", "marca", "logo-oficial", "logo-buum-oficial.png")
if os.path.exists(logo):
    trabajos.append({"img": rel(logo), "titulo": "Logo oficial BUUM", "tipo": "Marca",
                     "estado": "Aprobado", "nota": "Original del manual + contorno blanco", "fecha": fecha(logo)})
# 1.5) Mascota oficial
masc = os.path.join(ROOT, "buumia-catalogo", "marca", "mascota-oficial.png")
if os.path.exists(masc):
    trabajos.append({"img": rel(masc), "titulo": "Mascota oficial BUUM", "tipo": "Marca",
                     "estado": "Oficial", "nota": "gato Kitsune del manual", "fecha": fecha(masc)})
# 2) Anuncios aprobados
apr = os.path.join(MK, "aprobados")
if os.path.isdir(apr):
    for f in sorted(os.listdir(apr)):
        if f.lower().endswith((".png", ".jpg", ".jpeg", ".mp4")):
            p = os.path.join(apr, f)
            trabajos.append({"img": rel(p), "titulo": "Anuncio aprobado · reflector", "tipo": "Anuncio",
                             "estado": "9/9/9", "nota": f, "fecha": fecha(p)})
# 2.5) Contenido POR AUTORIZAR (pasó QC, espera OK del dueño — NO publicado)
pa = os.path.join(MK, "por-autorizar")
if os.path.isdir(pa):
    for f in sorted(os.listdir(pa)):
        if f.lower().endswith((".png", ".jpg", ".jpeg", ".mp4")):
            p = os.path.join(pa, f)
            trabajos.append({"img": rel(p), "titulo": "Contenido gatito · por autorizar", "tipo": "Por autorizar",
                             "estado": "Por autorizar", "nota": f, "fecha": fecha(p)})
# 3) Mascota (práctica gatitos)
gat = os.path.join(MK, "gatitos")
if os.path.isdir(gat):
    for f in sorted(os.listdir(gat)):
        if f.lower().endswith((".png", ".jpg", ".jpeg", ".mp4")):
            p = os.path.join(gat, f)
            trabajos.append({"img": rel(p), "titulo": "Mascota BUUM (práctica)", "tipo": "Gatito",
                             "estado": "Demo", "nota": f, "fecha": fecha(p)})

for t in trabajos:
    t["obs"] = OBS.get(os.path.basename(t["img"].split("?")[0]), "")

rutinas = [
 {"nombre": "Rutina semanal (motor del CEO)", "hace": "Toma el arsenal → 4 filtros → agenda la semana → escribe el calendario del panel",
  "cuando": "Domingos 20:00", "estado": "Activa (en tu PC)", "salida": "Publicaciones / Calendario"},
 {"nombre": "Rutina de gatitos (práctica)", "hace": "Genera mascota (imágenes/video/historias) → 4 filtros → publica en @buum.ia → mide y aprende",
  "cuando": "Diario (al desplegar en la nube)", "estado": "Por desplegar", "salida": "Galería · @buum.ia"},
 {"nombre": "Contenido de producto", "hace": "Anuncios de producto con el método director + luz realista",
  "cuando": "Al subir productos reales", "estado": "En pausa", "salida": "Galería / Meta"},
]

conex = [
 ["Gemini (imágenes/IA)", "🎨", "#8E75F8", "on", "Creación", "Activo", "generando"],
 ["Replicate (video)", "🎬", "#111", "on", "Video", "Activo", "Kling/Flux"],
 ["Facebook 𝗕𝗨𝗨𝗠", "👍", "#1877F2", "on", "Publicaciones", "Conectado", "listo para publicar"],
 ["Instagram @buum.ia", "📸", "#d62976", "on", "Publicaciones", "Conectado", "listo para publicar"],
 ["Shopify", "🛍️", "#95BF47", "pend", "Tienda", "Borrador", "tema listo, sin publicar"],
 ["Pagos (Mercado Pago)", "💳", "#00b1ea", "offl", "Cobro", "—", "por conectar"],
]

data = {"generado": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "trabajos": trabajos, "rutinas": rutinas, "conexiones": conex}
io.open(os.path.join(HERE, "datos.js"), "w", encoding="utf-8").write(
    "window.DATOS=" + json.dumps(data, ensure_ascii=False) + ";")
print("datos.js:", len(trabajos), "trabajos,", len(rutinas), "rutinas,", len(conex), "conexiones")
