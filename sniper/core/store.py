"""SQLite state.

Kenapa perlu state: satu snapshot tidak bisa membedakan meme yang SEDANG naik
dari meme yang sudah datar. Velocity butuh minimal dua observasi terpisah waktu,
jadi setiap hasil scan disimpan dan dibandingkan dengan scan sebelumnya.
"""
from __future__ import annotations

import json
import sqlite3
import time
from dataclasses import dataclass
from pathlib import Path

SCHEMA = """
CREATE TABLE IF NOT EXISTS terms (
    term            TEXT PRIMARY KEY,
    first_seen      INTEGER NOT NULL,
    last_seen       INTEGER NOT NULL,
    status          TEXT NOT NULL DEFAULT 'watching'
);
CREATE TABLE IF NOT EXISTS observations (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    term                TEXT NOT NULL,
    seen_at             INTEGER NOT NULL,
    heat                REAL NOT NULL,
    crypto_saturation   REAL NOT NULL,
    communities         INTEGER NOT NULL,
    payload             TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_obs_term_time ON observations(term, seen_at DESC);
CREATE TABLE IF NOT EXISTS alerts (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    term            TEXT NOT NULL,
    token_address   TEXT,
    chain           TEXT,
    score           REAL NOT NULL,
    sent_at         INTEGER NOT NULL
);
CREATE UNIQUE INDEX IF NOT EXISTS idx_alert_token ON alerts(token_address);
"""


# Dua observasi yang terlalu berdekatan tidak bisa menghasilkan laju yang
# bermakna — membaginya hanya melahirkan angka raksasa yang menipu skor.
MIN_SPAN_SECONDS = 300


@dataclass
class Velocity:
    """Perubahan heat antara observasi terbaru dan observasi pembanding."""

    delta: float          # selisih heat absolut
    per_hour: float       # laju kenaikan heat per jam
    samples: int          # jumlah observasi yang tercatat untuk term ini
    age_hours: float      # sudah berapa lama term ini dipantau


class Store:
    def __init__(self, path: str | Path) -> None:
        self.db = sqlite3.connect(str(path))
        self.db.row_factory = sqlite3.Row
        self.db.executescript(SCHEMA)
        self.db.commit()

    # ---------- writes ----------

    def record(self, term: str, heat: float, saturation: float,
               communities: int, payload: dict) -> None:
        now = int(time.time())
        self.db.execute(
            "INSERT INTO terms(term, first_seen, last_seen) VALUES(?,?,?) "
            "ON CONFLICT(term) DO UPDATE SET last_seen=excluded.last_seen",
            (term, now, now),
        )
        self.db.execute(
            "INSERT INTO observations(term, seen_at, heat, crypto_saturation, "
            "communities, payload) VALUES(?,?,?,?,?,?)",
            (term, now, heat, saturation, communities, json.dumps(payload)),
        )
        self.db.commit()

    def mark(self, term: str, status: str) -> None:
        self.db.execute("UPDATE terms SET status=? WHERE term=?", (status, term))
        self.db.commit()

    def log_alert(self, term: str, token_address: str | None,
                  chain: str | None, score: float) -> bool:
        """Return False kalau token ini sudah pernah di-alert (dedup)."""
        try:
            self.db.execute(
                "INSERT INTO alerts(term, token_address, chain, score, sent_at) "
                "VALUES(?,?,?,?,?)",
                (term, token_address, chain, score, int(time.time())),
            )
            self.db.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    # ---------- reads ----------

    def velocity(self, term: str) -> Velocity:
        # id DESC sebagai tie-break: beberapa observasi bisa jatuh di detik yang
        # sama, dan tanpa ini urutannya sembarang sehingga delta bisa terbalik.
        rows = self.db.execute(
            "SELECT seen_at, heat FROM observations WHERE term=? "
            "ORDER BY seen_at DESC, id DESC LIMIT 8",
            (term,),
        ).fetchall()
        if len(rows) < 2:
            return Velocity(0.0, 0.0, len(rows), 0.0)

        newest, oldest = rows[0], rows[-1]
        span_s = newest["seen_at"] - oldest["seen_at"]
        delta = newest["heat"] - oldest["heat"]
        if span_s < MIN_SPAN_SECONDS:
            # Datanya ada tapi belum cukup terpisah waktu; laporkan delta saja
            # dan biarkan per_hour 0 supaya scorer tidak memakainya.
            return Velocity(delta=delta, per_hour=0.0, samples=len(rows), age_hours=0.0)
        return Velocity(
            delta=delta,
            per_hour=delta / (span_s / 3600.0),
            samples=len(rows),
            age_hours=span_s / 3600.0,
        )

    def status(self, term: str) -> str | None:
        row = self.db.execute(
            "SELECT status FROM terms WHERE term=?", (term,)
        ).fetchone()
        return row["status"] if row else None
