---
name: departamento-contenido
description: Dirige las redes sociales de BUUM. Diseña el calendario de contenido (qué se publica, cuándo y a qué hora), define la mezcla de piezas, genera los prompts para que el Fundador cree el contenido, y organiza todo para publicación. Fase actual - crecimiento orgánico con memes/humor mexicano (no venta).
---

# Departamento de Contenido BUUM (crecimiento orgánico)

Meta de esta fase: **crecer seguidores y engagement REAL** (likes, compartidas,
alcance) en Facebook e Instagram con contenido viral — memes y humor mexicano
"raro" con el gato Kitsune. **Todavía NO se vende**; el producto aparece de fondo,
nunca como venta dura. Decisión del Fundador 2026-08-18.

## Principios de lo viral (escuela BUUM + redes 2026)
- **Gancho en 1 segundo**, funciona SIN sonido, relatable (que el mexicano diga "soy yo").
- Humor por encima de producto: la gente comparte lo que le da risa, no un anuncio.
- **El gato Kitsune con personalidad** (primera persona, tono juguetón tipo mascota famosa).
- Rotar formatos: MEME imagen · HISTORIA con encuesta/sticker · CARRUSEL mini-cómic ·
  REEL de recortes · DATO curioso gracioso · pregunta a la comunidad.
- Firma BUUM siempre presente (paleta naranja/azul + mascota) aunque el chiste mande.
- Prohibido: promesas falsas, "oferta/barato", foco de filamento, luz cálida en el producto.

## Cómo se dirige (el ciclo)
1. **Planear la semana:** con los datos reales (snapshot Meta: seguidores/alcance) +
   el calendario anterior, proponer el calendario de 7 días: para cada día un
   concepto + formato + hora de publicación + gancho + por qué crecería.
2. **Prompts:** por cada pieza, entregar al Fundador el prompt listo (con referencia
   si aplica) para que la genere en ChatGPT. Regla del proceso: Claude dirige, el
   Fundador genera, Claude organiza y publica.
3. **Aprobar:** el Fundador aprueba cada pieza generada (juez final).
4. **Calendario:** las piezas aprobadas entran a `marketing/calendario-contenido.json`
   con su fecha/hora exacta y estado `aprobado`.
5. **Publicar:** el publicador (cron en el servidor, `scripts/publicador/`) publica
   SOLO las piezas `aprobado` a su hora, en FB+IG, y las marca `publicado`.
6. **Medir y aprender:** al cierre de semana, leer alcance/likes de cada pieza
   (snapshot Meta) → mini-reporte: qué formato/gancho jaló → ajustar la mezcla.
   Aprendizajes maduros → skill `registro-aprendizaje`.

## Horas recomendadas (público mexicano, ajustables)
Pico de engagement: **~14:00 y ~20:30-21:30** hora del centro. En fase diaria:
1 pieza/día a las 20:30 (hora de mayor scroll). Historias pueden ir a media tarde.

## Reglas duras
- Solo entran al calendario piezas APROBADAS por el Fundador. El publicador jamás
  publica algo sin `estado: aprobado` y sin fecha/hora.
- Toda pieza pasa por jueces en modo SOCIAL (enganche, no venta) antes de aprobarse.
- Máximo 1 pieza de venta dura por semana durante esta fase (o cero); el resto es
  puro engagement. Cuando el Fundador diga "a vender", cambia la mezcla.
- Aplica Quality Gates a los datos que uses para decidir (alcance, crecimiento).
