#!/usr/bin/env python3
"""Publicador SEGURO y parametrizado del BIS (paso 7 del protocolo).
   NO tiene contenido hardcodeado. Publica LA pieza y EL copy que se le pasan, y SOLO con --publish.
   Por defecto es DRY-RUN (muestra qué haría, no publica). Uso:
     python publicar_pieza.py <video.mp4> <caption.txt> [--fb] [--ig] [--publish]
   Sin --publish => dry-run. Sin --fb/--ig => ambos.
   El gate humano (Fundador) es OBLIGATORIO antes de usar --publish (Constitucion Art. 17)."""
import sys, os, io, sys, time, json, urllib.request, urllib.parse, mimetypes, uuid
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
args=sys.argv[1:]
flags=[a for a in args if a.startswith("--")]; pos=[a for a in args if not a.startswith("--")]
if len(pos)<2: sys.exit(__doc__)
VIDEO,CAPFILE=pos[0],pos[1]
PUBLISH="--publish" in flags
do_fb=("--fb" in flags) or not ("--fb" in flags or "--ig" in flags)
do_ig=("--ig" in flags) or not ("--fb" in flags or "--ig" in flags)
if not os.path.exists(VIDEO): sys.exit("No existe el video: "+VIDEO)
CAPTION=io.open(CAPFILE,encoding="utf-8").read().strip() if os.path.exists(CAPFILE) else CAPFILE
print("="*54); print("PIEZA:",VIDEO); print("CANALES:", ("FB " if do_fb else "")+("IG" if do_ig else ""))
print("MODO:", "PUBLICAR EN VIVO" if PUBLISH else "DRY-RUN (no publica)")
print("-- COPY --\n"+CAPTION+"\n"+"="*54)
# Chequeo simple anti-deshonestidad en el copy (aviso, no bloqueo duro)
low=CAPTION.lower()
for bad in ["garant","10 año","10 anos","lista de espera","$","precio","cómpralo","compralo","pídelo","pidelo","oferta","descuento"]:
    if bad in low: print(f"[AVISO honestidad] el copy contiene '{bad}' — confirma que es apropiado (producto real/vendible).")
if not PUBLISH:
    print("\nDRY-RUN: todo listo. Para publicar (tras visto bueno del Fundador): agregar --publish"); sys.exit(0)
# --- PUBLICAR ---
def api(url,data=None,files=None,base="https://graph.facebook.com"):
    if files is None and data is not None:
        body=urllib.parse.urlencode(data).encode(); h=dict(UA);
        return json.load(urllib.request.urlopen(urllib.request.Request(url,data=body,headers=h),timeout=300))
acc=json.load(urllib.request.urlopen(urllib.request.Request(
    f"https://graph.facebook.com/{V}/me/accounts?"+urllib.parse.urlencode({"fields":"id,name,access_token,instagram_business_account","access_token":tok}),headers=UA),timeout=40))
page=acc["data"][0]; PAGE_ID=page["id"]; PAGE_TOKEN=page["access_token"]; IG=page["instagram_business_account"]["id"]
print("Pagina:",page["name"],PAGE_ID,"| IG:",IG)
if do_fb:
    print("FACEBOOK: subiendo...")
    b="----b"+uuid.uuid4().hex; CRLF="\r\n"; out=io.BytesIO()
    for k,v in {"description":CAPTION,"access_token":PAGE_TOKEN}.items():
        out.write(("--"+b+CRLF).encode()); out.write(('Content-Disposition: form-data; name="%s"%s%s'%(k,CRLF,CRLF)).encode()); out.write((v+CRLF).encode())
    fn=os.path.basename(VIDEO); out.write(("--"+b+CRLF).encode())
    out.write(('Content-Disposition: form-data; name="source"; filename="%s"%s'%(fn,CRLF)).encode())
    out.write(("Content-Type: video/mp4%s%s"%(CRLF,CRLF)).encode()); out.write(open(VIDEO,"rb").read()); out.write(CRLF.encode()); out.write(("--"+b+"--"+CRLF).encode())
    r=urllib.request.Request(f"https://graph-video.facebook.com/{V}/{PAGE_ID}/videos",data=out.getvalue(),headers={**UA,"Content-Type":"multipart/form-data; boundary="+b})
    j=json.load(urllib.request.urlopen(r,timeout=600)); print("   ", "OK id="+j["id"] if "id" in j else json.dumps(j)[:300])
if do_ig:
    print("IG: subiendo a hosting publico (catbox)...")
    b="----b"+uuid.uuid4().hex; CRLF="\r\n"; out=io.BytesIO()
    for k,v in {"reqtype":"fileupload"}.items():
        out.write(("--"+b+CRLF).encode()); out.write(('Content-Disposition: form-data; name="%s"%s%s'%(k,CRLF,CRLF)).encode()); out.write((v+CRLF).encode())
    out.write(("--"+b+CRLF).encode()); out.write(('Content-Disposition: form-data; name="fileToUpload"; filename="BUUM.mp4"%s'%CRLF).encode())
    out.write(("Content-Type: video/mp4%s%s"%(CRLF,CRLF)).encode()); out.write(open(VIDEO,"rb").read()); out.write(CRLF.encode()); out.write(("--"+b+"--"+CRLF).encode())
    up=urllib.request.urlopen(urllib.request.Request("https://catbox.moe/user/api.php",data=out.getvalue(),headers={**UA,"Content-Type":"multipart/form-data; boundary="+b}),timeout=600).read().decode().strip()
    print("   url:",up)
    cont=api(f"https://graph.facebook.com/{V}/{IG}/media",{"media_type":"REELS","video_url":up,"caption":CAPTION,"share_to_feed":"true","access_token":tok})
    cid=cont.get("id"); print("   contenedor:",cid)
    for _ in range(40):
        time.sleep(6); s=json.load(urllib.request.urlopen(urllib.request.Request(f"https://graph.facebook.com/{V}/{cid}?"+urllib.parse.urlencode({"fields":"status_code","access_token":tok}),headers=UA),timeout=40))
        if s.get("status_code")=="FINISHED":
            pub=api(f"https://graph.facebook.com/{V}/{IG}/media_publish",{"creation_id":cid,"access_token":tok}); print("   ","OK media="+pub["id"] if "id" in pub else json.dumps(pub)[:300]); break
        if s.get("status_code")=="ERROR": print("   ERROR proceso"); break
print("FIN.")
