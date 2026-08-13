# -*- coding: utf-8 -*-
"""Fondo BARATO con Replicate flux-dev (text-to-image, sin texto ni foco). ~2-3 centavos.
   Uso: python flux_bg.py <outname> "<prompt>"  -> contenido/pro/<outname>.png"""
import sys, json, os, io, sys, time, urllib.request, urllib.error
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
outname=sys.argv[1]; PROMPT=sys.argv[2]; AR=sys.argv[3] if len(sys.argv)>3 else "1:1"
MODEL="black-forest-labs/flux-dev"
def gen(out):
    body={"input":{"prompt":PROMPT,"aspect_ratio":AR,"output_format":"png","num_outputs":1}}
    d=None
    for i in range(4):
        try:
            d=json.load(urllib.request.urlopen(urllib.request.Request(
                f"https://api.replicate.com/v1/models/{MODEL}/predictions",data=json.dumps(body).encode(),headers=H),timeout=90)); break
        except urllib.error.HTTPError as e:
            print("crear HTTP",e.code,e.read().decode()[:160]); time.sleep(6*(i+1))
        except Exception as e:
            print("err",str(e)[:120]); time.sleep(6)
    if not d: return False
    g=d["urls"]["get"]
    for _ in range(90):
        time.sleep(3)
        s=json.load(urllib.request.urlopen(urllib.request.Request(g,headers=H),timeout=60))
        if s["status"]=="succeeded":
            o=s["output"]; url=o[0] if isinstance(o,list) else o; urllib.request.urlretrieve(url,out); return True
        if s["status"] in ("failed","canceled"): print("FALLO",s.get("error")); return False
    return False
print("Fondo barato flux-dev...")
print("OK" if gen(os.path.join(OUT,outname+".png")) else "FALLO")
