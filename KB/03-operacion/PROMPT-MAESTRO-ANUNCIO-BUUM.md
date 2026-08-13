# Motor Creativo Dinámico + ADN de calidad (NO plantillas)

> **Corrección de arquitectura (Fundador, 2026-07-17):** el Departamento de Marketing debe funcionar **igual que ChatGPT**: el Fundador da un **brief CORTO** ("foco 60W estilo Toy Story", "gatito con playera naranja y lentes rojos", "ponle sombrero de navidad") y **BUUM (el cerebro/LLM) EXPANDE ese brief en un prompt detallado AL VUELO** y lo manda a gpt-image-1. **NO hay prompts enlatados por imagen** (eso no escala). Este documento NO es una plantilla fija: es el **ADN de calidad** (reglas + estándar) que BUUM aplica dinámicamente a CUALQUIER pedido, más un ejemplo trabajado.

## Cómo funciona (el ciclo, como ChatGPT)
1. Fundador: brief corto en el chat.
2. **BUUM expande** → prompt premium detallado (escena + estilo + composición) aplicando SIEMPRE el ADN de abajo.
3. gpt-image-1 genera (referencias: foco real + logo). `moderation:low`.
4. BUUM **compara contra el checklist**, valida (candado: honestidad + luz blanca) y, si no llega, **reescribe el prompt y reintenta** (no se conforma con "medio").
5. Si el foco no queda 1:1 → incrusta la foto real encima.

## ADN de calidad (reglas que SIEMPRE se aplican, sea el tema que sea)
- Foco real de referencia (cúpula esmerilada + cuerpo facetado + E27); nunca genérico redondo.
- **Luz del foco BLANCA** (regla dura), salvo que el Fundador pida ambiente cálido de escena.
- Logo BUUM cuando sea anuncio; texto siempre bien escrito.
- Nivel premium (nítido, iluminación de cine, colores ricos; NO pastel lavado ni "medio").
- Sin Disney/Pixar/Miniso (inspiración de estilo, marca propia).

---

## Ejemplo trabajado #1 — estándar "felt/kawaii pop" (anuncio "que ilumina tu mundo")

> Aprobado por el Fundador 2026-07-17. Objetivo: igualar ESE nivel (vibrante, con insignias, texto limpio, foco real).

## Generador y ajustes técnicos
- **Motor:** `gpt-image-1` (motor premium de ChatGPT) vía `POST /v1/images/edits`.
- **Referencias (`image[]`):** (1) foto del **foco real** (`04-negocio/productos/fotos/60w-1-clean.png`), (2) **logo BUUM** (crop).
- **Parámetros:** `size:1024x1536`, `quality:high`, `moderation:"low"` (obligatorio: sin `low` el filtro de salida bloquea estilos con personaje/marca).
- **Costo:** ≈ **$0.26 USD/imagen**.
- **Script de referencia:** `buumia-tienda/marketing/gen_openai_yoyo2.py`.

## Regla de oro
El generador **recrea** el producto (no lo fotocopia). Si el foco no queda 1:1, **incrustar la foto real encima** (composite). Fórmula: **gpt-image-1 (escena) + foto real (producto) = anuncio PRO con el foco de verdad.**

## Checklist del ESTÁNDAR visual (comparar SIEMPRE contra esto)
- [ ] Azul **vibrante y saturado** (NO pastel lavado).
- [ ] Nubes de **pompón de fieltro 3D** nítidas.
- [ ] Logo **BUUM** (rojo + rayo) arriba-izquierda.
- [ ] Título doodle grande **"BUUM"** + tagline **"que ilumina tu mundo"**.
- [ ] Insignia marquesina **"FOCO DE 60 WATTS"** (roja con foquitos dorados).
- [ ] Pill **"LUZ BLANCA"** con icono de foco.
- [ ] Insignia **"CAJA CON 30 PIEZAS"**.
- [ ] Fila de 4 iconos: **LUZ BLANCA · AHORRA ENERGÍA · LARGA DURACIÓN · ALTA CALIDAD**.
- [ ] **Foco real** (cúpula esmerilada + cuerpo facetado + rosca E27) flotando con aro amarillo sobre globo de fieltro.
- [ ] Globos de pompón (verde/morado), estrellas y garabatos.
- [ ] **Luz BLANCA** (regla dura). Todo el texto **bien escrito**.
- [ ] Sin Disney/Pixar/Miniso/YOYO (todo lo nuestro).

## El PROMPT (copiar/pegar; en inglés porque el modelo responde mejor)
```
Vibrant, high-end kawaii advertising poster in a soft needle-felted plush craft 3D style, portrait, bright and punchy, professional key visual, sharp and colorful (NOT washed-out, NOT dull pastel).
BACKGROUND: a bright saturated sky-blue gradient. Fluffy 3D white pom-pom felt clouds. Playful childlike blue and yellow hand-drawn doodles (spirals, stars, tiny circles, a small lightning squiggle). Soft felt pom-pom balloons: a green one on the left and a purple one on the right.
HERO PRODUCT: use the bulb in the FIRST reference image as the EXACT real product - a high-power LED bulb with a smooth frosted prismatic dome top and a faceted diamond-cut matte white body tapering to a silver E27 screw base. Show it as the BIG floating centerpiece in the middle, with a hand-drawn yellow doodle ring/circle glowing behind it, hovering just above a cute green-and-blue felt planet globe at the bottom. Clean pure WHITE light. Keep the bulb shape exactly like the reference, do NOT make it a plain round bulb.
BRANDING & BADGES (render all text crisp, bold and correctly spelled in Spanish):
- Top-left corner: the red 'BUUM' logo badge from the SECOND reference image (bold white BUUM + yellow lightning bolt).
- Big playful hand-drawn blue doodle title 'BUUM' in a fun sketchy outline style, with a small blue script tagline underneath: 'que ilumina tu mundo'.
- Top-right: a glowing red marquee sign badge with a gold light-bulb border reading 'FOCO DE 60 WATTS' (the 60 large in yellow).
- A small blue rounded pill with a bulb icon reading 'LUZ BLANCA'.
- Bottom-right: a blue rounded badge reading 'CAJA CON 30 PIEZAS' (30 large in yellow).
- Bottom-left: four small round yellow-outline feature icons in a row with labels: 'LUZ BLANCA', 'AHORRA ENERGIA', 'LARGA DURACION', 'ALTA CALIDAD'.
Cheerful, premium, glossy soft studio lighting, rich saturated colors, high production value, adorable. Original design, no Disney, no Pixar, no movie branding.
```

## Cómo variar (mantener el estándar, cambiar el tema)
Cambiar SOLO el bloque BACKGROUND/tema y el título doodle; conservar logo, insignias, foco real y "luz blanca". Ver [[roles-creatividad-chatgpt]] y la Capa de Traducción Creativa.
