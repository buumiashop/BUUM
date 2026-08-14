# Fuentes de verdad — jerarquía y ubicación

> Documento de **mapa**, no de doctrina: solo dice QUÉ sistema es autoridad para
> cada tipo de información y DÓNDE vive. Las reglas viven en sus documentos.

| Tipo de información | Autoridad (fuente de verdad) | Ubicación |
|---|---|---|
| Verdad institucional (visión, reglas, doctrina, procesos, aprendizaje aprobado) | **KB en git** | `KB/` (raíz: `ARRANQUE.md`, `ESTADO-ACTUAL.md`) |
| Gobierno y decisiones de arquitectura | `KB/00-gobierno/` (CONSTITUCION, VISION-2030, ADRs) | `KB/00-gobierno/` |
| Calidad creativa (doctrina) | `KB/03-operacion/JUECES-DE-CALIDAD.md`; su código es `marketing/filtros_calidad.py` (manda el doc) | KB + `marketing/` |
| Memoria de conversación del agente | **SQLite** (no modifica la KB) | `/var/lib/buum/db/agente.db` (servidor) |
| Estado operativo y métricas | archivos de datos (cuando existan colectores, FASE 13D) | `datos/` (repo) y `/var/lib/buum/data/` (servidor) |
| Aprendizaje | `KB/05-aprendizaje/` — entra SOLO por commit aprobado por el Fundador | `KB/05-aprendizaje/` |
| Dirección (foco actual, backlog, veredictos del Fundador) | `KB/08-direccion/` (BACKLOG, DECISIONES; formales → `adr/`) | `KB/08-direccion/` |
| Secretos | archivos env del servidor (nunca en git, nunca en KB) | `/etc/buum/` (admin: `buum.env` · agente: `agent.env`) |
| Código | **git** (GitHub privado `buumiashop/BUUM`) | `C:\Users\playg\BUUM` (trabajo) ↔ `/opt/buum` (producción) |

## Centro de Mando — servidor canónico
- **Canónico:** `os/chat_servidor.py` en el droplet (127.0.0.1:8131, acceso por túnel SSH). Es el único con Chat BUUM real.
- Espejo de desarrollo: `os/servidor_panel.py` + vbs en el PC (puerto 8130). Si difieren, manda el del droplet.

## ⚠️ Advertencia temporal
Los números del Centro de Mando (tareas, juego, conexiones, calendario) son
**maqueta/localStorage**, NO datos reales del negocio, hasta que la FASE 13D
conecte colectores. No tomar decisiones con esos números.
