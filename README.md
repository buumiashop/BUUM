# BUUM — Sistema Operativo de la empresa
> Empresa mexicana de iluminación operada con IA. Esta carpeta es la instalación LIMPIA y VIVA del sistema.

## Qué es esto
El cerebro y las herramientas de BUUM: la memoria institucional (KB), la tienda, el motor de
marketing, los activos oficiales y (próximamente) el agente que vive 24/7 en el servidor.

## Estructura
| Carpeta | Qué vive aquí |
|---|---|
| `KB/` | **Knowledge Base** — la única fuente de verdad: reglas, procesos, productos, escuela de anuncios, jueces, decisiones |
| `agente/` | El agente BUUM (core, herramientas, políticas, trabajos programados, permisos) — en construcción |
| `os/` | **Centro de Mando** web (paneles, calendario, y próximamente la bandeja de chat) |
| `tienda/` | Tema Shopify vivo (`tema-vivo/`) y scripts de tienda |
| `marketing/` | Motor creativo: generación, composición, filtros de calidad, publicación en redes |
| `activos/` | Imágenes oficiales: `marca/` (logo, fuentes) y `productos/<REF>/` |
| `datos/` | Tareas, eventos y exports |
| `logs/` | Bitácoras |
| `config/` | Configuración y skills de la IA. **Los secretos NO viven en el repo** (ver `config.example.env`) |
| `scripts/` | Utilidades |
| `tests/` | Pruebas |

## Reglas de oro
1. **Secretos fuera del repositorio.** Solo `config.example.env` (nombres, sin valores).
2. **La carpeta antigua** `C:\Users\playg\OneDrive\Documents\CLAUDE 1 EJ` **es archivo histórico intocable.** Nada se borra de ahí; si algo falta, se rescata.
3. La KB manda: si un dato no está en la KB, no se afirma.
