# 6.1 Training with Slots

Training with slots is similar to Level 2. Rasa now also processes slot definitions.

## Training Command

From the **project root**, activate the virtual environment, then go to `level3` and run:

```bash
cd level3
python -m rasa train
```

On Codio the terminal opens at `~/workspace`. Run `source .venv/bin/activate` then `cd level3` before the command above.

## What Happens During Training

Rasa reads slot definitions from `domain/basics.yml`, validates slot types and structure, processes flows with `collect:` steps, ensures `utter_ask_*` responses exist for collected slots, and creates a model with slot information.

Wait for "Successfully saved model". A new `.tar.gz` file will appear in `level3/models/`.

You'll do the training in **Lab 6.1** (Part 1 or Part 2), then run the assessment when done.
