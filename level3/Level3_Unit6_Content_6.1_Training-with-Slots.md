Training with slots works the same way as in Level 2. You run `rasa train` from the `level3` folder and Rasa writes a model. What changes is the extra information Rasa packs into that model.

## What Rasa does when you train in Level 3

First, Rasa reads your **slot definitions** from `domain/basics.yml` and checks that types and structure are valid.

Next, it reads your **flows**. When a step uses `collect:`, Rasa records which slot to fill and how that step fits in the flow order.

It also checks that each collected slot has a matching **response** in the domain. For example, the `account` slot needs something like `utter_ask_account` so the bot knows what to say when it must ask for that slot.

When those pieces line up, the trained model includes your slots, your flows, and your actions. At runtime the bot can collect slot values and run your custom action with the data it already stored.

You still run training from `level3`. The model is simply aware of slot collection and how it connects to the domain and flows.

## What comes next in this unit

**Lab 6.1** walks through training with step-by-step notes for Codio and for a local machine. You will confirm that the model file was created and you will run the assessment. After that, section **6.2** and the rest of the unit focus on testing slot collection and slot state so you can debug your bot.
