# ADR-0014 — Arquitectura: Conocimiento / Estrategia / Producción + Motor de Evolución
- **Fecha:** 2026-07-17
- **Estado:** Aceptada (documento de transferencia del Fundador)
- **Contexto:** El Fundador transfiere el estado de la arquitectura de BUUM (el "SO" de la empresa; las IA son herramientas). Confirma decisiones ya analizadas.

## Decisión
1. **BUUM = organización digital / Sistema Operativo** de la empresa. Claude/ChatGPT/otras IA son **herramientas**, nunca BUUM. (Ya reflejado en modularidad de VISION-2030.)
2. **Separación estricta:** **Conocimiento** (permanente/verificable) · **Estrategia** (se decide en tiempo real) · **Producción** (contenido bajo demanda). El conocimiento **nunca** contiene creatividad.
3. **Docs de producto = documentos de CONOCIMIENTO**, no fichas creativas. **Guardar:** hechos, capacidades, restricciones, evidencias, aprendizajes, info técnica, manual, FAQs reales. **NO guardar:** prompts, videos, anuncios, campañas, escenas, ideas temporales, contenido creativo. El doc de producto **nunca dice cómo hacer publicidad**, solo qué es verdadero.
4. **Contenido bajo demanda:** cada solicitud genera contenido nuevo (no reutiliza campañas), consultando KB + identidad + objetivo + contexto actual + info reciente.
5. **Marketing piensa primero** (objetivos, inventario, prioridades, temporada, competencia, tendencias, historial) → estrategia → producción.
6. **Aprendizaje = conocimiento** (preguntas de clientes, info faltante, errores repetidos, qué campañas/decisiones funcionan), no "aprender anuncios".
7. **Motor de Evolución:** componente que analiza la organización y **propone** mejoras justificadas; **nunca** modifica la arquitectura automáticamente; requiere aprobación humana.

## Consecuencias
- La mayor parte ya está implementada; se **afina**, no se reinventa.
- Refinamiento concreto: limpiar docs de producto de cualquier creatividad/estrategia (ej. quitar "gancho de venta" de `FOCO-LED-60W.md`).
- Separar 3 cubos: **Conocimiento** (KB, permanente) · **ADN/Sistema/Plantillas** (reglas de "cómo", permanente) · **Contenido generado** (temporal/regenerable).
- Motor de Evolución = **Evolutiva** (roadmap post-PVOE), no bloquea la operación.

## Alineación con PVOE
Ninguna de estas mejoras es Crítica para operar. Se registran y se ejecutan como **Evolutiva** sin retrasar la PVOE.
