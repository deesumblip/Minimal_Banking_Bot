**Objective**: Add the hours and balance flows (and their responses) to your `level1` project so your agent is ready for training.

**Before You Begin**: You've passed both fill-in-the-blank checks in **Lab 3.5** (hours flow and balance flow). You are in the `level1` project (folder that contains `domain/`, `data/`, `config.yml`).

---

#### Step 1: Add two responses to the domain

Open **`level1/domain/basics.yml`**. Under the `responses:` section, add the two blocks below after your last response (e.g. after `utter_goodbye`). Use the same indentation (2 spaces).

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

#### Step 2: Create the hours flow file

Create **`level1/data/basics/hours.yml`** with this content (same as the flow you completed in Lab 3.5 Part 1):

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

#### Step 3: Create the balance flow file

Create **`level1/data/basics/balance.yml`** with this content (same as the flow you completed in Lab 3.5 Part 2):

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

#### Checklist

- `level1/domain/basics.yml` contains `utter_hours` and `utter_balance` under `responses:`
- `level1/data/basics/hours.yml` exists with flow `hours` and step `utter_hours`
- `level1/data/basics/balance.yml` exists with flow `balance` and step `utter_balance`

**In Codio**, use **Check It!** below to verify your project is ready for training (Lab 6.1).

{Check It!|assessment}(code-output-compare-350500005)
