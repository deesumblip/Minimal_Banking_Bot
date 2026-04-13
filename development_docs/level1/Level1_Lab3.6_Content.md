**Objective**: Add flows that use the `utter_hours` and `utter_balance` responses. You will paste in pre-written response text and flow files so the assessment for this section can verify your project.

**Why this lab**: In **Lab 3.5** you completed the hours and balance flow YAML with fill-in-the-blank exercises. Here you are given **exact, pre-written versions** of the responses and the corresponding flow files so your `level1` project matches what the **Lab 3.6** Check It! assessment expects.

**Before You Begin**: You’ve passed both fill-in-the-blank checks in **Lab 3.5** (or at least understand flow structure). You are in the `level1` project (folder that contains `domain/`, `data/`, `config.yml`).

---

## Step 1: Add two responses to the domain

Open **`domain/basics.yml`**. Under the `responses:` section, add the two blocks below. Place them after your last response (e.g. after `utter_goodbye`) and keep the same indentation (2 spaces).

**Paste this after `utter_goodbye` (and its `metadata` block):**

```yaml
  utter_hours:
    - text: "We're open Monday–Friday 9am–5pm and Saturday 9am–1pm. Closed Sundays."
      metadata:
        rephrase: True

  utter_balance:
    - text: "To check your balance, we'll need your account number. You can say 'Check my balance' and have your account number ready."
      metadata:
        rephrase: True
```

Save the file.

---

## Step 2: Replace the hours flow

Open **`data/basics/hours.yml`** (you created this in Lab 3.5). Replace all of its contents with the following. If the file doesn’t exist yet, create it with this content.

```yaml
flows:
  hours:
    name: bank hours
    description: Provide bank opening hours and schedule.
    steps:
      - action: utter_hours
```

Save the file.

---

## Step 3: Replace the balance flow

Open **`data/basics/balance.yml`** (you created this in Lab 3.5). Replace all of its contents with the following. If the file doesn’t exist yet, create it with this content.

```yaml
flows:
  balance:
    name: account balance help
    description: Explain how to check account balance.
    steps:
      - action: utter_balance
```

Save the file.

---

## Checklist

- [ ] `domain/basics.yml` contains `utter_hours` and `utter_balance` under `responses:`.
- [ ] `data/basics/hours.yml` exists and has a flow named `hours` with step `utter_hours`.
- [ ] `data/basics/balance.yml` exists and has a flow named `balance` with step `utter_balance`.

**Run the assessment when done** to pass the Lab 3.5 assessment.
