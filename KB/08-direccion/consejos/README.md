# Consejos de Dirección — archivo histórico

Cada Consejo emitido se guarda aquí como `YYYY-MM-DD.md`.

**Flujo oficial (FASE 13F, manual — sin cron todavía):**
1. BUUM-admin corre los colectores (`scripts/colectores/observar_*.py`) → snapshot fresco.
2. El Fundador pide "Consejo de Dirección" (bandeja o CLI) → el agente aplica la
   skill `consejo-direccion` completa (14 secciones, máx 3 prioridades).
3. El Fundador responde SOLO la sección "Decisiones requeridas".
4. BUUM-admin registra los veredictos en `DECISIONES.md` y archiva el Consejo aquí.
5. El Consejo siguiente lee el más reciente de esta carpeta para "QUÉ CAMBIÓ".

El agente genera; no archiva (sigue en solo lectura). Frecuencia: semanal.
