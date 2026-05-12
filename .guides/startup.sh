#!/bin/bash
# Source rasa_env into .bashrc for every new terminal
ENV_FILE="/home/codio/workspace/secure/rasa_env"
BASHRC="/home/codio/.bashrc"
MARKER="# Codio Rasa env (do not remove)"
if ! grep -q "$MARKER" "$BASHRC" 2>/dev/null; then
  echo "" >> "$BASHRC"
  echo "$MARKER" >> "$BASHRC"
  echo "[ -f \"$ENV_FILE\" ] && source \"$ENV_FILE\"" >> "$BASHRC"
fi
