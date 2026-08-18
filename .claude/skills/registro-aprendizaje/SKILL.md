---
name: registro-aprendizaje
description: Convierte un aprendizaje detectado (en un Consejo, un resultado o un evento) en una PROPUESTA formal de registro para la KB de aprendizaje. El agente propone; el Fundador aprueba; BUUM-admin registra. Nunca escribe la KB directamente.
---

# Registro de Aprendizaje BUUM (FASE 13G)

Cierra el ciclo: RESULTADO → APRENDIZAJE → (aprobación) → KB.
El agente **PROPONE**, el Fundador **DECIDE**, BUUM-admin **REGISTRA**. Jamás al revés.

## Cuándo usarla
- Sección 13 de un Consejo de Dirección con un aprendizaje maduro.
- Un resultado real confirmó o descartó una hipótesis registrada.
- El Fundador dio feedback que cambia cómo se trabaja.
- La realidad contradijo un documento oficial (además: Gate 13, conflicto).

## Formato de la propuesta (obligatorio)

```
PROPUESTA DE APRENDIZAJE

Tipo:      HECHO APRENDIDO | HIPÓTESIS CONFIRMADA | HIPÓTESIS DESCARTADA | PREGUNTA ABIERTA
Enunciado: (1-3 líneas, accionable — qué haremos distinto por saber esto)
Evidencia: (fuente + fecha; una sola observación débil NO confirma una hipótesis)
Gates:     (veredicto de quality-gates sobre la evidencia)
Destino:   KB/05-aprendizaje/LECCIONES.md | GUSTOS-DEL-FUNDADOR.md |
           LIBRO-DE-JUGADAS-MARKETING.md | (o actualización puntual de otro doc, citado)
Impacto:   (qué documento/proceso/decisión debería ajustarse, si aplica)

ESTADO: PROPUESTA — requiere aprobación del Fundador
```

## Reglas duras
- Una PREGUNTA ABIERTA no se disfraza de hecho; una observación única no "confirma".
- Si el aprendizaje contradice doctrina/decisión vigente → declararlo (Gate 13) y
  dejar que el Fundador decida; su decisión registrada más reciente prevalece.
- Aprendizajes estructurales (cambian arquitectura/gobierno) → proponer ADR en
  `KB/00-gobierno/adr/`, no una línea suelta.
- Tras el veredicto del Fundador, BUUM-admin hace el commit al destino y lo anota
  en `DECISIONES.md` si fue una decisión. El agente NUNCA escribe.
