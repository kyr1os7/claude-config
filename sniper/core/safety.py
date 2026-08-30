"""Rug / honeypot check.

BELUM DIIMPLEMENTASI — sengaja. Isinya chain-specific:
  - Solana : rugcheck.xyz API, cek mint & freeze authority, LP burned, top holders
  - EVM    : honeypot.is, cek buy/sell tax, ownership renounced, LP locked

Ini bukan pelengkap. Lihat catatan adverse selection di README: sebagian besar
token yang cocok dengan meme viral memang sengaja dipasang sebagai jebakan,
jadi filter inilah yang menentukan apakah strategi ini untung atau habis.
"""
from __future__ import annotations

from dataclasses import dataclass, field

from .discovery import Pair


@dataclass
class SafetyReport:
    safe: bool
    checked: bool = False
    flags: list[str] = field(default_factory=list)


def check(pair: Pair) -> SafetyReport:
    return SafetyReport(
        safe=False,
        checked=False,
        flags=["safety check belum dipasang — chain belum dipilih"],
    )
