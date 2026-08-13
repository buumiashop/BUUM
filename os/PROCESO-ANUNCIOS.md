# 📣 PROCESO DE ANUNCIOS BUUM (SOP) — de la idea a la publicación

> Proceso OBLIGATORIO para CADA pieza de contenido (imagen, video, historia, carrusel, meme).
> Nada se salta pasos. Nada se publica sin autorización del dueño. Diseñado para que cualquiera pueda operarlo.

## Roles (quién hace qué)
- **Director Creativo (IA):** inventa el concepto y dirige (ver `DIRECCION-CREATIVA.md` / `DIRECCION-VIDEO.md`).
- **Producción (IA):** genera la pieza (Gemini/Kling/ffmpeg/PIL).
- **Control de Calidad (IA):** los **4 filtros** (`filtros_calidad.py`) — Jefe de Marketing, Director Creativo/CIO, Crítico mundial DTC.
- **Dueño:** la autorización final. **Sin su OK no se publica NADA.**

## Flujo (los pasos)
1. **Idea / Concepto.** El Director Creativo elige un ángulo del banco de conceptos (variado: pro, arte, meme, realista, emocional — nunca genérico). Regla: 1 idea fuerte.
2. **Producción.** Se genera la pieza siguiendo la receta del WOW + reglas de marca (logo oficial, luz blanca, sin foco antiguo de vidrio — ver `buumia-brand-kit`).
3. **Curaduría.** Se generan varias variantes y se queda la mejor.
4. **Control de Calidad (4 filtros).** La pieza pasa por los 3 críticos IA. Solo lo que aprueban los 3 avanza. Lo rechazado se rehace o se descarta (con motivo).
5. **Cola "Por autorizar".** Lo aprobado por QC entra a la Galería del Centro de Mando con estado **"Por autorizar"**. NADA se publica todavía.
6. **Autorización del dueño.** El dueño revisa en el OS y da **✅ Autorizar** (o **✍️ Editar** con observación, o **🗑️ Eliminar**).
7. **Programación.** Lo autorizado se agenda (mañana/tarde/noche) en el calendario.
8. **Publicación.** En el horario, se publica en @buum.ia / Facebook. (Este paso se activa SOLO cuando el dueño lo autorice; hoy está en modo "no publicar".)
9. **Medición.** Se leen likes/alcance/guardados. Lo que engancha se repite y escala; lo que no, se cambia.

## Reglas de calidad (candados)
- ✅ On-brand: logo oficial, colores, luz blanca, "vale la pena".
- ✅ Enganche en 1 seg, ~95% visual, tipografía LIMPIA (texto con PIL, no de la IA).
- ⛔ Prohibido: foco antiguo de vidrio amarillo solo, promesas falsas, productos que no tenemos, logos redibujados por IA.
- 🎯 Meta: no genérico. Creatividad amplia (arte, meme, realista, emocional) para generar likes.

## Estado del proceso (control)
- Cada pieza tiene estado: `idea → producida → QC → por-autorizar → autorizada → programada → publicada → medida`.
- Todo se ve en el Centro de Mando (Galería + Rutinas + Calendario).

Relacionado: `MANUAL-DE-OPERACIONES.md`, `DIRECCION-CREATIVA.md`, `DIRECCION-VIDEO.md`, `EQUIPO.md`, `filtros_calidad.py`.
