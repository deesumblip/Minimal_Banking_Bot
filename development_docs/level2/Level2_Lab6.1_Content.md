Training in Level 2 is the same idea as Level 1: you run `rasa train` and Rasa writes a packaged model under **`models/`**. What changes is that Rasa now **also reads your custom actions** under **`actions/`** and folds them together with **`domain/`** and **`data/`**—so the model knows about `action_bank_hours` and `action_holiday_hours`, not only `utter_*` responses.

You should already have finished **Labs 3.1–5.1**: both actions appear in the domain, **`hours.yml`** uses `action_bank_hours`, and **`holiday_hours.yml`** uses `action_holiday_hours`.

Open a terminal with your **virtual environment activated from the project root** (the directory that contains **`level2/`**), then train from inside **`level2/`**:

```bash
cd level2
python -m rasa train
```

When that command runs, Rasa loads flows from **`data/`**—including **`hours.yml`**, **`holiday_hours.yml`**, and your unchanged Level 1 flows. It loads **`domain/`** (Level 1 responses and every entry under **`actions:`**). It checks that each registered action has a matching file under **`actions/`**, with a proper class and a **`name()`** that matches the domain. It then writes a **`.tar.gz`** into **`models/`** that includes that registration.

After a successful run, use **Lab 6.2** for Inspector setup plus a short testing checklist (example prompts, debug panel, common issues), and the extra domain/training verification assessment.

Submit the **Check It!** in the Codio guide once training has finished without errors and **`level2/models/`** contains at least one new **`.tar.gz`** (assessment `code-output-compare-1070925386`).
