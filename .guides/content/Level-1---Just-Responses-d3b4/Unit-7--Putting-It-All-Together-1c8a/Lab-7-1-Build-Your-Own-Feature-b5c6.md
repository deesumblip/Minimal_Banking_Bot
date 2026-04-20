**Objective:** Add one new response and one new flow to your banking agent, then test it.

#### Steps

1. Add a new response to `domain/basics.yml`, for example branch locations or an FAQ.
2. Create a new flow file in `data/basics/` that uses it. Use a clear `description:`.
3. Stop Inspector if it is running (Ctrl+C in the Inspector terminal).
4. Train from `level1` with the venv active:

```bash
cd /home/codio/workspace
source .venv/bin/activate
cd level1
python -m rasa train
```

5. Once training finishes, start Inspector again and test your new flow.

> To restart Inspector, click **[Start Rasa Inspector](open_terminal panel=1. Cmd bash /home/codio/workspace/.guides/scripts/start_rasa_inspect.sh)**, then click **Rasa Inspect** in the toolbar.

> Always stop the old Inspector before training and start a new session after. An open Inspector session uses the previous model until restarted.

**Use Check It!** below when done (Codio).

{Check It!|assessment}(code-output-compare-7772000001)


