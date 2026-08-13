# 🔎 AUDITORÍA FASE 1 — Mudanza a `BUUM/` (solo diagnóstico, nada se movió)
> 2026-08-13 · Regla cumplida: no se borró, movió ni modificó NADA. Solo lectura.

## 1. UBICACIÓN
`C:\Users\playg\OneDrive\Documents\CLAUDE 1 EJ` (dentro de OneDrive — ver Riesgos).

## 2. RESUMEN
- **6,352 archivos** en **462 carpetas** · **2.6 GB**
- Tipos principales: 1,643 .jpg (258 MB) · 1,349 .png (1.25 GB) · 251 .mp4 (1 GB) · 516 .liquid · 237 .py · 231 .md · 157 .html
- **~80% del peso son imágenes y videos de pruebas** (anuncios de prueba, renders, screenshots, ejercicios de aprendizaje).
- Áreas encontradas: Knowledge Base, tienda Shopify (5 temas), marketing/motor creativo, Centro de Mando (OS), catálogo/marca, proyectos de aprendizaje (sweetlab, kenchys), llaves.

## 3. MAPA (tamaño · veredicto)
| Carpeta | Archivos | MB | Categoría |
|---|---|---|---|
| `BUUM Knowledge Base/` | 155 | 111 | 🟢 VIVO |
| `buumia-os/` (Centro de Mando) | 28 | <1 | 🟢 VIVO |
| `tema-vivo/` (tema Shopify actual) | 566 | 121 | 🟢 VIVO (con ~60 capturas de prueba 🔵) |
| `buumia-tienda/` | 1,033 | 897 | 🟡 solo `marketing/` scripts clave; resto 🔵 |
| `buumia-catalogo/` (marca + catálogo) | 123 | 55 | 🟢 `marca/` · 🟡 resto |
| `buumia-productos/` (fotos crudas) | 29 | 24 | 🟡 |
| `empresa-buum/` (docs de diseño) | 13 | <1 | 🟡 → KB |
| `.claude/` + `.agents/` (skills de IA) | 156 | 1 | 🟢 VIVO |
| `buumia-theme-glass/` (tema publicado hoy) | 487 | 62 | 🟡 hasta publicar el nuevo |
| `buumia-theme/ -apple/ -marketplace/` | 1,206 | 18 | 🔵 HISTÓRICO |
| `aurora-cafe/` | 95 | 29 | 🟢 solo `claves.local.txt`; resto 🔵 |
| `sweetlab/` + `kenchys-video/` (aprendizaje) | 2,264 | 1,001 | 🔵 HISTÓRICO |
| `buumia-sistema/ -ceo/ -director/ -fondos/ vivo/ PAQUETE-IMAGEN-7/ consultoria_video/ video_tutorial_*/` | ~208 | ~376 | 🔵 HISTÓRICO |
| Raíz (14 archivos) | 14 | <1 | mixto (ver abajo) |

## 4. ARCHIVOS IMPORTANTES (núcleo del sistema)
| Ruta | Función | Cat. | Destino |
|---|---|---|---|
| `BUUM Knowledge Base/**` (ARRANQUE, ESTADO-ACTUAL, 00-gobierno, 03-operacion, 04-negocio, 05-aprendizaje, 06-contenido) | memoria institucional | 🟢 | **KB** |
| `BUUM Knowledge Base/activos-visuales/R54W50/**` | imágenes oficiales del reflector | 🟢 | **activos** |
| `tema-vivo/sections|assets|templates|config|snippets|layout|locales` | tema BUUM PRO (Shopify) | 🟢 | **tienda** |
| `buumia-os/**` | Centro de Mando web + calendario | 🟢 | **os** |
| `buumia-tienda/marketing/` → `motor_creativo.py, flux_bg.py, flux_kontext.py, limpiar_producto.py, compose_*.py, anuncios_refl_*.py, filtros_calidad.py, rutina_*.py, publicar (redes/)` + `DIRECCION-CREATIVA.md` | motor creativo vivo | 🟢 | **marketing** |
| `.claude/skills/` (buumia-marketing, buumia-anuncios-ganadores, panel) | skills de la IA | 🟢 | **config** (`.claude/` nuevo) |
| `buumia-catalogo/marca/**` (logo-buum-marco*.png, brand kit, fuentes) | identidad oficial | 🟢 | **activos** |
| `buumia-meta.env`, `buumia-shopify.env`, `aurora-cafe/claves.local.txt` | credenciales | 🟢 | **config** [SECRETO DETECTADO — NO MOSTRAR] |
| `empresa-buum/` (01–06 + manuales) | diseño de la empresa | 🟡 | KB (revisar vigencia) |
| Raíz: `BRIEF-EMPRESA-FABLE5.md`, `FABLE5-KICKOFF.md`, `REGLAS.txt`, `buumia-collections.json` | fundacionales / datos | 🟡 | KB / datos |
| **Memoria de Claude** (fuera de la carpeta, en `~/.claude/projects/...CLAUDE-1-EJ/memory/`) | memoria de la IA | 🟢 | ⚠️ copiar al proyecto nuevo |

## 5–9. CANDIDATOS POR DESTINO (resumen)
- **KB:** toda la Knowledge Base (menos activos-visuales) + empresa-buum + BRIEF/REGLAS de raíz.
- **os:** buumia-os completo.
- **marketing:** ~15 scripts vivos + escuela (la escuela ya está en skills/KB); NO migran los ~150 `gen_*`/`fabrica_par*` de prueba.
- **tienda:** tema-vivo (solo carpetas del tema, sin capturas) + `port_to_shopify.py`, `shopify_caja12.py` (revisar).
- **activos:** activos-visuales/R54W50 + buumia-catalogo/marca + buumia-productos (crudas, revisar).
- **config:** los 3 archivos de llaves + `.claude/` (skills) + `buumia-shopify.env`.

## 10. DUPLICADOS Y VERSIONES VIEJAS (se quedan en el archivo)
- 4 temas Shopify viejos (`buumia-theme*`) — el vivo es `tema-vivo/`.
- ~60 capturas de prueba en `tema-vivo/` (`crop-*`, `full*`, `v5–v9*`, `final*`, `_*.txt`).
- ~150 scripts one-shot (`gen_*`, `fabrica_par1..21`) + ~20 carpetas `anuncios-par*` con cientos de renders.
- `tienda-PRO.html`, `tienda-PRO-B.html`, `tienda-PRO-backup.html`, `tienda-final.html` (mockups ya superados).
- `sweetlab/` y `kenchys-video/` completos (ejercicios de aprendizaje, 1 GB).

## 11. SECRETOS ENCONTRADOS (solo ubicación)
- `buumia-meta.env` · `buumia-shopify.env` · `aurora-cafe/claves.local.txt` → migran a `config/`.
- ⚠️ `kenchys-video/.env` y `kenchys-video/capture/extracted/tokens.json` → quedan en el archivo histórico; **recomendación: rotar esas credenciales o vaciarlas** (decisión del Fundador).

## 12. RIESGOS DE LA MUDANZA
1. **OneDrive:** la carpeta vieja vive en OneDrive. Recomendación: la nueva `BUUM/` FUERA de OneDrive (más rápida, sin conflictos de sincronización) y respaldo vía **git → servidor**. Decisión del Fundador.
2. **Rutas fijas en scripts:** varios scripts buscan `aurora-cafe/claves.local.txt` y rutas de `CLAUDE 1 EJ`. Al mudar hay que actualizar ~10 rutas (lo hago yo en Fase 2).
3. **Memoria y skills de la IA** están ligadas a la ruta de la carpeta: hay que copiarlas al proyecto nuevo o la IA "olvida".
4. **Servidor local 8130** (vbs de inicio de Windows) apunta a la carpeta vieja → actualizar.
5. Shopify no se afecta (el tema vive en Shopify); solo cambia la carpeta local de trabajo.

## 13. PLAN DE MIGRACIÓN PROPUESTO (resumen)
| Origen | Cat. | Destino | Motivo | Riesgo |
|---|---|---|---|---|
| BUUM Knowledge Base (docs) | 🟢 | KB/ | memoria institucional | bajo |
| activos-visuales + marca | 🟢 | activos/ | imágenes oficiales | bajo |
| buumia-os | 🟢 | os/ | Centro de Mando | bajo |
| tema-vivo (solo tema) | 🟢 | tienda/tema-vivo/ | tema actual | bajo (rutas) |
| 15 scripts marketing + redes/ | 🟢 | marketing/ | motor creativo | medio (rutas de llaves) |
| 3 archivos de llaves | 🟢 | config/ | credenciales | medio (actualizar scripts) |
| .claude/skills + memoria IA | 🟢 | config/.claude/ | cerebro de la IA | medio (rutas de proyecto) |
| empresa-buum, BRIEF, REGLAS | 🟡 | KB/ | revisar vigencia | bajo |
| buumia-productos, catálogo Megaluz, theme-glass | 🟡 | REVISAR | confirmar uso | bajo |
| Todo lo demás (~2 GB) | 🔵 | NO MIGRAR | histórico | ninguno |

**FIN DE FASE 1 — DETENIDO.** Nada creado, movido ni borrado. Espero visto bueno del Fundador para Fase 2.
