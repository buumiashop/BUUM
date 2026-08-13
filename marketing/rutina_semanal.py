# -*- coding: utf-8 -*-
"""BUUM OS — RUTINA SEMANAL (el motor del CEO).
   Junta todo: toma el arsenal de contenido -> lo pasa por los 4 FILTROS de calidad ->
   los que PASAN se agendan en la semana (IG/FB/TikTok) -> escribe semana.js para el Centro de Mando.
   (Fase A / prueba en tu compu. Diseñado para moverse a la nube sin cambios.)
   Uso:  python rutina_semanal.py            (revisa las 8 más recientes)
         python rutina_semanal.py --n 20     (revisa 20)
         python rutina_semanal.py --all      (todas)
"""
import os, sys, io, json, shutil, datetime
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import filtros_calidad as fc   # reutiliza los 4 filtros (y ya reconfigura stdout a utf-8)

POOL = os.path.join(HERE, "revision_anuncios")   # arsenal de anuncios
APR = os.path.join(POOL, "por-aprobar"); REC = os.path.join(POOL, "rechazados")
SEMANA_JS = os.path.join(ROOT, "os", "semana.js")
RELBASE = "../buumia-tienda/revision_anuncios/por-aprobar/"   # ruta que el panel usa para las miniaturas
DIAS = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]
CANALES = ["ig", "fb", "tt"]
TEMA = "Reflectores solares recargables · armado de lanzamiento"

def main():
    a = sys.argv[1:]
    n = 8
    if "--all" in a: n = 10**9
    elif "--n" in a: n = int(a[a.index("--n") + 1])
    os.makedirs(APR, exist_ok=True); os.makedirs(REC, exist_ok=True)

    imgs = [f for f in sorted(os.listdir(POOL)) if f.lower().endswith((".png", ".jpg", ".jpeg"))]
    imgs = imgs[-n:] if n < len(imgs) else imgs
    print(f"🧠 CEO: plan de la semana = «{TEMA}». Revisando {len(imgs)} piezas por los 4 filtros...\n")

    aprobados, rechazados = [], []
    for f in imgs:
        ok, res = fc.revisar(os.path.join(POOL, f))
        punt = [r["puntaje"] for r in res]
        if ok:
            shutil.copy(os.path.join(POOL, f), os.path.join(APR, f))
            aprobados.append({"file": f, "img": RELBASE + f, "puntajes": punt})
        else:
            malo = next((r["motivo"] for r in res if r["ok"] is False), "")
            shutil.copy(os.path.join(POOL, f), os.path.join(REC, f))
            rechazados.append({"file": f, "motivo": malo})

    # agendar los aprobados en la semana (round-robin días/canales)
    cal = {str(i): [] for i in range(7)}
    for i, ap in enumerate(aprobados):
        d = i % 7; ch = CANALES[i % len(CANALES)]
        cal[str(d)].append({"ch": ch, "file": ap["file"], "img": ap["img"], "titulo": "Anuncio aprobado"})

    data = {
        "generado": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "tema": TEMA,
        "resumen": {"revisados": len(imgs), "aprobados": len(aprobados), "rechazados": len(rechazados)},
        "aprobados": aprobados, "rechazados": rechazados, "calendario": cal,
    }
    io.open(SEMANA_JS, "w", encoding="utf-8").write("window.SEMANA=" + json.dumps(data, ensure_ascii=False) + ";")
    print(f"\n✅ Semana lista: {len(aprobados)} pasaron (por-aprobar/), {len(rechazados)} rechazados.")
    print(f"   Escrito: buumia-os/semana.js  → el Centro de Mando ya lo muestra.")

if __name__ == "__main__":
    main()
