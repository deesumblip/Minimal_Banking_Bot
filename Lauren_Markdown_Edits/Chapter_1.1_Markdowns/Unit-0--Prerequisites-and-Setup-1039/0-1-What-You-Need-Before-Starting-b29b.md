
Before diving into building your first Rasa bot, let's make sure you have everything set up correctly.

**Prerequisites**: Python knowledge, command line familiarity, file editing, **Rasa license**. Plan for 2–3 hours. You can get your Rasa developer edition license [at this link](https://rasa.com/rasa-pro-developer-edition-license-key-request)

**Note for Codio Students**: Start with Lab 0.1 below to create a virtual environment and install Rasa. Follow the lab to set **RASA_LICENSE** (e.g. via `export RASA_LICENSE=...` or `.env` in project root or Codio environment variables) before running `rasa --version` or other Rasa commands.

**Note for Local Setup**: If you are repeating this exercise on your own machine (not in Codio), set **RASA_LICENSE** (e.g. create a `.env` file in your **project root** with):

   ```
   RASA_LICENSE=rasaxxx-your-license-here
   ```
Replace the placeholder with your actual Rasa license. Load it (e.g. `source .env` from project root) before running Rasa.  
**Never commit `.env` to version control.**
