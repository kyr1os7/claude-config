#!/usr/bin/env python3
"""Social Alpha Scanner — Solana, mode alert-only + paper trading.

  python run.py            # loop
  python run.py --once     # satu siklus lalu keluar
  python run.py --stats    # ringkasan paper trading lalu keluar
"""
from __future__ import annotations

import argparse
import sys
import time
import traceback

from core.config import Config
from core.discovery import Discovery
from core.grok import Grok
from core.notify import Telegram, format_alert, format_closed
from core.paper import PaperBook
from core.safety import SolanaSafety
from core.scanner import Scanner
from core.score import score
from core.store import Store


def track_paper(book: PaperBook, disc: Discovery, tg: Telegram) -> None:
    """Perbarui posisi terbuka dan laporkan yang tutup."""
    rows = book.open_positions()
    if not rows:
        return
    prices = disc.prices([r["token_address"] for r in rows])
    for row in rows:
        price = prices.get(row["token_address"])
        if price is None:
            continue
        closed = book.update(row, price)
        if closed:
            tg.send(format_closed(closed, book.stats()))
            print(f"[paper] tutup {closed.symbol}: {closed.pnl_x:.2f}x ({closed.reason})")


def scan(cfg: Config, scanner: Scanner, disc: Discovery, store: Store,
         safety: SolanaSafety, book: PaperBook, tg: Telegram) -> None:
    candidates = scanner.harvest()
    print(f"[harvest] {len(candidates)} kandidat")

    for c in candidates:
        if store.status(c.term) in ("alerted", "blacklist"):
            continue
        if c.heat < cfg.filters["min_heat"]:
            continue
        if len(c.communities) < cfg.filters["min_communities"]:
            continue

        try:
            sat = scanner.recheck_saturation(c.term)
            c.crypto_saturation = max(c.crypto_saturation,
                                      float(sat.get("crypto_saturation", 0)))
        except Exception as e:
            print(f"[saturation] {c.term}: {e}")

        store.record(c.term, c.heat, c.crypto_saturation, len(c.communities),
                     {"tickers": c.ticker_guesses, "growth": c.growth})

        if c.crypto_saturation > cfg.filters["max_crypto_saturation"]:
            print(f"[skip] {c.term} — CT sudah ramai ({c.crypto_saturation:.0f})")
            continue

        pairs = disc.find(c.term, c.ticker_guesses)
        pair = max(pairs, key=lambda p: p.liquidity_usd) if pairs else None
        s = score(c, store.velocity(c.term), pair)
        print(f"[score] {c.term}: {s.score:.0f} (token: {pair.symbol if pair else 'none'})")

        if s.score < cfg.scoring["alert_threshold"]:
            continue

        # Safety hanya relevan kalau ada token; watchlist tanpa token dilewat.
        report = safety.check(pair.token_address) if pair else None
        if report and not report.safe:
            print(f"[unsafe] {c.term}: {report.summary()}")
            store.mark(c.term, "blacklist")
            continue

        addr = pair.token_address if pair else None
        if not store.log_alert(c.term, addr, pair.chain if pair else None, s.score):
            continue
        if tg.send(format_alert(s, report)):
            store.mark(c.term, "alerted")
            print(f"[alert] terkirim: {c.term}")
        if pair and cfg.paper["enabled"]:
            if book.open(c.term, pair.chain, pair.symbol, pair.token_address, pair.price_usd):
                print(f"[paper] buka posisi {pair.symbol} @ ${pair.price_usd:.8f}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--once", action="store_true")
    ap.add_argument("--stats", action="store_true")
    args = ap.parse_args()

    cfg = Config()
    store = Store(cfg.store["path"])
    book = PaperBook(store.db, cfg.paper)

    if args.stats:
        s = book.stats()
        print(f"closed={s['closed']} wins={s['wins']} win_rate={s['win_rate']:.1%} "
              f"total={s['total_sol']:+.3f} SOL avg={s['avg_x']:.2f}x open={s['open']}")
        return 0

    grok = Grok(cfg.xai_key, model=cfg.scanner["model"])
    scanner = Scanner(grok, cfg.scanner)
    disc = Discovery(cfg.discovery)
    safety = SolanaSafety(cfg.safety)
    tg = Telegram(cfg.tg_token, cfg.tg_chat)

    scan_every = int(cfg.scanner["interval_minutes"]) * 60
    track_every = int(cfg.paper["track_interval_minutes"]) * 60
    next_scan = 0.0

    try:
        while True:
            now = time.time()
            try:
                # Posisi terbuka dilacak lebih sering daripada scan sosial:
                # harga memecoin bergerak jauh lebih cepat dari meme-nya.
                track_paper(book, disc, tg)
                if now >= next_scan:
                    scan(cfg, scanner, disc, store, safety, book, tg)
                    next_scan = now + scan_every
            except Exception:
                traceback.print_exc()
            if args.once:
                return 0
            time.sleep(track_every)
    except KeyboardInterrupt:
        return 0
    finally:
        grok.close()
        disc.close()
        safety.close()
        tg.close()


if __name__ == "__main__":
    sys.exit(main())
