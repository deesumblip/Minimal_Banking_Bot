# Pipeline: Chapter 1.3 vs Chapter 1.4

**Chapter 1.3 (Level 3) is unchanged:** `level3/config.yml` uses **`SearchReadyLLMCommandGenerator`** + **`FlowPolicy`**, same as before.

---

## Why Level 4’s `config.yml` differs (only here)

**Chapter 1.4 multi-slot flows** (amount → recipient → account_from) need reliable **free-text slot fills**. With **`SearchReadyLLMCommandGenerator`**, it is common to see:

- Amount OK (“250 dollars”)  
- Then **“I’m sorry I am unable to understand you…”** on short names (**“MC Hammer”**, **“JFK”**), etc.

That is a **known limitation** of the retrieval-oriented generator when you are **not** using Enterprise Search / RAG the way Rasa expects.

**Log signature:** If **`logs.out`** shows **`SetSlotCommand(name='transfer_money_amount', …)`** or **`transfer_money_recipient`** but your domain only has **`amount`**, **`recipient`**, **`account_from`**, the LLM is emitting **flow-prefixed** slot names that **are not in the domain**. You will see **`skip_command_slot_not_in_domain`** and **`CannotHandleCommand(reason='The slot predicted by the LLM is not defined in the domain.')`**. **Switch to `CompactLLMCommandGenerator`** in **`level4/config.yml`** and **retrain**—do not rename domain slots to `transfer_money_*`.

**`level4/config.yml`** therefore uses **`CompactLLMCommandGenerator`** (same `model_group: gpt-4o-mini`, same `FlowPolicy`). Rasa documents this as a good fit for **plain CALM** assistants without RAG.

| Folder | Command generator |
|--------|-------------------|
| `level3/` (Ch. 1.3) | `SearchReadyLLMCommandGenerator` |
| `level4/` (Ch. 1.4) | `CompactLLMCommandGenerator` |

The **`recipe`**, **`.env`**, and overall **`endpoints.yml`** layout match Level 3; the **`model_groups`** entry for command generation is **tuned in `level4/endpoints.yml`** (model + temperature)—see **Unit 0.2** in Chapter 1.4 for the full Chapter 1.3 → 1.4 checklist.

**`endpoints.yml` model** — The **`gpt-4o-mini`** *group id* still points Rasa at **`model: gpt-4o-2024-11-20`** for Level 4. **`gpt-4o-mini`** alone often mis-generates **FillSlot** commands for **recipient** names; **`gpt-4o`** is more reliable for CALM command DSL (higher API cost). NLG rephrase uses the same group.

**`flow_retrieval.turns_to_embed`** (here **5**) — By default, only the **last** user turn is embedded for flow retrieval. Short messages (**“How about 90 dollars?”**, **“MC Hammer”**) then match the wrong flows or lack context. Embedding **several** turns keeps *transfer* intent + prior slots in context (see [Rasa flow retrieval](https://rasa.com/docs/reference/config/components/llm-command-generators/#customizing-flow-retrieval)). Avoid **`active: false`** unless you have very few flows and hit token limits—disabling it made *amount* extraction flaky in testing.

**`transfer_money` flow** — Uses **`always_include_in_prompt: true`** and **`if: true`** so this flow stays in the LLM prompt (see [Flow properties](https://rasa.com/docs/reference/primitives/flows/#always-include-in-prompt)). Collect-step text is kept **short** so the command generator is not overloaded. **`endpoints.yml`** uses **`temperature: 0.1`** for slightly steadier generations.

---

## What students do

- Finish **Chapter 1.3** in **`level3/`** — no change.
- In **Chapter 1.4**, work in **`level4/`** and use the **`level4/config.yml`** from this repo (or change **one** line in a copied config: `SearchReady…` → `Compact…` for the transfer flow to behave reliably).

**Domain, flows, and actions** are still where multiple slots are defined; the generator swap is **only** so the LLM can fill those slots consistently.

---

## After changing `config.yml`

From **`level4/`**:

```bash
python -m rasa train
```

Then test in Inspector again.
