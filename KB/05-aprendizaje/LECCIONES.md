# Lecciones — registro vivo

> Paso 10 del flujo: cada campaña deja una lección medida. Las que se confirman suben al [Libro de Jugadas](LIBRO-DE-JUGADAS-MARKETING.md); las que fallan se retiran de la práctica (sin borrarse). Evidencia real, no teoría.

Formato: **fecha · pieza · esperado → real · lección · confianza**

---

- **2026-07-16 · Proceso (aún sin campaña publicada):** el candado atrapó dos veces contenido deshonesto antes de publicar (venta de producto en desarrollo; luz cálida en vez de blanca). *Lección:* la compuerta de honestidad funciona y es imprescindible. *Confianza: alta (observado).*
- **2026-07-16 · Baseline @buum.ia:** 420 seguidores, 5 posts previos (ver `06-contenido/baseline-ig.json`). *Lección:* punto de partida real para calibrar umbrales de resonancia, en vez de conjeturar. *Confianza: dato.*

*(La primera campaña real agregará la primera lección de resultados esperado-vs-real.)*

## Lección — Fotos de recepción sobre fondo CONTRASTANTE (para recorte automático)
2026-07-17 (reflector). El recorte automático fiel (rembg) falla con objetos **plateados/blancos/reflejantes** sobre **fondo claro** (mismo color → los confunde). Ej: el reverso del panel solar (plateado) se perdió; solo quedó el cable. **Regla para Recepción:** fotografiar los productos sobre **fondo CONTRASTANTE** (tela oscura/negra para objetos claros; fondo claro para objetos oscuros). Así el recorte automático sale limpio y el pipeline escala sin intervención. Alternativa para casos difíciles: modelo BiRefNet en Replicate (~2-5¢).
