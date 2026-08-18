---
name: quality-gates
description: Aplica los 14 Quality Gates de BUUM a cualquier dato, recomendación o plan antes de usarlo o proponerlo. Obligatoria antes de toda conclusión basada en datos y de toda acción propuesta. Devuelve veredictos PASS/FAIL/BLOCKED/NOT_APPLICABLE.
---

# Quality Gates de BUUM (FASE 13C)

Barrera obligatoria entre DATOS → INTERPRETACIÓN → PLAN → ACCIÓN.
Un gate NUNCA dice "me parece bien": produce un veredicto verificable.

## Veredictos permitidos (únicos)
- **PASS** — cumple.
- **FAIL** — no cumple.
- **BLOCKED** — no hay información suficiente para decidir.
- **NOT_APPLICABLE** — el gate no aplica a este caso.
Prohibido: "más o menos", "parece", "probablemente", "creo que".

## Regla crítica: NO_DISPONIBLE ≠ 0
- `ventas = 0` con fuente real → **dato REAL** (cero de verdad).
- `utilidad_real` sin costos en la fuente → **NO_DISPONIBLE** (jamás escribir 0 ni inventar).
Nunca conviertas uno en el otro.

## Los 14 gates

| # | Gate | Qué verificar | Si falla |
|---|---|---|---|
| 01 | **Fuente** | El dato tiene fuente identificable, timestamp, versión de colector/snapshot, clasificación e integridad (snapshots: `datos/snapshots/<fuente>/<día>/snapshot.json`) | Sin fuente verificable → BLOCKED |
| 02 | **Frescura** | ¿El dato es lo bastante reciente para ESTA decisión? Inventario → alta frescura; ventas del mes → tolera más; histórico → cualquiera. No inventar actualidad | Antigüedad insegura → BLOCKED |
| 03 | **Completitud** | Existen TODOS los datos necesarios para la operación. No completar mentalmente lo que falta | Falta un insumo → BLOCKED |
| 04 | **Clasificación** | REAL / CALCULADO / ESTIMADO / NO_DISPONIBLE se conservan. Un CALCULADO sobre datos reales sigue siendo CALCULADO, nunca asciende a REAL | Naturaleza intercambiada → FAIL |
| 05 | **Consistencia** | El mismo dato coincide en FUENTE→SNAPSHOT→API→UI→AGENTE. Si difieren, no usar silenciosamente ninguno | Diferencia detectada → FAIL (y reportarla) |
| 06 | **No invención** | Jamás inventar precios, costos, ventas, inventario, márgenes, ROAS, utilidad, conversiones, datos de clientes, resultados de campañas o "datos de mercado" como hechos. Lo inexistente = NO_DISPONIBLE; lo estimable = ESTIMADO declarado | Dato inventado → FAIL |
| 07 | **Plan antes de acción** | Toda acción propuesta está estructurada como plan (skill `formato-plan`). Nunca pasar de "detecté algo" a "lo ejecuto" | Sin plan → BLOCKED |
| 08 | **Autoridad** | Clasificar la propuesta: OBSERVACIÓN / RECOMENDACIÓN / PLAN / ACCIÓN AUTORIZADA / ACCIÓN NO AUTORIZADA. En v1 el agente es SOLO LECTURA: toda escritura o efecto externo = ACCIÓN NO AUTORIZADA (requiere aprobación del Fundador y capacidades que hoy no existen) | Acción no autorizada → BLOCKED |
| 09 | **Reversibilidad/Riesgo** | Evaluar impacto, reversibilidad, alcance, riesgo, dependencia externa. Lo difícil de revertir exige barrera superior (aprobación explícita) | Riesgo alto sin barrera → BLOCKED |
| 10 | **Coherencia con dirección** | Comparar con `KB/08-direccion/` (BACKLOG, DECISIONES, CICLO-OPERATIVO) y doctrina KB. La decisión REGISTRADA MÁS RECIENTE del Fundador prevalece sobre doctrina anterior | Contradice decisión vigente → FAIL |
| 11 | **Objetivo de negocio** | La propuesta declara qué mejora: ventas, margen, conversión, inventario, adquisición, retención, experiencia, operación. Sin propósito → actividad prohibida (ACTIVIDAD ≠ PROGRESO) | Sin objetivo → BLOCKED |
| 12 | **Evidencia** | Separar y etiquetar: HECHO / INTERPRETACIÓN / HIPÓTESIS / RECOMENDACIÓN. Una hipótesis jamás se presenta como hecho | Hipótesis disfrazada → FAIL |
| 13 | **Conflicto** | Dos fuentes oficiales contradictorias → NUNCA elegir en silencio. Emitir `CONFLICTO DETECTADO` con: fuente A, fuente B, diferencia, cuál prevalece según reglas (decisión más reciente del Fundador), o qué debe decidir el Fundador | — (el veredicto ES el conflicto declarado) |
| 14 | **Datos insuficientes** | Si falta información: no improvisar, no rellenar, no fingir certeza. `BLOCKED — DATOS INSUFICIENTES` + lista exacta de lo que falta | — |

## Formato de salida (obligatorio)

```
QUALITY GATE REPORT
Gate 01 — Fuente: PASS
Gate 02 — Frescura: PASS
Gate 03 — Completitud: BLOCKED — motivo: costo real no disponible
Gate 04 — Clasificación: PASS
(… solo los gates relevantes; los demás NOT_APPLICABLE …)

RESULTADO GENERAL: PASS | FAIL | BLOCKED
ACCIÓN: (qué se hace / qué NO se hace y por qué)
```

**Regla del resultado general:** si un gate crítico da FAIL o BLOCKED, el proceso
NO continúa automáticamente — se reporta y se detiene o se pide decisión al Fundador.

## Separación de responsabilidades
Esta skill **EVALÚA**. La skill `formato-plan` **ESTRUCTURA**. No mezclar.
