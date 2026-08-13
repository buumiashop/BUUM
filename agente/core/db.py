# -*- coding: utf-8 -*-
"""Memoria del agente BUUM: SQLite en /var/lib/buum/db/agente.db.
   3 tablas: conversations, messages, usage. Nunca se guardan secretos."""
import os
import sqlite3
import time
import uuid

DB_PATH = "/var/lib/buum/db/agente.db"


class DB:
    def __init__(self, path: str = DB_PATH):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        self.con = sqlite3.connect(path, check_same_thread=False)
        self.con.execute("PRAGMA journal_mode=WAL")
        self._crear()

    def _crear(self):
        self.con.executescript(
            """
            CREATE TABLE IF NOT EXISTS conversations(
                id TEXT PRIMARY KEY,
                started_at REAL NOT NULL,
                title TEXT
            );
            CREATE TABLE IF NOT EXISTS messages(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                conversation_id TEXT NOT NULL,
                ts REAL NOT NULL,
                role TEXT NOT NULL,
                content TEXT NOT NULL,
                model TEXT
            );
            CREATE TABLE IF NOT EXISTS usage(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                conversation_id TEXT NOT NULL,
                ts REAL NOT NULL,
                model TEXT NOT NULL,
                input_tokens INTEGER NOT NULL,
                output_tokens INTEGER NOT NULL,
                cost_usd REAL NOT NULL
            );
            """
        )
        try:  # migracion: hilar la sesion de claude por conversacion
            self.con.execute("ALTER TABLE conversations ADD COLUMN claude_session TEXT")
        except sqlite3.OperationalError:
            pass  # la columna ya existe
        self.con.commit()

    def nueva_conversacion(self, titulo: str = "") -> str:
        cid = uuid.uuid4().hex[:12]
        self.con.execute(
            "INSERT INTO conversations(id, started_at, title) VALUES(?,?,?)",
            (cid, time.time(), titulo[:120]),
        )
        self.con.commit()
        return cid

    def guardar_mensaje(self, cid: str, role: str, content: str, model: str = ""):
        self.con.execute(
            "INSERT INTO messages(conversation_id, ts, role, content, model) VALUES(?,?,?,?,?)",
            (cid, time.time(), role, content[:20000], model),
        )
        self.con.commit()

    def registrar_uso(self, cid: str, model: str, tokens_in: int, tokens_out: int, costo: float):
        self.con.execute(
            "INSERT INTO usage(conversation_id, ts, model, input_tokens, output_tokens, cost_usd) VALUES(?,?,?,?,?,?)",
            (cid, time.time(), model, tokens_in, tokens_out, costo),
        )
        self.con.commit()

    def existe_conversacion(self, cid: str) -> bool:
        return self.con.execute("SELECT 1 FROM conversations WHERE id=?", (cid,)).fetchone() is not None

    def poner_titulo_si_vacio(self, cid: str, titulo: str):
        self.con.execute(
            "UPDATE conversations SET title=? WHERE id=? AND (title IS NULL OR title='')",
            (titulo[:80], cid),
        )
        self.con.commit()

    def sesion_claude(self, cid: str):
        fila = self.con.execute("SELECT claude_session FROM conversations WHERE id=?", (cid,)).fetchone()
        return fila[0] if fila else None

    def guardar_sesion_claude(self, cid: str, sesion: str):
        self.con.execute("UPDATE conversations SET claude_session=? WHERE id=?", (sesion, cid))
        self.con.commit()

    def listar_conversaciones(self, limite: int = 50):
        filas = self.con.execute(
            """SELECT c.id, c.started_at, COALESCE(c.title,''),
                      COALESCE((SELECT MAX(ts) FROM messages m WHERE m.conversation_id=c.id), c.started_at)
               FROM conversations c ORDER BY 4 DESC LIMIT ?""",
            (limite,),
        ).fetchall()
        return [{"id": f[0], "inicio": f[1], "titulo": f[2], "ultimo": f[3]} for f in filas]

    def mensajes_de(self, cid: str, limite: int = 200):
        filas = self.con.execute(
            "SELECT ts, role, content FROM messages WHERE conversation_id=? ORDER BY id LIMIT ?",
            (cid, limite),
        ).fetchall()
        return [{"ts": f[0], "role": f[1], "texto": f[2]} for f in filas]

    def _gasto_desde(self, epoch: float) -> float:
        fila = self.con.execute("SELECT COALESCE(SUM(cost_usd),0) FROM usage WHERE ts>=?", (epoch,)).fetchone()
        return float(fila[0])

    def gasto_hoy(self) -> float:
        t = time.localtime()
        inicio_dia = time.mktime((t.tm_year, t.tm_mon, t.tm_mday, 0, 0, 0, 0, 0, -1))
        return self._gasto_desde(inicio_dia)

    def gasto_mes(self) -> float:
        t = time.localtime()
        inicio_mes = time.mktime((t.tm_year, t.tm_mon, 1, 0, 0, 0, 0, 0, -1))
        return self._gasto_desde(inicio_mes)
