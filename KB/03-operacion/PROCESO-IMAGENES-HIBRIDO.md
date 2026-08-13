# Proceso de Imágenes de Producto — HÍBRIDO (v2.0)
> v1.0 definida por el Fundador (2026-07-20). **v2.0 (2026-07-21): se añade el método del rompecabezas**, probado y aprobado.
> Razón del híbrido: la generación 100% automática **cambia físicamente el producto** → inaceptable.

---

## PARTE 1 — Fotos de catálogo (la materia prima)
1. **Fundador entrega:** todas las fotos del producto + info de la caja y el manual.
2. **BUUM clasifica y numera:** qué es producto, qué es documentación, qué se repite; los hechos van al Documento Maestro.
3. **BUUM define el set** de imágenes que necesita el producto (frente, trasera, accesorios, armado…).
4. **BUUM entrega prompt por prompt** para pegar en ChatGPT junto con la foto de referencia.
5. **Fundador genera** en ChatGPT (sale fiel y HD) y las devuelve.
6. **BUUM audita, nombra y acomoda** en la Biblioteca de Activos Visuales.

**Estándar:** fondo blanco puro · vista recta centrada · producto físicamente idéntico · sin texto ni marca inventados · HD.
⚠️ Los generadores tienden a **girar la foto 90°**. Si pasa, se corrige **rotando la imagen entera**, no la etiqueta.

---

## PARTE 2 — El método del rompecabezas 🧩 (para tienda y campaña)
> **Regla madre: el generador NUNCA toca el producto.**

Se probaron dos caminos con generador de pago (Flux, ~4 ¢ USD por imagen):

| Camino | Qué se pidió | Resultado |
|---|---|---|
| **A** | Que generara TODO, producto incluido | ❌ **Falló.** Inventó otro reflector (modelo distinto, con patas) y escribió medidas falsas: "32 m", "280 im". |
| **B** | Que generara **solo el escenario vacío** | ✅ **Funcionó.** Noche, pared, haz de luz — realista y bonito. |

Luego se pegó encima el reflector **real recortado** → resultado profesional **y** producto 100 % fiel.

> Idea original del Fundador: *"armamos todo el rompecabezas menos la pieza del reflector y la del panel; esas las ponemos nosotros a mano."*

### Los 3 pasos
1. **El generador hace el escenario** — noche, pared, patio, luz del ambiente. Se le pide explícitamente **sin producto, sin lámpara, sin objeto**.
2. **Nosotros pegamos la pieza real** — recortes con transparencia en `activos-visuales/R54W50/recortes/` (hechos con rembg).
3. **Se integra** — resplandor suave detrás y halo sobre los LEDs para que parezca encendido.

Scripts: `recortes.py` · `experimentos.py` (escenarios) · `montaje.py` (pegado).
⚠️ rembg falla con piezas **blancas sobre fondo blanco** (el soporte): ahí se recorta por umbral.

---

## Los dos tipos de imagen
| Tipo | Para qué | Cómo se hace | Costo |
|---|---|---|---|
| **Que explican** | Medidas, qué trae la caja, cómo se instala | Composición propia en Python, fondo blanco | Gratis |
| **Que enamoran** | El producto de noche, en una casa real | Escenario del generador + pieza real pegada | ~4 ¢ c/u |

---

## Reglas de estilo (aprobadas por el Fundador 2026-07-21)
- **Fondo blanco, limpio. SIN sombras** — la sombra ensucia.
- **Simetría estricta:** mismos tamaños, mismas alturas de texto, cotas en espejo.
- **Texto grande** — mínimo ~36 px en lienzo de 1400. Ver `05-aprendizaje/GUSTOS-DEL-FUNDADOR.md`.
- **Tipografía Segoe UI** (Black para títulos, Semibold para textos).
- Acentos y ortografía **siempre correctos** ("año", no "ano").
- Pensado **primero para el teléfono**: casi nadie compra en computadora.
- **Nunca deformar el producto ni inventar textos, medidas o etiquetas.**

---

## Futuro (automático)
Cuando los generadores dejen de alterar el producto, el paso 5 de la Parte 1 lo hará BUUM solo. La Parte 2 ya es automatizable hoy.
