# -*- coding: utf-8 -*-
"""Control de gasto del agente. Sin presupuesto configurado NO hay llamadas.
   Los limites duros adicionales viven en la consola de Anthropic (spend limit)."""

# Precios publicos por MILLON de tokens (entrada, salida) — actualizar si cambian.
# claude-sonnet-5 tiene precio de introduccion $2/$10 hasta 2026-08-31 (luego $3/$15):
# usamos el precio ALTO para no subestimar el gasto.
PRECIOS_USD_MTOK = {
    "claude-sonnet-5": (3.0, 15.0),
    "claude-haiku-4-5": (1.0, 5.0),
    "claude-opus-5": (5.0, 25.0),
}
PRECIO_DEFECTO = (5.0, 25.0)  # si el modelo no esta en la tabla, asumir caro


def costo_llamada(modelo: str, tokens_in: int, tokens_out: int) -> float:
    pin, pout = PRECIOS_USD_MTOK.get(modelo, PRECIO_DEFECTO)
    return (tokens_in / 1_000_000) * pin + (tokens_out / 1_000_000) * pout


class Presupuesto:
    def __init__(self, env: dict):
        self.diario = self._leer(env, "BUUM_DAILY_BUDGET_USD")
        self.mensual = self._leer(env, "BUUM_MONTHLY_BUDGET_USD")

    @staticmethod
    def _leer(env, clave):
        v = (env.get(clave) or "").strip()
        try:
            return float(v) if v else None
        except ValueError:
            return None

    @property
    def configurado(self) -> bool:
        return self.diario is not None and self.mensual is not None

    def permite(self, db) -> tuple[bool, str]:
        if not self.configurado:
            return False, (
                "PRESUPUESTO NO CONFIGURADO: faltan BUUM_DAILY_BUDGET_USD y/o "
                "BUUM_MONTHLY_BUDGET_USD en /etc/buum/buum.env. Sin presupuesto no hay llamadas."
            )
        hoy, mes = db.gasto_hoy(), db.gasto_mes()
        if hoy >= self.diario:
            return False, f"Presupuesto DIARIO agotado (${hoy:.4f} de ${self.diario:.2f}). Avisa al Fundador."
        if mes >= self.mensual:
            return False, f"Presupuesto MENSUAL agotado (${mes:.4f} de ${self.mensual:.2f}). Avisa al Fundador."
        return True, ""
