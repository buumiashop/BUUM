# 🏗️ REVISIÓN DE ARQUITECTURA — BUUM como Empresa Inteligente
> Revisión de nivel ingeniería. Objetivo: una arquitectura que dure 10 años, escale de pyme a internacional, y que **cada semana sea más inteligente que la anterior**. Evoluciona la arquitectura actual; no la reemplaza.
> Autor: Claude (CEO/arquitecto principal). Fecha: 2026-07-14. Complementa `00-PLANO-ARQUITECTONICO.md`.

---

## ✅ DECISIONES CERRADAS (2026-07-14, dueño)
1. **Cimientos primero** — se construye P0 (sustrato de datos + telemetría + fallback de proveedores) ANTES de instanciar más departamentos.
2. **ChatGPT como Director de Marketing = Opción A** (bucle humano acotado vía Estación de Contenido, ya definido en `00-PLANO-ARQUITECTONICO.md` §5–6). No se automatiza la app; el "Director" = dueño + ChatGPT entregando assets a `marketing/entrantes/`.
3. CEO = Claude · autonomía **99/1** · implementación **Skills + OS**.

## 0) VEREDICTO PRINCIPAL (léelo aunque no leas nada más)
La arquitectura actual **no tiene sistema nervioso**. Tiene un buen "organigrama" y buenos manuales, pero:
- El **conocimiento** vive como prosa en markdown → no se puede consultar, medir ni reutilizar a escala.
- El **estado** (autorizaciones, feedback, calendario) vive en el navegador (localStorage) y en archivos sueltos → no es durable, no se comparte, se puede perder.
- El **aprendizaje** está abierto: se registra feedback pero **nada lo consume**; "aprender" hoy = que yo edite manualmente un archivo.

**Consecuencia:** agregar más departamentos (Evolución, Investigación, etc.) sobre esta base es construir pisos sobre unos cimientos de arena. **La prioridad NO es más cajas en el organigrama; es construir el sustrato de datos, telemetría y gobierno.** El organigrama es la parte fácil y satisfactoria; el sustrato es lo que de verdad hace que la empresa "se vuelva más inteligente cada semana".

> Prueba de los 5 años aplicada: "¿más departamentos hoy hará a BUUM más inteligente en 5 años?" → **No.** "¿un sustrato de conocimiento + telemetría + gobierno de autonomía?" → **Sí.** Por eso el rediseño prioriza lo segundo.

---

## 1) DEBILIDADES CRÍTICAS DE LA ARQUITECTURA ACTUAL
| # | Debilidad | Severidad | Por qué mata el crecimiento |
|---|-----------|-----------|------------------------------|
| 1 | **Estado en `localStorage` + JS sueltos** (buum_estacion, buum_feedback, calendario.js, datos.js) | 🔴 Crítica | No es durable ni compartido; un cambio de navegador/cache borra autorizaciones y aprendizajes. Un "OS de empresa" no puede vivir en el navegador. |
| 2 | **Memoria = prosa en markdown** (SKILL.md, memory/*.md) | 🔴 Crítica | No se puede consultar ("¿qué campañas con gato rindieron?"), no escala, no alimenta aprendizaje automático. |
| 3 | **"Departamento = SKILL.md gigante"** | 🟠 Alta | Es exactamente el "prompt gigante" que NO quieres: reglas + historial + errores + métodos mezclados en un blob de contexto. |
| 4 | **Bucle de aprendizaje ABIERTO** | 🔴 Crítica | Se loguea feedback pero nadie lo procesa. El aprendizaje es manual. Contradice el objetivo #1 (empresa que aprende sola). |
| 5 | **Proveedores sin abstracción (SPOF)** | 🟠 Alta | Hoy OpenAI topado, Gemini sin saldo → producción detenida. Un límite de facturación NO debe frenar la empresa. |
| 6 | **Sin gobierno de costos (FinOps)** | 🟠 Alta | Se gastó y se topó sin presupuesto, sin telemetría, sin datos para decidir. |
| 7 | **Publicación programada = ilusión de UI** | 🟠 Alta | "Programado a las 19:00" es un estado en localStorage; no hay cola/scheduler/reintento real. Promesa hueca. |
| 8 | **Secretos en texto plano** (`aurora-cafe/claves.local.txt`) + sin auditoría | 🟡 Media hoy / 🔴 a escala | Sin bóveda de secretos ni registro de quién autorizó qué. |
| 9 | **Autonomía binaria** (preview→OK) | 🟠 Alta | No hay forma de medir confianza ni graduar autonomía. Sin esto, "autonomía por evidencia" es imposible. |

## 2) DÓNDE TU PLAN SE EQUIVOCARÍA (crítica honesta, como pediste)
1. **Demasiados departamentos, demasiado pronto.** Evolución + Tecnología IA + Investigación + partir Marketing en 10 roles, para una empresa **pre-ingresos** donde el humano aún genera imágenes a mano. Amazon/Apple no arrancaron con 15 departamentos; arrancaron con una **columna vertebral** que funcionaba y agregaron estructura cuando el volumen lo exigió. Instanciar 11 departamentos hoy crea sobrecarga de coordinación y mantenimiento, y la **ilusión** de empresa sin la sustancia. → Diseña el **framework** que permite que existan y crezcan departamentos; **activa 3-4**.
2. **"Investigación que nunca duerme" scrapeando Alibaba/Amazon/TikTok** es frágil y viola sus Términos (te bloquean/banean). → Usa **APIs oficiales** donde existan y una **cadencia de investigación** con fuentes confiables donde no. "Nunca duerme" = cron que se rompe.
3. **Los % de confianza deben CALCULARSE, no declararse.** "Marketing 98%" hardcodeado es peor que nada: fabrica confianza falsa. La confianza debe salir de un **historial real** (tasa de aprobación/error sobre N muestras, por tipo de tarea). Alineado con tu "nunca por intuición" — pero hay que hacerlo riguroso.
4. **ChatGPT como "Director" — reality check.** La **app chatgpt.com NO es controlable de forma soportada** (automatizarla viola ToS y es frágil). La **API sí** es controlable, pero eso NO es "la app con su auto-prompting"; es el modelo crudo. Replicar el comportamiento de la app = **construir tú un servicio** (expansión de prompt + generación + auto-crítica). No existe un botón mágico "ChatGPT dirige tu marketing". (Detalle en §7.)
5. **JARVIS requiere primero el sustrato de datos.** No puedes tener JARVIS sobre localStorage y markdown. Es una **consecuencia** de arreglar los cimientos, no un accesorio que se atornilla.
6. **El limitante real de crecimiento NO es el número de departamentos** — es (a) la falta de base de datos/conocimiento, (b) el bucle de aprendizaje abierto, (c) el humano generando cada imagen a mano. Un "Departamento de Evolución" no sirve si no hay telemetría estructurada que analizar.

## 3) LA ARQUITECTURA EVOLUCIONADA (6 capas)
Separa lo que hoy está mezclado. Cada capa es modular y reemplazable.

- **L0 · ADN BUUM (constitución inmutable):** misión, visión, valores, identidad, branding, tono, estándares de calidad, reglas duras, errores prohibidos. Versionado, referenciado por TODOS. Toda acción se valida contra el ADN (guardrail). Ningún departamento puede romperlo.
- **L1 · Sustrato de Conocimiento y Memoria (EL ARREGLO CLAVE):** tres memorias:
  - **Semántica / base de conocimiento:** hechos estructurados, playbooks, brand kit → **consultable**.
  - **Episódica / bitácora de eventos:** cada acción + resultado + "¿qué aprendimos?" → log append-only.
  - **Estado de trabajo:** tareas, calendario, pipeline → **datastore real** (empezar con SQLite/JSON con esquema en el droplet; **matar la dependencia de localStorage**).
  - **Capa de recuperación (retrieval):** los departamentos jalan a contexto **solo lo relevante**, no todo el blob.
- **L2 · Departamentos (capacidades) con CONTRATO estándar:** cada uno = una ficha {objetivo, responsabilidades, entradas, salidas, KPIs, límites, autoridad, protocolos, namespace de memoria, modelo de confianza, nivel de riesgo}. La **identidad** del departamento es el contrato + KPIs + memoria, **no la prosa**. Implementación = skill (parte ejecutable) + su namespace en L1.
- **L3 · Orquestación (CEO = Claude):** ruteo, delegación, protocolo de handoff entre departamentos, decisión usando confianza + presupuesto + guardrail de ADN. Un **bus de tareas** simple (tabla de tareas con estados) conecta departamentos.
- **L4 · Gobierno y Autonomía:** motor de confianza/evidencia (§5), FinOps (presupuestos por departamento + telemetría de costo), auditoría (quién/qué/cuándo/por qué), bóveda de secretos.
- **L5 · Interfaces:** Centro de Mando (JARVIS) = conversación + tablero **sobre L1–L4**; conectores externos (Meta, Shopify, proveedores) detrás de una **abstracción con fallback**.

## 4) LOS DEPARTAMENTOS NUEVOS, UBICADOS CORRECTAMENTE
- **Tecnología IA** = dueño de L1 (infra de memoria) + L4 (FinOps) + **abstracción de proveedores con fallback**. **CONSTRUIR PRIMERO** — arregla el SPOF y el costo, los problemas que HOY te detienen. Es el más importante de los tres.
- **Evolución** = proceso meta sobre la telemetría de L1/L4 (lee bitácora + KPIs → detecta cuellos de botella, errores repetidos → propone automatización → sube autonomía). Válido, pero **inútil hasta que exista la telemetría (L1)**. Secuencia: sustrato primero.
- **Investigación e Innovación** = productor de conocimiento hacia L1, con **cadencia** y **APIs oficiales** (no scraping 24/7). Convierte información en **conocimiento** (entradas estructuradas con "implicación para BUUM").

## 5) MOTOR DE CONFIANZA Y AUTONOMÍA (riguroso)
- Cada acción se etiqueta: {departamento, tipo-de-tarea, confianza, costo, resultado (se completa después)}.
- **Confianza = f(**tasa de éxito histórica del tipo-de-tarea, tamaño de muestra, recencia, varianza**)**. Arranque en frío = confianza baja → aprobación humana.
- **Niveles de riesgo:** publicar / gastar dinero = **alto** (umbral alto, quizá siempre humano hasta evidencia enorme); borradores internos = **bajo** (auto).
- **Regla de ejecución:** auto-ejecuta si `confianza ≥ umbral(riesgo)` **Y** dentro de presupuesto **Y** pasa guardrail de ADN; si no, **escala al dueño**.
- **La autonomía sube SOLO por evidencia** + el dueño **ratifica** el cambio de umbral (gobierno). Nunca por intuición.

## 6) MARKETING COMO AGENCIA CREATIVA
Sí, modélalo como agencia con **roles**: Director Creativo, Dirección de Arte, Fotografía Publicitaria, Branding, Copywriting, Video, Social Media, SEO, Performance, Analítica.
**Pero** (crítica): no instancies 10 agentes separados hoy — es sobre-ingeniería para el volumen actual. Define los roles como **funciones/checklists dentro del contrato del departamento Marketing**, y actívalos como sub-skills **cuando el volumen lo justifique**. Sé honesto sobre qué es "agente separado real" vs "rol que una IA desempeña":
- **Director Creativo** = ChatGPT (concepto/imagen) o el Servicio Creativo por API (§7).
- **Arte / Branding / Copy / Auditoría** = funciones de calidad que Claude ejecuta contra el ADN.
- **Performance / Analítica** = lee telemetría de L1.

## 7) INTEGRAR ChatGPT COMO DIRECTOR DE MARKETING (realista)
- **Opción A — hoy, bucle humano acotado:** la Estación entrega un **brief/prompt** → el humano usa la app de ChatGPT → deja el asset en `marketing/entrantes/` → Claude arma/publica. Confiable, sin ToS. El "Director" = humano + ChatGPT.
- **Opción B — Servicio Creativo sobre la API de OpenAI (el intermediario):** software que **nosotros construimos** y que recibe un **brief creativo** (no un prompt afinado a mano), hace **expansión de prompt + generación (gpt-image-1) + bucle de auto-crítica + verificación de marca**, y devuelve el asset terminado. **Este es el "ChatGPT autónomo como Director" real** — pero es código sobre la API, no la app. Requiere saldo OpenAI + el orquestador.
- **NO diseñar (imposible/ToS):** manejar chatgpt.com con un robot de forma autónoma.
- **Recomendación:** A ahora; construir B por partes. **Abstrae la interfaz "Director Creativo"** para que A o B queden intercambiables detrás del mismo contrato. Así el CEO nunca reescribe las instrucciones creativas: entrega un **brief**, no un prompt.

## 8) CENTRO DE MANDO → JARVIS (secuenciado)
= UI conversacional + conciencia situacional **sobre L1–L4**. Primero el sustrato; luego: chatear-con-la-empresa (consulta KB/telemetría vía herramientas), y superficie inmediata de ventas / utilidad / campañas / riesgos / recomendaciones / investigaciones / tareas / prioridades. Se construye **después** de los cimientos.

## 9) CONSEJO DIRECTIVO
Agregación **semanal automática**: cada departamento emite un reporte **estructurado** {resultados, KPIs, aprendizajes, errores, propuestas, necesidades, tendencia de confianza, gasto} → el CEO sintetiza → decisiones **registradas en la bitácora** (L1). Barato y de alto valor **una vez que existe la telemetría**.

## 10) SECUENCIA (roadmap honesto — orden importa)
- **P0 · Cimientos:** ADN en formato legible por máquina + mover el estado a un datastore real (matar dependencia de localStorage) + bóveda de secretos + abstracción de proveedores. *Sin esto, todo lo demás es teatro.*
- **P1 · Instrumentar:** telemetría en CADA acción. Levantar **Tecnología IA** (abstracción/fallback/costo).
- **P2 · Gobierno:** motor de confianza + Consejo Directivo + **Evolución** (ya tiene datos que masticar).
- **P3 · Expansión:** cadencia de **Investigación** + roles de agencia en Marketing + capa conversacional **JARVIS**.
- **P4+ · Escala:** multi-producto, multi-idioma, más departamentos vía el framework.

## 11) PRINCIPIOS DE DISEÑO (para los próximos 10 años)
- **Simple core, extensión limpia.** Las mejores arquitecturas de miles de millones son un núcleo simple con puntos de extensión, no 15 cajas el día 1.
- **Contratos, no prosa.** Los límites entre departamentos son interfaces con esquema.
- **Todo evento deja rastro + lección.** "¿Qué aprendimos?" es un registro estructurado, no una frase.
- **Autonomía por evidencia, con freno de ADN y de presupuesto.**
- **Proveedores desacoplados** (modelo/vendor intercambiable): hoy Replicate, mañana lo que sea mejor/más barato.
- **Right-sizing:** diseñar para 10 años, **implementar por etapas y barato**. Sobre-construir hoy = lastre que te frena (y frenarte contradice "aprender rápido").

---
*Este documento es la revisión viva. Cada cambio a la arquitectura debe justificar: qué problema resuelve, por qué mejora la empresa, qué beneficio e impacto futuro tiene — y pasar la prueba de los 5 años.*
