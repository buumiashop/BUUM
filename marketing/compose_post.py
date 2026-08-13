# -*- coding: utf-8 -*-
"""PLANTILLA DE MARCA BUUM: fondo (barato) + logo real + foco real + texto/iconos por codigo.
   Garantiza logo perfecto, foco real y texto correcto, con estilo consistente. Salida: contenido/pro/post_taller.png"""
import os, io, sys, math
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
HERE=os.path.dirname(os.path.abspath(__file__)); PRO=os.path.join(HERE,"contenido","pro")
ROOT=os.path.dirname(HERE)
BGNAME=sys.argv[1] if len(sys.argv)>1 else "bg_taller"
OUTNAME=sys.argv[2] if len(sys.argv)>2 else "post_taller"
BG=os.path.join(PRO,BGNAME+".png")
FOCO=os.path.join(ROOT,"activos/productos/foco-60w/60w-1-clean.png")  # pendiente migrar activo
LOGO=os.path.join(ROOT,"activos/marca/logo-oficial/logo-buum-oficial.png")
W=Hh=1024
def F(sz,black=True): return ImageFont.truetype(r'C:/Windows/Fonts/'+('ariblk.ttf' if black else 'arialbd.ttf'),sz)

bg=Image.open(BG).convert('RGB').resize((W,Hh))
bg=ImageEnhance.Brightness(bg).enhance(0.58)
img=bg.convert('RGBA')

# glow general que ilumina el espacio
def blob(cx,cy,rx,ry,col,blur):
    L=Image.new('RGBA',(W,Hh),(0,0,0,0)); ImageDraw.Draw(L).ellipse([cx-rx,cy-ry,cx+rx,cy+ry],fill=col)
    return L.filter(ImageFilter.GaussianBlur(blur))
img=Image.alpha_composite(img, blob(512,560,360,330,(255,255,255,95),85))
img=Image.alpha_composite(img, blob(512,830,320,80,(255,255,252,130),45))   # charco de luz en piso
img=Image.alpha_composite(img, blob(512,600,130,150,(255,255,252,205),35))  # nucleo brillante

# foco real (colgando)
foco=Image.open(FOCO).convert('RGBA')
fw=250; fh=int(foco.height*fw/foco.width); foco=foco.resize((fw,fh),Image.LANCZOS)
foco_top=560-fh//2
cordon=Image.new('RGBA',(W,Hh),(0,0,0,0)); ImageDraw.Draw(cordon).line([(512,250),(512,foco_top+18)],fill=(70,70,78,230),width=4)
img=Image.alpha_composite(img,cordon)
img.alpha_composite(foco,(512-fw//2,foco_top))

# bandas oscuras arriba/abajo para legibilidad
band=Image.new('RGBA',(W,Hh),(0,0,0,0)); bd=ImageDraw.Draw(band)
for y in range(0,250): bd.line([(0,y),(W,y)],fill=(6,9,15,int(205*(1-y/250))))
for y in range(852,Hh): bd.line([(0,y),(W,y)],fill=(6,9,15,int(215*((y-852)/(Hh-852)))))
img=Image.alpha_composite(img,band); img=img.convert('RGB'); d=ImageDraw.Draw(img)

def ctext(cx,y,txt,f,fill=(255,255,255)):
    bb=d.textbbox((0,0),txt,font=f); d.text((cx-(bb[2]-bb[0])/2,y),txt,font=f,fill=fill)

# logo oficial (key blanco si opaco)
logo=Image.open(LOGO).convert('RGBA'); arr=np.array(logo)
if arr[...,3].min()>250:
    wm=(arr[...,0]>238)&(arr[...,1]>238)&(arr[...,2]>238); arr[wm,3]=0; logo=Image.fromarray(arr)
lh=84; lw=int(logo.width*lh/logo.height); logo=logo.resize((lw,lh),Image.LANCZOS)
img.paste(logo,(34,24),logo)

# titular + subtitulo
ctext(512,120,'ILUMINA TODO UN ESPACIO',F(46))
ctext(512,172,'CON UN SOLO FOCO',F(46))
ctext(512,230,'Luz blanca 6500K   •   60W',F(24,False),(210,222,240))
ctext(360,past_y if False else 700,'ANTES',F(28),(180,188,200))
ctext(664,700,'DESPUES',F(28),(255,255,255))

# iconos de beneficios (dibujados a mano, blancos sobre circulo azul)
BLUE=(16,42,196); Wc=(255,255,255)
def icon(kind,cx,cy):
    if kind=='sun':
        d.ellipse([cx-7,cy-7,cx+7,cy+7],fill=Wc)
        for a in range(0,360,45):
            x,y=math.cos(math.radians(a)),math.sin(math.radians(a))
            d.line([(cx+11*x,cy+11*y),(cx+17*x,cy+17*y)],fill=Wc,width=3)
    elif kind=='bolt':
        d.polygon([(cx+4,cy-14),(cx-9,cy+2),(cx-1,cy+2),(cx-4,cy+14),(cx+10,cy-3),(cx+1,cy-3)],fill=Wc)
    elif kind=='e360':
        d.pieslice([cx-12,cy-14,cx+12,cy+10],200,340,fill=Wc)
        for dx in (-7,0,7): d.line([(cx+dx,cy+9),(cx+dx,cy+15)],fill=Wc,width=2)
    elif kind=='leaf':
        d.ellipse([cx-10,cy-12,cx+8,cy+10],fill=Wc); d.line([(cx-6,cy+7),(cx+5,cy-8)],fill=BLUE,width=2)
    elif kind=='clock':
        d.ellipse([cx-12,cy-12,cx+12,cy+12],outline=Wc,width=3)
        d.line([(cx,cy),(cx,cy-7)],fill=Wc,width=2); d.line([(cx,cy),(cx+6,cy+1)],fill=Wc,width=2)

items=[('sun','LUZ BLANCA','6500K'),('bolt','60W ALTA','POTENCIA'),('e360','ILUMINACION','360'),('leaf','AHORRA','ENERGIA'),('clock','LARGA','DURACION')]
centers=[512+(i-2)*178 for i in range(5)]; cy=900; R=30
for (k,l1,l2),cx in zip(items,centers):
    d.ellipse([cx-R,cy-R,cx+R,cy+R],fill=BLUE); icon(k,cx,cy)
    ctext(cx,cy+R+8,l1,F(15)); ctext(cx,cy+R+26,l2,F(15))

out=os.path.join(PRO,OUTNAME+".png"); img.save(out); print("OK ->",out)
