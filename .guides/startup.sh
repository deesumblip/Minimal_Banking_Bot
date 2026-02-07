#!/bin/bash
# Load Rasa license and OpenAI API key for students (values hidden in .guides/secure)
if [ -f "/home/codio/workspace/.guides/secure/rasa_env" ]; then
  source /home/codio/workspace/.guides/secure/rasa_env
fi