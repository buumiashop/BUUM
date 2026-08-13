# 👥 EQUIPO BUUM OS — las entidades que trabajan

> Cada "entidad" = un **agente de IA** con mandato + proceso + herramientas. El cerebro es Claude; corren por **rutinas programadas**. El dueño DIRIGE y aprueba; los agentes EJECUTAN.

## 🧠 CEO (orquestador)
- **Mandato:** que la empresa CREZCA. Lee el estado (ventas, stock, calendario), decide prioridades, reparte tareas a los departamentos, revisa lo que entregan y marca el rumbo.
- **Entrega:** estrategia + plan de la semana + decisiones (comprar / pautar / escalar / pausar / ofertar).
- **Se conecta con:** todos. Recibe reportes de cada área y regresa órdenes.
- **Rutina:** `rutina_semanal.py` (arma la semana). Doc: `ESTRATEGIA.md`.

## 🔎 Investigación & Producto
- **Mandato:** encontrar productos ganadores con **margen 2x** y saber a quién venderles.
- **Hace:** estudios de mercado (tendencias, demanda por ciudad: Guadalajara/Monterrey/CDMX), comparar proveedores, calcular costo/precio/margen, decidir qué sacar.
- **Entrega:** brief de producto + público objetivo → se lo pasa a Marketing.
- **Herramientas:** WebSearch (tendencias/competencia), datos de Shopify/Meta al conectar.

## 📣 Marketing & Contenido
- **Mandato:** producir contenido y anuncios de **nivel mundial** con el brief de Investigación.
- **Hace:** imágenes (Gemini), video (Kling+ffmpeg), copy, historias/reels/carruseles, y **pasa cada pieza por los 4 filtros**.
- **Entrega:** contenido aprobado a la cola "Por aprobar" del panel.
- **Herramientas:** skills `buumia-marketing`, `buumia-anuncios-ganadores`; `filtros_calidad.py` (los 4 filtros).

## 🛡️ Panel de Calidad (los 4 filtros)
1. Jefe de Marketing (on-brand, engancha, visual) · 2. Director Creativo/CIO (calidad técnica) · 3. Crítico "marca mundial" (¿lo publicaría Nike/Coca-Cola?) · 4. **Tú** (el sí final).
- Solo lo que pasa 1-2-3 llega a ti. Script: `filtros_calidad.py`.

## 🛒 Ventas & Clientes
- **Mandato:** convertir visitas en ventas y clientes que regresan.
- **Hace:** tienda, checkout, mayoreo, **Sofía/gatito IA** que asesora y cierra. Mensajes (WhatsApp/IG) con bot.

## 🚚 Operaciones & 💰 Finanzas
- **Mandato:** que nunca falte stock de lo que vende y que el dinero cuadre.
- **Hace:** inventario, punto de reorden, empaque/envíos; utilidad real, caja, control de créditos, y las 5 decisiones del lunes.

## Ritmo
- **Entre semana:** los agentes trabajan (generan, filtran, agendan).
- **Lunes (o cuando te metas):** revisas el Centro de Mando y apruebas la semana. Al principio apruebas todo; en el futuro, reglas auto-aprueban y tú solo revisas.

Relacionado: `BUUMIA-OS.md`, `ESTRATEGIA.md`, `centro-de-mando.html`.
