# Protocolo permanente · CEO (BIS) ↔ Director de Marketing (ChatGPT)

> **Dueño:** CEO/Arquitecto (BIS) · aprobado por el Fundador · **Versión:** 1.0 · **Función:** el estándar único y reutilizable para producir CUALQUIER contenido de BUUM. Define cómo el BIS solicita creatividad a ChatGPT, la valida, la almacena, la publica, la mide y aprende de ella.
> Se apoya en: Constitución (Art. 5, 17), ciclo de vida de la acción (Capa 3), ADR-0011 (hechos/estrategia) y ADR-0012 (ChatGPT crea; el BIS opera).

## Principio

**ChatGPT crea; el BIS opera.** Este protocolo es la interfaz permanente entre ambos. No se rediseña por pieza: toda pieza —imagen, video, reel, carrusel, historia— recorre estos mismos pasos. Es el ciclo del BIS (nace → encuadra → decide → ejecuta → aprende → conserva) aplicado al contenido.

## Roles en cada paso

| Paso | Quién |
|------|-------|
| Solicitar, briefear, validar, almacenar, publicar, medir, aprender | **BIS (Claude)** |
| Concebir, escribir prompts, generar imágenes/videos, entregar | **Director de Marketing (ChatGPT)** |
| Aprobar publicación, dinero, ADN | **Fundador** |

## Estados de una pieza

`Solicitada → En creación (ChatGPT) → Entregada → Validada / Rechazada → Almacenada → Publicada → Medida → Aprendida`

Una pieza no salta estados; cada uno deja traza.

---

## 1. Cuándo se solicita creatividad

El BIS solicita una pieza cuando existe una necesidad de contenido nacida de una de cuatro fuentes (y ninguna otra):
- **Calendario/estrategia:** el plan de contenido pide una pieza.
- **Un producto/encargo:** entra un producto (Encargo de Producto) que amerita contenido.
- **Un aprendizaje:** el libro de jugadas sugiere probar/repetir un ángulo.
- **Directiva del Fundador.**

El BIS decide *qué* se necesita y *cuándo* (coordinación); nunca inventa la creatividad. Una pieza sin fuente clara no se solicita.

## 2. Qué información se envía (contenido del brief)

El brief da el QUÉ y las barreras, nunca el CÓMO creativo. Contiene:
- **Objetivo** único (resonancia / dar a conocer / vender, cuando haya producto vendible).
- **Métrica y umbral de éxito** (la expectativa registrada, antes de crear).
- **Formato y canal** (reel 9:16, carrusel 4:5, historia, imagen…).
- **Restricciones duras** (las valida el BIS al recibir): honestidad (luz blanca real, solo stock real, sin claims falsos ni "lista de espera"), ADN de BUUM (marca, mascota, logo, vibra), reglas de red social.
- **Conocimiento aplicable:** extractos del libro de jugadas (qué ha funcionado; qué evitar).
- **Referencias/activos disponibles** (fotos de producto, frames, logo).
- **Prioridad** y fecha objetivo.

## 3. Formato del brief (BIS → ChatGPT)

```
BRIEF-<id> · <fecha>
Objetivo:            <uno>
Métrica + umbral:    <cómo se medirá el éxito>
Formato / canal:     <reel 9:16 / carrusel / imagen / historia>
Restricciones duras: <honestidad + ADN + reglas de red>
Del libro de jugadas:<qué funciona / qué evitar>
Referencias:         <rutas de activos>
Prioridad / fecha:   <...>
NO incluir:          <prompts creativos — eso lo decide ChatGPT>
```

## 4. Formato de la entrega (ChatGPT → BIS)

```
ENTREGA-<id> · responde a BRIEF-<id>
Pieza(s):        <archivo(s) final(es) o assets + detalle de generación>
Concepto/ángulo: <la idea en una frase>
Estilo/formato:  <estilo usado, dimensiones, canal>
Cumplimiento:    <nota de cómo respeta honestidad + ADN>
Notas:           <lo que el BIS deba saber para validar/medir>
```

## 5. Cómo se valida (candado de calidad — lo corre el BIS)

El BIS aplica el candado a cada entrega, en este orden. Nada avanza sin pasarlo:
1. **Compuerta de honestidad:** luz blanca real, solo stock real, sin claims falsos ni oferta cuando no hay venta. *Un fallo aquí = rechazo inmediato.*
2. **ADN:** marca, mascota, logo, vibra, colores correctos.
3. **Auditor de textos:** ortografía, acentos, contraste/legibilidad, nada encimado, sin texto basura.
4. **Calidad/puntaje:** ¿la publicaría una marca de nivel? Regla: **solo pasa 9+/10**. 7-8.9 → el BIS pide el ajuste concreto a ChatGPT; <7 sin potencial → se descarta.

Resultado: **Validada** (≥9, lista) o **Rechazada** (con el motivo exacto para que ChatGPT re-entregue).

## 6. Cómo se almacena en la Knowledge Base

Toda pieza **validada** se archiva en `06-contenido/` con su expediente (nada se pierde, todo trazable):
- El archivo final + su BRIEF + su ENTREGA + el puntaje del candado.
- Metadatos: fecha, objetivo, formato, canal, estilo/ángulo, estado.
Las piezas rechazadas también quedan registradas (para aprender de lo que no pasó).

## 7. Cómo se publica

Publicar es **reservado al Fundador** (Art. 17). El BIS:
1. Prepara el paquete de publicación (pieza validada + copy + destino).
2. Lo presenta al Fundador para **visto bueno**.
3. Con la aprobación, **ejecuta la publicación** por el canal (la herramienta concreta es intercambiable; el protocolo no depende de ella).
Sin aprobación registrada, nada se publica.

## 8. Cómo se mide

Publicada la pieza, el BIS captura el **resultado real** y lo contrasta con la **expectativa registrada** en el brief (paso 2). Se registra sin adornar. Métricas según el objetivo (resonancia: retención, guardados, compartidos, comentarios, seguidores; venta: clics, mensajes, ventas).

## 9. Cómo aprende el sistema

Del contraste esperado vs. real sale una **lección** con su nivel de confianza, que actualiza el **libro de jugadas** (`05-aprendizaje`): los ángulos/estilos que resuenan suben de confianza; los que fallan se retiran de la memoria activa (sin borrarse). Ese aprendizaje **alimenta el próximo brief** (paso 2). Así el sistema produce mejor contenido cada semana.

---

## Resumen del ciclo (una vuelta)

Necesidad → **BIS** briefea → **ChatGPT** crea → **BIS** valida (candado) → **BIS** almacena (KB) → **Fundador** aprueba → **BIS** publica → **BIS** mide → **BIS** aprende (libro de jugadas) → mejor brief siguiente.

Este protocolo es permanente. No se rediseña; se mejora por versión si la evidencia lo justifica.

## Registro de versiones

| Versión | Fecha | Cambio |
|---------|-------|--------|
| 1.0 | 2026-07-15 | Protocolo inicial CEO↔Director de Marketing. |
