#!/usr/bin/env python3
"""Verificacion SOLO LECTURA de la plomeria Meta (publicar + medir). No publica nada."""
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
    q=urllib.parse.urlencode(params)
    try:
        return json.load(urllib.request.urlopen(urllib.request.Request(url+"?"+q,headers=UA),timeout=40))
    except urllib.error.HTTPError as e:
        return {"__error__":e.code,"body":e.read().decode()[:300]}
    except Exception as e:
        return {"__error__":str(e)[:200]}
print("1) Validez del token (/me)...")
me=get(f"https://graph.facebook.com/{V}/me",{"fields":"id,name","access_token":tok})
print("   ",json.dumps(me,ensure_ascii=False)[:200])
if "__error__" in me: print("TOKEN INVALIDO O EXPIRADO -> requiere re-autorizacion del Fundador."); sys.exit(1)
print("2) Paginas + cuenta IG (/me/accounts)...")
acc=get(f"https://graph.facebook.com/{V}/me/accounts",{"fields":"id,name,instagram_business_account","access_token":tok})
if "__error__" in acc or not acc.get("data"): print("   ",json.dumps(acc,ensure_ascii=False)[:300]); sys.exit(1)
page=acc["data"][0]; PAGE_ID=page["id"]; IG=page.get("instagram_business_account",{}).get("id")
print(f"   Pagina FB: {page['name']} ({PAGE_ID}) | IG business: {IG}")
print("3) Lectura de metricas IG (medir)...")
if IG:
    ig=get(f"https://graph.facebook.com/{V}/{IG}",{"fields":"username,followers_count,media_count","access_token":tok})
    print("   ",json.dumps(ig,ensure_ascii=False)[:300])
print("VERIFICACION OK: token vivo, canales alcanzables, metricas legibles. NADA PUBLICADO.")
