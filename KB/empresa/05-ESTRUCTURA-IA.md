# 05 — ESTRUCTURA DE EMPRESA + LA IA COMO CEREBRO

> Cómo se organiza BUUM y qué hace exactamente la IA en cada área. Evolución del BUUM OS
> existente (`buumia-os/`), rediseñado para la empresa de novedades. Meta: **99% IA / 1% dueño**.

---

## 1. Organigrama (7 áreas + RH dormida)

```
                    DIRECCIÓN
             Dueño (1%) + IA CEO (99%)
                        │
  ┌─────────┬──────────┼──────────┬──────────┬──────────┐
PRODUCTO   MARKETING   VENTAS &   OPERACIONES FINANZAS  TECNOLOGÍA
& SOURCING             ATENCIÓN   & ALMACÉN
IA radar   IA pipeline IA chat +  Dueño →     IA libros  IA (Claude)
+ dueño    (ya hecho)  WhatsApp   ayudante →  + contador + servidor
elige                  del dueño  almacenistas (f3+)     local/nube
                                              [RH: dormida hasta F3]
```

## 2. Quién hace qué (la división 99/1)

| Área | La IA hace (99%) | El dueño hace (1%) |
|---|---|---|
| **Dirección** | Reportes, semáforos, planes A/B/C, análisis experto | Decide y autoriza |
| **Producto** | Radar semanal, score, negociación redactada, checklist de pedido | Elige 3 de 10, prueba muestras, PAGA |
| **Marketing** | Todo: crea, publica, mide, aprende (pipeline ya operando) | Da gusto/no-gusto (se registra en la skill) |
| **Ventas** | Contesta chat web, borradores de WhatsApp, cotizaciones, links de pago | Cierra clientes grandes, entrega local |
| **Operaciones** | Inventario, punto de reorden, guías, tabla de envíos | Empaca y entrega (hasta tener ayudante) |
| **Finanzas** | Caja diaria, 70/20/10, proyecciones, expediente de crédito | Autoriza pagos, firma |
| **Tecnología** | Se construye y mantiene sola (web, panel, integraciones) | Nada |

## 3. El patrón de decisión (la regla de oro del 99/1)

**La IA nunca pregunta "¿qué hacemos?" — presenta opciones listas para autorizar:**

> *"Toca reordenar. Analicé ventas, caja y tránsito. Opción A: 6,000 pzas, $228k, llega en 90
> días, caja queda en $45k. Opción B: 4,500 pzas… Opción C: … Recomiendo A por X. ¿Autorizas?"*

Formato fijo de toda propuesta: **contexto (2 líneas) → opciones A/B/C con números → recomendación
→ qué pasa si no se decide hoy**. El dueño responde con una palabra.

### Niveles de autonomía por monto (se amplían con la confianza)

| Nivel | Monto | Qué puede hacer la IA sola |
|---|---|---|
| 🟢 Libre | $0 (contenido, mensajes, guías, análisis) | Ejecuta y reporta después |
| 🟡 Aviso | Gasto ya presupuestado (ads del mes, APIs) | Ejecuta y avisa el mismo día |
| 🟠 Aprobación | $500–5,000 no presupuestado | Propone, dueño aprueba por WhatsApp |
| 🔴 Decisión | >$5,000, pedidos a China, contratos, contrataciones | A/B/C formal + autorización expresa |

## 4. Rutinas automáticas (el pulso de la empresa)

| Rutina | Frecuencia | Qué hace |
|---|---|---|
| **Reporte del día** | Diario 8 am | Ventas ayer, caja, stock, mensajes pendientes, semáforo |
| **Contenido del día** | Diario | 1 pieza publicada FB/IG (pipeline existente `buumia-marketing`) |
| **Radar de tendencias** | Lunes | 10 candidatos con score → dueño elige |
| **Cierre semanal** | Domingo | Números de la semana vs plan, inventario cuadrado, plan de la semana |
| **Cierre de mes** | Día 1 | Utilidad, aplicación 70/20/10, avance de fase, foto del roadmap |
| **Vigía de reorden** | Continuo | Avisa al llegar a punto de reorden de cada producto |

Infraestructura: servidor local siempre encendido (`http://127.0.0.1:8130`) + droplet
DigitalOcean (`165.227.181.176`) para rutinas en la nube. El centro de mando del BUUM OS
(`buumia-os/centro-de-mando.html`) evoluciona para mostrar: caja, stock, fase actual y la
**bandeja de autorizaciones** (lo único que el dueño debe tocar).

## 5. Plan de integraciones (qué conectar, en qué orden y para qué)

Ya conectado hoy: **Gemini, Replicate (Kling/MusicGen), Meta FB+IG, Shopify (borrador), Claude.**

| # | Integración | Fase | Para qué | Cómo opera la IA |
|---|---|---|---|---|
| 1 | **Mercado Pago API** | F0 | Links de pago, webhooks de cobro | Genera link por pedido, concilia pagos → caja automática |
| 2 | **Skydropx API** | F1 | Guías de envío | Cotiza, compra guía, manda tracking al cliente |
| 3 | **WhatsApp Business API** | F1–2 | Atención y cobro en el canal #1 de México | Borradores → luego respuesta directa con reglas |
| 4 | **Mercado Libre API** | F2 | Publicar, precios, preguntas | Publica catálogo, contesta preguntas <5 min, ajusta stock |
| 5 | **Meta Ads API** (ampliar la conexión actual) | F2 | Campañas pagadas | Crea/pausa anuncios según costo por venta; presupuesto 🟡 |
| 6 | **TikTok Shop + Ads** | F3 | El canal de novedades por excelencia | Publica producto + video, ads de catálogo |
| 7 | **Google Ads** | F3 | Búsquedas "focos por mayoreo", Shopping | Campañas de búsqueda con presupuesto 🟡 |
| 8 | **Amazon MX (SP-API)** | F4 | Marketplace grande + FBA | Catálogo y reposición FBA |
| 9 | **WMS propio (BUUM OS)** | F5 | Código de barras, picking, multi-ubicación | La IA lo construye sobre el panel existente |
| 10 | **Banca/SAT (lectura)** | F3+ | Conciliación y facturas automáticas | Lee estados de cuenta, prepara facturación al contador |

Regla de integración: **una a la vez, y no se conecta la siguiente hasta que la anterior opere
sola 2 semanas sin fallas.**

## 6. Qué hereda del BUUM OS actual (no se tira nada)

- `buumia-os/` (manuales, organigrama, centro de mando) → se convierte en el panel de ESTA empresa.
- Skills `buumia-marketing` + `buumia-anuncios-ganadores` → siguen siendo el departamento de marketing.
- Gatito vendedor IA → atención de la web nueva (pendiente subirlo a la nube, ya anotado).
- Tienda Shopify (tema 190418157890) → **en pausa como referencia**; la web propia nueva es la
  cara de la empresa. Si el menudeo escala fuerte (F2–3), Shopify se reactiva como carrito.
