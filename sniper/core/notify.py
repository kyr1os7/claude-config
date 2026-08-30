"""Kirim alert ke Telegram."""
from __future__ import annotations

import html

import httpx

from .paper import Closed
from .safety import SafetyReport
from .score import Scored


def _esc(s: str) -> str:
    return html.escape(str(s), quote=False)


def format_closed(c: Closed, stats: dict) -> str:
    win = c.pnl_sol > 0
    return "\n".join([
        f"{'✅' if win else '🔴'} <b>PAPER TRADE CLOSED</b> — {_esc(c.symbol)}",
        f"Meme: {_esc(c.term)}",
        "",
        f"• Hasil: <b>{c.pnl_x:.2f}x</b> ({c.pnl_sol:+.3f} SOL, net biaya)",
        f"• Puncak: {c.peak_x:.2f}x",
        f"• Alasan tutup: {_esc(c.reason)}",
        f"• Hold: {c.held_minutes:.0f} menit",
        "",
        f"📊 Total {stats['closed']} trade · win rate <b>{stats['win_rate']:.0%}</b> · "
        f"kumulatif <b>{stats['total_sol']:+.3f} SOL</b> · {stats['open']} posisi terbuka",
    ])


def format_alert(s: Scored, safety: SafetyReport | None = None) -> str:
    c, p = s.candidate, s.pair
    lines = [
        f"🚨 <b>SOCIAL ALPHA</b> — <b>{_esc(c.term)}</b>",
        f"Gap score: <b>{s.score:.0f}</b>/100",
        "",
        f"<b>Meme</b>: {_esc(c.description)}",
        f"<b>Heat</b>: {c.heat:.0f} · <b>CT saturation</b>: {c.crypto_saturation:.0f} · {_esc(c.growth)}",
    ]
    if c.communities:
        lines.append(f"<b>Komunitas</b>: {_esc(', '.join(c.communities))}")
    if c.origin:
        lines.append(f"<b>Asal</b>: {_esc(c.origin)}")

    lines.append("")
    if p:
        lines += [
            "📈 <b>TOKEN DITEMUKAN</b>",
            f"• {_esc(p.symbol)} — {_esc(p.name)} ({_esc(p.chain)}/{_esc(p.dex)})",
            f"• CA: <code>{_esc(p.token_address)}</code>",
            f"• FDV: ${p.fdv:,.0f} · LP: ${p.liquidity_usd:,.0f}",
            f"• Umur: {p.age_hours:.1f} jam · Vol 1h: ${p.vol_h1:,.0f}",
            f"• Buy/sell 1h: {p.buys_h1}/{p.sells_h1} ({p.buy_pressure:.0%} buy)",
            f"• <a href=\"{_esc(p.url)}\">Dexscreener</a>",
        ]
    else:
        lines.append("👀 <b>WATCHLIST</b> — meme naik, token belum ada")

    if s.reasons:
        lines += ["", "<b>Kenapa</b>: " + _esc(" · ".join(s.reasons))]
    if c.evidence:
        lines += ["", "<b>Bukti</b>:"] + [f"• {_esc(u)}" for u in c.evidence[:3]]

    if safety is not None:
        lines += ["", f"<b>Safety</b>: {_esc(safety.summary())}"]
    lines += ["", "⚠️ <i>Paper trade — bukan eksekusi nyata. Verifikasi sendiri sebelum beli.</i>"]
    return "\n".join(lines)


class Telegram:
    def __init__(self, token: str, chat_id: str, timeout: float = 20.0) -> None:
        self.url = f"https://api.telegram.org/bot{token}/sendMessage"
        self.chat_id = chat_id
        self.client = httpx.Client(timeout=timeout)

    def send(self, text: str) -> bool:
        try:
            r = self.client.post(self.url, json={
                "chat_id": self.chat_id,
                "text": text,
                "parse_mode": "HTML",
                "disable_web_page_preview": True,
            })
            r.raise_for_status()
            return True
        except httpx.HTTPError as e:
            print(f"[telegram] gagal kirim: {e}")
            return False

    def close(self) -> None:
        self.client.close()
