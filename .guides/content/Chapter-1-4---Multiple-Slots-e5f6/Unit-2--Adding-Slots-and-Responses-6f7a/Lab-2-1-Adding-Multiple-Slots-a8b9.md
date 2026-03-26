**Objective.** In Unit 2 you saw an example of the slots, ask responses, and action registration for the transfer flow. In this lab you will add your own version to `level4/domain/basics.yml`:

**Starting point:** Your **`level4/`** folder should already include the baseline banking agent (**Unit 0.1**). You are **adding** transfer domain fields on top of that baseline, not replacing the whole project.

**Prerequisite:** Complete **Lab 0.1** (Unit 0): fill-in-the-blanks, paste into **`level4/config.yml`** and **`level4/endpoints.yml`**, pass the **Code Test** (fill-in-the-blanks → paste → assessed file). See **Unit 0.2** for what those files must contain. If you **skipped Lab 0.1**, do it **before** this lab.

- Add the slots `amount`, `recipient`, and `account_from`
- Add the ask responses `utter_ask_amount`, `utter_ask_recipient`, and `utter_ask_account_from`
- Register the new action `action_process_transfer` (you will create the .py file in Lab 3.1)

## Step-by-Step Instructions

**Step 1.** Open `domain/basics.yml` in the `level4` folder. You should see your existing content (slots with `account`, responses, actions).

**Step 2.** Add the three new slots under the existing `slots:` section (after `account`):

```yaml
slots:
  account:
    type: text
  amount:
    type: text
  recipient:
    type: text
  account_from:
    type: text
```

Use two-space indentation. Each slot uses `type: text`.

**Step 3.** Add the three ask responses under `responses:`:

```yaml
  utter_ask_amount:
    - text: "How much would you like to transfer?"
      metadata:
        rephrase: False
  utter_ask_recipient:
    - text: "Who would you like to transfer money to?"
      metadata:
        rephrase: False
  utter_ask_account_from:
    - text: "Which account would you like to transfer from?"
      metadata:
        rephrase: False
```

Naming: `utter_ask_<slot_name>` for each slot.

**Why `rephrase: False` here?** With Rasa Pro (CALM), slot collection works best when these ask prompts stay fixed. If `rephrase: True` on `utter_ask_*` during collection, the model may reword the question; the command generator can then mis-map the user’s reply (especially free-text **recipient** or **account_from**) and respond with *“I’m sorry I am unable to understand you…”*. **`level4/config.yml`** must use **`CompactLLMCommandGenerator`** for this chapter (**Unit 0.2**). Keep **`rephrase: False`** on these three responses. You can leave `rephrase: True` on greetings and help text if you prefer.

**Step 4.** Add `action_process_transfer` to the `actions:` list.

**Important:** Keep **every** action your existing flows still use. The `holiday_hours` flow calls `action_holiday_hours`; if you drop it from the domain, `rasa train` will fail with *action … is not listed in the domain*. Your `actions:` list should include the existing actions **and** the new transfer action, for example:

```yaml
actions:
  - action_bank_hours
  - action_holiday_hours
  - action_check_balance_simple
  - action_process_transfer
```

You will create the file `action_process_transfer.py` in Lab 3.1; here you only add its name.

**Step 5.** Verify. Your domain should have:

- `slots:` with `account`, `amount`, `recipient`, `account_from`
- `utter_ask_amount`, `utter_ask_recipient`, `utter_ask_account_from` under `responses:`
- `action_process_transfer` in the `actions:` list, **without removing** `action_bank_hours`, `action_holiday_hours`, or `action_check_balance_simple`
- Valid YAML and all existing non-transfer content unchanged

---

## Part 1: In Codio

You do **not** need to activate the virtual environment for this lab — **Check It!** only checks your saved file.

1. **Open** `level4/domain/basics.yml` in the editor (from the file tree).
2. **Follow Steps 2–4 above** to add the three slots, the three ask responses, and `action_process_transfer` to the actions list.
3. **Verify** as in Step 5.

**Use Check It!** below when done (Codio).

{Check It!|assessment}(code-output-compare-401020001)

## Part 2: Running locally

1. Open your project in an editor. Go to the main project folder and open `level4/domain/basics.yml` (you do not need to activate the virtual environment for this lab, **Check It!** only checks your saved file).
2. Add the three slots, the three utter_ask_* responses, and `action_process_transfer` to the actions list **without removing** `action_bank_hours`, `action_holiday_hours`, or `action_check_balance_simple`.
3. Verify as above.

**Success criteria.** `domain/basics.yml` must contain:

- Slots: `amount`, `recipient`, `account_from` (each type text)
- Responses: `utter_ask_amount`, `utter_ask_recipient`, `utter_ask_account_from`
- Under `actions:`: `action_process_transfer` plus the existing actions (`action_bank_hours`, `action_holiday_hours`, `action_check_balance_simple`)
