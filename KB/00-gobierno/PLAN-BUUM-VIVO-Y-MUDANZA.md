# 🧠 PLAN — Sistema Operativo BUUM — siempre vivo + Mudanza a carpeta limpia
> Decisión del Fundador 2026-08-12. Objetivo: dejar de "recordarle" a la IA en cada chat.
> La IA debe ser una entidad SIEMPRE despierta, con memoria propia, que trabaja en el servidor
> y con la que se habla desde la interfaz BUUM (desde cualquier aparato, incluso un empleado futuro).

## Lo que YA tenemos (no se empieza de cero)
| Pieza | Estado |
|---|---|
| Servidor pagado (DigitalOcean `165.227.181.176`) | ✅ vivo, con llaves, Python, ffmpeg |
| Knowledge Base (memoria escrita) | ✅ pero vive en la laptop, no en el servidor |
| Centro de Mando web (`buumia-os/`) | ✅ paneles + calendario; le falta la bandeja de chat |
| Escuela de anuncios + jueces + gustos | ✅ documentados en la KB |
| Publicación Meta (FB/IG) | ✅ scripts funcionan; falta cron automático |

## Las 4 fases (en orden)
### Fase 1 — LA MUDANZA (limpia primero, todo lo demás encima)
Carpeta nueva y ligera. Solo se muda lo VIVO; lo demás se queda en `CLAUDE 1 EJ` como archivo histórico (no se borra nada).
**Estructura propuesta (a validar con ChatGPT + Fundador):**
```
BUUM/
├── KB/          ← Knowledge Base completa (la memoria; se sincroniza al servidor)
├── tienda/      ← tema Shopify vivo + scripts de tienda
├── marketing/   ← motor creativo + scripts vivos (SIN los cientos de pruebas viejas)
├── activos/     ← imágenes oficiales por producto (solo finales y recortes)
├── os/          ← Centro de Mando web + bandeja de chat
└── claves/      ← .env con todas las llaves
```
### Fase 2 — LA MEMORIA VIVE EN EL SERVIDOR
La KB se sube al droplet y se sincroniza sola (git). Cualquier chat (laptop, tablet, servidor)
lee la MISMA memoria. Se acabó el "no te acuerdas".
### Fase 3 — LA BANDEJA (hablar con BUUM desde la interfaz)
Chat dentro del Centro de Mando: cajita de texto → el agente en el servidor recibe, trabaja
y responde. Historial guardado. Sirve desde cualquier navegador (PC, tablet, teléfono).
Un empleado futuro entra a la misma interfaz y deja tareas igual.
### Fase 4 — SIEMPRE DESPIERTO (BUUM 24/7)
Agente corriendo 24/7 en el droplet (Claude Agent SDK): contesta a cualquier hora, publica
en redes con cron, aplica jueces/escuela solo, y avisa al Fundador solo lo importante.
> El gatito vendedor IA también se sube aquí (pendiente ya anotado).

## Decisiones que faltan del Fundador
1. ¿Visto bueno a la estructura de carpeta (después de oír a ChatGPT)?
2. La bandeja: ¿protegida con contraseña simple está bien para empezar?
3. Presupuesto API para el agente 24/7 (consume tokens por mensaje/tarea).

## Regla de la mudanza
**Nada se borra.** `CLAUDE 1 EJ` queda como caja de archivo. Si algo falta después, se rescata de ahí.
