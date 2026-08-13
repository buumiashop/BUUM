# ADR-0015 — Separar Knowledge Base y Biblioteca de Activos Visuales
- **Fecha:** 2026-07-17
- **Estado:** Aceptada (precisión del Fundador)
- **Contexto:** El Flujo Operativo dice "Marketing no usa fotos crudas, solo el Documento Maestro". Pero Marketing sí necesita recursos visuales oficiales para producir. Había ambigüedad sobre dónde viven esos recursos.

## Decisión
Dos activos oficiales **distintos**:
1. **Knowledge Base** — solo conocimiento permanente (hechos, especificaciones, capacidades, restricciones, aprendizajes). Define **QUÉ comunicar**.
2. **Biblioteca de Activos Visuales** — recursos gráficos oficiales del procesamiento (fotos limpias, PNG transparentes, HD, vistas, renders). Define **CON QUÉ producir**.

Marketing **consume ambos**; **nunca** usa fotos crudas de la Recepción. Las fotos crudas son insumo del Paso 3 (Procesamiento); su salida oficial es la Biblioteca.

## Ventajas
- Coherencia: el conocimiento no se mezcla con imágenes; cada activo tiene un propósito claro.
- Marketing tiene una fuente de recursos limpia y estandarizada.

## Desventajas / cuidado
- Hay que mantener el **vínculo** producto ↔ sus activos (un índice/carpeta por producto).

## Impacto
- Bajo. Formaliza lo que ya hacíamos (usábamos `60w-*-clean.png` como activos). Ubicación sugerida: `KB/.../productos/<producto>/activos/` o carpeta de biblioteca dedicada. Se define al correr la Recepción del reflector.
