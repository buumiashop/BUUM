# 📐 ESPECIFICACIONES DE IMÁGENES PARA SHOPIFY
> Cómo deben salir TODAS las imágenes de producto de la tienda BUUM. Creado 2026-07-22.
> Complementa `PROCESO-IMAGENES-HIBRIDO.md`.

---

## 1. Ficha técnica (lo que no se negocia)

| Característica | Qué usar | Por qué |
|---|---|---|
| **Forma** | **Cuadrada 1:1** | Shopify recorta a cuadrado en las cuadrículas. Si una es cuadrada y otra no, la galería "brinca". |
| **Tamaño** | **2048 × 2048 px** | Es el que recomienda Shopify: permite hacer zoom sin que se pixelee. |
| **Mínimo aceptable** | 1600 × 1600 px | Por debajo de esto, al hacer zoom se ve borroso. |
| **Máximo** | 4472 × 4472 px · 20 MB | Límite de Shopify. Más grande no sirve de nada. |
| **Formato** | **JPG** (calidad 85–90) | Pesa 4 veces menos que PNG y se ve igual. Shopify lo convierte solo a WebP. |
| **PNG** | Solo si necesita fondo transparente | Si no, pesa de más y el celular tarda en cargar. |
| **Peso del archivo** | **Menos de 500 KB** (ideal 200–350 KB) | En celular con datos, una imagen pesada se ve en blanco varios segundos. |
| **Fondo** | **Blanco puro #FFFFFF** | Se funde con la página. Un blanco "casi blanco" se ve como un cuadro gris. |
| **Aire alrededor** | El producto ocupa **80–85 %** del cuadro | Si lo llenas al 100 % se ve apretado; si es muy chico, se pierde en el celular. |
| **Sombras** | **Sin sombras** | Decisión del Fundador: ensucian. |
| **Nitidez** | Enfocado, sin ruido | Se ve en el zoom. |

---

## 2. Las 10 imágenes que debe tener el producto (en este orden)

El orden importa: **la #1 es la que sale en los anuncios, en Facebook, en Google y en la cuadrícula de la tienda.**

| # | Imagen | Para qué sirve | Estado |
|---|---|---|---|
| **1** | **Kit completo armado** (reflector + panel + control) | La portada. Se ve todo lo que recibe por su dinero. | ✅ `armado.png` |
| **2** | **En una pared de noche, encendido** ⭐ | La que enamora. El cliente se lo imagina en su casa. | 🟡 hecha con el método del rompecabezas |
| **3** | Reflector de frente | El producto solo, claro | ✅ `principal.png` |
| **4** | Reflector por detrás con su soporte | Muestra cómo se monta | ✅ `trasera.png` |
| **5** | **Medidas reales** | Quita la duda "¿de qué tamaño es?" | ✅ `tienda-medidas.png` |
| **6** | **Qué trae la caja** | Quita la duda "¿trae todo?" | ✅ `tienda-que-trae.png` |
| **7** | **Cómo se instala** | Quita el miedo "¿yo podré?" | ✅ `tienda-instalacion.png` |
| **8** | **El control explicado** | Muestra el valor extra | ✅ `tienda-control.png` |
| **9** | **Carga de día, alumbra de noche** | Explica lo solar | ✅ `tienda-autonomia.png` |
| **10** | **Aguanta la intemperie (IP66)** | Quita la duda "¿y si llueve?" | ✅ `tienda-intemperie.png` |

**Mínimo para vender:** 7 imágenes. **Óptimo:** 10. **Más de 12** ya cansa y hace lento el celular.

### Opcionales que suman
- Panel solar de frente y por detrás con el cable
- Control remoto solo
- Soporte y tornillos
- Vista 3/4 del reflector
- El producto en otros lugares: cochera, bodega, portón, rancho

---

## 3. Reglas para que se vea bien en el TELÉFONO
Casi nadie compra en computadora. Todo se decide en el celular.

- **Texto grande:** en un lienzo de 2048 px, mínimo **52 px**. Título ~100 px. Si no cabe grande, se quitan palabras — **nunca se achica la letra**.
- **Pocas palabras.** Una idea por imagen.
- **Contraste fuerte.** Azul marino o naranja sobre blanco. Nada de gris claro sobre blanco.
- **Nada importante en las orillas:** deja **8 % de margen** libre por si Shopify recorta.
- Prueba real: mira la imagen en tu propio celular a un brazo de distancia. Si tienes que acercarte, está mal.

---

## 4. Antes de subir cada imagen
- [ ] ¿Es cuadrada y del mismo tamaño que las demás?
- [ ] ¿Fondo blanco puro, sin manchas ni sombras?
- [ ] ¿El producto es **el nuestro**, sin deformar?
- [ ] ¿Los textos son ciertos? (nada inventado, nada que no esté en el Documento Maestro)
- [ ] ¿Acentos correctos? (año, día, batería, plástico)
- [ ] ¿Se lee bien en el celular?
- [ ] ¿Pesa menos de 500 KB?
- [ ] ¿Tiene **texto alternativo** escrito? (es lo que lee Google — suma para que te encuentren)

---

## 5. Texto alternativo (el que casi nadie pone y sí sirve)
Al subir cada imagen, Shopify pide un texto alternativo. Escribe lo que se ve, con las palabras que buscaría un cliente:

> ✅ "Reflector solar LED 50W con panel solar y control remoto, encendido en una pared de noche"
> ❌ "IMG_2043" · ❌ "reflector"

---

## 6. Nota sobre ChatGPT
ChatGPT entrega **1024 × 1024 px**. Está por debajo de lo recomendado.
👉 Genéralas ahí (salen fieles) y **pásamelas: yo las escalo a 2048 × 2048** con buen algoritmo y las convierto a JPG optimizado antes de subirlas.
