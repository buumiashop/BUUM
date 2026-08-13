# Migración a la BUUM Knowledge Base

> Qué conocimiento traemos del proyecto anterior y dónde va cada cosa. Es curatorial, no bulk-copy: solo migra **conocimiento definitivo**.

## Principios de migración

1. **Solo conocimiento definitivo.** No se migran chats, borradores, experimentos, código, temas de tienda, videos ni activos de herramienta.
2. **Distinguir conocimiento durable de diseño-de-prototipo.** BUUM v1 ("BUUMIA") fue investigación y prototipo. Su *conocimiento durable* (ADN, producto, mercado) migra; su *diseño de sistema* (OS, procesos, manuales de rol) queda **superado por el nuevo BIS** y va a archivo, no a la operación.
3. **Regla de graduación.** Lo que aún está en validación en el BIS no se migra hasta cerrarse; entonces gradúa.
4. **Nada se borra.** Lo superado se registra en `99-archivo/` para la historia.

## Leyenda de estado

✅ Migrado · ⏳ Migrar ahora (definitivo, listo) · 🎓 Graduar al validar · 📦 Archivar (superado) · 🚫 No migrar (herramienta/activo/chat)

---

## A · Documentos producidos por el BIS (espacio de trabajo → KB)

Origen: `C:/Users/playg/BUUM Intelligence System (BIS)/`

| Origen | Destino en KB | Estado |
|--------|---------------|--------|
| `00-constitucion/CONSTITUCION.md` | `00-gobierno/CONSTITUCION.md` | ✅ Migrado |
| `docs/adr/ADR-0001…0011.md` | `00-gobierno/adr/` | ⏳ Migrar ahora (gobernanza permanente) |
| `04-departamentos/FORMATO-ENCARGO-DE-PRODUCTO.md` | `03-operacion/` | ⏳ Migrar ahora (contrato aprobado) |
| `04-departamentos/FORMATO-PROPUESTA-DE-CAMPANA.md` | `03-operacion/` | ⏳ Migrar ahora (contrato aprobado) |
| `01-conocimiento/SISTEMA-DE-CONOCIMIENTO.md` | `02-arquitectura/` | 🎓 Graduar al validar (M1) |
| `02-arquitectura/ARQUITECTURA-CONCEPTUAL.md` | `02-arquitectura/` | 🎓 Graduar al validar (M2) |
| `03-sistema-operativo/SISTEMA-OPERATIVO.md` | `02-arquitectura/` | 🎓 Graduar al validar (M3) |
| `04-departamentos/DIRECTOR-DE-MARKETING-MVP.md` | `03-operacion/` | 🎓 Graduar al validar (M4) |
| `PLAN-MAESTRO.md`, `validacion/*`, `docs/auditorias/*` | — | 🚫 No migrar (documentos vivos de proyecto/experimento; viven en el espacio de trabajo) |

## B · Conocimiento del prototipo BUUM v1 ("BUUMIA")

Origen: `C:/Users/playg/OneDrive/Documents/CLAUDE 1 EJ/`

### Identidad / ADN → `01-identidad/`

| Origen | Destino | Estado |
|--------|---------|--------|
| `buumia-catalogo/marca/BRAND-KIT.md` | consolidado en `01-identidad/ADN-DE-BUUM.md` | ✅ Migrado (destilado) |
| `buumia-catalogo/marca/MASCOTA-BUUM.md` | consolidado en `ADN-DE-BUUM.md` | ✅ Migrado (destilado) |
| `buumia-os/nucleo/ADN-BUUM.md` | consolidado en `ADN-DE-BUUM.md` | ✅ Migrado (destilado) |
| `buumia-os/IDENTIDAD-SOCIAL.md` | consolidado en `ADN-DE-BUUM.md` | ✅ Migrado (destilado) |
| `buumia-catalogo/marca/manual-p1…p8.png` | `01-identidad/manual/` (activos) | ⏳ Migrar ahora (imágenes del manual de marca) |

### Producto / Negocio → `04-negocio/`

| Origen | Destino | Estado |
|--------|---------|--------|
| `buumia-catalogo/foco-led-60w/ficha-tecnica.md` | `04-negocio/productos/FOCO-LED-60W.md` | ✅ Migrado (⚠️ verificar vigencia de specs con Fundador) |
| `buumia-catalogo/foco-led-60w/tienda-shopify.md` | `04-negocio/productos/` | ⏳ Migrar (texto de producto; revisar vigencia) |
| `buumia-os/ESTRATEGIA.md` · `empresa-buum/01-ESTRATEGIA.md` | `04-negocio/` | ⏳ Migrar (revisar vigencia; consolidar en una sola estrategia) |
| `buumia-os/CEO-DOCTRINA-CRECIMIENTO.md` | `04-negocio/` | ⏳ Migrar (doctrina de crecimiento; revisar vigencia) |
| `empresa-buum/02-FINANZAS.md` · `04-ROADMAP-FASES.md` | `04-negocio/` | ⏳ Migrar (hechos/plan financiero; revisar vigencia) |

### Conocimiento de marketing → `05-aprendizaje/`

| Origen | Destino | Estado |
|--------|---------|--------|
| `buumia-catalogo/RUBRICA-MARKETING.md` | `05-aprendizaje/` | ⏳ Migrar (rúbrica = semilla del libro de jugadas) |
| `buumia-os/PROCESO-ANUNCIOS.md` · `ESTRATEGIA-CONTENIDO.md` · `empresa-buum/06-MARKETING.md` | `05-aprendizaje/` | ⏳ Migrar el *conocimiento* (qué funciona); el *proceso* queda superado por el Director de Marketing MVP |

### Superado por el nuevo BIS → `99-archivo/` (historia, no operación)

| Origen | Motivo |
|--------|--------|
| `buumia-os/BUUMIA-OS.md`, `GUIA-OS-EOS.md`, `MANUAL-DE-OPERACIONES.md`, `PROCESO-NUEVO-PRODUCTO.md`, `PROCESO-PRODUCTO.md`, `EQUIPO.md` | 📦 El diseño de OS/procesos/equipo del prototipo queda reemplazado por el BIS (Capas 2-4). |
| `empresa-buum/00-PLANO-ARQUITECTONICO.md`, `01-REVISION-ARQUITECTURA.md`, `03-OPERACIONES.md`, `05-ESTRUCTURA-IA.md` | 📦 Arquitectura del prototipo, superada por la Arquitectura Conceptual del BIS. |
| `empresa-buum/MANUAL-DUENO.md`, `MANUAL-IA.md`, `ANCLA-CHATGPT.md`, `buumia-os/MANUAL-CEO.md` | 📦 Los roles (Fundador, CEO-IA, ChatGPT) ahora los define la Constitución (Art. 14-15). Se archivan; su intención vive en el gobierno. |
| `BRIEF-EMPRESA-FABLE5.md`, `buumia-catalogo/README.md`, `buumia-catalogo/leer_manual.py` | 📦 Briefs y utilidades del prototipo. |

### No migrar → 🚫

| Origen | Motivo |
|--------|--------|
| `buumia-theme*/`, `buumia-tienda/`, `buumia-fondos/`, `buumia-productos/`, `buumia-sistema/`, `buumia-director/`, `buumia-ceo/` | Código, temas de tienda y activos de herramienta. No es conocimiento definitivo. |
| `sweetlab/`, `kenchys-video/`, `consultoria_video/`, `aurora-cafe/`, `vivo/`, `video_*` | Proyectos y experimentos ajenos o de práctica. |

---

## Auditoría de completitud (barrido total, 15 jul)

Se revisó **todo** el proyecto anterior, no una muestra. Clasificación en tres categorías. (El barrido corrigió una omisión importante: un cuerpo entero de conocimiento de marketing aprendido que estaba fuera.)

### ✅ Ya migrado (conocimiento definitivo, dentro de la KB)

| Conocimiento | Origen | Destino |
|--------------|--------|---------|
| Constitución | BIS | `00-gobierno/CONSTITUCION.md` |
| ADN (marca, mascota, colores, tipografía, filosofía de venta, vibra social) | `marca/BRAND-KIT`, `MASCOTA-BUUM`, `nucleo/ADN-BUUM`, `IDENTIDAD-SOCIAL` | `01-identidad/ADN-DE-BUUM.md` |
| Hechos del foco LED 60W | `foco-led-60w/ficha-tecnica.md` | `04-negocio/productos/FOCO-LED-60W.md` |
| Libro de jugadas de marketing (receta WOW, 3 capas, estilos ganadores, gustos del dueño, estudio de luz) | `BIBLIA_BUUMIA`, `DIRECCION-CREATIVA`, `DIRECCION-VIDEO`, `RUBRICA-MARKETING`, `PROCESO-ANUNCIOS`, `ESTRATEGIA-CONTENIDO` | `05-aprendizaje/LIBRO-DE-JUGADAS-MARKETING.md` |

### 🟡 Falta migrar — RESUELTO (15 jul, decisión del Fundador)

Ninguno pendiente.
- **Activos de marca y producto** → ✅ copiados: `01-identidad/manual/` (manual de marca p1-p8 + frame oficial del gatito) y `04-negocio/productos/fotos/` (fotos del foco). La KB es autosuficiente.
- **Estrategia y finanzas del prototipo** → 🔴 **referencia histórica, no definitiva.** La estrategia oficial se construirá sobre el nuevo BIS. Quedan en 99-archivo.
- **Ficha Shopify y guía web** → 🔴 referencia; su conocimiento durable ya vive en el ADN, el libro de jugadas o la ficha del foco.

### 🔴 No debe migrarse (pertenece al prototipo / es herramienta)

| Qué | Motivo |
|-----|--------|
| Diseño de sistema del prototipo: `buumia-os/BUUMIA-OS`, `GUIA-OS-EOS`, `MANUAL-DE-OPERACIONES`, `PROCESO-NUEVO-PRODUCTO`, `PROCESO-PRODUCTO`, `EQUIPO`, `DESPLIEGUE-NUBE`; `buumia-ceo/PLAN_MAESTRO`; `empresa-buum/00-PLANO`, `01-REVISION`, `03-OPERACIONES`, `05-ESTRUCTURA-IA` | Superado por el nuevo BIS. → 99-archivo. |
| Manuales de rol: `empresa-buum/MANUAL-DUENO`, `MANUAL-IA`, `ANCLA-CHATGPT`, `buumia-os/MANUAL-CEO` | Los roles ahora los define la Constitución (Art. 14-15). |
| Briefs del prototipo: `BRIEF-EMPRESA-FABLE5`, `FABLE5-KICKOFF`, `buumia-catalogo/README`, `LEEME`, `calendario` del prototipo | Documentos de arranque del prototipo, ya cumplidos. |
| Herramientas y activos de producción: `buumia-sistema/` (scripts, mp4), `buumia-theme*/` (temas Shopify), `.agents/skills/`, `.claude/skills/`, `buumia-productos/` (imágenes generadas) | Código/plantillas/activos, no conocimiento definitivo. |
| Proyectos ajenos: `sweetlab/`, `kenchys-video/`, `consultoria_video/`, `aurora-cafe/`, `vivo/`, `video_*` | No son BUUM. |

## Documentos del BIS (mecanismo separado: graduación)

No corren riesgo de perderse (viven en el repo). Graduarán a la KB al validarse: arquitectura (M1-M3) → `02-arquitectura/`; contratos Encargo/Propuesta y Director de Marketing (M4) → `03-operacion/`; ADRs → `00-gobierno/adr/`. `PLAN-MAESTRO`, `validacion/*` y auditorías permanecen en el espacio de trabajo.

## Veredicto de la migración

**✅ MIGRACIÓN OFICIALMENTE TERMINADA — 15 de julio de 2026.**

Todo el conocimiento definitivo de BUUM vive en la Knowledge Base; los activos de marca y producto están copiados (KB autosuficiente); el prototipo BUUM v1 queda como **referencia histórica**. La estrategia y finanzas del prototipo **no se consideran definitivas** (decisión del Fundador): son referencia; la estrategia oficial se construirá sobre el nuevo BIS con la operación.

A partir de aquí, la empresa depende **únicamente de documentos oficiales de la KB y nunca del historial de un chat.**
