# 🧬 ADN BUUM — Constitución de la empresa (L0, inmutable)
> Capa 0 de la arquitectura. **Ningún departamento puede romper el ADN.** Toda acción se valida contra este archivo (guardrail) antes de ejecutarse o publicarse.
> Misión, visión, valores e identidad **solo los cambia el dueño** (recogidos de los docs canónicos; ver §Fuentes). Las reglas duras y estándares **pueden endurecerse pero nunca relajarse** sin aprobación.
> v1 · 2026-07-14 · mantenido por el CEO (Claude).

## Misión (recogida de los docs; sujeta a ratificación del dueño)
Llevar novedades útiles y de buena calidad al mercado mexicano a **súper calidad y súper precio**, importándolas y distribuyéndolas de forma directa (modelo tipo TikTok Shop), empezando por iluminación. **Meta: generar dinero real y escalar** de pyme a empresa de importación/distribución.

## Visión
Convertir a BUUM en una **empresa inteligente de importación y distribución** que crece por categorías y etapas hasta una bodega/operación que abastece a México (y luego más allá), y cuya operación **aprende y mejora sola cada semana**.

## Valores
- **Vale la pena** (no "barato"): calidad real a precio justo.
- **Honestidad**: nunca prometer lo que el producto no da (ej. luz blanca es blanca).
- **Excelencia**: rehacer hasta que quede bien; la calidad manda sobre la prisa.
- **Disciplina de flujo**: rotación y caja sanas antes que vanidad.
- **Aprendizaje**: cada error se documenta para no repetirlo.

## Identidad de marca
- **Nombre:** BUUM. **Mascota:** gato Kitsune (personalidad de la marca).
- **Colores:** naranja `#EA5003`, azul `#001866` (+ variantes del brand kit).
- **Logo de uso preferido:** apilado con contorno blanco (`logo-buum-blanco.png`) para que no se pierda en ningún fondo.
- **Tono:** cercano, mexicano, alegre y confiable. Enganchar en **1 segundo**, ~95% visual, brillante (es iluminación).
- **Eslogan:** "Súper calidad y súper precio".

## Estándar de calidad (todo lo que se muestra/publica)
Nivel campaña: que una marca seria lo aprobaría para redes/espectacular. Calidad > velocidad > ahorro (el ahorro aplica a APIs, nunca a recortar QA).

## 🔒 REGLAS DURAS (guardrail — código y personas las verifican)
```json
{
  "version": 1,
  "reglas": {
    "luz_blanca": "El foco SOLO existe en luz BLANCA 6500K. La luz emitida y el ambiente deben leerse blancos/neutros, nunca cálidos/amarillos.",
    "foco_real": "Usar la foto real del foco (ficha técnica). Un solo foco, físicamente posible, sin cable flotando, nunca al revés.",
    "sin_marcas_terceros": "Prohibido reproducir logos, personajes o marcas de terceros (MINISO, One Piece, Toy Story, etc.). Se permite ESTILO genérico, nunca su IP.",
    "precios_reales": {"pieza": 99, "cada_uno": 75, "caja_12": 899, "moneda": "MXN"},
    "canales": ["instagram:@buum.ia", "facebook:BUUM"],
    "preview_obligatorio": "Nada se publica sin preview + OK del dueño.",
    "ortografia": "Ortografía y acentos perfectos; auditor de textos antes de mostrar.",
    "marca_visible": "Logo BUUM correcto y visible (contorno blanco); colores y fuentes oficiales."
  },
  "errores_prohibidos": [
    "luz cálida/amarilla en el foco",
    "foco tipo emoji/caricatura en vez del real",
    "texto encimado con foco o logo",
    "precios inventados o distintos a los reales",
    "publicar sin OK del dueño",
    "reproducir marca/personaje de terceros"
  ],
  "requiere_aprobacion_dueno": ["dinero", "seguridad", "publicación", "datos_sensibles", "modificar_ADN"]
}
```

## Fuentes canónicas (no duplicar aquí; este ADN las unifica y apunta)
- Marca: `buumia-catalogo/marca/BRAND-KIT.md`, `MASCOTA-BUUM.md`, manual p1–p8.
- Estrategia/valores: `empresa-buum/01-ESTRATEGIA.md`, `buumia-os/CEO-DOCTRINA-CRECIMIENTO.md`.
- Reglas de contenido: skill `buumia-marketing` (candado de calidad, auditor de textos).

> Cambios a misión/visión/valores/identidad = **solo el dueño**. Endurecer reglas duras = CEO puede; relajarlas = requiere aprobación.
