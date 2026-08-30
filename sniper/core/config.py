"""Config loading: config.yaml for tunables, .env for secrets."""
from __future__ import annotations

import os
from pathlib import Path

import yaml
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent


class Config:
    def __init__(self, path: Path | None = None) -> None:
        load_dotenv(ROOT / ".env")
        raw = yaml.safe_load((path or ROOT / "config.yaml").read_text())
        self.scanner = raw["scanner"]
        self.filters = raw["filters"]
        self.discovery = raw["discovery"]
        self.scoring = raw["scoring"]
        self.store = raw["store"]

    @property
    def xai_key(self) -> str:
        return self._require("XAI_API_KEY")

    @property
    def tg_token(self) -> str:
        return self._require("TELEGRAM_BOT_TOKEN")

    @property
    def tg_chat(self) -> str:
        return self._require("TELEGRAM_CHAT_ID")

    @staticmethod
    def _require(name: str) -> str:
        val = os.getenv(name)
        if not val:
            raise RuntimeError(f"{name} belum diset di .env")
        return val
