# ADR-0013 — Desacople de proveedor: la creatividad la genera solo el Director de Marketing (ChatGPT)

- **Estado:** Aceptado
- **Fecha:** 2026-07-16
- **Decide:** Fundador (refina ADR-0012)

## Contexto

ADR-0012 estableció que ChatGPT crea y el BIS opera. En la práctica, BUUM había estado llamando directamente a Gemini/Replicate/OpenAI para generar imágenes (p. ej. keyframes de REEL 001). Eso ata el sistema a un proveedor concreto y dispersa el estándar creativo entre varios modelos.

## Decisión

**El generador creativo oficial es el Director de Marketing (ChatGPT).** BUUM **no** usará directamente Gemini, Replicate, OpenAI ni ningún otro modelo para **generar creatividad** (conceptos, imágenes, videos, campañas, prompts creativos).

El rol de BUUM frente al contenido:
1. **Solicitar** la producción creativa al Director de Marketing (brief).
2. **Recibir** el resultado.
3. **Validar** (candado + honestidad).
4. **Almacenar** en la Knowledge Base.
5. **Publicar** (con el gate del Fundador).
6. **Medir** y aprender.

Beneficios: el sistema queda **desacoplado del proveedor de IA** y la creatividad mantiene un **estándar único**.

## Consecuencias

- Las herramientas de generación creativa del proyecto (`gen_*.py`, `gemini_image.py`, flux/Kling) dejan de ser ejecutadas por BUUM para crear; quedan como referencia/legado. Si ChatGPT las usa por dentro, es su decisión de herramienta.
- Las herramientas **operativas** de BUUM (publicar, medir, verificar conexiones) **siguen siendo de BUUM** (no son creatividad).
- El motor de contenido automático (rutina diaria) ya no genera por sí mismo: su papel se reduce a orquestar (calendario/filtros/publicación); la generación la aporta el Director de Marketing.
- No aplica al asistente de ventas (gatito): responder al cliente es operación de ventas, no producción creativa.
