"""Gap score: seberapa lebar jarak antara 'normie sudah meme-in' dan 'CT sudah trading'.

Skor tinggi butuh SEMUA ini benar sekaligus:
  - meme-nya panas di timeline normie
  - masih naik, bukan datar/turun
  - sudah lintas beberapa komunitas
  - kripto BELUM ramai
  - ada token yang bisa dibeli, masih muda, likuiditasnya hidup
"""
from __future__ import annotations

from dataclasses import dataclass

from .discovery import Pair
from .scanner import Candidate
from .store import Velocity

GROWTH_WEIGHT = {"accelerating": 1.0, "steady": 0.65, "fading": 0.15}


@dataclass
class Scored:
    candidate: Candidate
    pair: Pair | None
    score: float
    reasons: list[str]


def score(c: Candidate, v: Velocity, pair: Pair | None) -> Scored:
    reasons: list[str] = []

    heat = c.heat / 100.0
    gap = max(0.0, 1.0 - c.crypto_saturation / 100.0)
    growth = GROWTH_WEIGHT.get(c.growth, 0.5)

    # Velocity terukur menimpa klaim growth dari model kalau datanya ada.
    if v.samples >= 2:
        if v.per_hour > 3:
            growth = 1.0
            reasons.append(f"heat naik {v.per_hour:.1f}/jam selama {v.age_hours:.1f}h")
        elif v.per_hour < -2:
            growth = 0.1
            reasons.append(f"heat turun {v.per_hour:.1f}/jam — sudah lewat")

    spread = min(len(c.communities) / 3.0, 1.0)
    if len(c.communities) >= 3:
        reasons.append(f"lintas {len(c.communities)} komunitas")
    if c.crypto_saturation <= 15:
        reasons.append("CT belum sadar")

    base = 100.0 * heat * gap * growth * (0.55 + 0.45 * spread)

    if pair is None:
        # Meme-nya bagus tapi belum ada token: layak dipantau, belum layak beli.
        reasons.append("belum ada token — pantau")
        return Scored(c, None, base * 0.4, reasons)

    if pair.age_hours <= 3:
        base *= 1.15
        reasons.append(f"token baru {pair.age_hours:.1f} jam")
    if pair.buy_pressure >= 0.6:
        base *= 1.1
        reasons.append(f"buy pressure {pair.buy_pressure:.0%}")
    elif pair.buy_pressure <= 0.35:
        base *= 0.7
        reasons.append(f"jual dominan ({pair.buy_pressure:.0%} buy)")
    if pair.liquidity_usd < 15000:
        base *= 0.8
        reasons.append("likuiditas tipis")

    return Scored(c, pair, min(base, 100.0), reasons)
