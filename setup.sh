#!/bin/bash
# Restore Claude config from this repo to ~/.claude
# Usage: bash setup.sh

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
CLAUDE_DIR="$HOME/.claude"
MEMORY_DIR="$CLAUDE_DIR/projects/-Users-$(whoami)-Claude/memory"

echo "Installing Claude config from $REPO_DIR..."

# Core config files
cp "$REPO_DIR/CLAUDE.md" "$CLAUDE_DIR/"
cp "$REPO_DIR/RTK.md" "$CLAUDE_DIR/"
cp "$REPO_DIR/settings.json" "$CLAUDE_DIR/"

# Hooks
mkdir -p "$CLAUDE_DIR/hooks"
cp "$REPO_DIR/hooks/"* "$CLAUDE_DIR/hooks/"
chmod +x "$CLAUDE_DIR/hooks/"*.sh

# Memory
mkdir -p "$MEMORY_DIR"
cp "$REPO_DIR/memory/"*.md "$MEMORY_DIR/"

# MCP config (manual step)
if [ ! -f "$CLAUDE_DIR/mcp.json" ]; then
  echo ""
  echo "ACTION REQUIRED: Copy mcp.json.template to ~/.claude/mcp.json"
  echo "and fill in your actual credentials."
  cp "$REPO_DIR/mcp.json.template" "$CLAUDE_DIR/mcp.json"
fi

echo ""
echo "Done! Claude config restored."
