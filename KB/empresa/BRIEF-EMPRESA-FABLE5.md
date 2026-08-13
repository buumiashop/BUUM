# BRIEF MAESTRO — Diseñar la empresa BUUM desde cero (para Fable 5)

> **Para el modelo que lee esto (Fable 5):** estás en el mismo entorno de Claude Code y el mismo
> proyecto que el asistente anterior (carpeta `CLAUDE 1 EJ`). Tienes acceso a **los mismos archivos,
> la misma memoria, las mismas llaves y las mismas herramientas** (Gemini, Replicate, Meta, Shopify,
> Python, ffmpeg). No hay que copiarte nada: ya está todo aquí.
>
> **Tu misión NO es mejorar la tienda actual.** Es **diseñar una EMPRESA COMPLETA desde cero**: su
> estrategia, sus números, sus operaciones, su estructura, su web propia y su mapa de crecimiento —
> tomando lo que ya existe solo como **referencia y activo**, no como base a la que amarrarte.
> Al final el dueño decidirá si mueve BUUM a esta nueva estructura o la adopta como su nueva casa.

---

## 0. Primero que nada (arranque para Fable 5)

1. Lee la memoria: `C:\Users\playg\.claude\projects\C--Users-playg-OneDrive-Documents-CLAUDE-1-EJ\memory\MEMORY.md`
   y los archivos que enlaza. Ahí está TODO lo hecho (tienda, marca, marketing IA, OS, nube).
2. Lee el BUUM OS: carpeta `buumia-os/` (MANUAL-CEO.md, ESTRATEGIA.md, EQUIPO.md, MANUAL-DE-OPERACIONES.md, etc.).
3. Llaves y herramientas (ya conectadas y funcionando — no volver a pedirlas):
   - **Gemini** (imágenes/texto): `aurora-cafe/claves.local.txt` (`GEMINI_API_KEY`).
   - **Shopify**: `buumia-shopify.env` (ADMIN `shpat_`, THEME `shptka_`). Tienda `j0hshz-nm.myshopify.com`, tema borrador id `190418157890`.
   - **Replicate** (Kling video, MusicGen), **Meta** (Facebook "BUUM" + Instagram `@buum.ia`) — ya conectados.
   - **Python**: `C:\Users\playg\Tools\miniconda\python.exe`. **ffmpeg** instalado. Servidor local siempre encendido en `http://127.0.0.1:8130` (raíz del repo).
4. Reglas de trabajo del dueño: **muy visual** (siempre enséñale preview, imágenes inline o página en navegador EXTERNO con Start-Process); **economizar créditos/recursos** (juntar cambios, decidir con mockups baratos de Gemini ~4¢ antes de editar, aplicar en tandas + 1 solo push); respuestas directas y con evidencia. Idioma: **español (México)**.
5. Empieza **haciéndole las preguntas que te falten**, luego ejecuta y ve construyendo.

---

## 1. Qué somos hoy (activos ya construidos)

- **BUUM** = marca (mascota gato "Kitsune" + logotipo "BUUM"). Colores oficiales `#EA5003` (naranja), `#962D08`, `#102AC4` (azul), `#001866`. Fuentes Reglisse/Coolvetica/Gotham. Kit en `buumia-catalogo/marca/`.
- **Tienda Shopify** (borrador) enfocada en iluminación. Archivo de trabajo `buumia-tienda/tienda-PRO.html` → se porta a la sección `buumia-theme-glass/sections/buumia-cine.liquid` con `port_to_shopify.py` → push con Shopify CLI. Preview: `https://j0hshz-nm.myshopify.com?preview_theme_id=190418157890`.
- **Departamento de marketing con IA**: pipeline **Gemini (imágenes) → Kling en Replicate (animación) → ffmpeg (montaje) → Meta (FB/IG)**. Skills `buumia-marketing` y `buumia-anuncios-ganadores`. Ya hay comerciales y anuncios publicados.
- **Vendedores IA**: "gatito" chatbot vendedor + embajadora "Sofía" (asesora que ayuda a revender).
- **BUUM OS**: sistema operativo de empresa en `buumia-os/` (7 áreas activas + RH), centro de mando HTML, organigrama.
- **Nube**: droplet en DigitalOcean (IP `165.227.181.176`, SSH `~/.ssh/buum_os`) con Python/ffmpeg — genera contenido en la nube.
- **El dueño**: 20 años vendiendo, mentalidad de que "el buen producto se vende solo". Meta = **dinero real**.

---

## 2. La visión (a dónde vamos) — LO IMPORTANTE

**Una empresa de NOVEDADES que vende TODO lo vendible que genere dinero.** Modelo mental: tipo
**TikTok Shop / Temu / Amazon / Mercado Libre**, pero con **producto PROPIO importado de China**
(vía Alibaba y fábricas que se descubren en YouTube / buenos proveedores).

No es "una empresa de iluminación". La iluminación es solo el **arranque**. La empresa vende de todo lo genial:

- **Juguetes de tendencia** (estilo *Miniso* pero más genial): los coleccionables/brainrot del momento —
  dumplings de varios tamaños y colores, "mantequillas", "zanahorias gigantes", los ninjas de Netflix,
  "tralalero tralala", "bubu", etc. Rotan rápido; hay que **cazar la tendencia** y entrar a tiempo.
- **Casa, jardín, seguridad**, y más adelante **bodegas, minería… todo lo genial**.
- Se vende con **mercancía física, almacenes propios y paqueterías** para distribución — lo tradicional
  de una empresa real — **combinado con la IA como CEREBRO** (gran parte de la operación, contenido y decisiones).

**Meta final:** de cero hasta **superempresa**. Estructura, mapa y todo lo necesario para lograrlo.

---

## 3. La primera piedra (arranque real, con números)

- **3,000 focos LED 60W** (luz blanca, rosca E27). Es el primer producto.
- **Costo puesto aquí ≈ $40 MXN** por foco. **Precio de venta recomendado = $75 MXN** c/u.
- (Referencia actual en tienda: caja de 12 = $899.99, caja de 30 = $2,249.99, todo a ~$75 c/u.)
- De este primer lote y su margen **arranca toda la publicidad y toda la empresa**. Empezamos de cero,
  con **poco capital**, cuidando el flujo de dinero: validar barato → escalar (muestras → lote → volumen).

---

## 4. Filosofía y reglas (heredadas — respétalas)

- **Enganchar en 1 segundo. ~95% visual** (poco texto). Todo **BRILLANTE** y con factor **WOW**.
- Posicionamiento: **"Súper calidad y súper precio"**. Nunca "barato/oferta" → siempre **"vale la pena"**.
- **"Vender el sueño" es dirección INTERNA** (dueño ↔ IA), **nunca** texto visible al cliente. Al cliente:
  info y ayuda **honesta** (sin garantías falsas, sin prometer lo que no se cumple).
- **Misión social**: buena luz / buenos productos a buen precio para México ("granito de arena").
- **Mentalidad millonaria**: rehacer hasta que quede excelente. **Economizar** en todo (tiempo, dinero, créditos).

---

## 5. Qué quiero que ENTREGUES (todo, súper real y ejecutable)

Un **plan maestro completo** para llevar la empresa de cero a superempresa. Que incluya, mínimo:

1. **Estrategia y modelo de negocio.** Qué vende, a quién, propuesta de valor, ventaja competitiva, por qué gana. Cómo **elegir novedades por tendencia** (método para detectar y entrar a tiempo). Marca/estructura corporativa (¿BUUM como marca paraguas? ¿nombres de líneas?).
2. **Finanzas y números reales.** Costos, márgenes, precios, **inversión por fase**, punto de equilibrio, proyección de **flujo de caja**, cuánto **reinvertir vs. ahorrar**, **merma** y devoluciones. Del foco a $40→$75 hasta la operación grande.
3. **Operaciones.** *Sourcing* en China (Alibaba/fábricas), importación/aduana/logística, **almacén**, inventario y **rotación**, **paqueterías** y envíos a la república. Rotación "base + oportunidad".
4. **Escalado físico.** Cuándo y cómo **comprar terreno + construir bodega** para distribución masiva nacional; costos; cómo ahorrar para ello; cuándo dar cada salto.
5. **Estructura de empresa + rol de la IA.** Áreas/organigrama, procesos, y **dónde la IA es el cerebro** (qué automatiza: contenido, atención, decisiones, análisis).
6. **Marketing y ventas.** Adquisición, contenido, canales (redes, marketplaces, web propia). Reutiliza el **dept de marketing IA** ya existente (Gemini→Kling→ffmpeg→Meta).
7. **Tu propia página web / tienda.** Créala **como tú quieras**, usando las llaves y herramientas de aquí. Toma la tienda actual (`buumia-tienda/tienda-PRO.html`) **solo de referencia**.
8. **Roadmap por FASES con metas medibles.** De la Fase 1 (validar los 3,000 focos) hasta la bodega inteligente y la distribución nacional. Cada fase: objetivo, inversión, meta de dinero, criterio para pasar a la siguiente.
9. **Dos manuales (siempre actualizados).**
   - (a) **Manual técnico/operativo para la IA** (para ti y para cualquier IA que continúe): cómo está montado todo, procesos, comandos, dónde está cada cosa, cómo ejecutar cada tarea.
   - (b) **Manual sencillo para el dueño**, en lenguaje humano, **sin tecnicismos**, explicado paso a paso (o que se lo vayas explicando): qué es cada cosa, qué decisiones tomar y cómo.
10. **Autonomía 99% IA / 1% dueño (visión).** Diseña el sistema para que en el futuro la IA haga **casi todo** y el dueño **solo autorice**. Patrón de decisión: la IA hace **investigación profunda + análisis de mercado nivel experto** y le presenta al dueño **opciones listas para elegir**. Ejemplo: *"Vamos a encargar 3 productos nuevos → aquí tienes 10 opciones ya investigadas y validadas, elige/autoriza."* El dueño aprueba y la IA ejecuta.
11. **Automatización e integraciones totales (futuro), 100% funcional y nivel extremadamente experto.** Todo conectado: **Google Ads, Facebook/Meta Ads**, marketplaces, proveedores, pagos, envíos, métricas. Deja el plan de **qué conectar, en qué orden y cómo lo operará la IA**.

**Cómo trabajarlo:** primero pregúntame lo que falte; luego **ejecuta y construye** (documentos, números, y la web), enseñándome previews en el camino y economizando recursos.

---

## ⭐ El principio del rascacielos (entrégalo para construirlo en la REALIDAD)

Piensa que te pedimos construir un **rascacielos** y nosotros lo vamos a levantar en el mundo real.
**No basta el plano/estrategia**: necesitamos **absolutamente todo lo necesario para ejecutarlo**, como si
el manual dijera a quién llamar, a quién contratar y a quién pagar:

- **Lista de materiales**: qué productos, insumos, herramientas y software, con **costos**.
- **Contratistas y proveedores concretos**: a quién comprar, a quién contratar, dónde, y **a quién depositar**.
- **Personal**: **cuántas personas** contratar, **de qué** (roles), **cuándo**, y **cuánto pagar**.
- **Pasos de ejecución en orden**: quién hace qué, cuánto cuesta y cuándo.
- Tan aterrizado que el dueño (o quien sea) **pueda ejecutarlo sin adivinar nada**.

**Ambición:** construir el **mejor e-commerce del universo**. Tú eliges la **estrategia** (empezar local o
como más convenga). Súper genial, a tu manera, pero **100% real y ejecutable**.

---

## 6. Rutas y llaves (resumen rápido)

| Cosa | Dónde |
|---|---|
| Memoria (todo el historial) | `...\memory\MEMORY.md` (+ archivos enlazados) |
| BUUM OS (empresa) | `buumia-os/` |
| Tienda actual (referencia) | `buumia-tienda/tienda-PRO.html` |
| Marca / kit | `buumia-catalogo/marca/` |
| Llave Gemini | `aurora-cafe/claves.local.txt` |
| Shopify (tokens/tema) | `buumia-shopify.env` · tema `190418157890` · `j0hshz-nm.myshopify.com` |
| Python / ffmpeg | `C:\Users\playg\Tools\miniconda\python.exe` · ffmpeg en PATH |
| Servidor local | `http://127.0.0.1:8130` (raíz del repo, siempre encendido) |
| Nube | DigitalOcean droplet `165.227.181.176`, SSH `~/.ssh/buum_os` |

---

### Resumen en una frase
Diseña, desde cero y súper real, **la empresa de novedades importadas de China** (con IA como cerebro,
mercancía física, almacenes y paqueterías) que arranca vendiendo **3,000 focos LED a $75** y crece,
por fases medibles, hasta ser una superempresa con bodega propia y distribución nacional — y que sea el
**mejor e-commerce del universo**. Entrégalo con el **principio del rascacielos** (todo para construirlo
en la realidad: materiales, proveedores, personal, a quién pagar), con **dos manuales** (uno para la IA y
uno sencillo para el dueño), pensado para llegar a una **autonomía 99% IA / 1% dueño** con integraciones
totales (Google/Facebook Ads, marketplaces, pagos, envíos): estrategia, finanzas, operaciones, estructura,
roadmap y su **propia página web** — todo entregable y ejecutable.
