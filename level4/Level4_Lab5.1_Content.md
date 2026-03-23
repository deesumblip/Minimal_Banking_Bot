**Objective.** Train your Level 4 bot from the **`level4`** folder using the same pattern as Level 3: activate the virtual environment at the **project root**, then `cd level4` and run Rasa.

**What training uses:** Rasa reads your **domain** (slots and `utter_ask_*` responses), your **flows** (including `transfer_money`), and your **actions** (including `action_process_transfer`). If training fails, the messages usually point to **Lab 2.1** (domain), **Lab 3.1** (action), or **Lab 4.1** (flow).

After training succeeds, use **Check It!** in Codio (**Lab 5.1** assessment). Then continue to **Lab 5.2** for the completion check and Inspector.

---

## Part 1: In Codio

1. Open the terminal (starts at `~/workspace`, the project root).
2. Run `source .venv/bin/activate` — prompt should show `(.venv)`.
3. Run `cd level4` — confirm with `pwd` that the path ends in `level4`.
4. Run `python -m rasa --version`. If it fails, check the venv and Rasa Pro (**Lab 0.1**).
5. Run `python -m rasa train` — wait for **Successfully saved model** (about 1–3 minutes).
6. In the file tree, confirm `level4/models/` has a new `.tar.gz` file.

### Troubleshooting

| Symptom | What to check |
|--------|----------------|
| Slot or `utter_ask_*` errors | `level4/domain/basics.yml` (Lab 2.1) |
| Flow / collect errors | `level4/data/basics/transfer_money.yml` (Lab 4.1) |
| Action errors | `level4/actions/action_process_transfer.py` (Lab 3.1) |
| `No module named 'rasa'` | Activate `.venv` from project root, then `cd level4` again |
| License / API key | `.env` and Lab 0.1 |

When steps are complete, run **Check It!** for Lab 5.1 in Codio.

---

## Part 2: Running locally

1. Open your OS terminal and `cd` to the project root (folder with `level1` … `level4`, `.guides`).
2. Activate `.venv` (PowerShell: `.venv\Scripts\Activate.ps1`; CMD: `.venv\Scripts\activate.bat`; macOS/Linux: `source .venv/bin/activate`).
3. `cd level4`.
4. Ensure `.env` has `RASA_LICENSE` and `OPENAI_API_KEY` (Lab 0.1).
5. Run `python -m rasa train` until **Successfully saved model**.
6. Confirm a new `.tar.gz` in `level4/models/`.

Then proceed to **Lab 5.2**.
