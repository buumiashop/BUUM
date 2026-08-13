#!/usr/bin/env python3
"""SOLO LECTURA: linea base de resonancia de @buum.ia (posts existentes) para calibrar el umbral.
   Lee reach + guardados + compartidos + comentarios/likes de cada media y calcula tasa de resonancia.
   Guarda snapshot en BUUM Knowledge Base/06-contenido/baseline-ig.json. No publica."""
import sys, os, io, sys, json, urllib.request, urllib.parse
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.dirname(os.path.dirname(HERE)); V="v21.0"
def env(p):
    d={}
    for l in io.open(p,encoding="utf-8"):
        l=l.strip()
        if l and not l.startswith("#") and "=" in l: k,v=l.split("=",1); d[k.strip()]=v.strip()
    return d
tok=os.environ.get("META_USER_TOKEN") or (env(os.path.join(ROOT,"config","config.local.env")).get("META_USER_TOKEN") if os.path.exists(os.path.join(ROOT,"config","config.local.env")) else None) or sys.exit("Falta META_USER_TOKEN: variable de entorno o config/config.local.env")
UA={"User-Agent":"curl/8.4.0"}
def get(url,params):
    try:
        return json.load(urllib.request.urlopen(urllib.request.Request(url+"?"+urllib.parse.urlencode(params),headers=UA),timeout=40))
    except urllib.error.HTTPError as e: return {"__error__":e.code,"body":e.read().decode()[:200]}
    except Exception as e: return {"__error__":str(e)[:150]}
acc=get(f"https://graph.facebook.com/{V}/me/accounts",{"fields":"instagram_business_account","access_token":tok})
IG=acc["data"][0]["instagram_business_account"]["id"]
med=get(f"https://graph.facebook.com/{V}/{IG}/media",
        {"fields":"id,media_type,media_product_type,timestamp,permalink,like_count,comments_count,caption","limit":25,"access_token":tok})
rows=[]
for m in med.get("data",[]):
    mid=m["id"]
    ins=get(f"https://graph.facebook.com/{V}/{mid}/insights",{"metric":"reach,saved,shares","access_token":tok})
    d={x["name"]:x["values"][0]["value"] for x in ins.get("data",[])} if "data" in ins else {}
    reach=d.get("reach",0); saved=d.get("saved",0); shares=d.get("shares",0)
    likes=m.get("like_count",0); comments=m.get("comments_count",0)
    reson=(saved+shares+comments)
    rate=round(100*reson/reach,2) if reach else None
    rows.append({"id":mid,"type":m.get("media_product_type") or m.get("media_type"),"fecha":m.get("timestamp","")[:10],
                 "reach":reach,"saved":saved,"shares":shares,"comments":comments,"likes":likes,
                 "resonancia":reson,"tasa_resonancia_%":rate,"link":m.get("permalink","")})
    print(f"{m.get('media_product_type') or m.get('media_type'):8} {m.get('timestamp','')[:10]}  reach={reach:5} guard={saved:3} comp={shares:3} coment={comments:3} likes={likes:4}  resonancia={rate}%")
rates=[r["tasa_resonancia_%"] for r in rows if r["tasa_resonancia_%"] is not None]
prom=round(sum(rates)/len(rates),2) if rates else None
best=max(rates) if rates else None
snap={"cuenta":"@buum.ia","ig_id":IG,"posts":rows,"tasa_resonancia_promedio_%":prom,"tasa_resonancia_mejor_%":best}
out=os.path.join(ROOT,"KB","06-contenido","baseline-ig.json")
open(out,"w",encoding="utf-8").write(json.dumps(snap,ensure_ascii=False,indent=2))
print(f"\nLINEA BASE: resonancia promedio={prom}% | mejor={best}%  (n={len(rates)})")
print("Guardado ->",out)
