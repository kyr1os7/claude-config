# claude-config

Personal Claude Code configuration — memory, skills, hooks, and patterns.

## Structure

```
claude-config/
├── CLAUDE.md           # Global instructions (loads RTK.md)
├── RTK.md              # RTK token-optimization tool docs
├── settings.json       # Hooks config (PreToolUse: rtk-wrapper)
├── mcp.json.template   # MCP server template (copy + fill credentials)
├── hooks/
│   ├── rtk-rewrite.sh  # RTK command rewrite hook
│   └── rtk-wrapper.sh  # RTK wrapper for Bash tool
├── memory/
│   ├── MEMORY.md       # Memory index (auto-loaded by Claude)
│   └── *.md            # Individual memory files (feedback, reference, etc.)
└── setup.sh            # Restore script
```

## Restore / Setup on a new machine

```bash
git clone git@github.com:YOUR_USERNAME/claude-config.git
cd claude-config
bash setup.sh
# Then edit ~/.claude/mcp.json and fill in real credentials
```

## How memory works

Memory files are loaded automatically by Claude Code at the start of each conversation.  
Categories:
- `feedback_*.md` — how Claude should behave (corrections, confirmations)
- `reference_*.md` — pointers to external systems (Kintone apps, KPI sources)

## Adding new memory

Claude writes memory automatically, or manually:
```bash
# Example: add a new feedback memory
cat > ~/.claude/projects/-Users-$(whoami)-Claude/memory/feedback_new.md << 'EOF'
---
name: feedback-new
description: ...
metadata:
  type: feedback
---
...
EOF
# Then sync back to this repo:
cp ~/.claude/projects/-Users-$(whoami)-Claude/memory/*.md ~/claude-config/memory/
cd ~/claude-config && git add -A && git commit -m "sync memory" && git push
```
