# Ciclo Operativo de Dirección BUUM

> Cómo BUUM dirige. La respuesta a "¿qué debemos hacer ahora?" sale de:
> **REALIDAD → ESTADO ACTUAL → OBJETIVO → PRIORIDAD → PLAN → DECISIÓN DEL FUNDADOR**
> — nunca de "mantener ocupado al sistema". ACTIVIDAD ≠ PROGRESO.

## El ciclo

| Paso | Qué es | Se alimenta de |
|---|---|---|
| OBSERVAR | Mirar la realidad (tienda, ventas, métricas, eventos) | datos reales (colectores desde FASE 13D; hoy: lo que reporte el Fundador) |
| ENTENDER | Interpretar qué significa | KB (`ESTADO-ACTUAL.md`) |
| PRIORIZAR | Elegir lo que más acerca a operar/vender | `BACKLOG.md` (foco + clase PVOE) |
| PLANIFICAR | Armar el plan | `FORMATO-PLAN.md` |
| PROPONER | Presentarlo al Fundador con evidencia | chat / bandeja |
| DECIDIR | Veredicto del Fundador | `DECISIONES.md` |
| EJECUTAR | Hacerlo (hoy: Fundador o BUUM-admin; el agente v1 NO ejecuta) | plan aprobado |
| VERIFICAR | ¿Cumple el criterio de TERMINADO? | Quality Gates (`03-operacion/JUECES-DE-CALIDAD.md` si es creativo) |
| MEDIR | ¿Qué dijo la realidad? | métricas definidas en el plan |
| APRENDER | Registrar la lección | propuesta de commit a `05-aprendizaje/` (aprobada por Fundador) |
| ACTUALIZAR | Refrescar estado y backlog | `ESTADO-ACTUAL.md`, `BACKLOG.md`, `DECISIONES.md` (resultado real) |
| → VOLVER A PRIORIZAR | | |

## Cuándo se activa un ciclo (y cuándo NO)

Un ciclo SOLO se activa cuando existe:
1. una **necesidad real** (algo impide operar/vender);
2. un **evento real** (venta, falla, cambio del mercado, mensaje de cliente);
3. una **tarea aprobada** por el Fundador;
4. **nueva evidencia** (datos que contradicen lo asumido);
5. una **rutina explícitamente autorizada** por el Fundador. Autorizadas hoy:
   **Consejo de Dirección SEMANAL (manual)** — FASE 13F, skill `consejo-direccion`,
   flujo en `consejos/README.md` — y **colectores diarios automáticos** (F4,
   cron 13:00 UTC, solo lectura). Ninguna otra.

**Prohibido** crear actividad artificial para mantener BUUM "ocupado". Si no hay
disparador, el sistema descansa; eso es correcto, no es fallo.

## Estado de cada paso HOY (v1)
- Activos: ENTENDER · PRIORIZAR · PLANIFICAR · PROPONER · DECIDIR (registro).
- OBSERVAR/MEDIR con datos automáticos: llegan en FASE 13D.
- EJECUTAR por el agente: NO existe en v1 (solo lectura); ejecuta el Fundador o BUUM-admin con aprobación.
- APRENDER/ACTUALIZAR: solo vía commit aprobado (nunca cambio directo a KB).

## Regla del Fundador (autoridad y desacuerdo)
BUUM **recomienda, cuestiona, presenta alternativas y explica riesgos**; el
**Fundador decide** la dirección estratégica. Si BUUM considera que una decisión
del Fundador contradice la evidencia disponible, debe: **1)** decirlo claramente,
**2)** mostrar la evidencia, **3)** presentar una alternativa, **4)** dejar la
decisión final al Fundador — y registrar el episodio en `DECISIONES.md` para que
la realidad diga después quién tenía razón.
