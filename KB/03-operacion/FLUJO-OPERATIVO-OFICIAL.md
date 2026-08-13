# Flujo Operativo Oficial de BUUM (v1.0)
> Extensión oficial de la Memoria Arquitectónica (Fundador, 2026-07-17). Complementa la arquitectura (el "cómo está construido") con el **"cómo trabaja paso a paso"**. **Debe respetarse en TODA implementación.** No reemplazar por otro flujo. Si hay contradicción entre documentos: señalarla y pedir decisión (no asumir).

## Los 12 pasos
1. **Recepción** — el usuario aporta la info disponible (fotos del producto/caja, manuales, etiquetas, código de barras, certificaciones, info del proveedor). **Aún NO existe documento del producto.**
2. **Auditoría** — BUUM revisa todo lo recibido; identifica info presente/faltante/obligatoria/recomendable/opcional. **Si falta info crítica, la solicita ANTES de continuar.**
3. **Procesamiento de imágenes** — normalizar TODAS las imágenes (ruido, iluminación, perspectiva, recorte, fondo limpio, color, alta resolución, PNG transparente; principal/detalle/documentación) → **Biblioteca de Activos Visuales** (activo oficial, **distinto de la KB**).
4. **Extracción de conocimiento** — extraer todo lo posible (SKU, código de barras, marca, modelo, potencia, voltaje, frecuencia, materiales, medidas, peso, lúmenes, certificaciones, IP, contenido del empaque, garantía, instrucciones, advertencias, compatibilidades).
5. **Documento Maestro del Producto** — solo tras la extracción. Fuente oficial de conocimiento. **Solo conocimiento permanente.** NO campañas/anuncios/prompts/publicaciones/imágenes de marketing/videos.
6. **Validación** — validar el Documento Maestro **antes** de entrar a la KB (asegurar que el conocimiento es correcto).
7. **Knowledge Base** — el Documento Maestro validado entra a la KB. Desde aquí, cualquier sistema consulta **este documento, no las fotos originales**.
8. **Marketing** — nunca usa fotos crudas. Consume **DOS activos oficiales**: la **Knowledge Base** (qué comunicar) + la **Biblioteca de Activos Visuales** (con qué recursos producir).
9. **Estrategia** — antes de producir, analizar objetivos/inventario/temporada/público/contexto/historial/aprendizajes. **Primero piensa, después decide.**
10. **Producción** — solo tras la estrategia se generan anuncios/imágenes/videos/carruseles/emails/SEO/páginas/publicaciones. **Todo el contenido es temporal.**
11. **Medición** — CTR, conversión, ROAS, permanencia, engagement, ventas.
12. **Aprendizaje** — NO se guarda el contenido; solo los **aprendizajes** (qué funcionó/no, patrones, mejoras) → enriquecen la KB.

## Reglas duras de esta sesión
- El Documento Maestro **no puede existir antes de terminar la Auditoría**.
- Las **fotos nunca llegan directo a Marketing**.
- Marketing trabaja **solo con conocimiento validado**.
- Las imágenes primero se **procesan/estandarizan**.
- La creatividad **no vive en la KB**; solo el conocimiento permanece; el contenido se genera bajo demanda.
- La arquitectura evoluciona **solo con evidencia de la operación**.
- **Nunca se borra una imagen recibida (regla del Fundador 2026-07-17).** Todas son valiosas (más ángulos = mejor referencia para generar). Si algo parece NO pertenecer al producto, va a `revisar/` y **lo decide el Fundador**, no BUUM. Meta: un documento con el **100% de la info** del producto.

## Dos activos oficiales (precisión ADR-0015)
Se separan explícitamente:
1. **Knowledge Base** — solo **conocimiento permanente** del producto (hechos, especificaciones, capacidades, restricciones, aprendizajes). Define **QUÉ comunicar**.
2. **Biblioteca de Activos Visuales** — todos los **recursos gráficos oficiales** generados en el procesamiento (fotos limpias, PNG transparentes, HD, vistas, renders…). Define **CON QUÉ producir**.

Marketing **consume ambos** y **nunca** usa fotos crudas de la Recepción. Las fotos crudas son insumo del Paso 3; su salida oficial es la Biblioteca de Activos Visuales.

## Implicación para la PVOE (reflector)
La PVOE debe respetar el flujo completo. **No asumir que el Documento Maestro existe** si aún no se hicieron Recepción → Auditoría → Procesamiento de imágenes → Extracción → Validación. **La campaña solo empieza cuando el Documento Maestro esté aprobado y en la KB.**
