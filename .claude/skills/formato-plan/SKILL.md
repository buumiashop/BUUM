---
name: formato-plan
description: Estructura cualquier propuesta o acción del agente BUUM como un plan estándar compacto. Obligatoria para toda acción propuesta. Solo estructura; la evaluación la hace la skill quality-gates.
---

# Formato-Plan de BUUM (FASE 13C)

Toda acción propuesta se representa con esta plantilla ANTES de pedir aprobación.
Compacta: llenar cada campo en 1-3 líneas. No convertirla en burocracia.
Doctrina completa: `KB/08-direccion/FORMATO-PLAN.md`. HECHO ≠ TERMINADO
(`KB/00-gobierno/MODELO-DE-MADUREZ.md`).

```
PLAN — [nombre corto]

Objetivo:            (qué mejora del negocio: ventas/margen/conversión/inventario/
                      adquisición/retención/experiencia/operación)
Contexto:            (situación real actual, con fuente)
Datos utilizados:    (cada dato con su clasificación REAL/CALCULADO/ESTIMADO)
Fuentes:             (snapshot/KB/decisión, con fecha)
Hechos:              (solo hechos verificables)
Interpretaciones:    (lectura de los hechos, etiquetada como interpretación)
Supuestos:           (lo que se asume sin evidencia, declarado)
Acciones propuestas: (pasos concretos y verificables)
Riesgos:             (qué puede salir mal + mitigación + reversibilidad)
Quality Gates:       (veredicto por gate relevante — skill quality-gates)
Resultado de Gates:  PASS | FAIL | BLOCKED

ESTADO: PASS | BLOCKED | REQUIERE AUTORIZACIÓN
```

Reglas:
- El plan sin gates NO es un plan válido.
- En v1 (agente solo lectura) toda acción con efecto externo termina en
  `REQUIERE AUTORIZACIÓN` — la ejecuta el Fundador o BUUM-admin con su aprobación.
- Recomendación ≠ aprobación.
