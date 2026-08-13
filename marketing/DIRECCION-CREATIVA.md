# 🎬 DIRECCIÓN CREATIVA BUUM — La receta del WOW

> Por qué los anuncios de vitrina (Kling, Gemini, Flow) se ven extraordinarios y los de plantilla no.
> **No es el modelo — es la dirección.** Este es el cerebro que Marketing usa ANTES de generar.

## La verdad
Los ejemplos WOW usan los MISMOS modelos que nosotros. La diferencia está en 4 cosas:
1. **Una idea fuerte** (concepto/gancho), no "anuncio de producto".
2. **Prompt de director** (cámara, luz, encuadre, atmósfera, momento) — aquí vive el 90%.
3. **Volumen + curaduría** — el ejemplo perfecto es el mejor de ~20 intentos.
4. **Criterio duro** — nuestros 4 filtros (`filtros_calidad.py`).

## La receta del WOW (checklist de todo anuncio BUUM)
- [ ] **UNA idea** clara (transformación / seguridad / ahorro / deseo). No mezclar.
- [ ] **Un héroe**: el producto manda el cuadro, o el resultado que da (la luz).
- [ ] **Luz cinematográfica**: es iluminación → la LUZ es la protagonista (haz volumétrico, rim light, bloom elegante).
- [ ] **Momento**, no catálogo: algo pasando (la noche se ilumina, la entrada cobra vida).
- [ ] **~95% visual**, casi sin texto. Si hay texto: 3-4 palabras máximo, tipografía limpia.
- [ ] **Emoción**: orgullo de casa, seguridad, "vale la pena".
- [ ] **Acabado premium**: nítido, sin defectos de IA, color grade de cine, profundidad de campo.
- [ ] Colores de marca donde encaje (naranja #EA5003 / azul), nunca "barato/oferta".

## Fórmula de prompt de director (rellenar)
`[TIPO DE TOMA cinematográfica] de [PRODUCTO exacto de referencia], [ACCIÓN/momento], [LUZ: haz volumétrico / rim light / bloom], [AMBIENTE/escenario aspiracional], [ATMÓSFERA: neblina, partículas, color grade], [CALIDAD: ultra nítido, premium, award-winning, estilo Apple/Dyson/anuncio inmobiliario]. Cuadro 1:1. SIN texto, SIN logos, SIN personas.`

## Proceso (lo que hace Marketing)
1. Elige idea del brief (`ESTRATEGIA.md`).
2. Escribe 2-3 conceptos con la fórmula de director.
3. Genera **volumen** (5-8 variantes por concepto) con Gemini/Kling.
4. **Cura**: se queda con las 2 mejores.
5. Pasan por **los 4 filtros**. Solo lo que aprueba el "crítico mundial" llega al dueño.
6. Se agenda en la semana (`rutina_semanal.py`).

## ⚡ LECCIÓN CLAVE (probado con los 4 filtros, 2026-07-03)
Al aplicar el método, la calidad técnica saltó de 2-6/10 a **Director Creativo 9-10/10** (nivel mundial real). PERO el crítico mundial seguía rechazando con una razón nueva y precisa: *"render técnico correcto, pero sin **narrativa, emoción, concepto publicitario ni conexión de marca**."*
→ **Una imagen bella ≠ un anuncio.** El WOW que PASA necesita 3 capas, en orden:
1. **Base cinematográfica** (ya la dominamos: luz + producto héroe).
2. **CONCEPTO + EMOCIÓN**: una idea/frase con gancho ("La noche ya no manda"), no solo una foto bonita.
3. **MARCA BUUM**: logo + colores (naranja #EA5003 / azul) + tono "vale la pena", tipografía LIMPIA (nunca la de la IA).
Regla: el texto/logo se compone con control (PIL/diseño), NO se le pide a la IA (su tipografía se ve amateur → fue el defecto viejo).

## 💡 ESTUDIO DE LA LUZ (reflector/floodlight — cómo es en la realidad, 2026-07-03)
Feedback clave del dueño: un anuncio de iluminación vive de que la LUZ se vea REAL. Errores que hacen que se vea "linterna" o "gris con niebla":
- ❌ "haz volumétrico" / "beam" → crea un CONO directo tipo linterna. NO es así un reflector.
- ❌ "neblina atmosférica que hace visible el haz" → mete niebla/gris feo. QUITAR.
- ❌ escena demasiado oscura → parece apagado o sucio.
**Cómo ilumina un reflector LED (floodlight) DE VERDAD:**
- Es luz de **INUNDACIÓN AMPLIA**: como prender la luz de un cuarto oscuro → **baña toda el área** (piso, muebles, plantas, muros) de forma **pareja y clara**.
- Las superficies que alcanza se ven **BIEN ILUMINADAS, nítidas y brillantes** (blanco limpio), no en penumbra.
- **Caída natural**: más brillante cerca del reflector, más tenue en los bordes, pero **NUNCA negro total** (hay rebote/ambiente).
- **Aire limpio, SIN niebla**. Nada de haze gris.
- Detrás del reflector sí hay poca luz, pero la escena general se siente **encendida y acogedora**.
- Palabras que funcionan: "inunda de luz blanca amplia y pareja", "todo el patio bien iluminado y claro", "superficies nítidas y brillantes", "caída suave de luz", "aire limpio". Palabras a EVITAR: haz, beam, cono, niebla, neblina, haze, volumétrico.

## Referencias a estudiar (nivel objetivo)
Iluminación/hogar de nivel mundial: Apple (luz + producto), Dyson (producto héroe), Philips Hue / Govee (luz en ambiente), anuncios inmobiliarios de lujo (casa iluminada de noche), Nike (emoción + una idea).

Relacionado: `filtros_calidad.py`, `rutina_semanal.py`, `ESTRATEGIA.md`, `EQUIPO.md`.
