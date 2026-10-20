#!/bin/bash
# Setup Funtoco automation untuk Codex
# Usage: bash <(curl -fsSL https://raw.githubusercontent.com/kyr1os7/claude-config/main/codex/setup_codex.sh)
set -e

REPO_URL="https://github.com/kyr1os7/claude-config.git"
REPO_DIR="$HOME/funtoco-automation"
CODEX_DIR="$HOME/.codex"
AGENTS_FILE="$CODEX_DIR/AGENTS.md"

# 1. Clone / update repo prompt
if [ -d "$REPO_DIR/.git" ]; then
  echo "Update repo di $REPO_DIR ..."
  git -C "$REPO_DIR" pull --ff-only
else
  echo "Clone repo ke $REPO_DIR ..."
  git clone "$REPO_URL" "$REPO_DIR"
fi

# 2. Tambahkan bootstrap ke ~/.codex/AGENTS.md (tidak menimpa isi lain)
if [ ! -f "$REPO_DIR/codex/AGENTS.md" ]; then
  echo "ERROR: $REPO_DIR/codex/AGENTS.md tidak ditemukan. ~/.codex/AGENTS.md tidak diubah."
  exit 1
fi
mkdir -p "$CODEX_DIR"
touch "$AGENTS_FILE"
if grep -q "FUNTOCO-AUTOMATION:START" "$AGENTS_FILE"; then
  echo "Bootstrap sudah ada di $AGENTS_FILE — tidak diubah."
  echo "(Kalau mau update, hapus blok FUNTOCO-AUTOMATION:START..END lalu jalankan ulang.)"
else
  if [ -s "$AGENTS_FILE" ]; then
    cp "$AGENTS_FILE" "$AGENTS_FILE.bak.$(date +%Y%m%d%H%M%S)"
    printf '\n' >> "$AGENTS_FILE"
  fi
  cat "$REPO_DIR/codex/AGENTS.md" >> "$AGENTS_FILE"
  echo "Bootstrap ditambahkan ke $AGENTS_FILE (backup lama disimpan dengan akhiran .bak.*)"
fi

echo ""
echo "Selesai. Lanjut ke Langkah 4 di panduan: https://github.com/kyr1os7/claude-config/blob/main/codex/SETUP_CODEX.md"
