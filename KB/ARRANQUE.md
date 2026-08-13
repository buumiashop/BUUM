# ⚡ ARRANQUE — Lee esto PRIMERO en cada chat nuevo
> Objetivo: que un chat nuevo arranque sabiendo TODO, sin que el Fundador repita nada. **Leer solo este archivo basta para empezar.**

## 1. Conexiones — YA ESTÁN LISTAS (no volver a pedir llaves, no reconfigurar)
| Servicio | Estado | Dónde está la llave |
|---|---|---|
| **OpenAI** (gpt-image-1) | ✅ con saldo | `aurora-cafe/claves.local.txt` → `OPENAI_API_KEY` |
| **Replicate** (flux, kontext, Kling) | ✅ | `aurora-cafe/claves.local.txt` → `REPLICATE_API_TOKEN` |
| **Meta** (Facebook BUUM + Instagram @buum.ia) | ✅ conectado | `claves.local.txt` → `META_USER_TOKEN` |
| **Shopify** (tema + productos) | ✅ conectado | `buumia-shopify.env` (Admin API + Theme token) |
| **Gemini** | ⚠️ sin saldo | `claves.local.txt` → `GEMINI_API_KEY` |
| **ElevenLabs / Notion** | ✅ | `claves.local.txt` |
| **Servidor local** | ✅ siempre prendido | `http://127.0.0.1:8130` |
| **Servidor nube** | ✅ DigitalOcean | IP `165.227.181.176` |
| **Mercado Pago** | ❌ falta conectar | decisión del Fundador |

> **REGLA:** nunca preguntar "¿tienes la llave de X?" — están todas ahí. Solo leer el archivo.

## 2. Herramientas ya construidas (usar, no rehacer)
Carpeta `buumia-tienda/marketing/`:
- `motor_creativo.py` — genera con gpt-image-1 (t2i o edit)
- `flux_kontext.py` — edita fotos con Replicate (barato)
- `flux_bg.py` — fondos baratos
- `limpiar_producto.py` — recorte fiel automático (rembg)
- `compose_post.py` / `compose_story.py` — plantillas de marca

## 3. Gobierno (leer solo si aplica al tema)
`00-gobierno/`: VISION-2030 · MODELO-DE-MADUREZ · PVOE-OBJETIVO-INMEDIATO · adr/
`03-operacion/`: FLUJO-OPERATIVO-OFICIAL · JUECES-DE-CALIDAD · PROCESO-IMAGENES-HIBRIDO · POLITICA-GARANTIA-DEVOLUCIONES
`01-identidad/`: SISTEMA-VISUAL-BUUM
`05-aprendizaje/`: GUSTOS-DEL-FUNDADOR ← **leer SIEMPRE antes de crear contenido**

## 4. Reglas de ORO del Fundador (no romper)
1. **Respuestas cortas.** Ir al grano.
2. **Regla de 2 intentos:** si algo falla 2 veces, PARAR y decir la verdad. No insistir.
3. **No mostrar pasos intermedios** — solo el resultado final. (Las imágenes son lo que más crédito consume.)
4. **Nunca borrar imágenes** del Fundador; las dudosas van a `revisar/`.
5. **Nunca deformar el producto** ni inventar texto/etiquetas.
6. **Economizar:** juntar cambios, un solo preview, generador barato primero.
7. Producto = reflector solar 50W (equivale 500W). NUNCA foco de filamento.

## 5. ESTADO ACTUAL — se actualiza al cerrar cada chat
👉 **Ver `ESTADO-ACTUAL.md`** (qué se hizo, en qué punto vamos, qué sigue).
