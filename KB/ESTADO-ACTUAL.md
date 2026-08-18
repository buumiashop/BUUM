# 📍 ESTADO ACTUAL — dónde vamos exactamente
> Actualizado: **2026-08-17** (🟢 TIENDA ABIERTA AL PUBLICO desde 2026-08-17: tema publicado, producto activo, SIN contraseña — verificado desde el exterior). Se reescribe cada "cambia de chat".

## Objetivo inmediato
**Lanzar la tienda con UN solo producto: el Reflector Solar 50W** (paquete de 2). Empezar a vender, practicar publicidad y correr el ciclo completo. Después integrar más productos.

---

## 🟢 LO QUE YA ESTÁ LISTO
- **Producto reflector** en Shopify: paquete de 2, **$1,299**, inventario **10**, peso **4 kg (⚠️ NO verificado físicamente — pendiente pesar)**, caja **32×19×5 cm**, SKU R54W50, 13 fotos, descripción + ficha técnica. Handle: `reflector-solar-led-50w-con-control-remoto-equivale-a-500w`. ✅ **ACTIVO** (2026-08-17).
- **Pagos**: Mercado Pago Checkout Pro activo (tarjeta, OXXO, meses). El dinero cae en la cuenta MP del Fundador.
- **Legal**: políticas (privacidad auto, reembolsos, términos, envíos, contacto) + **banner de cookies** activado.
- **Tema "BUUM PRO preview" id `191665471810`: PUBLICADO (tema en vivo, 2026-08-17)**. Contenido 100%: hero 3 escenas, galería de arte día/noche con efectos, portadas claras, paquetería conectada (Envia automática + Skydropx comparador). Ya convertido a **puro reflector**:
  - Iconos 3D claros de marca (bolsa, lupa, rayo, WhatsApp, carrito) + menú hamburguesa con iconos + Mayoreo/Usuario.
  - Logo/gatito más grande. WhatsApp verde en la barra (656 314 3071). Redes sociales 44px.
  - Barra de confianza PRO (compra segura, pago protegido MP, envío asegurado, producto real).
  - Hero del reflector + tarjeta "Comprar ahora" → **producto real**. Reseñas y FAQ del reflector.
  - **Ocultado**: catálogo de focos, video de focos, categorías, juego de mayoreo/Sofía.

## ⬜ LO QUE FALTA (para lanzar)
1. **El Fundador dijo: "hay que editar varias cosas"** → EMPEZAR EL CHAT NUEVO preguntando QUÉ editar exactamente.
2. **Publicar el tema** "BUUM PRO preview" (que pase a tema activo). Lo hace BUUM por CLI.
3. **Activar el producto reflector** (borrador → activo) para que se pueda comprar.
4. **Quitar la contraseña** de la tienda (Fundador, 1 clic) cuando quiera abrir al público.
5. Después: **anuncios/marketing** → medir → aprender (etapa 10-12 del flujo).

---

## 🔧 CÓMO SE EDITA EL TEMA (importante — método que SÍ funciona)
- El **token de tema** (`shptka_...`) NO sirve con llamadas directas a la API, **solo con la Shopify CLI**. Token guardado en `buumia-shopify.env` → `SHOPIFY_THEME_TOKEN` (el bueno: `[TOKEN RETIRADO — va en config/config.local.env, nunca en la KB]`).
- Tienda usa el **nuevo Dev Dashboard** (ya no hay apps personalizadas clásicas). El token admin (`SHOPIFY_ADMIN_TOKEN`) solo tiene `write_products` (sirve para producto/precio/inventario-tracking, NO para inventario-cantidad, páginas, temas).
- **Flujo de edición**: `shopify theme pull/push --store j0hshz-nm --theme <id> --path tema-vivo` (con `export SHOPIFY_CLI_THEME_TOKEN=...`). Tema en vivo real = "BUUMIA Glass (borrador)" id `190418157890`. Copia de trabajo local en `tema-vivo/`. Homepage = sección `sections/buumia-cine.liquid` (todo el contenido vive ahí, es una sola sección).
- **Para VER el render** (el panel del navegador no compone capturas y la tienda tiene contraseña): levantar `python -m http.server` en `tema-vivo/` + generar `preview.html` (reemplazando `{{ 'x' | asset_url }}`→`assets/x`) + captura con **Edge headless**: `msedge --headless=new --screenshot=out.png --window-size=390,ALTO URL`. Verificar DOM con el navegador MCP vía `javascript_tool` (sí funciona sin captura).
- Iconos: se generan con Replicate flux (claves en `aurora-cafe/claves.local.txt`), se les quita fondo con `rembg`, se aclaran con PIL. Assets del reflector en `tema-vivo/assets/` (ico-*.png, refl-*.png).

## 📦 Datos del producto (reflector)
- Reflector 19×15×5 cm · Panel 30×17×1 cm · Caja 32×19×5 cm · ~2 kg c/u (4 kg el 2-pack) — **⚠️ estimado, NO verificado**: pesar físicamente antes de usarlo como dato oficial (ficha técnica, Shopify, envío, cotización, publicidad, documentación).
- Panel+cable+conector = **UNA SOLA PIEZA**. NO mencionar baterías (regla). Etiqueta "50W/500W" abajo-derecha.
- Método de precios: costo×3. Reflector cuesta $300 → 2-pack $1,299. **OJO competencia:** focos/reflectores similares a ~$300 en ML → margen difícil; por eso venta local + este 2-pack.

## Siempre despierto (F4 — 2026-08-18)
- Bandeja + Centro de Mando: servicio systemd `buum-bandeja` (usuario buum-agent,
  auto-arranque y auto-reinicio; sobrevive reinicios del droplet). Acceso: tunel SSH 8131.
- Colectores AUTOMATICOS diarios: cron de `buum` a las 13:00 UTC (7am Chihuahua) ->
  snapshots frescos cada manana, log en /var/log/buum/colectores.log.
- Consejo de Direccion: MANUAL a peticion (doctrina 13F); con datos siempre frescos.

## Datos reales (FASE 13D)
Colectores solo-lectura en `scripts/colectores/` (Shopify + Meta) -> snapshots en
`datos/snapshots/` (servidor; gitignored) -> `/api/datos` -> Centro de Mando (tiles
REAL/CALC) y agente. Correr a mano: `python3 scripts/colectores/observar_shopify.py` (como buum).

## Prioridades vivas
Foco actual y backlog de dirección: ver `KB/08-direccion/BACKLOG.md`.

## Mapa de fuentes de verdad
Jerarquía y ubicación de cada tipo de información (KB, SQLite, datos, secretos,
servidor canónico del Centro de Mando): ver `KB/02-arquitectura/FUENTES-DE-VERDAD.md`.

## Reglas de oro (no romper)
- Respuestas cortas. Regla de 2 intentos. No mostrar pasos intermedios. Economizar créditos.
- **Verificar SIEMPRE con captura/DOM antes de subir** (lección cara: editar a ciegas salió mal varias veces).
- Nunca inventar specs (regla de promesas): beneficio en marketing, número solo en ficha técnica.
- Hay un producto de **foco 60W ACTIVE** en Shopify (aparte); por ahora la tienda va SOLO del reflector.
