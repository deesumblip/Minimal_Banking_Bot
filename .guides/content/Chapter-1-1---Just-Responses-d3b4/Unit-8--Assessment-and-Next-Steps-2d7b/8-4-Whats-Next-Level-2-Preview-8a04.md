To restart your bot, click **[Start Rasa Inspector](open_terminal panel=1; cmd bash /home/codio/workspace/.guides/scripts/start_rasa_inspect.sh)**. Then click Rasa Inspect in the main toolbar above to load the chat tab.

Level 2 **builds on your existing Level 1 bot** (same domain, same flows; no new bot).

**Level 2 adds**: Custom Python actions; new flows that use actions; action registration in the domain (`actions:` section).

**Example**: "What are your bank hours?" – Level 1 would need a static response; Level 2 uses `action_bank_hours` (Python) for dynamic hours. You'll create the action class, register it, and add a flow that calls it.
