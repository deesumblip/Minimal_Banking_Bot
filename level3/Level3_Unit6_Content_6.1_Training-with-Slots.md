Training with slots is similar to Level 2: you run `rasa train` from the `level3` folder so Rasa builds a model. The difference is what Rasa includes in that model.

## What Rasa does when you train (Level 3)

Rasa reads your **slot definitions** from `domain/basics.yml` and checks that slot types and structure are valid. It processes your **flows** and any steps that use `collect:` so it knows which slots to fill and in what order. It also checks that each collected slot has a matching **response** (e.g. `utter_ask_account` for the `account` slot). When everything is consistent, it produces a model that knows about your slots, flows, and actions—so at runtime the bot can collect slot values and call your custom action with the right data.

So training with slots is still "run training from level3"; the extra step is that the model now encodes slot collection and how it ties to your domain and flows.

## What's coming up

In **Lab 6.1** you'll run the training (with step-by-step instructions for Codio and for running locally), verify the model was saved, and run the assessment. After that, **6.2** and the rest of the unit cover testing slot collection and understanding slot state so you can debug and improve the bot.
