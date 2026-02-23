# 7.1 Complete Bot Walkthrough

A full conversation ties together Level 1 (responses), Level 2 (actions), and Level 3 (slot memory).

You'll do the walkthrough in **Lab 7.1**. You will start Inspector and run a session start so the bot greets you. You'll say "Check my balance" and the bot will ask for the account (slot empty). You'll provide "1234" and the bot will store it, run the action, and reply with the balance. You'll say "What's my balance?" again and the bot will remember 1234 and reply without asking (slot persistence). You'll say "What are your hours?" and the Level 2 flow will run.

Levels 1, 2, and 3 work together: responses, actions, and slot memory. Lab 7.1 has no graded assessment.
