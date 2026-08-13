# MANUAL TÉCNICO PARA LA IA (Claude / cualquier modelo que continúe)

> Lee esto primero. Aquí está cómo está montado TODO y cómo ejecutar cada tarea de la empresa
> BUUM. Mantenlo actualizado: cada cambio estructural se refleja aquí ANTES de cerrar la sesión.
> Última actualización: 2026-07-10 (Fable 5, diseño inicial de la empresa).

---

## 1. Mapa del proyecto

| Cosa | Dónde |
|---|---|
| **Empresa (este diseño)** | `empresa-buum/` — docs 01–06, manuales, `plan.html`, `web/` |
| Memoria persistente | `C:\Users\playg\.claude\projects\C--Users-playg-OneDrive-Documents-CLAUDE-1-EJ\memory\MEMORY.md` |
| BUUM OS (panel/centro de mando) | `buumia-os/` (servidor `servidor_panel.py`, panel `centro-de-mando.html`) |
| Marca (logo, colores, manual) | `buumia-catalogo/marca/` (`logo-buum.png`, `logo-buum-horizontal.png`, `BRAND-KIT.md`) |
| Fotos del foco 60W (fondo limpio) | `buumia-catalogo/foco-led-60w/fotos/60w-*-clean.png` |
| Ficha técnica foco | `buumia-catalogo/foco-led-60w/ficha-tecnica.md` |
| Tienda Shopify (PAUSADA, referencia) | `buumia-tienda/tienda-PRO.html` → tema borrador `190418157890` en `j0hshz-nm.myshopify.com` |
| Marketing IA (skills) | `buumia-marketing`, `buumia-anuncios-ganadores` (invocar por Skill tool) |

## 2. Llaves y servicios (YA conectados — nunca volver a pedirlos)

| Servicio | Credencial | Uso |
|---|---|---|
| Gemini | `aurora-cafe/claves.local.txt` → `GEMINI_API_KEY` | Imágenes (~4¢) y texto |
| Replicate | conectado (ver skills marketing) | Kling video, MusicGen |
| Meta | conectado — FB "BUUM" + IG `@buum.ia` | Publicación |
| Shopify | `buumia-shopify.env` (`shpat_`, `shptka_`) | Solo si se reactiva el carrito |
| Python | `C:\Users\playg\Tools\miniconda\python.exe` | Scripts |
| ffmpeg | en PATH (`C:\Users\playg\Tools\`) | Video |
| Servidor local | `http://127.0.0.1:8130` = raíz del repo, SIEMPRE encendido (vbs en Inicio). **No usar preview_start.** | Previews |
| Nube | droplet DigitalOcean `165.227.181.176`, SSH `~/.ssh/buum_os` | Rutinas cloud |

## 3. Reglas de trabajo con el dueño (obligatorias)

1. **Español (México), directo y con evidencia.**
2. **Muy visual:** todo entregable se enseña como preview — imagen inline o página en navegador
   EXTERNO: `Start-Process "http://127.0.0.1:8130/ruta"`.
3. **Economizar créditos:** juntar cambios y aplicarlos en UNA tanda; mockup barato de Gemini
   antes de rehacer visuales; 1 solo preview/push por tanda.
4. **Decisiones = formato A/B/C con números + recomendación.** Niveles de autonomía por monto
   (ver [05-ESTRUCTURA-IA.md](05-ESTRUCTURA-IA.md) §3): >$5,000, pedidos a China, contratos → autorización expresa.
5. Reglas de marca/venta: solo stock real, sin garantías infladas, sin marca del proveedor,
   nunca "barato/oferta", precio claro, honestidad total al cliente.
6. **No puedes:** colocar pedidos en Alibaba, mover dinero, firmar. **Sí puedes:** redactar la
   orden/mensajes, comparar, preparar todo para que el dueño pague en 5 minutos.

## 4. La web propia

- Código: `empresa-buum/web/index.html` (autocontenida: CSS/JS inline, imágenes por ruta relativa
  a `buumia-catalogo/` y `buumia-tienda/`).
- Preview local: `http://127.0.0.1:8130/empresa-buum/web/index.html`.
- Producción (pendiente F0): dominio propio + servir estático desde el droplet (nginx) o GitHub
  Pages. Checkout actual: WhatsApp con mensaje precargado + link de Mercado Pago (generar por pedido).
- Editar = editar el HTML directo. Mantener: 1 producto = 1 verdad (precios de
  [02-FINANZAS.md](02-FINANZAS.md)); nada de productos sin stock.

## 5. Tareas recurrentes (cómo se ejecuta cada una)

| Tarea | Cómo |
|---|---|
| Contenido diario | Invocar skill `buumia-marketing` (pipeline y aprendizaje están ahí) |
| Anuncio nuevo con estrategia | Invocar `buumia-anuncios-ganadores` antes de crear |
| Radar de tendencias (lunes) | WebSearch: TikTok Creative Center MX, Temu/Amazon movers, ML tendencias, Google Trends → tabla 10 candidatos con score BUUM (§5 de [01-ESTRATEGIA.md](01-ESTRATEGIA.md)) |
| Reporte diario / cierre semanal | Datos del panel BUUM OS (`buumia-os/datos.js`, `gen_datos.py`) + formato semáforo |
| Guías de envío | Hoy: cotizar en skydropx.com manualmente y dejar link al dueño. F1: integrar API |
| Links de cobro | Hoy: dueño los genera en app Mercado Pago; la IA redacta el mensaje. F0–1: API |
| Pedido a China | Redactar orden completa (specs, cantidad, DDP, NOM por escrito, Trade Assurance) → checklist de pago para el dueño → registrar fecha y ETA en memoria |

## 6. Estado actual y pendientes vivos (actualizar SIEMPRE aquí)

**Hecho (2026-07-10):** diseño completo de la empresa (docs 01–06 + manuales + plan.html + web v1).
**Decisiones del dueño registradas:** lote 3,000 ya pagado/apartado; pedido AÚN NO colocado;
persona física con RFC; almacén = casa/cochera; ciudad PENDIENTE de confirmar.

**Pendientes (en orden):**
1. Dueño confirma ciudad → precotizar envíos y afinar costos de bodega/terreno de su zona.
2. Colocar el pedido de 3,000 focos (la IA redacta la orden; dueño paga en Alibaba).
3. Comprar dominio + subir la web al droplet.
4. Alta Mercado Pago + plantillas de cobro.
5. Producir las 30 piezas de contenido de Fase 0.
6. Armar la cartera de 50 contactos con el dueño.
7. Heredados: gatito IA a la nube ([[gatito-cloud-pendiente]]), sección nueva del BUUM OS que el
   dueño olvidó (preguntar cuando se acuerde).
