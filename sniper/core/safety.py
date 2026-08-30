"""Safety check Solana: mint/freeze authority, LP lock, sebaran holder.

Dua lapis, sengaja:

  1. RPC Solana langsung — mint authority & freeze authority. Ini fakta
     on-chain yang otoritatif; kalau mint authority masih hidup, dev bisa
     mencetak suplai tak terbatas kapan saja dan tidak ada skor vendor yang
     membuat itu aman.
  2. rugcheck.xyz — LP lock, konsentrasi holder, insider, risiko terkenal.

Modul ini FAIL-CLOSED: kalau pengecekan gagal atau timeout, token dianggap
TIDAK aman. Diam-diam meloloskan token karena API mati adalah cara paling
mudah kehilangan uang di strategi ini.
"""
from __future__ import annotations

import os
from dataclasses import dataclass, field

import httpx

RUGCHECK_URL = "https://api.rugcheck.xyz/v1/tokens/{mint}/report"
PUBLIC_RPC = "https://api.mainnet-beta.solana.com"

# Alamat yang wajar memegang porsi besar dan bukan tanda bahaya.
BURN_ADDRESSES = {
    "11111111111111111111111111111111",
    "1nc1nerator11111111111111111111111111111111",
}


@dataclass
class SafetyReport:
    safe: bool
    checked: bool = False
    flags: list[str] = field(default_factory=list)      # pemblokir keras
    warnings: list[str] = field(default_factory=list)   # catatan lunak

    def summary(self) -> str:
        if not self.checked:
            return "⚠️ safety check tidak selesai"
        if self.flags:
            return "⛔ " + " · ".join(self.flags)
        return "✅ lolos" + (f" (catatan: {', '.join(self.warnings)})" if self.warnings else "")


class SolanaSafety:
    def __init__(self, cfg: dict, timeout: float = 20.0) -> None:
        self.cfg = cfg
        self.rpc = os.getenv("SOLANA_RPC_URL") or PUBLIC_RPC
        self.client = httpx.Client(timeout=timeout,
                                   headers={"User-Agent": "social-alpha-scanner"})

    # ---------- lapis 1: RPC otoritatif ----------

    def _authorities(self, mint: str) -> tuple[str | None, str | None]:
        """Return (mintAuthority, freezeAuthority). Raise kalau tidak terbaca."""
        r = self.client.post(self.rpc, json={
            "jsonrpc": "2.0", "id": 1, "method": "getAccountInfo",
            "params": [mint, {"encoding": "jsonParsed"}],
        })
        r.raise_for_status()
        value = (r.json().get("result") or {}).get("value")
        if not value:
            raise ValueError("akun mint tidak ditemukan")
        info = value["data"]["parsed"]["info"]
        return info.get("mintAuthority"), info.get("freezeAuthority")

    # ---------- lapis 2: rugcheck ----------

    def _rugcheck(self, mint: str) -> dict:
        r = self.client.get(RUGCHECK_URL.format(mint=mint))
        r.raise_for_status()
        return r.json()

    # ---------- gabungan ----------

    def check(self, mint: str) -> SafetyReport:
        rep = SafetyReport(safe=False)
        c = self.cfg

        try:
            mint_auth, freeze_auth = self._authorities(mint)
        except Exception as e:
            rep.flags.append(f"gagal baca authority: {e}")
            return rep

        if c.get("require_authorities_revoked", True):
            if mint_auth:
                rep.flags.append("mint authority masih aktif (suplai bisa dicetak)")
            if freeze_auth:
                rep.flags.append("freeze authority masih aktif (token bisa dibekukan)")

        try:
            rc = self._rugcheck(mint)
        except Exception as e:
            rep.flags.append(f"rugcheck tidak terjangkau: {e}")
            return rep

        if rc.get("rugged"):
            rep.flags.append("ditandai rugged oleh rugcheck")

        # LP lock — ambil market dengan likuiditas terbesar.
        markets = rc.get("markets") or []
        lp_pcts = []
        for m in markets:
            lp = m.get("lp") or {}
            pct = lp.get("lpLockedPct")
            if pct is not None:
                lp_pcts.append(float(pct))
        if lp_pcts:
            best_lp = max(lp_pcts)
            if best_lp < c.get("min_lp_locked_pct", 80):
                rep.flags.append(f"LP terkunci hanya {best_lp:.0f}%")
        else:
            rep.flags.append("status LP lock tidak terbaca")

        # Sebaran holder — abaikan alamat burn dan pool LP.
        lp_addrs = {
            (m.get("liquidityA") or "") for m in markets
        } | {(m.get("liquidityB") or "") for m in markets}
        holders = []
        for h in (rc.get("topHolders") or []):
            addr = h.get("address", "")
            if addr in BURN_ADDRESSES or addr in lp_addrs or h.get("isLP"):
                continue
            holders.append(h)

        if holders:
            top = float(holders[0].get("pct", 0))
            top10 = sum(float(h.get("pct", 0)) for h in holders[:10])
            if top > c.get("max_top_holder_pct", 15):
                rep.flags.append(f"holder terbesar {top:.1f}%")
            if top10 > c.get("max_top10_pct", 40):
                rep.flags.append(f"top-10 pegang {top10:.1f}%")
            insiders = sum(1 for h in holders[:20] if h.get("insider"))
            if insiders:
                rep.warnings.append(f"{insiders} wallet insider di top-20")
        else:
            rep.warnings.append("data holder kosong")

        for risk in (rc.get("risks") or []):
            if str(risk.get("level", "")).lower() in ("danger", "high"):
                rep.flags.append(f"rugcheck: {risk.get('name')}")

        rep.checked = True
        rep.safe = not rep.flags
        return rep

    def close(self) -> None:
        self.client.close()
