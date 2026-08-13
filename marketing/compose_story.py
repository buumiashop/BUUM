# -*- coding: utf-8 -*-
"""HISTORIA BUUM 9:16 (automatica, $0): gradiente de marca + foco real + logo + texto por codigo.
   Salida: contenido/pro/historia1.png"""
import os, io, sys, math
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
HERE=os.path.dirname(os.path.abspath(__file__)); PRO=os.path.join(HERE,"contenido","pro")
ROOT=os.path.dirname(HERE)
FOCO=os.path.join(ROOT,"activos/productos/foco-60w/60w-1-clean.png")  # pendiente migrar activo
LOGO=os.path.join(ROOT,"activos/marca/logo-oficial/logo-buum-oficial.png")
W,H=1080,1920
def F(sz,black=True): return ImageFont.truetype(r'C:/Windows/Fonts/'+('ariblk.ttf' if black else 'arialbd.ttf'),sz)

# gradiente vertical de marca (azul BUUM)
top=np.array([0,18,70]); bot=np.array([13,36,140])
g=np.zeros((H,W,3),np.uint8)
for y in range(H): g[y,:]=(top+(bot-top)*(y/H)).astype(np.uint8)
img=Image.fromarray(g,'RGB').convert('RGBA')

def blob(cx,cy,rx,ry,col,blur):
    L=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(L).ellipse([cx-rx,cy-ry,cx+rx,cy+ry],fill=col)
    return L.filter(ImageFilter.GaussianBlur(blur))
img=Image.alpha_composite(img, blob(540,1080,400,400,(255,255,255,70),120))
img=Image.alpha_composite(img, blob(540,1010,170,210,(255,255,252,180),60))

# foco real
foco=Image.open(FOCO).convert('RGBA'); fw=520; fh=int(foco.height*fw/foco.width); foco=foco.resize((fw,fh),Image.LANCZOS)
img.alpha_composite(foco,(540-fw//2,1076-fh//2))
img=img.convert('RGB'); d=ImageDraw.Draw(img)

def ctext(cx,y,txt,f,fill=(255,255,255)):
    bb=d.textbbox((0,0),txt,font=f); d.text((cx-(bb[2]-bb[0])/2,y),txt,font=f,fill=fill)
def sparkle(cx,cy,r,col=(255,214,10)):
    d.line([(cx-r,cy),(cx+r,cy)],fill=col,width=6); d.line([(cx,cy-r),(cx,cy+r)],fill=col,width=6)
for (x,y,r) in [(180,620,26),(910,700,22),(150,1250,18),(930,1300,24),(250,300,16)]: sparkle(x,y,r)

# logo oficial arriba
logo=Image.open(LOGO).convert('RGBA'); arr=np.array(logo)
if arr[...,3].min()>250:
    wm=(arr[...,0]>238)&(arr[...,1]>238)&(arr[...,2]>238); arr[wm,3]=0; logo=Image.fromarray(arr)
lh=110; lw=int(logo.width*lh/logo.height); logo=logo.resize((lw,lh),Image.LANCZOS)
img.paste(logo,(540-lw//2,80),logo)

# titular
ctext(540,300,'UN SOLO FOCO',F(96))
ctext(540,410,'ILUMINA TODO',F(96),(255,214,10))
# subtitulo
ctext(540,1520,'Foco LED 60W  ·  Luz blanca 6500K',F(40,False),(210,222,245))

# pill MUY PRONTO (naranja de marca)
t='MUY PRONTO'; f=F(46); bb=d.textbbox((0,0),t,font=f); tw=bb[2]-bb[0]
pw=tw+90; px=540-pw//2; py=1630
d.rounded_rectangle([px,py,px+pw,py+92],radius=46,fill=(234,80,3))
d.text((540-tw/2,py+20),t,font=f,fill=(255,255,255))
ctext(540,1770,'@buum.ia',F(34,False),(190,205,235))

out=os.path.join(PRO,"historia1.png"); img.save(out); print("OK ->",out)
