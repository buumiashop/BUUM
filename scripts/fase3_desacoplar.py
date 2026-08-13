# -*- coding: utf-8 -*-
"""FASE 3 — Desacoplar BUUM de CLAUDE 1 EJ. Backup + reemplazos exactos por archivo.
   Regla: ningun reemplazo global; cada cambio es explicito y se verifica."""
import os, shutil, py_compile, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

B = r"C:\Users\playg\BUUM"
BK = os.path.join(B, "datos", "backup-fase-3")
OLDROOT_A = 'ROOT="C:/Users/playg/OneDrive/Documents/CLAUDE 1 EJ"'
OLDROOT_B = 'ROOT=r"C:/Users/playg/OneDrive/Documents/CLAUDE 1 EJ"'
CLAVES = ['os.path.join(ROOT,"aurora-cafe","claves.local.txt")',
          'os.path.join(ROOT, "aurora-cafe", "claves.local.txt")']
CFGLINE = 'os.path.join(ROOT,"config","config.local.env")'

def guard(var):
    # lee variable de entorno primero; luego config.local.env si existe; si no, aviso claro
    return ('os.environ.get("%s") or (env(%s).get("%s") if os.path.exists(%s) else None) or '
            'sys.exit("Falta %s: variable de entorno o config/config.local.env")'
            % (var, CFGLINE, var, CFGLINE, var))

# (ruta relativa, [(viejo, nuevo), ...])
EDITS = {
 r"marketing\motor_creativo.py": [
   ("HERE=os.path.dirname(os.path.abspath(__file__)); TIENDA=os.path.dirname(HERE); ROOT=os.path.dirname(TIENDA)",
    "HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.dirname(HERE)"),
   ('KEY=env(%s)["OPENAI_API_KEY"]' % CLAVES[0], "KEY=" + guard("OPENAI_API_KEY")),
 ],
 r"marketing\flux_bg.py": [
   ("HERE=os.path.dirname(os.path.abspath(__file__)); TIENDA=os.path.dirname(HERE); ROOT=os.path.dirname(TIENDA)",
    "HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.dirname(HERE)"),
   ('tok=env(%s)["REPLICATE_API_TOKEN"]' % CLAVES[0], "tok=" + guard("REPLICATE_API_TOKEN")),
 ],
 r"marketing\flux_kontext.py": [
   ("HERE=os.path.dirname(os.path.abspath(__file__)); TIENDA=os.path.dirname(HERE); ROOT=os.path.dirname(TIENDA)",
    "HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.dirname(HERE)"),
   ('tok=env(%s)["REPLICATE_API_TOKEN"]' % CLAVES[0], "tok=" + guard("REPLICATE_API_TOKEN")),
 ],
 r"marketing\filtros_calidad.py": [
   ("HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))",
    "HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)"),
   ('GKEY = env(%s).get("GEMINI_API_KEY")' % CLAVES[1],
    'GKEY = os.environ.get("GEMINI_API_KEY") or (env(%s).get("GEMINI_API_KEY") if os.path.exists(%s) else None)' % (CFGLINE, CFGLINE)),
 ],
 r"marketing\compose_post.py": [
   (OLDROOT_B, "ROOT=os.path.dirname(HERE)"),
   ('FOCO=os.path.join(ROOT,"BUUM Knowledge Base/04-negocio/productos/fotos/60w-1-clean.png")',
    'FOCO=os.path.join(ROOT,"activos/productos/foco-60w/60w-1-clean.png")  # pendiente migrar activo'),
   ('LOGO=os.path.join(ROOT,"buumia-catalogo/marca/logo-oficial/logo-buum-oficial.png")',
    'LOGO=os.path.join(ROOT,"activos/marca/logo-oficial/logo-buum-oficial.png")'),
 ],
 r"marketing\compose_story.py": [
   (OLDROOT_B, "ROOT=os.path.dirname(HERE)"),
   ('FOCO=os.path.join(ROOT,"BUUM Knowledge Base/04-negocio/productos/fotos/60w-1-clean.png")',
    'FOCO=os.path.join(ROOT,"activos/productos/foco-60w/60w-1-clean.png")  # pendiente migrar activo'),
   ('LOGO=os.path.join(ROOT,"buumia-catalogo/marca/logo-oficial/logo-buum-oficial.png")',
    'LOGO=os.path.join(ROOT,"activos/marca/logo-oficial/logo-buum-oficial.png")'),
 ],
 r"marketing\compose_ad.py": [
   ("HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))",
    "HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)"),
   ('LOGO = os.path.join(ROOT, "buumia-catalogo", "marca", "logo-oficial", "logo-buum-oficial.png")',
    'LOGO = os.path.join(ROOT, "activos", "marca", "logo-oficial", "logo-buum-oficial.png")'),
 ],
 r"marketing\anuncios_refl_a1a2.py": [
   ("ROOT = os.path.dirname(os.path.dirname(HERE))", "ROOT = os.path.dirname(HERE)"),
   ('KB   = os.path.join(ROOT, "BUUM Knowledge Base", "activos-visuales", "R54W50")',
    'KB   = os.path.join(ROOT, "activos", "productos", "R54W50")'),
   ('LOGO = os.path.join(ROOT, "tema-vivo", "assets", "logo-buumia-original.png")',
    'LOGO = os.path.join(ROOT, "tienda", "tema-vivo", "assets", "logo-buumia-original.png")'),
 ],
 r"marketing\anuncios_refl_finales.py": [
   ("ROOT = os.path.dirname(os.path.dirname(HERE))", "ROOT = os.path.dirname(HERE)"),
   ('KB   = os.path.join(ROOT, "BUUM Knowledge Base", "activos-visuales", "R54W50")',
    'KB   = os.path.join(ROOT, "activos", "productos", "R54W50")'),
   ('LOGO = os.path.join(ROOT, "tema-vivo", "assets", "logo-buumia-original.png")',
    'LOGO = os.path.join(ROOT, "tienda", "tema-vivo", "assets", "logo-buumia-original.png")'),
 ],
 r"marketing\anuncios_refl_v2.py": [
   ("ROOT = os.path.dirname(os.path.dirname(HERE))", "ROOT = os.path.dirname(HERE)"),
   ('KB   = os.path.join(ROOT, "BUUM Knowledge Base", "activos-visuales", "R54W50")',
    'KB   = os.path.join(ROOT, "activos", "productos", "R54W50")'),
   ('LOGO = os.path.join(ROOT, "buumia-catalogo", "marca", "logo-buum-marco.png")',
    'LOGO = os.path.join(ROOT, "activos", "marca", "logo-buum-marco.png")'),
 ],
 r"marketing\rutina_diaria.py": [
   ("ROOT = os.path.dirname(os.path.dirname(HERE))", "ROOT = os.path.dirname(HERE)"),
   ('VID  = os.path.join(ROOT, "buumia-tienda", "video")', 'VID  = os.path.join(HERE, "video")  # pendiente migrar videos'),
   ('K = env(%s)' % CLAVES[1],
    'K = {**(env(%s) if os.path.exists(%s) else {}), **os.environ}' % (CFGLINE, CFGLINE)),
 ],
 r"marketing\rutina_imagenes.py": [
   ("ROOT = os.path.dirname(os.path.dirname(HERE))", "ROOT = os.path.dirname(HERE)"),
   ('FOCO = os.path.join(ROOT, "buumia-catalogo", "foco-led-60w", "fotos", "60w-1-clean.png")',
    'FOCO = os.path.join(ROOT, "activos", "productos", "foco-60w", "60w-1-clean.png")  # pendiente migrar activo'),
   ('LOGO = os.path.join(ROOT, "buumia-catalogo", "marca", "logo-buum-horizontal.png")',
    'LOGO = os.path.join(ROOT, "activos", "marca", "logo-buum-horizontal.png")'),
   ('GKEY = env(%s)["GEMINI_API_KEY"]' % CLAVES[1], "GKEY = " + guard("GEMINI_API_KEY")),
 ],
 r"marketing\rutina_semanal.py": [
   ("HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))",
    "HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)"),
   ('POOL = os.path.join(HERE, "..", "revision_anuncios")', 'POOL = os.path.join(HERE, "revision_anuncios")'),
   ('SEMANA_JS = os.path.join(ROOT, "buumia-os", "semana.js")', 'SEMANA_JS = os.path.join(ROOT, "os", "semana.js")'),
 ],
 r"marketing\rutina_gatitos.py": [
   ("HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))",
    "HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)"),
 ],
 r"marketing\redes\publicar.py": [
   ('ROOT = "C:/Users/playg/OneDrive/Documents/CLAUDE 1 EJ"',
    'HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))'),
   ('tok = env(%s)["META_USER_TOKEN"]' % CLAVES[1], "tok = " + guard("META_USER_TOKEN")),
 ],
 r"marketing\redes\publicar_pieza.py": [
   ('ROOT="C:/Users/playg/OneDrive/Documents/CLAUDE 1 EJ"; V="v21.0"',
    'HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.dirname(os.path.dirname(HERE)); V="v21.0"'),
   ('tok=env(%s)["META_USER_TOKEN"]' % CLAVES[0], "tok=" + guard("META_USER_TOKEN")),
 ],
 r"marketing\redes\medir_baseline.py": [
   ('ROOT="C:/Users/playg/OneDrive/Documents/CLAUDE 1 EJ"; V="v21.0"',
    'HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.dirname(os.path.dirname(HERE)); V="v21.0"'),
   ('tok=env(%s)["META_USER_TOKEN"]' % CLAVES[0], "tok=" + guard("META_USER_TOKEN")),
   ('out=os.path.join(ROOT,"BUUM Knowledge Base","06-contenido","baseline-ig.json")',
    'out=os.path.join(ROOT,"KB","06-contenido","baseline-ig.json")'),
 ],
 r"marketing\redes\verificar_meta.py": [
   ('ROOT="C:/Users/playg/OneDrive/Documents/CLAUDE 1 EJ"; V="v21.0"',
    'HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.dirname(os.path.dirname(HERE)); V="v21.0"'),
   ('tok=env(%s)["META_USER_TOKEN"]' % CLAVES[0], "tok=" + guard("META_USER_TOKEN")),
 ],
}

fallos = []; ok = []
for rel, subs in EDITS.items():
    p = os.path.join(B, rel)
    bkp = os.path.join(BK, rel)
    os.makedirs(os.path.dirname(bkp), exist_ok=True)
    shutil.copy2(p, bkp)
    src = io.open(p, encoding="utf-8").read()
    changed = src
    for old, new in subs:
        if old not in changed:
            fallos.append(f"{rel}: NO ENCONTRADO -> {old[:70]}")
            continue
        changed = changed.replace(old, new, 1)
    # asegurar import sys si el guard lo usa
    if "sys.exit(" in changed and "import sys" not in changed.split("\n", 6)[0:6].__str__() and "import sys" not in changed:
        changed = changed.replace("import ", "import sys, ", 1)
    if changed != src:
        io.open(p, "w", encoding="utf-8").write(changed)
        ok.append(rel)

print("MODIFICADOS:", len(ok))
for f in ok: print("  ", f)
print("FALLOS:", len(fallos))
for f in fallos: print("  !!", f)

# compilar todos los .py de marketing
print("\nCOMPILACION:")
bad = 0
for base, _, files in os.walk(os.path.join(B, "marketing")):
    for f in files:
        if f.endswith(".py"):
            try:
                py_compile.compile(os.path.join(base, f), doraise=True)
            except Exception as e:
                bad += 1; print("  ERROR", f, str(e)[:120])
print("  errores:", bad)
