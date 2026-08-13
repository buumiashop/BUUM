# -*- coding: utf-8 -*-
"""Limpieza FIEL y AUTOMATICA de fotos reales de producto (no-generativo, escalable).
   rembg isnet-general-use + alpha matting + realce -> PNG transparente HD.
   Uso: python limpiar_producto.py <carpeta_recepcion> <carpeta_biblioteca> <archivo>=<nombre> ..."""
import os, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from rembg import remove, new_session
from PIL import Image, ImageOps, ImageEnhance
SESS = new_session('isnet-general-use')

def limpiar(fp):
    img = ImageOps.exif_transpose(Image.open(fp).convert('RGB'))
    s = 1500/max(img.size)
    if s < 1: img = img.resize((int(img.width*s), int(img.height*s)), Image.LANCZOS)
    img = ImageOps.autocontrast(img, cutoff=1)
    cut = remove(img, session=SESS, alpha_matting=True, alpha_matting_foreground_threshold=245,
                 alpha_matting_background_threshold=12, alpha_matting_erode_size=11)
    bb = cut.split()[3].getbbox()
    if bb: cut = cut.crop(bb)
    a = cut.split()[3]; rgb = cut.convert('RGB')
    rgb = ImageEnhance.Brightness(rgb).enhance(1.12)
    rgb = ImageEnhance.Color(rgb).enhance(1.08)
    rgb = ImageEnhance.Contrast(rgb).enhance(1.05)
    rgb = ImageEnhance.Sharpness(rgb).enhance(1.5)
    cut = Image.merge('RGBA', (*rgb.split(), a))
    sc = 2000/max(cut.size)
    if sc > 1: cut = cut.resize((int(cut.width*sc), int(cut.height*sc)), Image.LANCZOS)
    return cut

if __name__ == "__main__":
    rec, bib = sys.argv[1], sys.argv[2]; os.makedirs(bib, exist_ok=True)
    for arg in sys.argv[3:]:
        fn, name = arg.split("=")
        out = os.path.join(bib, name+".png")
        limpiar(os.path.join(rec, fn)).save(out)
        print("fiel ->", name+".png")
    print("BIBLIOTECA actualizada (fiel)")
