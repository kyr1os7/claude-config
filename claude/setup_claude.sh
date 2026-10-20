#!/bin/bash
# Setup Funtoco automation untuk Claude
# Usage: bash <(curl -fsSL https://raw.githubusercontent.com/kyr1os7/claude-config/main/claude/setup_claude.sh)
set -e

BLOCK_URL="https://raw.githubusercontent.com/kyr1os7/claude-config/main/claude/CLAUDE.md"
CLAUDE_DIR="$HOME/.claude"
CLAUDE_FILE="$CLAUDE_DIR/CLAUDE.md"

# 1. Ambil blok bootstrap dari GitHub
BLOCK="$(curl -fsSL "$BLOCK_URL")" || {
  echo "ERROR: gagal mengambil $BLOCK_URL. ~/.claude/CLAUDE.md tidak diubah."
  exit 1
}

# 2. Tambahkan ke ~/.claude/CLAUDE.md (tidak menimpa isi lain)
mkdir -p "$CLAUDE_DIR"
touch "$CLAUDE_FILE"
if grep -q -e "FUNTOCO-AUTOMATION:START" -e "## Automation Bootstrap" "$CLAUDE_FILE"; then
  echo "Bootstrap sudah ada di $CLAUDE_FILE — tidak diubah."
else
  if [ -s "$CLAUDE_FILE" ]; then
    cp "$CLAUDE_FILE" "$CLAUDE_FILE.bak.$(date +%Y%m%d%H%M%S)"
    printf '\n' >> "$CLAUDE_FILE"
  fi
  printf '%s\n' "$BLOCK" >> "$CLAUDE_FILE"
  echo "Bootstrap ditambahkan ke $CLAUDE_FILE"
fi

echo ""
echo "Selesai. Lanjut ke Langkah 4 di panduan: https://github.com/kyr1os7/claude-config/blob/main/claude/SETUP_CLAUDE.md"
