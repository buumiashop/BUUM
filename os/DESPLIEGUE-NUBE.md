# ☁️ DESPLIEGUE EN LA NUBE — DigitalOcean (servidor 24/7 sin tu compu)

> Meta: que BUUM OS corra solo día y noche. Tú creas la cuenta (lleva tu correo/tarjeta); yo dejo TODO lo demás listo.
> Costo objetivo: **~75-110 MXN/mes** (droplet más barato). Y hay **crédito gratis de bienvenida** (suele ser $200 USD / 60 días para cuentas nuevas) → los primeros ~2 meses pueden salir GRATIS.

## PARTE 1 — Lo que haces TÚ (una vez, ~10 min)
1. Entra a **digitalocean.com** → **Sign up** (con tu correo). Agrega método de pago (pide tarjeta; aplican el crédito gratis).
2. **Create → Droplet**:
   - **Región:** la de EE. UU. más cercana (New York o San Francisco).
   - **Imagen:** Ubuntu 24.04 LTS.
   - **Tipo:** Basic → Regular → **el más barato** ($4/mo 512MB = ~75 MXN, o $6/mo 1GB = ~110 MXN, recomendado por holgura).
   - **Autenticación:** contraseña (elige una y guárdala) — es lo más fácil.
   - Crear droplet. Copia la **IP** que te da.
3. Abre la **consola web** del droplet (botón "Console" en DigitalOcean) — ahí puedes pegar comandos sin instalar nada.

## PARTE 2 — Lo que hago YO (con lo de arriba)
- Te doy **un bloque de comandos** para pegar en esa consola: instala Python, ffmpeg y las dependencias, y baja el código de BUUM OS.
- Configuramos las **llaves** (Gemini, Replicate, Meta) en el servidor de forma segura (archivo privado, no se sube a ningún lado).
- Programo las **rutinas** (cron): generar contenido de gatitos → 4 filtros → publicar en @buum.ia/FB → medir → aprender. Todo automático.
- Dejo el **Centro de Mando** accesible para que revises desde tu celular/compu cuando quieras.

## Seguridad y control
- Las llaves viven SOLO en tu servidor (archivo local con permisos), nunca en repos públicos.
- Empezamos en modo **práctica con gatitos** (sin productos, sin precios, sin clientes) → cero riesgo.
- Tú puedes apagar/pausar todo desde el panel o borrando el droplet (deja de cobrar al instante).

## Cuando termine la semana de práctica
- Si funciona → seguimos igual pero ya con **productos reales** (reflectores) y el proceso de `PROCESO-PRODUCTO.md`.
- Si algo falla → lo afinamos; nada en vivo se rompe porque es solo mascota.

**Tu siguiente paso:** crea la cuenta + el droplet (Parte 1) y pásame la **IP**. Yo sigo con la Parte 2.

Relacionado: `BUUMIA-OS.md`, `centro-de-mando.html`, `PROCESO-PRODUCTO.md`, `EQUIPO.md`.
