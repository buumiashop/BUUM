# ADR-0018 — Biblioteca de Activos Visuales: estándar, estructura y frontera (Pasos 3/7/8)
- **Fecha:** 2026-07-17 · **Estado:** Aceptada
- **Contexto:** Faltaba el estándar de procesamiento, la ubicación de la Biblioteca y la frontera activo-oficial vs contenido-temporal.

## Decisión (C2)
**Repositorio dedicado, separado de los docs de conocimiento** (respeta "dos activos distintos"):
`BUUM Knowledge Base/activos-visuales/<sku>/`

- **Estándar mínimo de procesamiento:** PNG transparente para el producto · ≥2000px lado mayor · fondo limpio · color corregido · naming consistente (`principal.png`, `detalle-N.png`, subcarpeta `hd/`, `render-*`).
- **Vínculo:** el Documento Maestro referencia la carpeta `<sku>/` de la Biblioteca.
- **Frontera (activo vs contenido):** a la Biblioteca solo van **activos neutrales reutilizables** (producto limpio, vistas, renders **sin copy**). Las **piezas de campaña** (con texto/CTA/oferta) son **contenido temporal** → NO van a la Biblioteca; solo su **aprendizaje** va a la KB.

## Alternativas
- C1 Carpeta dentro de cada producto en la KB (mezcla imágenes pesadas con conocimiento).

## Estándar de procesamiento de FOTOS REALES (2026-07-17, por evidencia)
Las fotos reales del producto se limpian con método **NO-generativo** (fiel + automático + escalable): recorte con `rembg` modelo **isnet-general-use + alpha matting** → **realce** (brillo/color/contraste/nitidez) → fondo estudio/transparente. **PROHIBIDO usar un generador (gpt-image-1) para retocar fotos reales:** inventa etiquetas, modelo y hasta el número de LEDs (evidencia: prueba reflector, 16 LEDs → 20, "R54W50" → "RS-1W50"). El generador se usa **solo para imágenes CREADAS** (lámpara armada, ángulos, contexto). Script: `buumia-tienda/marketing/` (pipeline fiel). Opción de escala futura: modelo de recorte en Replicate (BiRefNet ~2-5¢) si se quiere aún más fino.

## Imágenes de PRODUCTO para la biblioteca (decisión del Fundador 2026-07-17)
Las imágenes de producto de la biblioteca (que usa el generador para hacer publicidad) van **LIMPIAS: sin texto, sin números, sin marca** (nada de "TIANLAI" ni marca propia). Razón: al cliente no le importa el texto chico y así **nada se deforma ni miente**; la info real (50W, equivale 500W, IP66, solar, etc.) va en el **Documento Maestro y en la publicidad**, no pegada en la foto.
- **MÉTODO CORRECTO (corrección del Fundador 2026-07-17): INPAINTING, no regeneración.** Regenerar (flux-kontext/gpt-image-1) **cambia físicamente el producto** = sigue engañando al cliente. Lo correcto: partir de la **foto real** (recorte fiel) y **borrar SOLO los textos con inpainting enmascarado** (`flux_fill.py`, Replicate **flux-fill-pro ~5¢**): el producto queda **pixel-idéntico** y solo se rellenan las zonas de texto. **Se conserva únicamente "50W"** (el resto de textos fuera; la info va en el Documento Maestro y la publicidad). Nunca dejar textos garabateados ni marca ajena.
- Herramienta: `buumia-tienda/marketing/flux_kontext.py`.
- Fotos reales CON texto (verdad) se quedan en `recepcion/` (fuente de verdad). La biblioteca = versiones limpias.

## Consecuencias
- Se requiere un índice/vínculo producto↔activos (el Documento Maestro lo provee).
- El pipeline es un script → **automático para N productos**.
