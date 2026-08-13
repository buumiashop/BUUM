# Capa de Traducción Creativa

> **Dueño:** CEO/BIS · **Función:** hacer al Departamento de Marketing **independiente del proveedor de IA**. BUUM recibe la **intención creativa** (la estrategia) y la **traduce automáticamente al protocolo óptimo del generador disponible**, preservando la idea. Cada modelo tiene su idioma, fortalezas y buenas prácticas; esta capa adapta la comunicación para sacar el mejor resultado de cada herramienta.

## Principio
La **intención creativa NO cambia**; lo que cambia es **cómo se le habla a cada generador**. Si un generador no está disponible (sin saldo, caído, caro), BUUM **rutea a la mejor alternativa disponible** y traduce el prompt a su idioma. El resultado busca la misma intención con la mejor calidad posible de esa herramienta.

## Entrada: la intención creativa (lo que ChatGPT/estrategia define)
- **Concepto/gancho** (la idea, ej. "el foco como héroe estilo Toy Story").
- **Sujeto** (el producto exacto: foco 60W real).
- **Estilo/mood** (claymation, cine, pop, minimal…).
- **Formato/canal** (reel 9:16, carrusel 4:5, historia, post).
- **Restricciones DURAS (nunca cambian, sea cual sea el generador):** luz del foco **blanca** (6500K); **sin precio/venta** si el producto no es vendible; ADN BUUM (logo contorno blanco, gato Kitsune, vibra); honestidad total.

## Catálogo de generadores (fortalezas + cómo se le habla + nivel de costo)
| Generador | Fortaleza | Cómo traducir el prompt | Nivel/costo |
|---|---|---|---|
| **gpt-image-1** (OpenAI / motor de ChatGPT) | Anuncios foto-reales premium, texto integrado, sigue instrucciones, image-to-image con referencia | Describir el ANUNCIO COMPLETO en un solo prompt (escena + texto integrado); pasar el foco real como referencia; `input_fidelity:high` | **Premium** (~17-25¢) |
| **ChatGPT app** (suscripción del Fundador) | Misma calidad que gpt-image-1, auto-mejora el prompt | El Fundador la dispara con la intención; BUUM importa y sigue el flujo | Premium (ya pagado) |
| **flux-kontext** (Replicate) | Mantiene el producto exacto en escenas realistas; barato; sin cuota diaria | input_image = foco real + prompt de escena real + "pure cool WHITE light"; un cambio por edición | **Barato-medio** (~2-6¢) |
| **Kling** (Replicate, video) | Animación desde start+end frames | image-to-video = SOLO movimiento + 1 movimiento de cámara + marcadores temporales | Medio (video) |
| **Gemini** (nano banana) | Rápido, edición iterativa | referencias + editar por pasos; débil para "anuncio premium" | Barato (con cuota) |
| **MusicGen** (Replicate) | Música instrumental | prompt de estilo (mexicano, sin voz) | Barato |

## Regla de ruteo (qué generador por pieza + según disponibilidad)
1. **Pieza premium / héroe** (la que sí vale la pena): `gpt-image-1`. **Si su API no está disponible** (hoy: tarjetas rechazadas) → **ChatGPT app** (el Fundador la dispara) o **flux-kontext** (Replicate) como mejor alternativa.
2. **Diario / genérico** (historias, "buenos días", posts simples, pruebas): **flux-kontext / Replicate** (barato). Gemini si tiene saldo.
3. **Video:** Kling (Replicate). **Música:** MusicGen (Replicate).
4. Siempre: BUUM valida con el candado (honestidad + calidad) antes de mostrar/publicar, sea cual sea el generador.

## Estado de disponibilidad (vivo)
- ✅ Replicate (flux/Kling/MusicGen) — funcionando.
- ⚠️ OpenAI `gpt-image-1` — sin saldo (tarjetas rechazadas). Premium se cubre por ChatGPT app o flux mientras.
- ⚠️ Gemini — sin saldo. Lo barato se cubre por flux/Replicate.
- ✅ ChatGPT app — disponible (suscripción del Fundador) para premium.

**Resultado:** aunque OpenAI y Gemini estén sin saldo, el marketing sigue operando (Replicate + ChatGPT app). La capa preserva la intención y usa la mejor herramienta disponible.
