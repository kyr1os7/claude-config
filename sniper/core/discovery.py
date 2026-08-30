"""Cari token yang sudah ter-deploy untuk sebuah term, lewat Dexscreener.

Dexscreener dipilih karena chain-agnostic dan tanpa API key, jadi modul ini
tetap sama apakah nanti eksekusinya di Solana atau EVM.
"""
from __future__ import annotations

import time
from dataclasses import dataclass

import httpx

SEARCH_URL = "https://api.dexscreener.com/latest/dex/search"
TOKENS_URL = "https://api.dexscreener.com/latest/dex/tokens/{addresses}"


@dataclass
class Pair:
    chain: str
    dex: str
    pair_address: str
    token_address: str
    name: str
    symbol: str
    price_usd: float
    fdv: float
    liquidity_usd: float
    age_hours: float
    vol_h1: float
    buys_h1: int
    sells_h1: int
    url: str

    @property
    def buy_pressure(self) -> float:
        total = self.buys_h1 + self.sells_h1
        return self.buys_h1 / total if total else 0.0


def _f(d: dict | None, *keys: str, default: float = 0.0) -> float:
    cur: object = d
    for k in keys:
        if not isinstance(cur, dict):
            return default
        cur = cur.get(k)
    try:
        return float(cur)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return default


class Discovery:
    def __init__(self, cfg: dict, timeout: float = 20.0) -> None:
        self.cfg = cfg
        self.client = httpx.Client(timeout=timeout, headers={"User-Agent": "social-alpha-scanner"})

    def search(self, query: str) -> list[Pair]:
        try:
            resp = self.client.get(SEARCH_URL, params={"q": query})
            resp.raise_for_status()
        except httpx.HTTPError:
            return []
        now_ms = time.time() * 1000
        pairs = []
        for p in (resp.json().get("pairs") or []):
            created = p.get("pairCreatedAt")
            age_h = (now_ms - created) / 3_600_000 if created else 1e9
            pairs.append(
                Pair(
                    chain=p.get("chainId", ""),
                    dex=p.get("dexId", ""),
                    pair_address=p.get("pairAddress", ""),
                    token_address=(p.get("baseToken") or {}).get("address", ""),
                    name=(p.get("baseToken") or {}).get("name", ""),
                    symbol=(p.get("baseToken") or {}).get("symbol", ""),
                    price_usd=_f(p, "priceUsd"),
                    fdv=_f(p, "fdv"),
                    liquidity_usd=_f(p, "liquidity", "usd"),
                    age_hours=age_h,
                    vol_h1=_f(p, "volume", "h1"),
                    buys_h1=int(_f(p, "txns", "h1", "buys")),
                    sells_h1=int(_f(p, "txns", "h1", "sells")),
                    url=p.get("url", ""),
                )
            )
        return pairs

    def prices(self, addresses: list[str]) -> dict[str, float]:
        """Harga USD terbaru per token address. Dipakai melacak posisi paper."""
        out: dict[str, float] = {}
        for i in range(0, len(addresses), 30):   # batas Dexscreener per panggilan
            chunk = addresses[i:i + 30]
            try:
                resp = self.client.get(TOKENS_URL.format(addresses=",".join(chunk)))
                resp.raise_for_status()
            except httpx.HTTPError:
                continue
            for p in (resp.json().get("pairs") or []):
                addr = (p.get("baseToken") or {}).get("address")
                price = _f(p, "priceUsd")
                # Beberapa pair per token; pakai yang likuiditasnya terbesar.
                if addr and price > 0:
                    liq = _f(p, "liquidity", "usd")
                    prev = out.get(addr)
                    if prev is None or liq > out.get(f"_liq_{addr}", 0):
                        out[addr] = price
                        out[f"_liq_{addr}"] = liq
        return {k: v for k, v in out.items() if not k.startswith("_liq_")}

    def find(self, term: str, tickers: list[str]) -> list[Pair]:
        """Cari term + semua tebakan ticker, lalu saring pakai config."""
        seen: dict[str, Pair] = {}
        for q in [term, *tickers]:
            for p in self.search(q):
                if p.token_address and p.token_address not in seen:
                    seen[p.token_address] = p
        return [p for p in seen.values() if self._passes(p)]

    def _passes(self, p: Pair) -> bool:
        c = self.cfg
        return (
            p.chain in c["chains"]
            and p.age_hours <= c["max_pair_age_hours"]
            and p.liquidity_usd >= c["min_liquidity_usd"]
            and 0 < p.fdv <= c["max_fdv_usd"]
        )

    def close(self) -> None:
        self.client.close()
