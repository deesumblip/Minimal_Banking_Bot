#!/bin/bash
# Codio runs this file from .guides/startup.sh (NOT from .guides/secure/startup.sh).
# We add a source line to ~/.bashrc so every NEW terminal loads the vars
# (startup.sh runs in one process; terminals don't inherit it otherwise).
ENV_FILE=""
if [ -f "/home/codio/workspace/.guides/secure/rasa_env" ]; then
  ENV_FILE="/home/codio/workspace/.guides/secure/rasa_env"
elif [ -f "/home/codio/workspace/secure/rasa_env" ]; then
  ENV_FILE="/home/codio/workspace/secure/rasa_env"
fi
if [ -n "$ENV_FILE" ]; then
  BASHRC="/home/codio/.bashrc"
  MARKER="# Codio Rasa env (do not remove)"
  if ! grep -q "$MARKER" "$BASHRC" 2>/dev/null; then
    echo "" >> "$BASHRC"
    echo "$MARKER" >> "$BASHRC"
    echo "[ -f \"$ENV_FILE\" ] && source \"$ENV_FILE\"" >> "$BASHRC"
  fi
fi