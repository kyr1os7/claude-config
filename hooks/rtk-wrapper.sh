#!/usr/bin/env bash
# Wrapper untuk RTK hook — menambahkan PATH agar rtk bisa ditemukan saat eksekusi

RTK_BIN="/Users/sandypratamatelaumbanua/.local/bin"

# Jalankan RTK hook dengan PATH yang benar agar hook bisa menemukan rtk
INPUT=$(cat)
OUTPUT=$(echo "$INPUT" | env PATH="$RTK_BIN:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin" /Users/sandypratamatelaumbanua/.claude/hooks/rtk-rewrite.sh 2>/dev/null)
EXIT_CODE=$?

if [ -z "$OUTPUT" ]; then
  exit $EXIT_CODE
fi

# Ambil command hasil rewrite dari JSON
CMD=$(echo "$OUTPUT" | jq -r '.hookSpecificOutput.updatedInput.command // empty' 2>/dev/null)

if [ -z "$CMD" ]; then
  echo "$OUTPUT"
  exit 0
fi

# Tambahkan PATH ke command hasil rewrite agar rtk bisa ditemukan saat eksekusi
PATCHED="export PATH=\"$RTK_BIN:\$PATH\" && $CMD"

# Kembalikan JSON dengan command yang sudah di-patch
echo "$OUTPUT" | jq --arg cmd "$PATCHED" '.hookSpecificOutput.updatedInput.command = $cmd'
