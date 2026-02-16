# Lab 2.1: Understanding YAML Syntax for Responses

**Objective**: Learn YAML syntax by exploring existing responses.

#### Steps

1. **Open the Domain File**
   - Navigate to `domain/basics.yml` in your IDE
   - You should see existing responses like `utter_greet`, `utter_help`, and `utter_contact`

2. **Identify Response Structure**
   - Find the `responses:` section
   - Notice how each response is indented with 2 spaces
   - Notice the `-` (dash) before `text:`
   - Notice the `metadata:` section aligned with `text:`

3. **Explore Response Variations**
   - Check if any responses have multiple variations (multiple `- text:` items)
   - Notice how variations are at the same indentation level

**AI Coach**: If you're confused about YAML syntax, ask the AI Coach: "What does the dash before text: mean?" or "Why do I need metadata: rephrase: True?"
