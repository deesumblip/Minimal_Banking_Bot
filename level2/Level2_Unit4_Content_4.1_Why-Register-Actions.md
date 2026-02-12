### 4.1 Why Register Actions?

You created **action_holiday_hours** in Lab 3.1. For Rasa to use it (and the example **action_bank_hours**), both must be listed in the domain. Actions must be registered in the domain file so Rasa knows they exist—without registration, Rasa won't find your actions even if the Python files exist.

**File Location**: `domain/basics.yml`

**Analogy**: Registering an action is like adding a phone number to your contacts - you need to tell Rasa "this action exists and here's its name."

---
