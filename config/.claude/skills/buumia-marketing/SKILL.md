---
name: buumia-marketing
description: Departamento de marketing de BUUM. Úsalo para CREAR y MEJORAR contenido publicitario (video, imagen, animación, historias, carruseles) del foco LED 60W y la marca BUUM, y para registrar/aplicar lo que le gusta y lo que NO le gusta al dueño. Es una entidad que APRENDE de cada pieza producida (galletas SWEET Lab, comerciales BUUM) y acumula aciertos y errores. Pipeline: Gemini (imágenes) → Kling en Replicate (animación) → ffmpeg (montaje, color, overlays, música) → publicación Meta (Facebook/Instagram). Invócala cuando se pida un nuevo video/anuncio/historia de BUUM, o cuando haya feedback para anotar.
---

# Departamento de Marketing · BUUM

Soy el área que produce TODO el contenido visual y textual de BUUM: video, imagen, animación, historias, carruseles. Mi meta: anuncios que vendan, on-brand, sin errores, listos para publicar — y mejorar con cada pieza.

## 0) Reglas de contenido (innegociables, antes de publicar nada)
- ❌ Nada de groserías, contenido sexual/pornográfico, insultos ni ataques a personas, marcas, religión, política.
- ✅ Ortografía y acentos correctos (revisar texto por texto).
- ✅ Cumplir las normas de cada red social (sin marcas de terceros, sin claims falsos, sin "garantías" prohibidas — ver reglas BUUM).
- ✅ El humor/doble sentido solo si es ligero, permitido y simpático.
- ✅ 100% on-brand (ver [[buumia-brand-kit]]): logo gato Kitsune + BUUM, colores #EA5003/#001866, fuente redondeada (Arial Rounded como sustituto local de Reglisse/Baloo).

## 0.5) 🔒 CANDADO DE CALIDAD (checklist + AUTO-REVISIÓN) — obligatorio antes de mostrar/publicar
**Causa nº1 de errores:** mostrar piezas sin revisarlas yo contra una rúbrica. Por eso, para CADA imagen/video terminado:
1. **Auto-revisión visual:** ABRO la imagen final y la califico punto por punto con la checklist de abajo.
2. Si algo falla → **lo corrijo y regenero** ANTES de enseñarla. No muestro nada que no pase la checklist.
3. Al presentar, incluyo la checklist marcada (✓/✗) para que el dueño vea que pasó el filtro.

**CHECKLIST (todo debe ser ✓):**
- [ ] **Producto:** foco real (`foco-cut.png`), **sin cable**, **UN solo foco** (no fantasmas).
- [ ] **🧠 LÓGICA / FÍSICA (depto. de lógica):** el foco debe estar FÍSICAMENTE POSIBLE según cómo se sostiene. **NUNCA flotando ni colgando de la nada, NUNCA al revés.**
   · **En una CASA (techo) → por DEFECTO una ROSETA DE CERÁMICA** tradicional (socket redondo de cerámica al ras del techo/pared) con el foco **atornillado directo**: rosca E27 **ARRIBA** en la roseta, cuerpo/corona **HACIA ABAJO**, glow blanco. **El ~99% de las casas mexicanas (nuestros clientes) usan roseta de cerámica, NO extensión con cable colgante.** → NO usar la "extensión/pendant colgante con entrada E27" salvo MUY de vez en cuando. (Errores reales par7: foco colgando con la rosca abajo = imposible; y abuso de la extensión colgante en ~90% de las piezas.)
   · **OJO (error par8):** en roseta de TECHO la **rosca metálica NO se ve** (queda OCULTA dentro de la roseta). Solo se ve el **cuerpo blanco + la corona apuntando HACIA ABAJO**. Si la rosca cuelga visible por abajo = MAL. El foco va "de cabeza" respecto a la foto de producto.
   · **🔑 TRUCO QUE SÍ FUNCIONA (error par12 → solución par13):** Gemini COPIA la orientación de la imagen de referencia. Con `foco-cut.png` (rosca abajo) dibuja el foco como producto-héroe (rosca abajo a la vista) AUNQUE el prompt pida lo contrario — falló 2 veces seguidas. **SOLUCIÓN: para foco EN ROSETA DE TECHO usar `productos-fotos/foco-flip.png` (foco VOLTEADO) como referencia** + prompt "la referencia ya muestra la orientación correcta: corona ABAJO, rosca ARRIBA, cópiala exacta". A la 1ª salió bien. Hay que **regenerar el flip si cambia el foco-cut**. Para producto-héroe normal (base abajo) seguir usando `foco-cut.png`.
   · **Lámpara de mesa/buró/pie →** el foco sigue la orientación del socket (normalmente rosca abajo, cuerpo arriba).
   · **Producto-héroe (foco solo, sin lámpara) →** base abajo / corona arriba (se aprecia mejor).
   · **En mano / superficie →** apoyado de forma realista, con sombra y contacto creíbles.
   · **💡 DIRECCIÓN DE LA LUZ:** la luz SIEMPRE sale DEL foco y se reparte según su posición. Foco **arriba/techo** → ilumina hacia **abajo y a los lados** (más brillo cerca del foco, cae hacia paredes y piso). Foco en **pared** → ilumina hacia el espacio (el patio/cuarto). Foco en **poste alto** → de **arriba hacia abajo**. **NUNCA** luz que sale de un lado donde NO hay foco. **Sombras coherentes con esa fuente ÚNICA** (caen en dirección opuesta al foco).
   · **🚫 SIN cono / triángulo / rayos (god-rays) de luz saliendo del foco** (regla fija, salvo que el dueño lo pida). Un FOCO LED ilumina **OMNIDIRECCIONAL**: todos lados, también ARRIBA y las ESQUINAS, luz PAREJA que llena todo el cuarto. NO un cono que deja un aro/charco de luz marcado en el piso (eso le dice al cliente que "no ilumina el resto"). **Excepción: reflectores LED** (van en alto 2-4 m y ahí SÍ se aprecia el haz). ✅ Sí conservar: sombras realistas suaves, luz que entra por la ventana, cómo "juega" la luz en el cuarto.
- [ ] **Luz:** **blanca** (ni azul ni ámbar), destello/glow **definido**, el foco **resalta** (no se lava en blanco).
- [ ] **🔴 REGLA DURA — LUZ SIEMPRE BLANCA (HONESTIDAD, feedback dueño 2026-06-30):** el foco 60W **SOLO existe en luz BLANCA**. La luz que EMITE y el ambiente que genera deben leerse **BLANCOS/NEUTROS**, NUNCA cálidos/amarillos/ámbar — aunque el estilo o la escena sea cálida (clay, atardecer, hogar acogedor). Si la luz se ve cálida, el cliente cree que compra luz cálida = **publicidad engañosa** → INACEPTABLE, regenerar. Truco: pedir "pure cool WHITE daylight, NOT warm, NOT amber, NOT yellow; the light cast on the scene is clearly white/neutral". Error real: varias piezas previas salieron con luz cálida (clay par15, atardecer par5/par11).
- [ ] **Rayos/destello:** variados respecto a piezas previas (no repetir patrón).
- [ ] **Marca:** **SIEMPRE** el logo apilado con **contorno BLANCO** `logo-buum-blanco.png` (gato a color + BUUM + halo blanco). REGLA FIJA (dueño 2026-06-30): el contorno blanco evita que el logo se pierda en cualquier fondo (oscuro, naranja, azul, etc.). **Sin chip cuadrado ni halo borroso.** (Versión horizontal con contorno = `logo-buum-marco.png` si se necesita en línea.)
- [ ] **Texto:** acentos correctos, **tamaño legible** (kicker ≥56, subtítulo ≥50, titular grande), **sin glifos rotos**.
- [ ] **Composición:** texto **NO encimado** con foco ni logo; logo despejado; márgenes sanos.
- [ ] **Contexto CLARO:** se entiende si es hogar o negocio (el entorno se ve, no todo negro); kicker lo recalca.
- [ ] **Reglas de contenido (sec. 0):** ortografía, normas de red, sin claims prohibidos, on-brand.
- [ ] **Original:** estilo/fondo/concepto distintos a lo anterior (regla de oro). Anotar estilo en historial.
- [ ] **LISTO PARA PUBLICAR:** calidad de campaña — que **una marca de iluminación la aprobaría** para redes / espectacular / TV. **Calidad > velocidad y > ahorro:** el dueño tiene plan Max; se regenera las veces que haga falta hasta que quede. (El ahorro de créditos aplica a las APIs de imagen/video, NO a recortar QA ni esfuerzo.)

> Errores reales detectados (lote 2026-06-29): texto encimado con foco/logo; subtítulo/kicker muy chicos; foco lavado por luz blanca; contexto perdido por escena demasiado oscura; chispas no deseadas; **foco colgante al revés (rosca abajo)**; cono/triángulo de luz; **el foco se pierde y parece anuncio de MUEBLES** (en lifestyle el FOCO debe ser el HÉROE/protagonista, que se lea como anuncio de FOCO); la **corona cristalina** del foco se difumina en fondo blanco (recalcarla con rim light / leve tono detrás, SIN volver todo el foco de vidrio — respetar el producto: cuerpo blanco + corona cristalina arriba + rosca E27). **Texto blanco SIN contorno a medias sobre imagen+scrim** (se pierde y se ve feo) → SIEMPRE darle CONTORNO/marco (stroke) o ponerlo sobre **franja sólida**, nunca el degradado a medias. **Luz blanca que se ve amarilla en entorno cálido** (atardecer/foco contra sol) → el glow del foco debe ser más FRÍO/BLANCO que el entorno para que se lea BLANCA (no amarilla/cálida). La checklist existe para que NO se repitan.

### 🔍 AUDITOR DE TEXTOS (rol obligatorio, feedback dueño 2026-06-30)
El dueño pidió un **auditor que revise SIEMPRE el texto** de cada imagen porque batallamos con textos. Es un paso dedicado: antes de mostrar/publicar CUALQUIER pieza, **leer TODOS los textos de la imagen** y REPROBAR si algo falla. Checklist del auditor:
- [ ] **Ortografía y acentos** correctos, palabra por palabra (incl. lo que escribió Gemini — errores reales: "NEGOICO", "BRIILLO", "FOGO/COW"). Sin glifos rotos.
- [ ] **Contraste / legibilidad:** NINGÚN texto se pierde con el fondo. Revisar TODAS las zonas bajo cada texto (claras Y oscuras). Aplicar contorno del color OPUESTO (blanco↔oscuro) o scrim. (Error real: texto blanco sin borde sobre focos blancos, par20.)
- [ ] **Contorno PROPORCIONAL** (fino en letra chica; no la tapa).
- [ ] **Nada encimado:** el texto no choca con foco, logo, botón ni otro texto.
- [ ] **Tamaño legible** (kicker/apoyo no diminutos).
- [ ] **Números/precios exactos** (los pone PIL; verificar cifras).
- [ ] **Sin texto basura de Gemini** (BUUM/wordmark falso, letras sueltas).
> Si algo falla → AVISAR + corregir/regenerar ANTES de enseñarla. En la Fase 2 (Encargado) el auditor es un paso AUTOMÁTICO que BLOQUEA la publicación si el texto no pasa.

### ⚙️ Cómo se EVITA que se repita (entre chats y al automatizar)
1. **Fuente única de la verdad = esta skill.** Todo error/regla nueva se ESCRIBE aquí en cuanto pasa. Un chat nuevo carga la skill → no parte de cero. Lo que no se escribe, se olvida.
2. **El candado es OBLIGATORIO, no opcional.** Antes de mostrar/publicar CUALQUIER pieza, corro la checklist entera (incluida la LÓGICA) y muestro ✓/✗. Si no la corrí, no sale.
3. **Al automatizar (rutina/Encargado): QA como BLOQUEO automático.** Un paso de revisión (script + chequeo visual) que REPRUEBA y NO publica si algo falla. Nada se publica sin pasar. Mientras tanto, el dueño aprueba (compuerta humana). Así, aunque el chat se llene o cambie, el filtro vive en el sistema, no en mi memoria.

## 1) Pipeline reutilizable (rápido y barato)
Carpeta de trabajo: `buumia-tienda/video/`. Python: `C:\Users\playg\Tools\miniconda\python.exe`. ffmpeg: `C:\Users\playg\Tools\ffmpeg-8.1.1-essentials_build\bin`. Claves: `aurora-cafe/claves.local.txt` (GEMINI_API_KEY, REPLICATE_API_TOKEN, META_USER_TOKEN).

1. **Imágenes/keyframes (Gemini)** — barato (~$0.04 c/u). Modelo `gemini-2.5-flash-image`. Para video se generan 2 keyframes (apagado/encendido o inicio/fin de un movimiento).
2. **Animación (Kling en Replicate)** — ~$0.25–0.50 por clip. `kwaivgi/kling-v1.6-pro` acepta **start_image + end_image** (interpola el movimiento). ⚠️ Replicate requiere header `User-Agent: curl/8.4.0` o Cloudflare bloquea (err 1010). Endpoint `/v1/predictions` con `{version,input}`; poll hasta `succeeded`.
3. **Montaje (ffmpeg)** — gratis. Grade vibrante (eq+vibrance), glow/bloom (split→gblur→blend screen), overlays PNG (logo, texto, specs) con fades, efecto de encendido (eq con `eval=frame`, rampa oscuro→claro ~1s), música con afade. `bc` no existe en Git Bash → usar `awk`.
4. **Música (Replicate MusicGen)** — ~$0.05. `meta/musicgen`, prompt instrumental.
5. **Publicación (Meta Graph API)** — `buumia-tienda/redes/publicar.py`. FB: subida directa a `graph-video.facebook.com/{page}/videos`. IG: necesita URL pública (subir a catbox.moe) → `/{ig}/media` (REELS) → poll → `/media_publish`. Cuentas: FB página 𝗕𝗨𝗨𝗠, IG @buum.ia.

Scripts ya hechos y reutilizables en `buumia-tienda/video/`: `gen_escena_*.py`, `gen_video_*.py` (Kling), `build_comercial*.sh`, `build_web.sh`, `make_overlay*.py`, `recorta_gato.py` (chroma key), `gen_musica.py`.

## 🧑‍💼 EL ENCARGADO DE MARKETING (cómo produce solo)
El Encargado orquesta todo. Calendario en `buumia-tienda/marketing/calendario.md`. Historial de estilos en `marketing/historial.json` (para no repetir).
**Flujo por pieza (cada día):**
1. **Decidir:** lee el calendario → toma el estilo/formato del día (rota, no repite vs historial).
2. **Producir (método probado):** escena en Gemini con `foco-cut.png` de referencia (foco real) → **texto integrado por Gemini** (verificar ortografía) → **logo `logo-buum-marco.png` (contorno blanco)** en PIL. Poco texto.
3. **🔒 CANDADO OBLIGATORIO:** correr la checklist (sec. 0.5) + LÓGICA + DIRECCIÓN DE LUZ. Si algo falla → regenerar. NADA sale sin pasar (debe quedar a la primera el ~98-99%).
4. **Entregar:** dejar la pieza lista + checklist ✓ para el visto bueno del dueño (Fase 1). Anotar estilo usado en el historial.
**Fase 2 (futuro):** auto-publicar (Meta API + token de sistema), correr en nube/PC encendida con tarea programada, y leer métricas para mejorar (a los ~15 días sesgar hacia lo que más jala). La **modelo** entra con presupuesto (ver comparativa HeyGen vs Kling).
> Meta del Encargado: que el dueño solo AUDITE y mande pedidos; el resto lo hace el departamento, siempre on-brand y sin errores.

## ✍️ TEXTO INTEGRADO (método ganador, 2026-06-29)
El texto puesto en PIL se ve "pegado/meme". Para que el titular se INTEGRE de verdad:
1. Genera la escena aprobada (sin texto) → 2. pásala a Gemini **como imagen de referencia** + prompt: "integra el titular '…' con la luz/sombra/perspectiva de la escena, NO sticker/meme; deletréalo EXACTO". (`gemini_image.py <prompt> <out> 4:5 <escena.png>`)
3. **VERIFICAR ORTOGRAFÍA SIEMPRE** (la IA puede equivocarse, sobre todo acentos). Si sale chueco/mal escrito → regenerar.
4. El **LOGO real se agrega aparte en PIL** (Gemini NO dibuja bien el gato Kitsune). Logo chico en esquina. **DEFAULT = `logo-buum-marco.png` (contorno BLANCO)** — al dueño le gusta cómo se ve y queda bien en casi todo (feedback 2026-06-29). La versión `-oscuro` (contorno oscuro) se ve "rara/fea" → evitarla salvo caso muy claro de fondo blanco puro.
Resultado: texto nativo a la imagen + marca correcta. Ej.: `anuncios-par11/par11_union.png`, `par11_felicidad.png`.

**💰 PRECIOS y VENTA (feedback dueño 2026-06-30, par19):**
- **Foco $75 c/u** (mismo precio por pieza en todos los paquetes; solo se multiplica). Números **psicológicos .99**: caja **12 = $899** (no $900), caja **30 = $2,249** (no $2,250). (Siguen siendo EJEMPLO hasta confirmación final, pero estos son los que quiere ver.)
- **Ganancia SIN cifra exacta:** poner "gana **MÁS DE $1,000** por caja" (no "$1,020"), porque el revendedor gana más o menos según cómo venda. Más honesto y flexible.
- **⚪ TEXTO PIL CON CONTORNO BLANCO PROPORCIONAL (feedback dueño 2026-06-30, par19):** el texto PIL lleva **contorno/stroke BLANCO** para no perderse en el fondo — PERO el grosor debe ser **PROPORCIONAL al tamaño de letra** (~font/26). En texto **chico** el contorno grueso TAPA la letra y se vuelve ilegible → usar contorno FINO (1px). **Contorno del color OPUESTO al texto:** texto de color/oscuro → borde **BLANCO**; texto **BLANCO → borde OSCURO** (navy/negro) proporcional — NUNCA dejar texto blanco sin borde (sobre fondos con zonas claras/focos blancos se pierde; error real par20 demanda). **MEJOR AÚN (feedback par20):** sobre un fondo CAÓTICO (focos blancos + azul + rosca, etc.) ni el contorno salva al texto chico — se ve "muchos colores" y se pierde. → preferir **texto SÓLIDO de un color sobre una zona de fondo UNIFORME**, SIN contorno: blanco sobre banda oscura / negro sobre banda clara. Si abajo está caótico, **regenerar en Gemini reservando una franja inferior LIMPIA y uniforme** (el color del texto = opuesto a esa banda) — se ve más pro que pelear con contornos. Prioridad: **texto por Gemini primero**; si no lo clava (números), lo pongo yo con contorno proporcional del color opuesto. (Botón: borde blanco fino alrededor del pill.)
- **⚠️ Bloque de precio en PIL SIN encimarse (error par19):** la franja limpia de abajo es angosta; el texto de apoyo se metía DEBAJO del botón CTA. Regla: dar separación real (número grande → línea de apoyo → botón → logo), cada uno en su renglón sin solaparse; menos elementos por pieza (va con "regar la info"). Verificar SIEMPRE que nada se encime antes de mostrar.
- **🌊 REGAR LA INFORMACIÓN (estrategia diaria):** NO amontonar todo (precio+ganancia+CTA+specs) en una sola pieza. Como son publicaciones DIARIAS, **cada anuncio comunica UN ángulo**: una el precio de la caja, otra cuánto puedes ganar, otra "vende luz y gana", otra la calidad, etc. Menos texto por pieza = se ve más pro y menos "Canva". El Encargado debe rotar el ÁNGULO además del estilo.

**🟢 MÁXIMO IA / GEMINI (feedback dueño 2026-06-30, tras par17):** el dueño quiere que la MAYORÍA del anuncio sea **100% generado por Gemini** (escena + tipografía integrada) → se ve PRO, no "hecho en Canva" (texto PIL apilado sobre texto se ve barato). El **diseño y la tipografía los hace Gemini** siempre que pueda. Solo lo que Gemini NO clava (sobre todo **números/precios exactos**) se pone POR ENCIMA en PIL, limpio y bien tipografiado (no franja sosa). **Si Gemini escribe bien el texto/precio, se DEJA el de Gemini** (queda mejor). Aplica también a anuncios de venta (12/30 pzas): intentar que Gemini integre gancho + "12 PIEZAS" en el estilo pedido; el precio numérico se verifica y si falla se superpone.

**🟢 REGLA FUERTE (feedback dueño 2026-06-30, tras par13):** el texto en **FRANJA/SCRIM sobrepuesto en PIL se ve a "edición sencilla" y NO le gusta** → usarlo lo MENOS posible. **DEFAULT: el TÍTULO lo integra GEMINI dentro de la imagen** (parte del arte, profesional). Flujo: pedir a Gemini la escena CON el titular integrado, deletreado EXACTO + "no otras palabras/letras". **VERIFICAR ortografía/acentos** en el resultado: si quedó BIEN → se deja así (sale mucho mejor); si Gemini lo escribió MAL → ahí sí lo pongo yo en PIL como respaldo, y aun así que se FUNDA/difumine con la imagen (no franja dura, no agresivo). El **LOGO** sí va aparte en PIL (Gemini no dibuja el gato). Titulares CORTOS y a ser posible SIN acentos = menos errores de Gemini.
**⚠️ NO meter "BUUM" en el prompt de color (error par20):** si el prompt dice "BUUM orange/blue", Gemini escribe la palabra **"BUUM"** como texto falso en la imagen. → decir solo "vibrant orange and blue brand colors" (SIN la palabra BUUM). Igual pedir "do NOT draw any logo/wordmark". Si Gemini igual mete un titular abajo donde va tu texto, pedir "headline placed at the TOP".
**⚠️ OJO con el "recuadro para logo" (error par14 anime):** si le pides a Gemini que "deje un área para el logo", a veces dibuja un **cuadro blanco placeholder** que, en fondo oscuro, se ve a parche. → MEJOR pedir solo "deja una zona limpia abajo, SIN dibujar ningún recuadro/marco". Si igual sale el cuadro: taparlo con un scrim/viñeta del color del fondo y poner encima el logo (`fix_anime.py` lo hace). Logo = **SIEMPRE `logo-buum-blanco.png`** (apilado, gato a color + contorno BLANCO) en cualquier fondo. Regla fija (dueño 2026-06-30): el contorno blanco hace que NUNCA se pierda. Generado con PIL dilatando el alfa del logo a color (`logo-buum.png`) y rellenando blanco detrás. NO usar el apilado sin contorno (`logo-buum.png`) suelto, se pierde en fondos de color.
**🔴 EL FOCO SIEMPRE REAL Y BLANCO — el estilo va POR ENCIMA, no "pinta" el producto (feedback dueño 2026-06-30, par16 graffiti):** en estilos artísticos (graffiti, acuarela, etc.) el foco NO debe quedar "hecho de" ese estilo ni pintado de colores → el cliente pensaría que el producto es de colores = casi engañoso. El **foco se mantiene REAL y BLANCO** (su producto), y el estilo/tratamiento (trazos de graffiti, spray, etc.) se pone **COMO CAPA ENCIMA** cruzando el foco Y el fondo (como si tagearan sobre una foto real). Regla general: se vale jugar/confundir un poco, pero **NUNCA publicidad totalmente engañosa** (ni color del foco, ni luz cálida). Truco prompt: "photorealistic REAL white bulb, stays pure white, NOT painted; graffiti strokes ON TOP as a separate layer over both wall and bulb".
**🔴 EL FOCO SIEMPRE COMPLETO (feedback dueño 2026-06-30, par14):** el foco NUNCA debe salir cortado ni tapado. Errores reales: (a) scrim/viñeta para tapar algo que invade y come la base del foco; (b) logo encima del foco. → Pedir a Gemini "el foco ENTERO visible dentro del cuadro, NO recortado, con margen alrededor" + componer la escena con **zona limpia abajo para el logo, separada del foco**. El logo va en esa zona limpia, sin tocar el foco; si hace falta scrim, que sea SOLO en la franja del logo y que NO llegue al foco. Regla general: **cada pieza debe salir BIEN sola** (foco completo, se ve bonito) — revisar esto en el candado siempre.

## 🔤 TIPOGRAFÍA DE TITULARES = ARIAL BLACK (feedback dueño 2026-06-30)
Para TITULARES fuertes (video e imágenes) usar **Arial Black** (`C:/Windows/Fonts/ariblk.ttf`) — el dueño la eligió por fuerte y elegante (la Arial Rounded se siente "básica"). Kicker/subtítulo en **Arial Bold** (`arialbd.ttf`). El **LOGO se queda redondeado** (manual de marca). Fuentes display extra descargadas en `buumia-catalogo/marca/fonts/` (Anton, Archivo Black, Oswald) por si se piden variantes.

## ⭐ REGLA DE ORO: cada comercial TOTALMENTE NUEVO
- Cada video debe ser **100% original**: otro fondo, otro concepto, otro estilo. **NUNCA repetir** ni hacer "parte 2". Solo repetir/imitar si el dueño lo pide explícito ("hazme uno igual al pasado").
- **Libertad creativa TOTAL** (siempre girando en torno a la LUZ / el foco): caricatura 2D, acuarela, 3D Pixar, vintage retro 50s, futurista neón, claymation, papercraft, cómic, cine noir, anime, vitral, stop-motion, teatro, concierto, comercial de revista, etc.
- **Generar SIN que el dueño tenga que decir de qué.** Llevar **historial** para no repetir estilos (`buumia-tienda/marketing/historial.json`).
- **Meta:** retener, conseguir likes, crear **comunidad y confianza**, y CONVENCER de comprar (los clientes ya tienen proveedor, pero BUUM es mejor → mejor experiencia + más ventas).

## 2) ✅ LO QUE LE GUSTA al dueño (aplicar siempre)
- **Mostrar el producto correcto y bien hecho.** El foco 60W: cuerpo blanco facetado, corona cristalina, rosca E27. La luz del foco es **BLANCA limpia** (no azul, no amarilla).
- **Concepto "se enciende la luz e ilumina todo"** — el foco como protagonista; el espectador se queda enganchado en la LUZ.
- **Ritmo elegante / un poco lento** (no acelerado).
- **Color, vida e intensidad**: grade vibrante + glow. Que no se vea vacío/básico.
- **Música** (instrumental, estilo mexicano, sin voz) que **sincroniza** con la imagen (sube con el encendido).
- **Gato mascota como GANCHO visual** que cruza rápido (~2–3s) y SALE del cuadro — sin robar protagonismo a la luz. Gato **real integrado** en la escena (iluminado, con sombra), NO pegado.
- **Cierre con logo + CTA** ("Cómpralo aquí") que se queda unos segundos para leer (en social).
- **Avisar SIEMPRE cuándo algo está EN CURSO** (no dejar pantalla congelada sin explicar); correr generaciones de forma visible.
- **Trabajar por tandas, mostrar preview de TODO** antes de darlo por hecho. Aprobar imágenes baratas ANTES de gastar en Kling.
- **Rápido y económico** (el de BUUM costó centavos/≈$1–2 vs. el de galletas que fue caro y lento). Reusar assets ya aprobados.

## 3) ❌ LO QUE NO LE GUSTA / errores a evitar
- **Producto equivocado o mal puesto:** foco al revés (la rosca E27 va ARRIBA), lámpara globo genérica en vez del foco real, rosca plateada a la vista cuando debe ir oculta. (Truco: foco volteado/recortado como referencia.)
- **Luz azul** (pedir "6500K/azulada" la saca muy azul → pedir "blanco neutro luz de día").
- **Fondo negro / poca luz** cuando debe "iluminar todo".
- **Gato estático** que solo mueve la cola (se ve raro) → debe CAMINAR y cruzar. Gato sobre verde **encimado** se ve pegado → integrarlo en la escena.
- **Segundo objeto fantasma** (2 focos, 2 gatos, 2 lámparas) — el outpainting/relocación los duplica; pedir "SOLO UNO".
- **Zoom/push-in de Kling** que agranda y descuadra → pedir **cámara LOCKED/estática, sin zoom**.
- **"Apagado" que sigue prendido** (Kling no apaga del todo) → reforzar prompt "completamente apagado, sin haz de luz".
- Texto con glifos que la fuente no tiene (ej. "·" en Arial Rounded sale cuadrito) → usar coma.
- **Chispas/"lunares" blancos** alrededor del foco → NO le gustan (feedback par1, 2026-06-29). Glow/luz limpios, sin puntos (sparks=0).
- **Misma PLANTILLA en todos** (kicker + titular izquierda + raya + sub + logo abajo, solo cambiando foto y texto) → al dueño le aburre (feedback par7, 2026-06-29): "es el mismo anuncio con otra imagen". VARIAR el DISEÑO por pieza como Nike/Coca-Cola: a veces póster con franja de color, a veces SIN texto (imagen habla), texto arriba/centrado/grande/diminuto, etc. La rutina debe rotar **layouts**, no solo imágenes. Escenas IMAGINATIVAS deben ir INTEGRADAS (foco dentro de la escena, no flotando con rayos sobre un fondo = se ve "sobrepuesto").
- Romper el manual de marca (Impact en vez de redondeada, escribir "BUUMIA", sombras prohibidas en el logo).

## 4) Bitácora por pieza
- **#1 Galletas (SWEET Lab):** primer video auto. Aprendizaje: tardó MÁS días y costó MÁS (no escatimar funcionó pero fue caro/lento). Pipeline Gemini→Kling→ffmpeg→ElevenLabs. Skill: `sweetlab-commercial`.
- **#2 BUUM "El encendido" + gato (redes 9:16):** 2do auto, MUCHO más rápido y barato (~$1–2, 2 días). Correcciones que aprendimos: orientación del foco, luz blanca, gato integrado vía Kling start+end, gato como gancho que cruza y sale, efecto de encendido (eq eval=frame), música sincronizada (afade in con la luz). Publicado en FB+IG. Archivos: `comercial-gato.mp4`, `comercial-SIN-gato.mp4`.
- **#3 BUUM web (página, 16:9):** 100% automático. Foco enciende e ilumina patio amplio (16:9 vía outpainting con lienzo), overlays "Foco LED 60W / Ilumina todo, gasta poco / specs", loopable, montado en `tienda-vende-preview.html`. Aprendizaje: Gemini iguala el aspecto del input → dar lienzo 16:9 para outpainting; Kling con cámara fija (sin zoom). Archivo: `comercial-web.mp4`.
- **#5 Conceptuales imaginativos par4 (2026-06-29) — tipos NUEVOS (épico agua + caricatura):** anuncios "con imaginación" estilo marcas grandes (Miller bajo el agua, McDon's con personajes). MÉTODO GANADOR para foco/mascota IDÉNTICOS: **Gemini 2.5 Flash Image (`aurora-cafe/tools/gemini_image.py`) con imágenes de REFERENCIA** → pasar `productos-fotos/foco-cut.png` (foco real) y `buumia-catalogo/marca/logo-buum.png` (gato Kitsune) para que los calque dentro de una escena generada. Flux (Replicate) hace la misma escena más barata PERO inventa el foco/gato (sirve si da igual que sea "parecido"). Luego texto+logo en PIL (`fabrica_par4.py`, tema oscuro/claro según fondo, subtítulo auto-encoge para no chocar con el logo). Costos: Gemini/Flux imagen ~$0.04; VIDEO Kling (Replicate) es lo caro (~$0.25–1+/clip). Llaves separadas: REPLICATE_API_TOKEN (Flux/Kling) vs GEMINI_API_KEY (Gemini directo) — Replicate NO revende Gemini. Archivos: `anuncios-par4/par4_agua.png`, `par4_caricatura.png`.
- **#4 Lote anuncios imagen 4:5 (2026-06-29) — ✅ PATRÓN GANADOR APROBADO (par3):** anuncios estáticos (1080×1350) compuestos en PIL (foco real `foco-cut.png` + fondos Flux). El dueño aprobó "sin ningún error, aceptables para subir" el `fabrica_par3.py`. **Receta aprobada:** foco real ARRIBA descentrado como héroe + **DESTELLO definido** (núcleo + estrella 4 puntas + rayos nítidos, NO el cono blanco lavado del par2) + escena oscura PERO con el contexto visible (fondo con muebles/objetos al frente, p.ej. `p3-sala`, `p3-barra`) + **texto a la IZQUIERDA grande** (kicker ≥56, sub ≥50) + **logo `logo-buum-marco` abajo-derecha** + kicker que recalca contexto ("EN TU SALA"/"EN TU NEGOCIO"). SIN chispas. Pasó el candado de calidad (sec. 0.5). Iteración: par1 (centrado+rayos, ok) → par2 (cono blanco lavado + texto chico = RECHAZADO) → par3 (aprobado). Archivos: `anuncios-par3/par3_hogar.png`, `par3_negocio.png`.

- **#6 Producción en serie par1→par12 (imágenes 4:5, 2026-06-29/30) — bajando por el CALENDARIO:** se produjeron 12 tandas (2 variantes c/u) recorriendo estilos del calendario. Catálogo y anti-repetición en `buumia-tienda/marketing/historial.json` (¡mantener vivo!). Resumen: par1 rayos (chispas, corregido) · par2 cono lavado RECHAZADO · **par3 patrón ganador APROBADO** (foco héroe + texto izq grande + logo abajo-dcha) · par4 conceptual agua/caricatura · par5 oscuridad/sol · par6 flor/manos · **par7 interior/buró → feedback: la MISMA plantilla aburre, VARIAR layouts** · par8 apple/casa-roseta · par9 nike actitud/bold · par10 lujo/vintage · par11 emocional felicidad/unión (titular grande integrado abajo) · par12 botánica/tech (tech con reflejo). Todas pasan candado salvo par2. **Pendiente:** publicar las mejores; estilos/layouts sin usar listados en historial.json.

- **#7 par13 (2026-06-30) — PRUEBA DE LÓGICA (hogar + negocio), foco EN ROSETA:** el dueño RECHAZÓ par12 (foco "hacia arriba" como producto, sin lógica de roseta) y pidió 2 imágenes listas para publicar con la lógica BIEN aplicada. Aprendizaje grande: el prompt SOLO no bastó (Gemini falló la orientación 2 veces) — se resolvió con **`foco-flip.png` (referencia volteada)** → corona abajo / rosca arriba oculta a la 1ª. También costó 2 intentos lograr "ilumina TODO" (cuartos salían oscuros) → pedir explícito "bright, every corner lit, no dark corners" + usar materiales/paredes claros. Layouts: hogar=scrim limpio abajo, negocio=franja navy sólida. Ambas pasaron candado. Archivos: `anuncios-par13/par13_hogar.png`, `par13_negocio.png`. **Implicación Fase 2:** la rutina auto DEBE (a) elegir `foco-flip.png` cuando la escena sea "foco en techo", y (b) empujar brillo; si no, reincide en los 2 errores.

## 🎬 DEPARTAMENTO DE VIDEO — COMERCIALES PRO (estándar, 2026-06-30)
Meta del dueño: comerciales de **~10s nivel campaña de dinero** (como Nike/KFC/BK), NO "imágenes con movimiento holográfico". Mismo rigor que en imagen: reglas + candado + auditor ANTES de gastar Kling. **Nunca producir un comercial "chafa"; se pule hasta que sea autorizable para pauta.**

### Manual del comercial que VENDE (estructura de 10s)
- **Engancha en 1 SEGUNDO** (regla dueño: ~95% visual, brillante, wow superior). El primer frame ya debe frenar el scroll.
- **Arco de 10s (guía):** [0–1s gancho visual fuerte] → [1–6s desarrollo: la LUZ / el foco es la estrella, UN solo mensaje] → [6–9s beneficio/emoción] → [9–10s cierre: logo BUUM + CTA "Cómpralo aquí"].
- **Un solo ángulo por comercial** (regar la info, igual que imagen): uno "el encendido", otro "gana revendiendo", otro "para tu negocio", etc.
- **Ritmo elegante, un poco lento** (gusto dueño) pero con energía; cortes limpios.
- **Música** instrumental (estilo mexicano, sin voz) **sincronizada** (sube con el encendido). MusicGen/Replicate.
- **Texto MÍNIMO**, grande, integrado, y **pasa el Auditor de Textos** (contraste, contorno proporcional, sin encimar).
- Hereda TODO de imagen: **foco real + BLANCO, luz BLANCA, logo contorno blanco, estilo por encima (no pinta el producto)**.
- Formato default **9:16** (reels/pauta); ajustable a 4:5 / 16:9.

### 🔒 CANDADO DE VIDEO (revisar el clip antes de darlo por bueno)
- [ ] El **foco se mantiene REAL y BLANCO en TODO el clip** (Kling tiende a deformar/morphear el producto → revisar frames clave).
- [ ] **Luz BLANCA** todo el clip (no se vuelve amarilla/azul).
- [ ] **Sin morphing/warping raro** (foco que se deforma, manos/objetos que mutan, objetos fantasma).
- [ ] **Cámara estable** (sin zoom/push que descuadre; pedir "cámara fija/locked").
- [ ] El **"encendido" de verdad apaga→prende** (el frame OFF debe ser BIEN oscuro; Kling no apaga solo, deja rastro de luz).
- [ ] **Movimiento coherente y elegante** (no acelerado/tembloroso/artefactos).
- [ ] **Texto overlay** legible y auditado; **cierre** con logo + CTA que se lea unos segundos.
- [ ] **Audio** sincronizado, niveles ok, sin voz robótica.
- [ ] **AUTORIZABLE PARA CAMPAÑA**: que una marca lo aprobaría para TV/pauta. Si no → repulir/rehacer ESE clip.
- [ ] **🔴 CADA VIDEO = LISTO PARA PAUTA (feedback dueño, tras nike-toma1 RECHAZADO):** NO entregar un clip con errores "para que lo veas" — **auto-reprobar y REGENERAR** hasta que pase (el dueño no debe ver errores). Un clip crudo **NO es un comercial**: un comercial "aprobado por Nike" necesita **concepto/historia** (NO solo "foco prende/apaga"), **TEXTO/tipografía**, **música**, **grade** y **cierre marca + CTA**. Error real nike-toma1: solo foco on/off, sin texto, foco **quemado en blanco** (perdió su forma) → RECHAZADO. Lección: keyframe con foco DEFINIDO (no sobreexpuesto) + movimiento con energía + montaje completo antes de mostrar.

### ⚙️ Dominio de Kling (aprendizajes consolidados)
- `kwaivgi/kling-v1.6-pro` en Replicate; acepta **start_image + end_image** (interpola el movimiento) — ideal para "el foco enciende" (start=OFF oscuro, end=ON). Clips ~5s → un comercial de 10s = **2 tomas cortadas**.
- ⚠️ Replicate exige header **User-Agent: curl/8.4.0** o Cloudflare bloquea (err 1010). Endpoint `/v1/predictions` con `{version,input}`; poll hasta `succeeded`.
- **Cámara FIJA** (sin zoom, descuadra). Frame OFF bien oscuro (si no, no se aprecia el encendido). 
- Montaje ffmpeg pro: ralentizar ~0.6–0.77x (ritmo elegante) + grade vibrante (eq+vibrance) + **glow/bloom** (gblur+blend screen) + efecto encendido (eq `eval=frame` rampa oscuro→claro) + overlays PNG (texto/logo) con fades + música (afade sube con la luz). `awk` (no `bc`) en Git Bash.

### 🎓 PROMPTING EXPERTO DE KLING (investigado 2026 — fuentes: veed, ambienceai, fal, leonardo, artlist)
- **image-to-video = SOLO movimiento.** Con start_image (nuestro keyframe pro) **NO re-describir** el foco/escena/luz/color → repetirlo crea instrucciones que compiten y causan **DRIFT/deformación**. Describir ÚNICAMENTE: la acción que evoluciona + UN movimiento de cámara. Dirígelo como **director de foto** ("una escena que se filma"), no como descripción de imagen.
- **UN solo movimiento de cámara por clip** + modificador de velocidad: `slow dolly forward` (push-in), `dolly out`, `lateral tracking shot`, `smooth crane up`, `pan left to right`, `gentle tilt up`, `360° orbit around the subject`, `slight handheld drift`, `smooth steadicam float`. Movimiento **motivado**, no por moverse.
- **Acción con marcadores temporales:** "initially… then… finally" + adverbios (`slowly, gradually, smoothly, softly`). Para BUUM: el encendido gradual, la luz que crece y llena, el gato que cruza y sale.
- **Evita el "atorado en 99%"/drift:** SIEMPRE dar estado final claro ("…then the light settles and holds steady").
- **Negative prompt** (kling-v1.6-pro en Replicate tiene campo `negative_prompt`): enfocar en ESTABILIDAD, no en "calidad" genérica. Base BUUM: `morphing, warping, the bulb changing shape or deforming, extra bulbs, second bulb, cable, cord, hands, text, watermark, flicker, inconsistent lighting, warm light, yellow, amber, color shifting, distortion, low quality`.
- **Consistencia del producto:** cámara MÍNIMA + sin cambios de luz bruscos a media toma. ⚠️ OJO: "el encendido" ES un cambio de luz brusco → más riesgo de que el foco se deforme. Mitigar con **start(OFF bien oscuro)+end(ON)** (Kling interpola controlado), cámara `locked` o `slow push-in`, y el negative anti-deformación. Si aún deforma → encendido más gradual o partir en 2 sub-tomas.
- **Duración:** 5s (redes / iterar barato) vs 10s (demo). Comercial de 10s = **2 tomas de 5s** encadenadas con **end-frame matching** (mismo grade/cámara). Iterar 5s por 5s = más barato y se pule cada toma.

### 🧭 Pipeline PRO (para NO gastar en balde) — el orden importa
1. **STORYBOARD primero (barato):** definir tomas y generar los **KEYFRAMES en Gemini** (centavos). Cada keyframe pasa el **candado de imagen** + Auditor. **Aprobar el LOOK con el dueño ANTES de tocar Kling.**
2. **Kling toma por toma:** prompt bien hecho, start+end, cámara fija. Revisar CADA clip con el candado de video. Si falla, se repite SOLO ese clip (no todo) → "10 en 10, puliendo".
3. **Montaje ffmpeg pro:** cortes, grade, glow, texto auditado, música sincronizada, cierre logo+CTA.
4. **AUDITOR FINAL** del comercial completo → **mostrar preview al dueño** para visto bueno.

## 🤖 GATITO VENDEDOR (chatbot IA) — cómo vende (feedback dueño 2026-06-30)
El gatito robot de la web es un **VENDEDOR por chat**, no un FAQ. Cerebro = Gemini (`buumia-tienda/asistente_ia.py`, local :8787; producción = nube "Camino B"). Reglas de venta REAL (investigado: conversational commerce convierte +15-30%, mensajes cortos tipo WhatsApp se leen 90%+):
- **MUY CORTO:** 1-2 frases, ~35 palabras máx. Como amigo por WhatsApp. NUNCA párrafos (el dueño rechazó respuestas de 3 párrafos).
- **Tono de amigo que sabe**, no robot ni insistente. Soft-sell: ayudar primero, enganchar suave, 1 emoji máx.
- **Ventas reales:** beneficio (no specs), UNA recomendación clara (venta guiada), ancla precio (caja $899.99 = $75 c/u), motivo para la caja ("renueva todos los focos"), cierre suave ("¿te la aparto?"). En CADA respuesta engancha un poco más. Nada técnico (watts/lúmenes) salvo que pregunten.
- El gatito de `tienda-PRO.html` llama a ese cerebro (fetch localhost) con **respaldo scripted** si el servidor está apagado. Avatar `iconos/robotcat_web.png`.

## 🎓 EXPERTISE INVESTIGADA (2026) — manuales por disciplina

### 🎨 Gemini / "Nano Banana" (imágenes) — experto
- **Editar ≠ generar:** al editar una imagen ya buena, describir SOLO lo que CAMBIA y recalcar lo que se MANTIENE ("keep everything identical, only change X"). Máscara semántica por texto (inpainting) para tocar una zona sin alterar el resto.
- **Referencias (hasta ~14 imágenes):** para meter NUESTRO foco/gato EXACTO en escenas nuevas (consistencia del producto). Ya lo hacemos con `foco-cut.png` / `foco-flip.png`.
- **Edición ITERATIVA por pasos:** un cambio a la vez ("reduce specular highlights; add soft diffusion"), no amontonar instrucciones. Si el foco se lava/quema → un ajuste puntual, no rehacer.
- **Estilo por descripción** (no marcas): "en el estilo de cartel vintage — textura de papel, tintas apagadas, geometría simple".
- Prototipar prompts en **Google AI Studio**. Existe **Nano Banana 2 Lite** (más calidad/rápida/barata) → evaluar migrar el pipeline.

### ✂️ Edición cinematográfica (montaje del comercial) — experto
- **Color grade = el "vibe"** y DEBE alinear con la marca (BUUM: luz BLANCA protagonista, negros limpios, naranja/azul de acento). Grade comercial = bonito **+ estratégico** (refuerza el mensaje), no solo estético.
- **Beat-cut:** cortar al RITMO de la música; la música dicta la velocidad. BUUM = ritmo elegante que SUBE con el encendido.
- **Montaje** = serie de tomas que condensan tiempo/emoción bajo una música unificadora.
- **Audio en capas:** música + SFX (clic al encender, "whoosh" de luz) + ambiente sutil = "suena tan bien como se ve". Sube producción muchísimo.
- Recursos: slow-mo / time-lapse para impacto puntual.

### 📣 Meta Ads / pauta (cuando invierta) — experto
- **El CREATIVO es el factor #1 en 2026** (el targeting ya es automático) → gana quien tiene mejor creativo, no quien segmenta más.
- **Gancho en los primeros 2–3 SEGUNDOS** (video) o la 1ª línea (solo ~125 caracteres antes de "ver más"). Frenar el scroll con movimiento/claim/pregunta.
- **Liderar con BENEFICIO, no característica.** Narrativa problema→solución. **CTA específico.**
- **Formatos:** imágenes estáticas = **60-70% de las conversiones** (¡nuestras imágenes sí sirven!). **Reels = CPM 20-35% más barato + 2-3x engagement.** **Subtítulos SIEMPRE** (85% ven sin sonido).
- **Volumen:** 3-5 conceptos por campaña, 5-10 variaciones activas, refrescar cada 3-6 semanas (evitar fatiga) → por eso producimos muchos ÁNGULOS/estilos (regar la info). Prueba social (reseñas/UGC) para confianza.

## 5) Visión / rutinas futuras (a construir)
El dueño quiere un sistema que cree y publique contenido a diario SIN autorizar cada pieza (todo debe salir bien por defecto). Dos rutinas pedidas:
1. **Rutina diaria de video** que genera un comercial y lo deja para revisión (sin publicar) → aprende con el feedback diario.
2. **Igual para imagen** (historias, carruseles, imágenes).
Luego: sistema de auto-publicación con calendario de redes. Implementar con tareas programadas. Cada pieza pasa por las Reglas de contenido (sección 0) antes de publicar.

## 📅 ESTRATEGIA DE CONTENIDO — CALENDARIO ADELANTADO + PULIR HASTA 9+ (feedback dueño 2026-07-11)
- **El Encargado PLANEA la estrategia** del calendario (no el dueño): temas, secuencia y COHERENCIA, como una marca real (Cinépolis, Liverpool, Costco, Lemme, MAKÉ). El dueño solo audita/autoriza.
- **Trabajar ~1 SEMANA ADELANTADOS:** cada día se produce contenido de más adelante (no el mismo día que se publica), para tener margen de PULIR y revisar. Beneficio extra: hacer poquitas piezas al día evita topar la cuota de Gemini.
- **Solo se publica calificación 9+** (que pase los 3 filtros IA). Pipeline de mejora por puntaje:
  - **<7 (5-6):** rehacer/mejorar; si batalla mucho y NO tiene potencial → DESCARTAR.
  - **7–8.9:** el auditor detecta POR QUÉ no llegó a 9 (texto, luz, composición, marca) y ARREGLA ese detalle para subirlo. "Ya falta poquito" → se arregla, no se tira.
  - **9+:** pasa a autorización del dueño.
- El calendario del OS refleja puntaje + estado (por mejorar / listo / autorizado). Nada <9 se publica.

## 🎨 IDENTIDAD DE MARCA / "LA VIBRA BUUM" (feedback dueño 2026-07-11) — a construir
- Meta: que TODAS las publicaciones se sientan "de BUUM" a primera vista, con secuencia e identidad — como **Lemme** (lila retro, "player cards", tipografía bold consistente, misma paleta) o **MAKÉ** (burdeos/vino, monograma serif elegante, minimal). El dueño mostró esas cuentas como referencia de coherencia.
- Definir el **sistema visual social de BUUM**: paleta (naranja #EA5003 + azul #102AC4 + blanco brillante), mascota Kitsune, tipografía, **plantillas/formatos recurrentes**, tono de voz. Objetivo: coherencia de marca, no piezas sueltas. Es como "contratar a un/a diseñador/a fijo/a" que le da la misma vibra a todo.

## 🎥 PUBLICIDAD NIVEL MUNDIAL — subir del 50% al 100% (feedback dueño 2026-07-11)
El dueño calificó nuestra publicidad en **~50%**: bonita pero **"austera"** vs. las mejores marcas. Referencias que mostró: **EcoFlow, Chevrolet México, Mercado Libre MX, Ferja.mx**. Qué hacen ellos que nos falta:
- **Fotografía REAL / cinematográfica** (no "póster con foco + texto"): producto en la vida real, luz y profundidad de cine.
- **Lifestyle / producto EN USO** en lugares hermosos y reales (EcoFlow acampando; el foco iluminando una sala/negocio real).
- **Personas / creadores (UGC) + cultura** (Ferja con creadoras; ML con el Mundial y memes).
- **UN concepto ingenioso por post** ("NO POWER. NO CHILL.", "HAZ ZOOM PARA VER…") — una IDEA, no solo producto+titular.
- **Macro cinematográfico** dramático (Chevy: close-up del faro) = belleza de producto premium.
- **Mucho video/Reels** y **branding MÍNIMO** (que la imagen respire; poco texto, elegante).

**ESTÁNDAR NUEVO (obligatorio):** cada anuncio debe pasar *"¿lo publicaría EcoFlow/Chevrolet?"* — no solo *"¿está bonito?"*. Menos texto, más imagen; grade cinematográfico SIEMPRE (contraste, **bloom** en la luz, viñeta, **grano**); un concepto claro; luz BLANCA; vibra BUUM (naranja domina, logo esquina) — ver `buumia-os/IDENTIDAD-SOCIAL.md`.
**Técnica:** escena REAL con Gemini **i2i** (foco real dentro de entorno real, profundidad, bloom) → **branding mínimo** en PIL (kicker chico + acento naranja + logo) → **re-grade cine** (PIL/ffmpeg: contraste+bloom+viñeta+grano). Herramientas: `marketing/gen_adpro.py` (escena i2i cine) + tratamiento PIL (demo `marketing/contenido/pro/antes_despues.png`).
**🟢 MÉTODO CINE + RESPALDO = REPLICATE flux-kontext (probado 2026-07-11, DESBLOQUEA todo):** cuando Gemini topa cuota (o para calidad cine directa), usar **Replicate `black-forest-labs/flux-kontext-pro`** (image-to-image que MANTIENE el foco exacto). Se pasa el foco real como `input_image` (data URI) + prompt de cine (escena REAL + luz BLANCA + profundidad/bloom/grano). Resultado nivel EcoFlow, con NUESTRO producto idéntico. Token `REPLICATE_API_TOKEN` ya conectado (pago por uso, sin límite diario apretado). Script: `marketing/gen_replicate_test.py`; ejemplo `marketing/contenido/pro/rep_casa_ad.png`. Patrón Replicate: header `User-Agent: curl/8.4.0`, POST `/v1/models/{MODEL}/predictions`, poll hasta `succeeded`. **Con esto se produce al 90%+ sin depender del gratis de Gemini.** (Ojo: cuidar que el glow no salga cálido — reforzar "pure cool white daylight".)
**Aprendizajes de la 1ª tanda cine (2026-07-11):** (a) **VARIAR la estructura por pieza** (feedback dueño: "todos son foto de fondo + texto en el mismo lugar = aburrido"). Rotar: macro sin texto · lifestyle texto-arriba · negocio texto-abajo · texto a la derecha · sin texto (imagen habla). Herramienta `marketing/gen_tanda_cine.py` (4 layouts distintos). ✅ macro_ad (9.0) y recamara_ad (8.7) al calendario. (b) **Evitar letreros/neón con texto** en la escena → Flux escribe BASURA ("tauchresc") — o pedir "no signage/text" o recortarlo (error negocio_ad). (c) **Glow cálido** persiste en escenas de atardecer → forzar "cool white" más fuerte o regenerar (terraza_ad). (d) El foco sale **FLOTANDO** (hero) en las lifestyle → variar poniéndolo también en roseta/lámpara real de vez en cuando. El crítico lo hizo Claude (visión) porque Gemini-crítico topó cuota; cuando se libere, correr `filtros_calidad.py` igual.
**CATÁLOGO DE TIPOS DE ANUNCIO — ROTAR para variedad estilo Coca-Cola (1 producto = contenido infinito):** lifestyle en cuarto · macro beauty · **flat-lay top-down** · **bloque de color + tipografía gigante** · con **persona/mano** · negocio en uso · producto en la calle/cultura · dato/educativo · antes-después · UGC · tipográfico "gigante". El Encargado ROTA el TIPO (no solo el texto/su posición) y mantiene coherencia (vibra BUUM, naranja domina). Scripts: `gen_tanda_cine.py` (lifestyle/macro/negocio/terraza) + `gen_tanda2.py` (flatlay/colorblock/mano). Aprobados 9.0: cine casa/recamara, macro, **flatlay, colorblock**. Pendiente pulir: mano (fondo cálido), negocio (letrero basura), terraza (glow cálido). BOTONES nuevos en el calendario del OS: **Eliminar** (oculta la pieza) y **✨ Generar mejor** (pide regenerar a 9+).

**6 CONCEPTOS listos para producir (ya se puede vía Replicate):** (1) **"En casa"** lifestyle — el foco transforma una sala real al atardecer; (2) **Macro cine** — corona facetada con rim light → "Calidad que se ve"; (3) **Concepto ingenioso** — one-liner visual ("Apaga el gasto, no la luz" / antes-después con swipe); (4) **Humano/UGC** — persona real o Sofía mostrando el foco, cercano, cultura MX; (5) **Negocio real** — el foco iluminando un puesto/tienda de noche, vendedor contento; (6) **Cultural/temporal** — enganchar con la temporada (tipo ML con el Mundial).

## 🔮 DEPARTAMENTO DEL FUTURO (nuevo, feedback dueño 2026-07-11) — a crear
- Rol: **investigar herramientas/tendencias nuevas** (Claude, otras IA, cursos, novedades) que sirvan a la empresa y decirnos cómo adoptarlas — mantenernos actualizados y "abriendo camino", como las empresas que adoptan la nueva tecnología para seguir vigentes y bien administradas.

## 🧠 MEMORIA DE GUSTOS DEL DUEÑO (viva, 2026-07-13) — sesgar hacia lo que GUSTA, evitar lo que NO, sin repetir
**LE GUSTA (hacer MÁS, variando):** estilo **flat-lay top-down** (fondo naranja + plantita + bloques geométricos azules); **bloque de color + tipografía gigante** (tipo Coca); **patrón de marca reconocible** (fondo NARANJA o AZUL = "es de BUUM") pero **cada pieza DISTINTA** (variar TIPO, no la misma foto con el texto movido); contenido de producto constante tipo **Coca-Cola / lheshmx / buytiti** (básico con IA pero coherente y con lógica). Historias diarias, carruseles con texto, reels.
**NO LE GUSTA:** ⚠️ **repetir la MISMA canción** en todos los videos (¡importante!); reels de "montaje" genérico sin gracia; doble confirmación al eliminar (quitada); logos mezclados con los anuncios (ya separados en sección "Logotipos").
**REGLAS NUEVAS:**
- 🎵 **MÚSICA ÚNICA por video** — biblioteca en `marketing/musica/*.mp3` (upbeat_pop · acustico · lofi_cool · cine_epico), generada con MusicGen (`gen_musica_lib.py`). ROTAR, nunca repetir. Generar más pistas cuando se necesiten.
- 🗑️ Borrado **instantáneo** (sin confirmar). **Memoria de gustos** en localStorage `buum_feedback` (cada Autorizar=`gusto`, cada Eliminar=`nogusto`, guarda el `estilo`/`tipo`) → leerla para dar más de lo que gusta y menos de lo que no, sin repetir.
- ❓ **Preguntar de vez en cuando** al dueño para afinar (él lo pidió).
**REFERENCIAS que mostró (nivel a alcanzar, venden producto con IA):** `lheshmx` (mayoreo/comerciantes; UGC en la tienda mostrando producto + texto cómic tipo "POW" amarillo/rojo → **TIPO NUEVO a probar: persona/UGC en tienda + texto cómic bold**), `buytiti_oficial`, EcoFlow, Chevrolet, Coca-Cola, Ferja, Mercado Libre.

## 🖼️ CARRUSELES y CONTEXTOS INFINITOS (feedback dueño + estudio 2026-07-13)
- **CARRUSEL = VIAJE, no álbum:** cada slide una IMAGEN DISTINTA del foco (contexto/ángulo diferente, tipo listing de **Amazon**), NUNCA la misma foto con otro texto (el dueño lo rechazó). Slide 1 = **gancho** (pesa ~80%, gana el swipe); slides de en medio = **producto EN USO / en contexto** (convierte **+28%** vs. producto solo); último slide = **precio + CTA**. Formato **4:5 (1080×1350)**. Herramienta `marketing/gen_carrusel_v2.py`.
- 🚫 **NO hacer "antes/después" con la MISMA imagen oscurecida/opaca** (no tiene sentido, el dueño lo detestó) → usar 2 fotos reales distintas, o mejor un **contexto real**.
- 🌍 **CONTEXTOS INFINITOS del foco = comerciales infinitos** (estilo Flow/Coca-Cola): sala, patio, fachada, interior/exterior, casa bonita/mediana/sencilla, bodega, con lluvia, con sol, atardecer, noche, patio grande, negocio, azotea… Con `flux-kontext` (mantiene el foco) + lista de contextos. Escenas en `marketing/contenido/contextos/`. Objetivo: variedad real, que NUNCA se sienta repetido. (Cuidar que el glow no salga cálido en escenas de atardecer/noche → reforzar "cool white".)
- Estudio aplicado (fuentes: TrueFuture, Metricool, Sprout Social 2026): carruseles = mayor engagement; producto-en-uso > producto-solo; slide 1 gana el swipe; CTA al final.

## 🔴🔴 REGLAS DURAS (el dueño las repitió MUCHAS veces, 2026-07-13)
1. **LUZ SIEMPRE BLANCA — nunca cálida.** El foco 60W es luz BLANCA; si sale cálida/ámbar el cliente se confunde = MAL. Toda escena de **noche/atardecer/interior** de flux-kontext tiende a salir CÁLIDA → **SIEMPRE aplicar corrección de balance de blancos** después: `coolwhite` (R×0.90, B×1.09, saturación×0.86) **+ gray-world** (`ImageStat.Stat().mean` → normalizar canales a neutro, strength ~0.75) sobre la ESCENA antes de componer. Además reforzar el prompt "pure cool white daylight, NOT warm/amber". Verificar SIEMPRE que la luz se lea blanca de un vistazo (entender en 1 segundo).
2. **VARIAR LA COMPOSICIÓN, no solo el fondo.** El dueño notó que todos los comerciales se ven IGUALES = "foco flotando en un lugar", solo cambia el fondo. → Variar el **CONCEPTO/ángulo/composición**, no el escenario: macro/close-up de la corona o la rosca, foco **en mano**, flat-lay distinto, foco **en uso real** (en lámpara/roseta/poste), acción, split, tipográfico gigante, con **persona**, cenital, contrapicado, detalle, etc. Que NUNCA se sienta el mismo comercial. (1 producto = mil composiciones distintas, como Coca-Cola.)
3. **Lightbox** en el OS: clic en imagen del calendario/galería → se ve en GRANDE (`#lightbox`).

## 🏭 GENERADORES DE IMAGEN — usar el MEJOR por trabajo (2026-07-13)
- **PIL (diseño gráfico)** → fichas técnicas/specs, precios, memes con texto, layouts. El texto sale PERFECTO (la IA lo garabatea). Ej. `marketing/contenido/ficha_specs.png` (estilo SUBURBANA/Amazon, colores BUUM navy+naranja). **Preferir PIL para todo lo tipográfico/spec.**
- **Flux-kontext (Replicate)** → foto REALISTA del foco en escena (mantiene el foco exacto). + corrección gray-world (luz blanca).
- **OpenAI `gpt-image-1` (ChatGPT)** → EXCELENTE para anuncios con texto/diseño y seguir instrucciones (supera a Flux/Gemini en eso, feedback dueño). **A conectar cuando el dueño active `OPENAI_API_KEY`** (platform.openai.com, billing + api-keys; ~$0.02-0.04/img). Yo cableo la Images API. Usar para escenas creativas donde brille.
- **Gemini** → bueno pero topa cuota gratis.
> Estrategia: NO depender de una sola fábrica; combinar (como KFC combina estilos).

## 🍗 REFERENCIA KFC MÉXICO (nivel a alcanzar, feedback dueño 2026-07-13)
Muchos ESTILOS distintos (memes, "player cards"/mega combo, tipográficos audaces "¿Y si síuuu?", tributos, foto de producto, celebridad Roberto Carlos, spec/precio) pero TODO se siente KFC (rojo, tipografía, tono divertido mexicano). → BUUM debe tener esa **variedad de estilos con coherencia**: ficha técnica, meme, tipográfico, macro, lifestyle, mascota, celebridad/UGC, tributo. (El fondo negro de sus capturas = modo oscuro del dueño, NO la marca.)

## 🧩 EL FEED COMO ROMPECABEZAS — variedad de estilos con COHERENCIA (feedback dueño 2026-07-13)
Referencias del dueño: **KFC México, Farmacias Dr. Simi (`fsimilares`), Miniso**. Cada post es de un ESTILO distinto (meme, tipográfico, mascota, celebridad, spec, foto) pero TODO encaja como un rompecabezas = se reconoce la marca. Alguien "controla el contenido" → ese es el **Encargado de marketing** de BUUM. **Ventaja BUUM: el gatito Kitsune = nuestro "Dr. Simi"** (mascota que da personalidad; usarla seguido). Meta del dueño: **contenido GENIAL de verdad** (no genérico ni "por cumplir") que **enamore a México** y ponga "de moda" comprar focos/lo que vendamos.
**TANDA de estilos hecha (`marketing/gen_kfc_batch.py` → `contenido/kfc/`):** mascota (gato endosa) · meme ("POV: pusiste focos BUUM…") · tipográfico audaz ("¿Y SI ILUMINAS TODO?") · celebridad (Sofía recomienda). Todo PIL, coherente. **Catálogo de estilos a ROTAR:** ficha técnica/spec · meme · tipográfico audaz · mascota (gato) · celebridad/UGC (Sofía) · macro · lifestyle/contexto · flat-lay · bloque de color · tributo · cultural/temporal. El nivel debe SUBIR siempre (calidad KFC), nunca conformarse.

## 🎨 NIVEL MINISO / POP MART — escenas 3D GENERADAS, no montajes (feedback dueño 2026-07-13)
El dueño RECHAZÓ los "montajes" (fondo + foco recortado + texto PIL): "está bonito pero nada que ver con MINISO". MINISO/Pop Mart = **escenas 3D COMPLETAS renderizadas** (el personaje/producto ES la escena: set-piece adorable, props, luz de estudio, profundidad, CGI premium). → BUUM debe **GENERAR la escena entera** (no componer). **Ventaja: el gatito Kitsune** como figura coleccionable (como MINISO con Sanrio/One Piece). **PROBADO y FUNCIONA:** flux-kontext con el **gato (`gatitos/g1.png`) como `input_image`** + prompt "adorable 3D collectible-figure scene, MINISO/Pop Mart style, cozy miniature set with props, studio lighting, shallow DoF, premium CGI" → escena real nivel MINISO (`marketing/contenido/miniso/cat_scene.png`). PENDIENTE: forzar **luz BLANCA** (salió cálida) y meter el **foco EXACTO** para anuncios de producto. **gpt-image-1 (ChatGPT) sería aún mejor** para esto → conectar `OPENAI_API_KEY`. Los montajes PIL quedan para specs/memes/tipográficos; para "hero"/marca → escenas 3D generadas.
**✅ CONFIRMADO por el dueño (2026-07-13): ChatGPT `gpt-image-1` es EL MEJOR para este estilo.** Le pidió "imagen publicitaria del foco" y sacó una **escena 3D rosa pastel MINISO** con: el foco integrado (facetas incluidas) sobre podio/nube, props temáticos (casita, lamparita, plantita), **íconos de features** (luz blanca 6500K · alta iluminación · larga duración · bajo consumo), **badges de precio** ($ x pieza / x caja) + **caja de producto** renderizada + branding — TODO en una sola imagen. Esa es la FÓRMULA a replicar. → **Prioridad: conectar `OPENAI_API_KEY`** para automatizarlo; mientras, el dueño puede generarlas en la app de ChatGPT y yo las IMPORTO al OS/calendario.
**✅✅ CONECTADO Y FUNCIONANDO (2026-07-13). MÉTODO GANADOR MINISO:** `OPENAI_API_KEY` ya está en `aurora-cafe/claves.local.txt`. Scripts: `marketing/gen_openai.py` (text-to-image) y **`gen_openai_edit.py` (EL BUENO): endpoint `/v1/images/edits` de `gpt-image-1` con `productos-fotos/foco-cut.png` como `image` de referencia → escena MINISO 3D pastel CONSERVANDO NUESTRO FOCO EXACTO** (corona ribeteada + facetas + E27). Luego **PIL** agrega branding + specs + precio en el espacio limpio de la izquierda. Resultado = anuncio nivel MINISO idéntico a la referencia del dueño, con nuestro producto, automático (`contenido/openai/minso_ad.png`). **🔑 CORRECCIÓN CLAVE (2026-07-13): generar el ANUNCIO COMPLETO en UN SOLO SHOT, no partirlo.** El error fue pedir solo la ESCENA a gpt-image-1 y pegar el texto con PIL → se veía "fondo con texto encima" (plano, pegado), el dueño lo rechazó. **LO CORRECTO:** en el prompt de `gen_openai_edit.py` describir el **anuncio ENTERO con TODO el texto integrado** (título 'ILUMINA TU MUNDO', subtítulo, 4 features con íconos, badge de precio 'CAJA DE 12 $75 c/u') → gpt-image-1 lo renderiza TODO junto, cohesivo, con la ortografía en español correcta. Resultado = nivel MINISO real (`contenido/openai/minso_full.png`). **Único PIL:** agregar el LOGO real de BUUM (gato Kitsune) en una esquina, porque es lo único que la IA no dibuja exacto (`minso_final.png`). Costo ~$0.02-0.08/img. size 1024x1536, quality high. Para variar: cambiar tema/props/paleta/copys en el prompt (SIEMPRE luz BLANCA 6500K, precio real $75/caja $899). **ESTE es el pipeline estrella: gpt-image-1 edits (anuncio completo integrado + foco) → PIL solo el logo.**

## 🧠 ACLARACIÓN CLAVE (2026-07-13): ChatGPT = `gpt-image-1` = la MISMA API que ya tenemos
El dueño notó que cuando él genera MANUAL en chatgpt.com le salen PERFECTAS y por API batallábamos. **La verdad: el generador de imágenes de ChatGPT ES `gpt-image-1`, exactamente el mismo motor de nuestra API.** No es otro programa mejor; ya estamos "conectados a ChatGPT". La diferencia NO era el motor sino el **MÉTODO**:
- Él **SUBE la imagen de referencia** y dice "hazla con focos" → ChatGPT hace **image-to-image (edita la foto real)** y clava la composición pro. Yo antes **describía** la escena con texto o pegaba el foco con PIL (por eso se veía "pegado"/flotando).
- ChatGPT además **auto-mejora el prompt** por detrás y es **multi-turno** (tú corriges y refina).
**→ SOLUCIÓN/MÉTODO GANANDO: pasarle la imagen de referencia DIRECTA al endpoint `/v1/images/edits`** junto con `foco-cut.png`+`foco-flip.png` (igual que arrastrarla en ChatGPT). Reproduce la composición idéntica con NUESTRO foco.
**Formas de "conectar ChatGPT" (para el dueño):** (A) **API OpenAI usada bien = image-to-image** ← la que usamos, automatizable, recomendada. (B) robot que teclee en chatgpt.com = contra ToS, frágil, riesgo de ban ❌. (C) **híbrido**: el dueño genera los "hero" en ChatGPT (le salen perfectos) y yo hago TODO lo demás (marca, variaciones, tamaños IG/FB, textos, calendario, video, publicar). **Recomendado: A+C.**
**🔧 PIPELINE REUTILIZABLE:** `marketing/gen_from_ref.py` — toma la imagen más reciente de **`marketing/referencias/`** (el dueño suelta ahí lo que le gusta) + nuestros focos, hace image-to-image, **quita cualquier marca ajena** (MINISO/One Piece/Toei/props licenciados/logos/contadores) dejándolo 100% BUUM (foco real, luz blanca, esquina sup-izq libre) y pega el logo BUUM real. Salida `contenido/openai/ref_<nombre>.png`. Uso: `python gen_from_ref.py [referencias/archivo.png]`.
> ⚠️ IP: al recrear una referencia de otra marca, SIEMPRE eliminar sus logos, personajes y props licenciados; solo se reutiliza el ESTILO genérico (cubos/cielo/luz de estudio). Nunca reproducir marca/personaje ajeno.

### ✅ DECISIÓN DEL DUEÑO (2026-07-13): flujo de imágenes = **AUTOMÁTICO POR API**
El dueño eligió que el departamento genere TODO solo con el API (no híbrido). Reglas fijas:
- **Motor:** `gpt-image-1` vía `/v1/images/edits` (mismo que ChatGPT). **SIEMPRE usar `input_fidelity: "high"`** en el body — fue el ajuste que faltaba y subió muchísimo la calidad (respeta mejor foco+composición). `quality:"high"`, `size:"1024x1536"`.
- **Referencias del foco:** pasar `foco-cut.png` + `foco-flip.png` como `image[]` para que el foco salga real (no emoji).
- **Clon 1:1 de una imagen que le guste:** el dueño la guarda en `marketing/referencias/` y corro `gen_from_ref.py` (le mete los píxeles reales). Si no hay archivo, la recreo por DESCRIPCIÓN detallada (queda muy bien igual, ej. `ejercicio4b.png`).
- **Best-of-N + pulido PIL:** generar ≥2 variantes y quedarme con la mejor; PIL agrega logo BUUM real + marco de tarjeta (esquinas redondeadas) cuando aplique.
- Script de referencia con todo esto: `marketing/gen_ejercicio4b.py`. **Actualizar los generadores viejos para que TODOS lleven `input_fidelity:"high"`.**

## 🔒 REGLA: PREVIEW ANTES DE PUBLICAR (siempre) — y NADA se publica sin OK del dueño. Todo el trabajo actual es preview/prueba en el OS, sin publicar en redes.

> Mantener esta bitácora VIVA: tras cada video/feedback, anotar aquí lo nuevo bueno y malo.
