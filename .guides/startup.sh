#!/bin/bash
# Preload Rasa env vars for every terminal (secure/rasa_env or .guides/secure/rasa_env)
if [ -f "/home/codio/workspace/secure/rasa_env" ]; then
  source /home/codio/workspace/secure/rasa_env
elif [ -f "/home/codio/workspace/.guides/secure/rasa_env" ]; then
  source /home/codio/workspace/.guides/secure/rasa_env
fi