# FABLE5-KICKOFF — Brief para el modelo Fable 5 (BUUM)

> Pégale a Fable 5 solo esto: **"Lee FABLE5-KICKOFF.md y arranca."**
> Este archivo lo escribió Opus (que tiene todo el contexto) para que gastes tus tokens PENSANDO, no explorando.

## 0) REGLAS DE ECONOMÍA (tokens escasos — obedécelas)
- Cero preámbulo, cero "¿cómo estás?", cero resúmenes de lo que vas a hacer. **Entrega el trabajo directo.**
- **NO explores el repo.** Ya tienes el contexto abajo + `.claude/.../memory/MEMORY.md` (se carga solo). Solo abre un archivo si lo NOMBRO aquí.
- **NO hagas ediciones pequeñas ni `push`.** Tú eres ARQUITECTO: produces PLANOS reutilizables (archivos). Opus los ejecuta barato en el otro chat.
- Respuestas DENSAS, sin relleno. Guarda tus salidas como ARCHIVOS (para que persistan y Opus las use).
- No repitas lo que ya está en la memoria. Trabaja en 1-2 tandas grandes, no muchas chiquitas.

## 1) QUÉ ES BUUM (contexto, no lo re-investigues)
- **BUUM** = tienda mexicana (Shopify) que arranca vendiendo un **Foco LED 60W** (luz blanca, rosca E27; cajas 12/30/50 a $75 c/u), pero la visión es **tienda de NOVEDADES** e importación/distribución desde China. Marca oficial: gato Kitsune + "BUUM". Colores: naranja `#EA5003`, navy `#001866`, azul `#102AC4`. Eslogan: "Súper calidad y súper precio".
- **Filosofía del dueño:** vender HONESTO ("vale la pena", nada de garantías falsas ni productos que no hay), enganchar en 1 segundo, ~95% visual, BRILLANTE, "más guau" siempre, mentalidad millonaria, rehacer hasta que quede excelente. Habla español (México). Es MUY visual: siempre hay que MOSTRARLE preview.
- **Regla de eficiencia:** trabajar por TANDAS, decidir con mockups baratos antes de tocar el archivo real, 1 solo preview/push por tanda.

## 2) ESTADO ACTUAL DE LA TIENDA (archivo fuente: `buumia-tienda/tienda-PRO.html`)
Secciones, en orden: portada hero (arte 3D/futurista `cover/fut1.png` + logo centrado slim) → barra de íconos (Productos/Mayoreo/Buscar/Compra fácil/Usuario/Carrito) → hero-carrusel de 3 anuncios → categorías deslizables (Focos + Reflectores/Solares/Ventiladores "Pronto") → **Productos** (5 tarjetas: 1 pza/pack 4/caja 12/30/50, imágenes `productos/p1-p5.png`, carrito localStorage) → tira "Pago seguro/Envío/Bien empacado" → **Míralo en acción** (comercial 16:9 `video/comercial-gato16.mp4`: foco encendido + gato al fondo) → frase puente → **Mayoreo = JUEGO de reventa** (carrusel de modelos con slider "cuánto ganas": Foco real + Reflector/Solar "Pronto") → **Confianza** (reseñas placeholder) → barra trust. Encabezados de sección `.sec` = badge + título + subtítulo + línea de acento. **Gatito IA vendedor** (abajo-dcha) conectado a Gemini en LOCAL (`asistente_ia.py`, :8787), en la nube usa respaldo scripted.

## 3) PIPELINE Y HERRAMIENTAS (ya funciona, reúsalo — no lo reinventes)
- **Imágenes:** Gemini `gemini-2.5-flash-image` (image-to-image o text-to-image). Scripts: `gen_cover.py`, `gen_productos_pro.py`, `gen_models.py`, `gen_caja12.py`. Llave `GEMINI_API_KEY` en `aurora-cafe/claves.local.txt`.
- **Video:** Kling v1.6-pro en Replicate (`REPLICATE_API_TOKEN`). OJO: header `User-Agent: curl/8.4.0` o Cloudflare bloquea; endpoint `/v1/models/kwaivgi/kling-v1.6-pro` → `latest_version`. Montaje con ffmpeg (`C:/Users/playg/Tools/ffmpeg-8.1.1-essentials_build/bin/`).
- **Python:** `C:/Users/playg/Tools/miniconda/python.exe`.
- **Publicar en Shopify:** `port_to_shopify.py` convierte `tienda-PRO.html` → sección liquid `buumia-theme-glass/sections/buumia-cine.liquid` (scope `.bx`, rutas→`asset_url`) y copia assets. Luego `shopify theme push --store j0hshz-nm.myshopify.com --theme 190418157890 --only ...` con `SHOPIFY_CLI_THEME_TOKEN` (de `buumia-shopify.env`). Preview: `https://j0hshz-nm.myshopify.com?preview_theme_id=190418157890`. Producto foco = borrador id `10386084921666` (2 variantes: 12 y 30). Fuente Baloo del kit está corrupta → usar `C:/Windows/Fonts/ariblk.ttf`.
- **Fonts extra fiables:** `ariblk.ttf`, `ARLRDBD.TTF`.

## 4) TU MISIÓN (produce estos 3 archivos, densos y listos para usar por Opus)
1. **`BUUM-ART-DIRECTION.md`** — sistema visual "guau" y COHERENTE para toda la tienda: paleta exacta, tipografía, estilo de portada/secciones/tarjetas, uso de glow/glass/3D, reglas de motion, y una lista clara de DO / DON'T. Meta: que cualquier pieza futura se vea de lujo y consistente. Incluye 3-4 "moodboard en palabras" concretos.
2. **`BUUM-PROMPTS.md`** — biblioteca de PROMPTS MAESTROS para Gemini y Kling, uno por tipo de pieza (portada, foto de producto fondo blanco, lifestyle, íconos de sección 3D, comercial con gato, anuncio). Cada prompt: parámetros, negativos, y el truco de lienzo 16:9 para forzar formato. Meta: que salga "guau" a la PRIMERA y ahorre créditos de Gemini/Kling.
3. **`BUUM-ROADMAP.md`** — plan PRIORIZADO y concreto (tabla: tarea · por qué · impacto · esfuerzo · quién=Opus/dueño) que cubra: mejoras de la página para llevarla a "excelente", **gatito IA a la nube (serverless) + carrito real Shopify**, **checkout/pagos Mercado Pago (tarjeta/OXXO)**, y siguiente producto a validar (visión novedades/importación). Pasos que Opus pueda ejecutar sin ti.

## 5) FORMATO
- Escribe los 3 archivos directamente en la raíz del proyecto. Al final, UNA lista de 5-8 bullets con "lo primero que Opus debe ejecutar". Nada más. Sé breve en el chat; el valor va en los archivos.
