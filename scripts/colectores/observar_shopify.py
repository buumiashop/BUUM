# -*- coding: utf-8 -*-
"""FASE 13D — Colector de realidad: SHOPIFY (SOLO LECTURA).

Lee productos y pedidos reales via Admin API (GET unicamente) y los guarda como
snapshot verificable en datos/snapshots/shopify/YYYY-MM-DD/.

Reglas:
- Solo GET. Jamas modifica nada en Shopify.
- Cada metrica se clasifica: REAL (viene de la fuente) o CALCULADO (formula
  sobre datos reales). Lo no disponible se declara NO_DISPONIBLE, nunca se inventa.
- Sin datos personales de clientes en el snapshot (privacidad): ni nombres, ni
  direcciones, ni correos.
- Sin secretos en snapshot ni en logs.

Uso:  python3 scripts/colectores/observar_shopify.py
Corre como usuario `buum` (servidor, lee /etc/buum/buum.env) o local
(lee config/config.local.env).
"""
import io
import json
import os
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone

VERSION = "1.0"
API = "2025-01"
AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))  # repo root


def cargar_env():
    for ruta in ("/etc/buum/buum.env", os.path.join(RAIZ, "config", "config.local.env")):
        if os.path.exists(ruta):
            d = {}
            for l in io.open(ruta, encoding="utf-8"):
                l = l.strip()
                if l and not l.startswith("#") and "=" in l:
                    k, v = l.split("=", 1)
                    d[k.strip()] = v.strip()
            return d, ruta
    sys.exit("Sin archivo de credenciales")


def get(tienda, token, ruta, intento=0):
    req = urllib.request.Request(
        f"https://{tienda}/admin/api/{API}/{ruta}",
        headers={"X-Shopify-Access-Token": token, "Accept": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r), None
    except urllib.error.HTTPError as e:
        return None, f"HTTP {e.code} en {ruta}"
    except Exception as e:
        return None, f"{type(e).__name__} en {ruta}"


def real(v):     return {"valor": v, "tipo": "REAL"}
def calc(v, f):  return {"valor": v, "tipo": "CALCULADO", "formula": f}
def nodisp(por): return {"valor": None, "tipo": "NO_DISPONIBLE", "motivo": por}


def main():
    env, origen_env = cargar_env()
    tienda, token = env.get("SHOPIFY_STORE"), env.get("SHOPIFY_ADMIN_TOKEN")
    if not tienda or not token:
        sys.exit("Faltan SHOPIFY_STORE / SHOPIFY_ADMIN_TOKEN")

    ahora = datetime.now(timezone.utc)
    errores, advertencias = [], []

    # ---- PRODUCTOS (REAL) ----
    prods, e = get(tienda, token, "products.json?limit=250")
    if e: errores.append(e)
    productos = []
    for p in (prods or {}).get("products", []):
        for v in p.get("variants", []):
            productos.append({
                "producto": p.get("title"),
                "sku": v.get("sku"),
                "precio": v.get("price"),
                "inventario": v.get("inventory_quantity"),
                "estado": p.get("status"),
                "publicado_en_tienda": bool(p.get("published_at")),
                "peso_gramos": v.get("grams"),
                "actualizado_fuente": p.get("updated_at"),
            })

    # ---- PEDIDOS (REAL; sin datos personales) ----
    cuenta, e = get(tienda, token, "orders/count.json?status=any")
    if e: errores.append(e)
    ords, e = get(tienda, token,
                  "orders.json?status=any&limit=250&fields=id,name,created_at,total_price,"
                  "subtotal_price,total_tax,total_discounts,financial_status,fulfillment_status,"
                  "currency,line_items,total_shipping_price_set,cancelled_at")
    if e: errores.append(e)
    pedidos = []
    for o in (ords or {}).get("orders", []):
        pedidos.append({
            "pedido": o.get("name"),
            "creado": o.get("created_at"),
            "total": o.get("total_price"),
            "subtotal": o.get("subtotal_price"),
            "impuestos": o.get("total_tax"),
            "descuentos": o.get("total_discounts"),
            "envio_cobrado": ((o.get("total_shipping_price_set") or {}).get("shop_money") or {}).get("amount"),
            "moneda": o.get("currency"),
            "estado_pago": o.get("financial_status"),
            "estado_envio": o.get("fulfillment_status") or "sin_preparar",
            "cancelado": bool(o.get("cancelled_at")),
            "articulos": [{"titulo": li.get("title"), "cantidad": li.get("quantity"),
                           "precio": li.get("price"), "sku": li.get("sku")}
                          for li in o.get("line_items", [])],
        })

    activos = [o for o in pedidos if not o["cancelado"]]
    unidades = sum(a["cantidad"] or 0 for o in activos for a in o["articulos"])
    ventas_brutas = round(sum(float(o["total"] or 0) for o in activos), 2)
    impuestos_tot = round(sum(float(o["impuestos"] or 0) for o in activos), 2)
    descuentos_tot = round(sum(float(o["descuentos"] or 0) for o in activos), 2)

    metricas = {
        "pedidos_totales_historicos": real((cuenta or {}).get("count")) if cuenta else nodisp("orders/count fallo"),
        "pedidos_en_snapshot": calc(len(pedidos), "len(pedidos descargados, max 250)"),
        "pedidos_activos": calc(len(activos), "pedidos no cancelados"),
        "unidades_vendidas": calc(unidades, "suma de cantidades en pedidos no cancelados"),
        "ventas_brutas": calc(ventas_brutas, "suma de total_price de pedidos no cancelados (incluye IVA)"),
        "impuestos": calc(impuestos_tot, "suma de total_tax"),
        "descuentos": calc(descuentos_tot, "suma de total_discounts"),
        "ventas_netas_sin_iva": calc(round(ventas_brutas - impuestos_tot, 2), "ventas_brutas - impuestos"),
        "utilidad_real": nodisp("Shopify no expone el costo real del producto ni el costo de las guias"),
        "inventario_reflector": next((real(p["inventario"]) for p in productos if p["sku"] == "R54W50"), nodisp("SKU R54W50 no encontrado")),
    }

    snapshot = {
        "fuente": "shopify",
        "tienda": tienda,
        "version_colector": VERSION,
        "extraido_en": ahora.isoformat(),
        "periodo": {"nota": "estado actual completo; pedidos: los 250 mas recientes de toda la historia"},
        "estado": "OK" if not errores else ("PARCIAL" if productos or pedidos else "FALLIDO"),
        "errores": errores,
        "advertencias": advertencias,
        "metricas": metricas,
        "productos": productos,
        "pedidos": pedidos,
    }

    dia = ahora.strftime("%Y-%m-%d")
    destino = os.path.join(RAIZ, "datos", "snapshots", "shopify", dia)
    os.makedirs(destino, exist_ok=True)
    with io.open(os.path.join(destino, "snapshot.json"), "w", encoding="utf-8") as f:
        json.dump(snapshot, f, ensure_ascii=False, indent=1)
    with io.open(os.path.join(destino, "metadata.json"), "w", encoding="utf-8") as f:
        json.dump({"fuente": "shopify", "version_colector": VERSION, "extraido_en": ahora.isoformat(),
                   "credenciales_desde": origen_env.replace(os.sep, "/"), "estado": snapshot["estado"],
                   "errores": errores}, f, ensure_ascii=False, indent=1)
    print(f"SNAPSHOT {snapshot['estado']} -> datos/snapshots/shopify/{dia}/ | productos: {len(productos)} | pedidos: {len(pedidos)}")


if __name__ == "__main__":
    main()
