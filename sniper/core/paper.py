"""Paper trading: catat posisi hipotetis dan lacak hasilnya sampai tutup.

Tujuannya satu — memberi PENYEBUT. Screenshot bot yang beredar hanya
menunjukkan trade yang menang; yang menentukan strategi ini layak atau tidak
adalah win-rate dan rata-rata kerugian, dan itu hanya muncul kalau setiap
sinyal dicatat, termasuk yang gagal.

Biaya dimodelkan (slippage dua sisi + fee per sisi) karena tanpa itu angka
PnL-nya bohong pada dirinya sendiri.
"""
from __future__ import annotations

import sqlite3
import time
from dataclasses import dataclass

SCHEMA = """
CREATE TABLE IF NOT EXISTS paper_positions (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    term            TEXT NOT NULL,
    token_address   TEXT NOT NULL UNIQUE,
    chain           TEXT NOT NULL,
    symbol          TEXT NOT NULL,
    entry_price     REAL NOT NULL,
    entry_at        INTEGER NOT NULL,
    size_sol        REAL NOT NULL,
    high_price      REAL NOT NULL,
    exit_price      REAL,
    exit_at         INTEGER,
    exit_reason     TEXT,
    pnl_x           REAL,
    pnl_sol         REAL,
    status          TEXT NOT NULL DEFAULT 'open'
);
"""


@dataclass
class Closed:
    term: str
    symbol: str
    token_address: str
    pnl_x: float
    pnl_sol: float
    reason: str
    held_minutes: float
    peak_x: float


class PaperBook:
    def __init__(self, db: sqlite3.Connection, cfg: dict) -> None:
        self.db = db
        self.cfg = cfg
        self.db.executescript(SCHEMA)
        self.db.commit()

    def open(self, term: str, chain: str, symbol: str,
             token_address: str, price: float) -> bool:
        if price <= 0:
            return False
        try:
            self.db.execute(
                "INSERT INTO paper_positions(term, token_address, chain, symbol, "
                "entry_price, entry_at, size_sol, high_price) VALUES(?,?,?,?,?,?,?,?)",
                (term, token_address, chain, symbol, price, int(time.time()),
                 float(self.cfg["size_sol"]), price),
            )
            self.db.commit()
            return True
        except sqlite3.IntegrityError:
            return False   # sudah pernah dibuka

    def open_positions(self) -> list[sqlite3.Row]:
        return self.db.execute(
            "SELECT * FROM paper_positions WHERE status='open'"
        ).fetchall()

    def update(self, row: sqlite3.Row, price: float) -> Closed | None:
        """Perbarui satu posisi dengan harga terbaru; tutup kalau kena aturan."""
        c = self.cfg
        pid = row["id"]
        high = max(float(row["high_price"]), price)
        self.db.execute("UPDATE paper_positions SET high_price=? WHERE id=?", (high, pid))

        entry = float(row["entry_price"])
        raw_x = price / entry
        held_min = (time.time() - row["entry_at"]) / 60.0

        reason = None
        if raw_x >= float(c["take_profit_x"]):
            reason = f"take profit {c['take_profit_x']}x"
        elif raw_x <= 1 - float(c["stop_loss_pct"]) / 100.0:
            reason = f"stop loss -{c['stop_loss_pct']}%"
        elif held_min >= float(c["max_hold_minutes"]):
            reason = f"time stop {c['max_hold_minutes']}m"

        if reason is None:
            self.db.commit()
            return None

        # Biaya: slippage dikenakan pada masuk dan keluar, fee flat per sisi.
        slip = float(c["slippage_pct"]) / 100.0
        net_x = raw_x * (1 - slip) ** 2
        size = float(row["size_sol"])
        pnl_sol = size * (net_x - 1.0) - 2 * float(c["fee_sol"])

        self.db.execute(
            "UPDATE paper_positions SET status='closed', exit_price=?, exit_at=?, "
            "exit_reason=?, pnl_x=?, pnl_sol=? WHERE id=?",
            (price, int(time.time()), reason, net_x, pnl_sol, pid),
        )
        self.db.commit()
        return Closed(
            term=row["term"], symbol=row["symbol"], token_address=row["token_address"],
            pnl_x=net_x, pnl_sol=pnl_sol, reason=reason,
            held_minutes=held_min, peak_x=high / entry,
        )

    def stats(self) -> dict:
        r = self.db.execute(
            "SELECT COUNT(*) n, "
            "SUM(CASE WHEN pnl_sol > 0 THEN 1 ELSE 0 END) wins, "
            "COALESCE(SUM(pnl_sol), 0) total, "
            "COALESCE(AVG(pnl_x), 0) avg_x "
            "FROM paper_positions WHERE status='closed'"
        ).fetchone()
        n = r["n"] or 0
        return {
            "closed": n,
            "wins": r["wins"] or 0,
            "win_rate": (r["wins"] or 0) / n if n else 0.0,
            "total_sol": r["total"] or 0.0,
            "avg_x": r["avg_x"] or 0.0,
            "open": len(self.open_positions()),
        }
