**Starting point:** Chapter 1.4 assumes you began with the **final banking agent at the end of Chapter 1.3** and added transfer pieces in **`level4/`** (see **`Level4_Unit0_Content_0.1_Your-Level-3-Banking-Agent.md`**).

**Objective.** Train your Level 4 agent from the **`level4`** folder using the same pattern as Level 3: activate the virtual environment at the **project root**, then `cd level4` and run Rasa.

**What training uses:** Rasa reads your **domain** (slots and `utter_ask_*` responses), your **flows** (including `transfer_money`), and your **actions** (including `action_process_transfer`). If training fails, the messages usually point to **Lab 2.1** (domain), **Lab 3.1** (action), or **Lab 4.1** (flow).

After training succeeds, use **Check It!** in Codio (**Lab 5.1** assessment). Then continue to **Lab 5.2** for the completion check and Inspector.

---

## Part 1: In Codio

1. Open the terminal (starts at `~/workspace`, the project root).
2. Run `source .venv/bin/activate` — prompt should show `(.venv)`.
3. Run `cd level4` — confirm with `pwd` that the path ends in `level4`.
4. Run `python -m rasa --version`. If it fails, check the venv and Rasa Pro (**Lab 0.1**).
5. **Pipeline check (important):** Open **`config.yml`** in this **`level4/`** folder. It must use **`CompactLLMCommandGenerator`** for Chapter 1.4 (not **`SearchReadyLLMCommandGenerator`** from Chapter 1.3). If you copied **`level3/` → `level4/`** without **Unit 0.2** pipeline updates, fix **`config.yml`** and **`endpoints.yml`** first—otherwise training **bakes the wrong command generator** into the model and you can see *“unable to understand you”* on transfer slots. Compare with this repo’s **`level4/config.yml`** if unsure.
6. **Endpoints check:** Open **`endpoints.yml`**. Under **`model_groups`**, the group with **`id: gpt-4o-mini`** must use **`model: gpt-4o-2024-11-20`** and **`temperature: 0.1`** (see **Unit 0.2** section 2). Do **not** leave **`model: gpt-4o-mini-…`** with a high **`temperature`** here—free-text **recipient** often fails to fill reliably. Match this repo’s **`level4/endpoints.yml`**.
7. Run `python -m rasa train` — wait for **Successfully saved model** (about 1–3 minutes).
8. In the file tree, confirm **`models/`** (under **`level4`**) has a new `.tar.gz` file.

### Troubleshooting

| Symptom | What to check |
|--------|----------------|
| Slot or `utter_ask_*` errors | `level4/domain/basics.yml` (Lab 2.1) |
| Flow / collect errors | `level4/data/basics/transfer_money.yml` (Lab 4.1) |
| Action errors | `level4/actions/action_process_transfer.py` (Lab 3.1) |
| `No module named 'rasa'` | Activate `.venv` from project root, then `cd level4` again |
| License / API key | `.env` and Lab 0.1 |
| Transfer slots mis-fill; *unable to understand you*; logs show **`SearchReadyLLMCommandGenerator`** | **`level4/config.yml`** must use **`CompactLLMCommandGenerator`**. Fix config, **`python -m rasa train`** again from **`level4`**, restart Inspector (**Lab 5.2**, **`PIPELINE_CHAPTER_1_3_AND_4.md`** *—repository Markdown; not a guide page*) |
| **Recipient** name skips or wrong; **FillSlot** flaky; **`config.yml`** already uses **Compact** | **`level4/endpoints.yml`**: **`model_groups`** for **`gpt-4o-mini`** should use **`gpt-4o-2024-11-20`** and **`temperature: 0.1`** (**Unit 0.2**). Retrain from **`level4/`** |

When steps are complete, run **Check It!** for Lab 5.1 in Codio.

---

## Part 2: Running locally

1. Open your OS terminal and `cd` to the project root (folder with `level1` … `level4`, `.guides`).
2. Activate `.venv` (PowerShell: `.venv\Scripts\Activate.ps1`; CMD: `.venv\Scripts\activate.bat`; macOS/Linux: `source .venv/bin/activate`).
3. `cd level4`.
4. **Pipeline check:** Same as Part 1 step 5—**`CompactLLMCommandGenerator`** in **`level4/config.yml`** before training.
5. **Endpoints check:** Same as Part 1 step 6—**`level4/endpoints.yml`** **`model_groups`** matches **Unit 0.2** / this repo.
6. Ensure `.env` has `RASA_LICENSE` and `OPENAI_API_KEY` (Lab 0.1).
7. Run `python -m rasa train` until **Successfully saved model**.
8. Confirm a new `.tar.gz` in `level4/models/`.

Then proceed to **Lab 5.2** — run the **completion check**, then **Inspector** using the **scripted transfer** table in Lab 5.2 (amount → recipient → account → demo confirmation).
