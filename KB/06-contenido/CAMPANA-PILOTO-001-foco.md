# Campaña Piloto 001 — Foco LED 60W (validación del flujo completo)

> Objetivo: **demostrar que toda la empresa funciona de punta a punta.** NO vender (foco en Agotado, inventario 0, honesto). Producto piloto: Foco LED 60W.
> Expediente que amarra los 14 pasos del lanzamiento y quién ejecuta cada uno.

## Los 14 pasos y su estado

| # | Paso | Responsable | Estado |
|---|------|-------------|--------|
| 1 | Producto preparado | BUUM | ✅ (activo, Agotado) |
| 2 | Ficha técnica final | BUUM | ✅ (specs 60W/E27/6500K/5700lm/25000h) |
| 3 | Página Shopify terminada | BUUM | ✅ ([producto](https://admin.shopify.com/store/buumia/products/10386084921666)) |
| 4 | Fotografías finales | BUUM (assets existentes) | ✅ (3 fotos limpias en el producto) |
| 5 | Recursos gráficos para redes | **ChatGPT** | 🟡 brief listo (abajo) |
| 6 | Video publicitario | **ChatGPT** | 🟡 brief listo |
| 7 | Carrusel | **ChatGPT** | 🟡 brief listo |
| 8 | Historia | **ChatGPT** | 🟡 brief listo |
| 9 | Publicación Facebook | BUUM prepara · **Fundador** aprueba | 🟡 pendiente creatividad + tu OK |
| 10 | Publicación Instagram | BUUM prepara · **Fundador** aprueba | 🟡 pendiente creatividad + tu OK |
| 11 | Calendario registrado | BUUM | ✅ (esta campaña, ver abajo) |
| 12 | Sistema de medición preparado | BUUM | ✅ (métricas Meta + línea base @buum.ia) |
| 13 | Dashboard mostrando la campaña | BUUM | 🟡 registro creado; falta reflejarlo en la vista |
| 14 | Registro del aprendizaje | BUUM | ✅ (slot listo, se llena al medir) |

## Medición (expectativa registrada ANTES de publicar)
- Métrica: resonancia = (guardados+compartidos+comentarios) ÷ alcance, + retención en video.
- Umbral tentativo `[baja confianza]`: resonancia ≥3%, retención ≥40% a 3s (calibración; primer dato real).
- Línea base @buum.ia: 420 seguidores (ver `baseline-ig.json`).
- Nota de honestidad: la campaña NO invita a comprar (producto Agotado/en desarrollo); es contenido de marca/expectación.

## Calendario
- Pieza principal (video/reel): día objetivo de publicación a definir con el Fundador.
- Carrusel + historia: mismo día / día siguiente.
- Registrado en el calendario de contenido del sistema.

## Aprendizaje (se llena al cerrar)
- Resultado real vs. esperado → lección → libro de jugadas.

---

## BRIEF para el Director de Marketing (ChatGPT) — pasos 5-8

- **Objetivo:** contenido de marca del Foco LED 60W. **NO venta** (el producto está en desarrollo/Agotado). Generar interés y expectación, honesto.
- **Restricción dura:** luz del foco **BLANCA** (6500K), nunca cálida. Sin precio, sin "cómpralo", sin "lista de espera". Fiel al ADN BUUM (logo contorno blanco, vibra, gato Kitsune).
- **Piezas:**
  - **Video (reel 9:16, ~10-12s):** el foco encendido iluminando un espacio; gancho en 1-2s; cierre con firma BUUM.
  - **Carrusel (4:5):** slide 1 gancho, slides el foco en contexto/beneficios, último slide marca (sin precio).
  - **Historia (9:16):** una pieza vertical rápida, gancho visual.
  - **Gráfico de red (post):** el foco héroe + "ilumina un espacio completo con un solo foco".
- **Referencias/assets:** fotos limpias del foco en `04-negocio/productos/fotos/`; keyframes del reel en `buumia-tienda/marketing/contenido/reel001/`.
- **Entrega:** las piezas → BUUM las valida (candado + honestidad), almacena, prepara la publicación y las mide.

---

## ACTUALIZACIÓN — MODO OPERACIÓN (2026-07-17)
Motor de imágenes arreglado (gpt-image-1, endpoint correcto) + **Motor Creativo automatizado** (`buumia-tienda/marketing/motor_creativo.py`).
- Paso 5 (recursos gráficos) → OPERATIVO (3 piezas al estándar).
- Copy (FB + IG) → OPERATIVO.
- Pasos 9/10 (publicación) → preparados, esperando gate del Fundador.
- Paso 6 (video Kling) → Pendiente del Fundador (costo ~$0.30-2 USD; nunca probado).
- Paquete listo: `06-contenido/PAQUETE-CAMPANA-001-listo-publicar.md`.
- Siguiente cuello de botella no-Fundador: reflejar la campaña en el Dashboard (paso 13).
