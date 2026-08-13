# -*- coding: utf-8 -*-
"""MOTOR CREATIVO BUUM — automatiza brief->imagen con gpt-image-1 (consistente, con reintento).
Uso:
  python motor_creativo.py <outname> <t2i|edit> <WIDTHxHEIGHT> <prompt.txt> [ref1.png ref2.png ...]
- t2i  = /images/generations (texto puro; máximo estilo/creatividad)
- edit = /images/edits (con referencias; producto exacto)
Reintenta hasta 3 veces ante error de red/servidor. Salida en contenido/pro/<outname>.png"""
import os, io, sys, base64, requests, time
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.dirname(HERE)
def env(p):
    d={}
    for l in io.open(p,encoding="utf-8"):
        l=l.strip()
        if l and not l.startswith("#") and "=" in l: k,v=l.split("=",1); d[k.strip()]=v.strip()
    return d
KEY=os.environ.get("OPENAI_API_KEY") or (env(os.path.join(ROOT,"config","config.local.env")).get("OPENAI_API_KEY") if os.path.exists(os.path.join(ROOT,"config","config.local.env")) else None) or sys.exit("Falta OPENAI_API_KEY: variable de entorno o config/config.local.env")
OUT=os.path.join(HERE,"contenido","pro"); os.makedirs(OUT,exist_ok=True)

def run():
    outname, mode, size, promptfile = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    refs = sys.argv[5:]
    prompt = io.open(promptfile, encoding="utf-8").read().strip()
    out = os.path.join(OUT, outname+".png")
    H={"Authorization":"Bearer "+KEY}
    for attempt in range(3):
        try:
            if mode=="t2i":
                r=requests.post("https://api.openai.com/v1/images/generations",
                    headers={**H,"Content-Type":"application/json"},
                    json={"model":"gpt-image-1","prompt":prompt,"size":size,"quality":"high","n":1,"moderation":"low"},
                    timeout=300)
            else:
                files=[("image[]",(os.path.basename(p),open(p,"rb"),"image/png")) for p in refs]
                r=requests.post("https://api.openai.com/v1/images/edits",
                    headers=H, data={"model":"gpt-image-1","prompt":prompt,"size":size,"quality":"high","n":"1","moderation":"low"},
                    files=files, timeout=300)
            if r.status_code==200:
                j=r.json(); open(out,"wb").write(base64.b64decode(j["data"][0]["b64_json"]))
                if j.get("usage"): print("usage", j["usage"])
                print("OK ->", out); return True
            print("HTTP", r.status_code, r.text[:200]); time.sleep(6*(attempt+1))
        except Exception as e:
            print("err", str(e)[:150]); time.sleep(6*(attempt+1))
    print("FALLO tras 3 intentos"); return False

if __name__=="__main__":
    run()
