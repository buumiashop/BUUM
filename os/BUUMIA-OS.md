# 🧠 BUUMIA OS — Sistema operativo de la empresa (v1)

> El "molde" para operar BUUMIA como una empresa ordenada, automatizada y replicable (estilo cadena),
> que pueda crecer de 10 a 300+ productos **sin caos** y funcionar aunque el fundador no esté operando todo el día.

## Principios de diseño (el por qué)
1. **Sistemas, no personas.** Cada área es un SISTEMA documentado (proceso + checklist + métricas + dueño). Si entra una persona, solo "se enchufa" al sistema.
2. **Lean hoy, escalable mañana.** Hoy somos Fundador + IA. No abrimos 22 departamentos: agrupamos en **7 áreas activas** que cubren todo, y se subdividen al crecer.
3. **La IA hace el grueso** (repetitivo/masivo: contenido, fichas, anuncios, reportes). **El humano decide** (dinero, calidad final, relaciones, visión).
4. **Plantillas/moldes** para que todo salga igual de bien (anuncios, fichas, fotos) — primera vez bien hecho.
5. **El CEO aprueba todo cobro/inversión** hasta que se automatice por reglas.
6. **Todo se mide en utilidad real**, no en "se ve bonito".

---

## 🗺️ Organigrama (7 áreas activas + 1 dormida)
```
                        DIRECCIÓN / CEO  (Fundador + Claude estratega)
                                  │
   ┌───────────┬───────────┬──────┼───────────┬───────────┬───────────┐
   │           │           │      │           │           │           │
 PRODUCTO   MARKETING    VENTAS  OPERACIONES FINANZAS   BUUMIA OS
 & ABASTO  & CONTENIDO  & CLIENTES & LOGÍSTICA           IA/TECNOLOGÍA
                                  
            (PERSONAS / RH — dormida, se activa al contratar)
```
Cada área hoy la corren **Fundador + IA**; el diseño deja claro a quién se delega después.

---

## 🏢 Las 7 áreas (qué hace cada una)

### 1) DIRECCIÓN / CEO  · prioridad ALTA
- **Objetivo:** rumbo, metas, prioridades y decisiones; que la empresa avance sin caos.
- **Hace:** metas (trimestre/semana), revisa métricas, aprueba dinero, decide productos (escalar/pausar/liquidar), expansión.
- **Responsable:** hoy Fundador + Claude (asesor). Futuro: Fundador como director.
- **IA:** tablero de métricas, resúmenes, recomendaciones, planeación de tareas y calendario.
- **Humano:** decisiones finales, aprobaciones de dinero, visión, relaciones clave.
- **Herramientas:** Panel BUUMIA OS, Notion, métricas Shopify/Meta.
- **Checklist diario:** ver ventas + mensajes + caja · aprobar pendientes · definir tarea del día.
- **Semanal:** revisar métricas · decidir sobre productos · armar plan de la semana.
- **Métricas:** ventas, utilidad real, flujo de caja, # pedidos, CAC, productos ganadores.
- **Contratar:** asistente/gerente operativo cuando el fundador esté saturado (Fase 3).

### 2) PRODUCTO & ABASTO  · prioridad ALTA
*(fusiona: Productos + Investigación de mercado + Proveedores/Importaciones + Inventario)*
- **Objetivo:** encontrar, validar y abastecer productos ganadores con buen margen.
- **Hace:** detecta ideas, investiga demanda, compara proveedores, pide muestras, valida calidad, calcula costo, fija precios, controla inventario y reórdenes.
- **IA:** investigación de mercado, comparar precios China vs MX, calcular márgenes, fichas técnicas, alertas de stock.
- **Humano:** pedir/recibir muestras, validar calidad física, negociar proveedor, decidir compra.
- **Herramientas:** Alibaba/1688, catálogo (`buumia-catalogo/`), hoja de costos, Shopify inventario.
- **Diario:** revisar stock de productos activos · pendientes de muestra.
- **Semanal:** 1-2 ideas nuevas investigadas · revisar reórdenes · margen por producto.
- **Métricas:** margen real, rotación (días en vender), % productos ganadores, quiebres de stock.
- **Contratar:** comprador/abastecedor en Fase 3.

### 3) MARKETING & CONTENIDO  · prioridad ALTA
*(fusiona: Marketing + Producción de contenido + Foto/Video)*
- **Objetivo:** que la marca se vea pro y que cada producto venda con contenido.
- **Hace:** branding, fotos/render, anuncios, reels, carruseles, guiones, copies, campañas por nicho, **talento virtual** (personajes IA).
- **IA:** generar fotos/anuncios/videos/guiones desde la **plantilla oficial** (motor de contenido), variantes por nicho, calendarizar.
- **Humano:** aprobar lo que se publica (rúbrica), dar dirección creativa, decidir campañas.
- **Herramientas:** motor de anuncios (`buumia-catalogo/`), Gemini (imagen), Replicate/Kling (video), ElevenLabs (voz), Brand Kit (`marca/`), API Meta.
- **Diario:** publicar lo agendado · 1 pieza de contenido.
- **Semanal:** plan de contenido · revisar qué post jaló · refrescar campañas.
- **Métricas:** alcance, engagement, mensajes generados, costo por mensaje, ventas atribuidas.
- **Contratar:** creador de contenido/editor en Fase 3.

### 4) VENTAS & CLIENTES  · prioridad ALTA
*(fusiona: Ventas mayoreo + menudeo + E-commerce + Atención al cliente)*
- **Objetivo:** convertir interés en pedidos y clientes que recompran.
- **Hace:** tienda Shopify, ventas por WhatsApp/DM, mayoreo, cotizaciones, seguimiento, postventa, recompra, reseñas.
- **IA:** respuestas automáticas (FAQ, precios, mayoreo), catálogo, recordatorios de seguimiento/recompra, cotizador.
- **Humano:** cerrar ventas grandes de mayoreo, casos especiales, relación con clientes clave.
- **Herramientas:** Shopify, WhatsApp Business, bot/respuestas, CRM simple (lista de clientes).
- **Diario:** contestar todos los mensajes · confirmar pedidos · seguimiento a interesados.
- **Semanal:** recontactar clientes (recompra) · revisar embudo.
- **Métricas:** # pedidos, ticket promedio, tasa de respuesta, % recompra, conversión.
- **Contratar:** atención al cliente/ventas cuando los mensajes rebasen al fundador (Fase 2).

### 5) OPERACIONES & LOGÍSTICA  · prioridad ALTA
*(fusiona: Operaciones + Logística + Calidad)*
- **Objetivo:** que cada pedido llegue bien y a tiempo, sin errores.
- **Hace:** recibir pedido, confirmar pago, separar, empacar, enviar, rastrear, garantías, calidad.
- **IA:** generar guías/etiquetas, avisar al cliente, checklist de empaque, registro de incidencias.
- **Humano:** empacar, llevar a paquetería, revisar calidad física.
- **Herramientas:** paqueterías (Estafeta/FedEx/local), inventario Shopify, checklist de empaque.
- **Diario:** empacar y enviar pedidos del día · confirmar entregas · resolver incidencias.
- **Semanal:** revisar tiempos de envío · mermas/garantías.
- **Métricas:** % pedidos a tiempo, errores de empaque, costo de envío real, devoluciones.
- **Contratar:** encargado de empaque/almacén cuando los pedidos rebasen ~10-15/día (Fase 2-3).

### 6) FINANZAS  · prioridad ALTA
*(fusiona: Finanzas + Contabilidad)*
- **Objetivo:** saber si ganamos dinero de verdad y decidir con números.
- **Hace:** utilidad real por producto, flujo de caja, registro de ingresos/gastos, precios/márgenes, reinversión.
- **IA:** calcular utilidad real por SKU, tablero de caja, alertas (margen bajo, gasto alto), proyecciones.
- **Humano:** aprobar compras/inversiones, pagos, impuestos.
- **Herramientas:** hoja de finanzas, datos Shopify/Meta, fórmula de utilidad real.
- **Diario:** registrar ingresos/gastos · ver caja.
- **Semanal:** utilidad por producto · cuánto reinvertir vs guardar.
- **Métricas:** utilidad neta, margen %, flujo de caja, dinero en banco, ROI de publicidad.
- **Contratar:** contador (externo) desde ya para impuestos; analista financiero en Fase 4.

### 7) BUUMIA OS · IA / TECNOLOGÍA  · prioridad ALTA
*(fusiona: IA/Automatización + Tecnología/Panel)*
- **Objetivo:** construir y mantener el sistema que automatiza y conecta todo.
- **Hace:** panel BUUMIA OS, automatizaciones, motores (contenido/anuncios), integraciones (Shopify API, Meta API), datos/métricas, plantillas.
- **IA/Claude:** construye scripts, motores y paneles; conecta APIs; arma reportes.
- **Humano:** decidir qué automatizar, dar accesos/llaves, aprobar.
- **Herramientas:** Claude Code, Python, APIs (Shopify, Meta, Gemini, Replicate), Notion.
- **Métricas:** # tareas automatizadas, tiempo ahorrado, errores evitados.
- **Nota:** esta área es la que hace posible "el fundador no opera todo".

### (8) PERSONAS / RH — **dormida** (se activa al contratar)
- Cuando se contrate, aquí van: perfiles, manuales de puesto, capacitación (con los checklists de cada área), evaluación. Hoy no se necesita.

---

## 📦 Sistema de Producto (todo producto pasa por aquí)
**Pipeline:** idea → investigación → comparar proveedores → muestra → validar calidad → costo real → precio menudeo → precio mayoreo → ficha técnica → fotos → videos → anuncios → publicar → prueba de venta → medir → **decisión**.
**Gates (no avanza si falla):** margen mínimo definido · calidad aprobada · costo confirmado.
**Decisiones:** escalar · mejorar · pausar · liquidar · reordenar · cambiar proveedor · solo mayoreo · solo menudeo · en paquete · eliminar.
**Ficha por producto (carpeta `buumia-catalogo/<sku>/`):** ficha técnica · fotos limpias · imágenes publicitarias · videos/guiones · descripción tienda · contenido redes · precios (menudeo/mayoreo) · proveedor · costo/margen · inventario · estado · métricas.

## 🎬 Sistema de Contenido
- Por producto: fotos pro · imágenes publicitarias · reels/verticales · carruseles · guiones · copies · anuncios · demostraciones.
- **Talento virtual (personajes IA):** señora instaladora · modelo joven · chico técnico · persona mayor (fácil de usar) · comerciante de mayoreo · familia en casa. Son el "elenco" reutilizable de marketing.
- Todo sale de **plantillas oficiales** (mismo estilo siempre) y pasa por la **rúbrica** antes de publicar.

## 🛒 Sistema de Ventas
- **Tipos de producto:** solo mayoreo · solo menudeo · ambos · gancho · premium · temporada · recompra.
- **Canales:** tienda Shopify · WhatsApp · redes · mayoreo directo.
- **Flujo:** captar → cotizar/responder → cerrar → postventa → recompra. Garantías y reseñas incluidas.

## 🚚 Sistema de Operación
Recibir pedido → confirmar pago → separar inventario → empacar (checklist) → enviar → rastrear/entregar → resolver problemas/garantías → pedir reseña → medir satisfacción → disparar recompra.

## 💰 Sistema Financiero (regla de oro)
**Utilidad real = Precio de venta − (costo producto + envío + empaque + publicidad + comisiones + merma).**
Reglas de decisión:
- Margen sano y rota rápido → **escalar / reinvertir**.
- Margen bajo pero rota → **subir precio o vender en paquete**.
- No rota → **pausar/liquidar**, no recomprar.
- Reinversión: prioridad a productos ganadores; siempre dejar colchón de caja.

---

## 🚀 Plan de implementación por fases

**FASE 1 — Cimientos (ahora · 1-10 productos)**
- Cerrar Brand Kit + logo oficial + **plantilla de anuncios** (motor de contenido).
- Subir el 1er producto (foco 60W) con ficha + fotos + anuncios listos.
- Configurar Shopify (pagos transferencia + envío por cliente) y publicar tienda mayoreo.
- Activar publicación IG/FB por API. Panel BUUMIA OS con tareas/checklists.
- **Todo lo corre Fundador + IA.**

**FASE 2 — Tracción (10-50 productos · primeras ventas estables)**
- Bot de atención/WhatsApp. Automatizar fichas/anuncios por plantilla.
- **Primera contratación:** atención al cliente o empaque (lo que más sature).
- Métricas automáticas por producto.

**FASE 3 — Estructura (50-150 productos)**
- Responsables por área (Producto, Marketing, Ventas, Operaciones).
- Manuales de puesto (desde los checklists). RH se activa.
- Más automatización; el fundador dirige, no opera.

**FASE 4 — Escala (200-300+ · más canales/ciudades)**
- Playbooks replicables, expansión, analista financiero, posibles bodega/tienda física (cuando los números lo paguen).

## 🤖 Qué se automatiza YA vs DESPUÉS
- **Ya:** fichas técnicas, recorte de fotos, anuncios por plantilla, publicación IG/FB, reportes/métricas básicas, respuestas frecuentes.
- **Después:** bot de ventas completo, cotizador de mayoreo, guías de envío, recompra automática, reglas de reinversión, generación de talento virtual a escala.

## 🏗️ Cuándo contratar (disparadores)
- **Atención/Ventas:** cuando los mensajes rebasen al fundador (Fase 2).
- **Empaque/Almacén:** ~10-15 pedidos/día (Fase 2-3).
- **Contenido:** cuando haya >20-30 productos que mantener (Fase 3).
- **Comprador/Abasto:** múltiples proveedores/importaciones activas (Fase 3).
- **Contador externo:** desde ya (impuestos).

---

## 🔄 v2 — Departamentos antiguos integrados (conservar / mejorar / rehacer)
| Antiguo | → Nueva área | Decisión |
|---|---|---|
| **Gerencia** | Dirección/CEO | **MEJORAR** → tablero + reporte ejecutivo semanal automático (todas las métricas que pediste). |
| **Ventas** | Ventas & Clientes | **MEJORAR** → reporte CRM + tablero (clientes nuevos/recurrentes/inactivos, embudo, seguimiento, metas). |
| **Servicio al cliente** | Ventas & Clientes (Atención) | **CONSERVAR** → flujo **ManyChat → n8n** (responde auto / escala / registra / reporte semanal). |
| **Operaciones** | Operaciones & Logística | **CONSERVAR casi todo** → inventario (SKU, ubicación, min/max, cobertura), **fórmula de resurtido**, recepción, picking/empaque con escaneo, envíos, **sync web = stock real**. Está muy bien hecho. |
| **Finanzas y contabilidad** | Finanzas | **CONSERVAR el ritmo "revisión solo lunes"** + las 5 decisiones de la semana. |
| **Marketing** | Marketing & Contenido | **REHACER** → de manual (Canva, edición a mano) a **100% IA** (motor de contenido masivo). |
→ Tu estructura vieja **encaja en las 7 áreas**; conservo lo operativo (es oro) y modernizo lo manual.

## 🧭 El gran cambio: de "Panel del CEO" → "Centro de Mando BUUMIA OS"
- El Panel del CEO **no se cancela: evoluciona.** Antes = lista de TODO lo que hace el fundador. Ahora = **cockpit** donde cada **departamento (jefe IA)** trabaja solo entre semana y te deja **solo las decisiones de CEO**.
- **Ritmo (tu revisión de lunes, pero para toda la empresa):** entre semana la IA opera y genera reportes; **el lunes = junta de dirección**: revisas el tablero de cada departamento (🟢🟡🔴) y tomas las **5 decisiones de la semana** → 📦 compra · 🚀 ads · 📉 pausa · 🎁 oferta · 📈 escalar.
- El fundador pasa de **operador** a **director que revisa departamentos**.

## 🏪 Modelo franquicia (KFC/McDonald's) aplicado a PRODUCTOS
Cada producto nuevo entra por una **línea de producción estandarizada** (como abrir una sucursal ya lista):
`llega producto → sesión de fotos → recorte/edición (IA) → ficha técnica (IA) → paquete de marketing masivo (imágenes, anuncios, videos, copys, campañas por público: niños / papás / general / mayoreo) → publicar en sintonía (tienda + redes + historias) → medir → decisión.`
Así, **100 productos nuevos en agosto para Navidad = 100 "sucursales" listas para vender**, sin caos. Escalable a 300, 500+.

## 🛠️ Stack tecnológico (AI-first — SIN n8n/ManyChat salvo que sea necesario)
- **Cerebro:** **Claude (yo)** ejecuta cada módulo: estrategia, contenido, fichas, reportes, soporte a decisiones. + **Python** para conectar/orquestar (no se necesita n8n).
- **Datos:** Shopify (ventas/inventario/pedidos) y Meta (ads/redes), leídos directo por **API**.
- **Motor de contenido IA:** Gemini (imagen), Replicate/Kling (video), ElevenLabs (voz), plantillas — ya construido.
- **Publicación/ads:** Meta API (IG/FB) — ya conectado.
- **Atención/chat:** chatbot con IA (se define la herramienta cuando toque; ManyChat es opcional, NO obligatorio).
- **Interfaz:** Centro de Mando BUUMIA OS (`buumia-os/centro-de-mando.html`).
- **Nota:** los "departamentos antiguos" del fundador YA NO se usan; fueron solo contexto. BUUMIA OS es nuevo, AI-first.

## ⚠️ Realidad de datos (honesto)
Los reportes (Gerencia, Ventas, Finanzas) **necesitan datos reales** y hoy hay **0 ventas / 0 productos publicados**. Por eso ahora construimos el **SISTEMA** (plantillas de reporte + automatización); se llenan **solos** cuando empiece a vender. El primer paso real sigue siendo **Fase 1: publicar el primer producto y prender el flujo de datos.**
