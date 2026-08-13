# Auditor de Calidad — QA antes de que la imagen llegue al Fundador
> Regla del Fundador (2026-07-17): **al Fundador SOLO le llegan imágenes ya bien hechas, para autorizar.** Nunca imágenes con errores que él tenga que arreglar. Toda imagen pasa por un auditor ANTES de mostrarse.

## Principio clave (prevenir > corregir)
Los 2 errores típicos de la IA son: **(a) foco deformado** y **(b) texto/logo inventado**. Se **eliminan por construcción** con el método **HÍBRIDO**:
- La IA hace SOLO la **escena/fondo** (lo que hace bien).
- BUUM pone por **código** el **foco REAL**, el **logo oficial REAL** y el **texto/iconos** → **imposible** que salgan deformados o mal escritos.
- Herramientas: `motor_creativo.py` (escena) + `compose_post.py` (plantilla híbrida). Ver [[roles-creatividad-chatgpt]] y `PROMPT-MAESTRO-ANUNCIO-BUUM.md`.

## Flujo con Auditor (automático)
1. **Generar** la escena (IA).
2. **Componer** el híbrido (foco/logo/texto reales por código).
3. **AUDITAR** (checklist abajo). Lo hace BUUM antes de mostrar nada.
4. Si **PASA** → llega al Fundador **solo para autorizar/publicar**.
5. Si **NO pasa** (p. ej. la escena salió fea) → **regenerar** automáticamente. BUUM avisa con transparencia: *"regeneré N veces, costo total $X"*. Si el Fundador dijo "no importa el costo, haz contenido", regenera sin preguntar.

## Checklist del Auditor (todo debe cumplirse)
- [ ] **Foco = el real** (cúpula esmerilada + cuerpo facetado + E27). NO redondo, NO deformado, NO puntiagudo.
- [ ] **Logo = oficial** (gato Kitsune BUUM), nítido, completo, no cortado.
- [ ] **Todo el texto** bien escrito (sin "STAL POTBIDIA", sin "3S0"): titular, subtítulo, iconos.
- [ ] **Luz BLANCA** (regla dura).
- [ ] Marca coherente (colores, tipografía, misma vibra del feed).
- [ ] Encuadre limpio (nada cortado ni encimado), formato correcto.
- [ ] Honestidad (no promete lo que el producto no es).

## Costo / decisión del Fundador
- Escena premium (gpt-image-1): ~$0.26. Escena barata (flux): ~$0.03. El foco/logo/texto por código: **$0**.
- Regenerar una escena mala = otra escena (~$0.26). El Auditor lo reporta. El Fundador decide el techo de costo (o "no importa, haz contenido").
