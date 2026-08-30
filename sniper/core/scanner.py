"""Harvest kandidat meme dari X lewat Grok, lalu ukur saturasi kripto-nya."""
from __future__ import annotations

from dataclasses import dataclass, field

from .grok import Grok

HARVEST_PROMPT = """You are a cultural trend scanner, NOT a crypto analyst.

Find memes, slang, phrases, characters, images, or moments that are spreading
RIGHT NOW on X among GENERAL / NON-CRYPTO audiences, within the last {window} hours.

HARD RULES — a candidate is disqualified if any apply:
- It is older than 48 hours or already a well-established meme.
- It is primarily being discussed by crypto, trading, or "CT" accounts.
- It is a paid brand campaign, an ad, or an astroturfed trend.
- It is a major news event with no memeable short-form handle.
- Its name cannot plausibly become a 1-2 word ticker.

For each candidate, judge these HONESTLY. Do not inflate:
- heat (0-100): how widely it is spreading across ordinary timelines.
- crypto_saturation (0-100): how much crypto/CA/ticker spam is ALREADY attached
  to it. 0 = crypto has not noticed at all. 100 = every reply is a contract address.
- growth: "accelerating" | "steady" | "fading"
- communities: the DISTINCT non-crypto communities it has crossed into
  (e.g. sports fans, K-pop, gaming, political, art, general normie).
  One community only = weak signal.

Return STRICT JSON:
{{
  "candidates": [
    {{
      "term": "exact word or phrase as people write it",
      "ticker_guesses": ["SHRUB", "SHRUBS"],
      "description": "one sentence on what it is and why it spread",
      "heat": 0-100,
      "crypto_saturation": 0-100,
      "growth": "accelerating|steady|fading",
      "communities": ["...", "..."],
      "origin": "where it started, if identifiable",
      "evidence": ["https://x.com/... sample post", "..."]
    }}
  ]
}}

Return at most {limit} candidates, best signal first. If nothing genuinely
qualifies, return an empty list — an empty list is a valid and useful answer."""

SATURATION_PROMPT = """Search X for the exact term "{term}" combined with crypto
context (cashtags, "CA", contract addresses, pump.fun, launch, "dev", "ape").

Answer STRICT JSON:
{{
  "crypto_saturation": 0-100,
  "tickers_seen": ["..."],
  "contract_addresses_seen": ["..."],
  "first_crypto_mention_hours_ago": number or null,
  "verdict": "untouched|early|crowded|late"
}}

crypto_saturation 0 means no crypto account has attached a token to this term.
100 means it is fully saturated and the trade is already over."""


@dataclass
class Candidate:
    term: str
    ticker_guesses: list[str]
    description: str
    heat: float
    crypto_saturation: float
    growth: str
    communities: list[str] = field(default_factory=list)
    origin: str = ""
    evidence: list[str] = field(default_factory=list)

    @classmethod
    def from_dict(cls, d: dict) -> "Candidate":
        return cls(
            term=str(d.get("term", "")).strip(),
            ticker_guesses=[str(t).upper().lstrip("$") for t in d.get("ticker_guesses", [])],
            description=str(d.get("description", "")),
            heat=float(d.get("heat", 0)),
            crypto_saturation=float(d.get("crypto_saturation", 100)),
            growth=str(d.get("growth", "steady")),
            communities=[str(c) for c in d.get("communities", [])],
            origin=str(d.get("origin", "")),
            evidence=[str(e) for e in d.get("evidence", [])],
        )


class Scanner:
    def __init__(self, grok: Grok, cfg: dict) -> None:
        self.grok = grok
        self.cfg = cfg

    def harvest(self) -> list[Candidate]:
        window = int(self.cfg["window_hours"])
        prompt = HARVEST_PROMPT.format(window=window, limit=self.cfg["max_candidates"])
        data = self.grok.ask_json(prompt, window_hours=window, max_results=40, min_favs=200)
        out = []
        for raw in data.get("candidates", []):
            c = Candidate.from_dict(raw)
            if c.term:
                out.append(c)
        return out

    def recheck_saturation(self, term: str) -> dict:
        """Panggilan kedua, khusus term ini. Harvest cenderung meremehkan
        saturasi karena fokusnya di timeline normie; ini yang mengoreksi."""
        data = self.grok.ask_json(
            SATURATION_PROMPT.format(term=term),
            window_hours=int(self.cfg["window_hours"]),
            max_results=20,
        )
        return data
