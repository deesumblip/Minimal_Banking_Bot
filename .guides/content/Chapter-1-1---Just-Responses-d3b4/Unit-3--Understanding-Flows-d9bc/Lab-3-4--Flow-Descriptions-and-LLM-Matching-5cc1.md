**Objective**: Learn the structure of the hours and balance flows, then add them (and their responses) to your project so your bot is ready for training.

**Before You Begin**:
- ✅ You've completed Lab 3.2 (created goodbye.yml)
- ✅ You understand flow structure (flows:, name:, description:, steps:)
- ✅ You know where `data/basics/` and `domain/basics.yml` are located

---

#### Why These Flows?

The `description` field is **critical** because the LLM uses it to match user messages to flows. For example, when a user asks "What are your hours?" or "How do I check my balance?", the LLM reads flow descriptions and triggers the right flow.

You will complete **two fill-in-the-blank** flows (hours and balance), then add those flows and the matching responses to your project.

---

#### Part 1: Complete the hours flow (fill in the blanks)

Fill in the blanks to complete the **hours** flow YAML. This flow will provide bank opening hours.

{Check It!|assessment}(fill-in-the-blanks-303400101)

---

#### Part 2: Complete the balance flow (fill in the blanks)

Fill in the blanks to complete the **balance** flow YAML. This flow will explain how to check account balance.

{Check It!|assessment}(fill-in-the-blanks-303400102)

---

#### Part 3: Add the flows and responses to your project

Once you've passed both fill-in-the-blank checks, add the **exact** content below to your `level1` project. This ensures your bot has the responses and flows the assessment expects.

**Step 1: Add two responses to the domain**

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

**Step 2: Create the hours flow file**

Create **`level1/data/basics/hours.yml`** with this content (same as the flow you completed in Part 1):

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

**Step 3: Create the balance flow file**

Create **`level1/data/basics/balance.yml`** with this content (same as the flow you completed in Part 2):

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

- [ ] Part 1 and Part 2: Both fill-in-the-blank assessments passed
- [ ] `level1/domain/basics.yml` contains `utter_hours` and `utter_balance` under `responses:`
- [ ] `level1/data/basics/hours.yml` exists with flow `hours` and step `utter_hours`
- [ ] `level1/data/basics/balance.yml` exists with flow `balance` and step `utter_balance`

**Run the assessment below** to verify your project is ready for training (Lab 6.1).

{Check It!|assessment}(code-output-compare-350500005)
