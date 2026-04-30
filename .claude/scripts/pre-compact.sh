#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

INPUT=$(cat)
IFS=$'\t' read -r TRANSCRIPT_PATH TRIGGER <<< "$(echo "$INPUT" | bash "$SCRIPT_DIR/find-python.sh" -c "
import json,sys
d=json.load(sys.stdin)
print(d.get('transcript_path','') + '\t' + d.get('trigger','unknown'))
" 2>/dev/null || printf '\tunknown')"

if [ -n "$TRANSCRIPT_PATH" ] && [ -f "$TRANSCRIPT_PATH" ]; then
  VAULT_DIR="${CLAUDE_PROJECT_DIR:-$(pwd)}"
  BACKUP_DIR="$VAULT_DIR/thinking/session-logs"
  mkdir -p "$BACKUP_DIR"
  TIMESTAMP=$(date +%Y%m%d_%H%M%S)
  BACKUP_PATH="$BACKUP_DIR/session_${TRIGGER}_${TIMESTAMP}.jsonl"
  cp "$TRANSCRIPT_PATH" "$BACKUP_PATH"

  # Keep last 30 backups, prune older ones
  ls -t "$BACKUP_DIR"/session_*.jsonl 2>/dev/null | tail -n +31 | xargs rm -f 2>/dev/null || true

  # Auto-summarize via local ollama (detached; must never block compaction).
  # Only on auto-compaction — manual compactions mean the user is actively
  # driving and the summary would land too late to matter that session.
  if [ "$TRIGGER" = "auto" ] && [ "${OM_SUMMARIZER_DISABLE:-}" != "1" ]; then
    LOG_FILE="$VAULT_DIR/thinking/session-summaries/.summarizer.log"
    mkdir -p "$(dirname "$LOG_FILE")"
    nohup bash "$SCRIPT_DIR/find-python.sh" "$SCRIPT_DIR/summarize-session.py" \
      --transcript "$BACKUP_PATH" \
      --vault "$VAULT_DIR" \
      >>"$LOG_FILE" 2>&1 &
    disown 2>/dev/null || true
  fi
fi

exit 0
