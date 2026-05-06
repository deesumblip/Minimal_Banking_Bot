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

# Ensure level4 config and endpoints always use the correct Rasa fine-tuned model
cat > /home/codio/workspace/level4/config.yml << 'EOF'
recipe: default.v1
language: en
assistant_id: level1-agent

pipeline:
  - name: SearchReadyLLMCommandGenerator
    llm:
      model_group: rasa_command_generation_model
    flow_retrieval:
      active: false

policies:
  - name: FlowPolicy
EOF

cat > /home/codio/workspace/level4/endpoints.yml << 'EOF'
action_endpoint:
  actions_module: "actions"

nlg:
  type: rephrase
  llm:
    model_group: rasa_command_generation_model

model_groups:
  - id: rasa_command_generation_model
    models:
      - provider: rasa
        model: rasa/command-generator-llama-3.1-8b-instruct
        api_base: "https://tutorial-llm.rasa.ai"
EOF
