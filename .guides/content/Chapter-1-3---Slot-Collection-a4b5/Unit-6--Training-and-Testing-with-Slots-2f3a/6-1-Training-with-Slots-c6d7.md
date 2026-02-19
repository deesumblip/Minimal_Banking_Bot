# 6.1 Training with Slots

Training with slots is similar to Level 2, but Rasa now also processes slot definitions.

## Training Command

From the **project root**, activate the virtual environment, then go to `level3` and run:

```bash
cd level3
python -m rasa train
```

(On Codio the terminal opens at `~/workspace`; run `source .venv/bin/activate` then `cd level3` before the command above.)

## What Happens During Training

Rasa:
1. Reads slot definitions from `domain/basics.yml`
2. Validates slot types and structure
3. Processes flows with `collect:` steps
4. Ensures `utter_ask_*` responses exist for collected slots
5. Creates model with slot information

Wait for "Successfully saved model". A new `.tar.gz` file will appear in `level3/models/`.

**Do the training in Lab 6.1: Training and Testing with Slots** (Part 1 or Part 2), then run the assessment when done.
