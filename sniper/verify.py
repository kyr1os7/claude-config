#!/usr/bin/env python3
"""Cek semua dependensi eksternal sebelum menjalankan bot.

Bentuk respons Dexscreener, rugcheck, dan xAI TIDAK bisa diverifikasi di
lingkungan tempat kode ini ditulis (egress diblokir), jadi jalankan ini dulu
di mesinmu. Skrip ini memastikan field yang diandalkan kode memang ada —
bukan sekadar "server-nya hidup".

    python verify.py
"""
from __future__ import annotations

import os
import sys
import traceback

import httpx

OK, BAD = "  ✅", "  ❌"


def check(name: str):
    def deco(fn):
        print(f"\n[{name}]")
        try:
            fn()
        except Exception as e:
            print(f"{BAD} {type(e).__name__}: {e}")
            traceback.print_exc(limit=1)
            return False
        return True
    return deco


def main() -> int:
    from dotenv import load_dotenv
    load_dotenv()
    results = []

    @check("Dexscreener search")
    def _():
        r = httpx.get("https://api.dexscreener.com/latest/dex/search",
                      params={"q": "bonk"}, timeout=20)
        r.raise_for_status()
        pairs = r.json().get("pairs") or []
        assert pairs, "tidak ada pairs — bentuk respons mungkin berubah"
        p = pairs[0]
        for field in ("chainId", "dexId", "pairAddress", "baseToken",
                      "priceUsd", "fdv", "liquidity", "txns", "pairCreatedAt"):
            assert field in p, f"field '{field}' hilang"
        print(f"{OK} {len(pairs)} pairs, semua field yang dipakai kode ada")
    results.append(_)

    @check("Solana RPC (mint/freeze authority)")
    def _():
        rpc = os.getenv("SOLANA_RPC_URL") or "https://api.mainnet-beta.solana.com"
        usdc = "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v"
        r = httpx.post(rpc, timeout=20, json={
            "jsonrpc": "2.0", "id": 1, "method": "getAccountInfo",
            "params": [usdc, {"encoding": "jsonParsed"}]})
        r.raise_for_status()
        info = r.json()["result"]["value"]["data"]["parsed"]["info"]
        assert "mintAuthority" in info and "freezeAuthority" in info
        print(f"{OK} RPC ok via {rpc.split('//')[1].split('/')[0]}")
    results.append(_)

    @check("rugcheck.xyz")
    def _():
        bonk = "DezXAZ8z7PnrnRJjz3wXBoRgixCa6xjnB7YaB1pPB263"
        r = httpx.get(f"https://api.rugcheck.xyz/v1/tokens/{bonk}/report", timeout=30)
        r.raise_for_status()
        d = r.json()
        present = [k for k in ("markets", "topHolders", "risks", "rugged") if k in d]
        assert present, "tidak satu pun field yang dipakai kode ditemukan"
        print(f"{OK} field tersedia: {present}")
        if len(present) < 4:
            missing = set(("markets", "topHolders", "risks", "rugged")) - set(present)
            print(f"  ⚠️  hilang: {missing} — sesuaikan core/safety.py")
    results.append(_)

    @check("xAI Grok + Live Search")
    def _():
        key = os.getenv("XAI_API_KEY")
        assert key, "XAI_API_KEY belum diset di .env"
        r = httpx.post("https://api.x.ai/v1/chat/completions", timeout=90,
                       headers={"Authorization": f"Bearer {key}"},
                       json={"model": os.getenv("XAI_MODEL", "grok-4"),
                             "messages": [{"role": "user", "content":
                                           'Reply with JSON {"ok":true} only.'}],
                             "search_parameters": {"mode": "on",
                                                   "sources": [{"type": "x"}],
                                                   "max_search_results": 1},
                             "response_format": {"type": "json_object"}})
        if r.status_code >= 400:
            raise AssertionError(f"HTTP {r.status_code}: {r.text[:300]}")
        print(f"{OK} {r.json()['choices'][0]['message']['content'].strip()[:60]}")
    results.append(_)

    @check("Telegram")
    def _():
        tok, chat = os.getenv("TELEGRAM_BOT_TOKEN"), os.getenv("TELEGRAM_CHAT_ID")
        assert tok and chat, "TELEGRAM_BOT_TOKEN / TELEGRAM_CHAT_ID belum diset"
        r = httpx.post(f"https://api.telegram.org/bot{tok}/sendMessage", timeout=20,
                       json={"chat_id": chat, "text": "✅ Social Alpha Scanner terhubung."})
        r.raise_for_status()
        print(f"{OK} pesan tes terkirim")
    results.append(_)

    passed = sum(1 for r in results if r)
    print(f"\n{'='*46}\n{passed}/{len(results)} lolos")
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
