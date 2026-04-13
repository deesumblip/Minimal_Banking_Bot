**Objective.** Register the MCP server in **`level6/endpoints.yml`** so the sub-agent can connect to **`mcp_server/banking.py`**. **Same pattern as earlier labs:** fill-in-the-blanks for the **`mcp_servers`** block, merge into **`endpoints.yml`**, then **Code Test**.

## Step-by-Step Instructions

**Step 1.** Open **`level6/endpoints.yml`**. Keep **`action_endpoint`**, **`nlg`**, **`tools`**, and **`model_groups`** unchanged.

**Step 2.** Complete the **Fill in the blanks** below for the **`mcp_servers`** entry.

{Check It!|assessment}(fill-in-the-blanks-501060112)

**Step 3.** Merge the **passed** YAML into **`endpoints.yml`**: add the **`mcp_servers:`** block (typically **after** **`tools:`** and **before** **`model_groups:`**). If your starter file has the same lines **commented out**, replace them with your completed block or uncomment and fix values. Save.

**Step 4.** **Use Check It!** below for the graded **Code Test** (Codio).

{Check It!|assessment}(code-output-compare-501060002)

## Running locally

From project root activate the venv. After merging **`endpoints.yml`**, start the MCP server from **`level6/`** (separate terminal. Needed before Inspector tests):

```bash
cd level6
python mcp_server/banking.py
```
