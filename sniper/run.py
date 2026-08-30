#!/usr/bin/env python3
"""Social Alpha Scanner — loop utama (mode alert-only).

  python run.py          # jalan terus sesuai interval di config.yaml
  python run.py --once   # satu siklus lalu keluar (buat tes)
"""
from __future__ import annotations

import argparse
import sys
import time
import traceback

from core.config import Config
from core.discovery import Discovery
from core.grok import Grok
from core.notify import Telegram, format_alert
from core.scanner import Scanner
from core.score import score
from core.store import Store


def cycle(cfg: Config, scanner: Scanner, disc: Discovery,
          store: Store, tg: Telegram) -> None:
    candidates = scanner.harvest()
    print(f"[harvest] {len(candidates)} kandidat")

    for c in candidates:
        if store.status(c.term) in ("alerted", "blacklist"):
            continue
        if c.heat < cfg.filters["min_heat"]:
            continue
        if len(c.communities) < cfg.filters["min_communities"]:
            continue

        # Koreksi saturasi lewat pencarian terarah; harvest cenderung meremehkan.
        try:
            sat = scanner.recheck_saturation(c.term)
            c.crypto_saturation = max(
                c.crypto_saturation, float(sat.get("crypto_saturation", 0))
            )
        except Exception as e:
            print(f"[saturation] {c.term}: {e}")

        if c.crypto_saturation > cfg.filters["max_crypto_saturation"]:
            print(f"[skip] {c.term} — CT sudah ramai ({c.crypto_saturation:.0f})")
            store.record(c.term, c.heat, c.crypto_saturation, len(c.communities), {})
            continue

        pairs = disc.find(c.term, c.ticker_guesses)
        pair = max(pairs, key=lambda p: p.liquidity_usd) if pairs else None

        store.record(c.term, c.heat, c.crypto_saturation, len(c.communities),
                     {"tickers": c.ticker_guesses, "growth": c.growth})
        s = score(c, store.velocity(c.term), pair)
        print(f"[score] {c.term}: {s.score:.0f} "
              f"(token: {pair.symbol if pair else 'none'})")

        if s.score < cfg.scoring["alert_threshold"]:
            continue
        token_addr = pair.token_address if pair else None
        if not store.log_alert(c.term, token_addr, pair.chain if pair else None, s.score):
            continue
        if tg.send(format_alert(s)):
            store.mark(c.term, "alerted")
            print(f"[alert] terkirim: {c.term}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--once", action="store_true", help="satu siklus lalu keluar")
    args = ap.parse_args()

    cfg = Config()
    grok = Grok(cfg.xai_key, model=cfg.scanner["model"])
    scanner = Scanner(grok, cfg.scanner)
    disc = Discovery(cfg.discovery)
    store = Store(cfg.store["path"])
    tg = Telegram(cfg.tg_token, cfg.tg_chat)
    interval = int(cfg.scanner["interval_minutes"]) * 60

    try:
        while True:
            started = time.time()
            try:
                cycle(cfg, scanner, disc, store, tg)
            except Exception:
                traceback.print_exc()
            if args.once:
                return 0
            sleep_for = max(interval - (time.time() - started), 30)
            print(f"[idle] tidur {sleep_for/60:.1f} menit\n")
            time.sleep(sleep_for)
    except KeyboardInterrupt:
        return 0
    finally:
        grok.close()
        disc.close()
        tg.close()


if __name__ == "__main__":
    sys.exit(main())
