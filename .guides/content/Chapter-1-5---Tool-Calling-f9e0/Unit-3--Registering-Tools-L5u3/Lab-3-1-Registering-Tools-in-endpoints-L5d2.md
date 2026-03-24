**Objective.** In Unit 3.1 you saw the example of the `tools:` section in endpoints.yml. In this lab you will add your own version to `level5/endpoints.yml` so Rasa can discover and use the tool functions you created in Lab 2.1.

## Step-by-Step Instructions

**Step 1.** Open `level5/endpoints.yml`. Ensure existing sections (action_endpoint, nlg, model_groups) are unchanged.

**Step 2.** Add a new section **tools** (e.g. after the action_endpoint or before model_groups):


tools:
  tools_module: "tools"

Use 2-space indentation. The value `"tools"` is the name of the Python module (the `tools/` folder).

**Step 3.** Save the file. Verify that the YAML is valid and that no other sections were removed or broken.

**Step 4.** **In Codio**, use **Check It!** below. The grader will check that `endpoints.yml` contains a `tools:` key and `tools_module: "tools"`.

{Check It!|assessment}(code-output-compare-501030001)
