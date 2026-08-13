# -*- coding: utf-8 -*-
"""flux-kontext (Replicate, economico) para editar una foto real: limpiar/quitar texto, fondo estudio.
   Uso: python flux_kontext.py <outname> <input.jpg> <aspect> <prompt.txt> [modelo]
   modelo: pro (barato ~4c) | max (~8c). Salida: contenido/pro/<outname>.png"""
import sys, json, os, io, sys, time, base64, urllib.request, urllib.error
from PIL import Image, ImageOps
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.dirname(HERE)
def env(p):
    d={}
    for l in io.open(p,encoding="utf-8"):
        l=l.strip()
        if l and not l.startswith("#") and "=" in l: k,v=l.split("=",1); d[k.strip()]=v.strip()
    return d
tok=os.environ.get("REPLICATE_API_TOKEN") or (env(os.path.join(ROOT,"config","config.local.env")).get("REPLICATE_API_TOKEN") if os.path.exists(os.path.join(ROOT,"config","config.local.env")) else None) or sys.exit("Falta REPLICATE_API_TOKEN: variable de entorno o config/config.local.env")
H={"Authorization":"Bearer "+tok,"Content-Type":"application/json","User-Agent":"curl/8.4.0"}
OUT=os.path.join(HERE,"contenido","pro"); os.makedirs(OUT,exist_ok=True)
outname, inp, aspect, promptfile = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
model = "black-forest-labs/flux-kontext-"+(sys.argv[5] if len(sys.argv)>5 else "pro")
PROMPT=io.open(promptfile,encoding="utf-8").read().strip()
im=ImageOps.exif_transpose(Image.open(inp).convert("RGB")); s=1024/max(im.size)
if s<1: im=im.resize((int(im.width*s),int(im.height*s)))
buf=io.BytesIO(); im.save(buf,"PNG"); datauri="data:image/png;base64,"+base64.b64encode(buf.getvalue()).decode()
def gen(out):
    body={"input":{"prompt":PROMPT,"input_image":datauri,"aspect_ratio":aspect,"output_format":"png","safety_tolerance":2}}
    d=None
    for i in range(4):
        try:
            d=json.load(urllib.request.urlopen(urllib.request.Request(
                f"https://api.replicate.com/v1/models/{model}/predictions",data=json.dumps(body).encode(),headers=H),timeout=90)); break
        except urllib.error.HTTPError as e: print("HTTP",e.code,e.read().decode()[:160]); time.sleep(6*(i+1))
        except Exception as e: print("err",str(e)[:120]); time.sleep(6)
    if not d: return False
    g=d["urls"]["get"]
    for _ in range(100):
        time.sleep(3); s=json.load(urllib.request.urlopen(urllib.request.Request(g,headers=H),timeout=60))
        if s["status"]=="succeeded":
            o=s["output"]; url=o[0] if isinstance(o,list) else o; urllib.request.urlretrieve(url,out); return True
        if s["status"] in ("failed","canceled"): print("FALLO",s.get("error")); return False
    return False
print("Editando con", model, "...")
print("OK" if gen(os.path.join(OUT,outname+".png")) else "FALLO")
