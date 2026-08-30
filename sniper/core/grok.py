"""Client xAI (Grok) dengan Live Search ke X.

CATATAN: bentuk payload `search_parameters` mengikuti Live Search xAI. Kalau
xAI mengubah skemanya, satu-satunya tempat yang perlu diedit adalah
`_search_params()` di bawah. Verifikasi di https://docs.x.ai/docs/guides/live-search
"""
from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone

import httpx

API_URL = "https://api.x.ai/v1/chat/completions"


class Grok:
    def __init__(self, api_key: str, model: str = "grok-4", timeout: float = 120.0) -> None:
        self.model = model
        self.client = httpx.Client(
            timeout=timeout,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
        )

    @staticmethod
    def _search_params(window_hours: int, max_results: int,
                       min_favs: int | None = None) -> dict:
        since = datetime.now(timezone.utc) - timedelta(hours=window_hours)
        x_source: dict = {"type": "x"}
        if min_favs is not None:
            # Saring post receh supaya sinyal tidak tenggelam oleh noise.
            x_source["post_favorite_count"] = min_favs
        return {
            "mode": "on",
            "sources": [x_source, {"type": "web"}, {"type": "news"}],
            "from_date": since.strftime("%Y-%m-%d"),
            "max_search_results": max_results,
            "return_citations": True,
        }

    def ask_json(self, prompt: str, *, window_hours: int,
                 max_results: int = 30, min_favs: int | None = None) -> dict:
        body = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "search_parameters": self._search_params(window_hours, max_results, min_favs),
            "response_format": {"type": "json_object"},
            "temperature": 0.3,
        }
        resp = self.client.post(API_URL, json=body)
        resp.raise_for_status()
        data = resp.json()
        content = data["choices"][0]["message"]["content"]
        parsed = json.loads(content)
        parsed["_citations"] = data.get("citations", [])
        return parsed

    def close(self) -> None:
        self.client.close()
