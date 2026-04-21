# Setting Up GitHub Actions to Publish to Codio

This guide walks through configuring [Codio’s GitHub API integration](https://docs.codio.com/develop/develop/ide/tools/ghapi.html#implementing-workflow-actions) so that pushes to `main` automatically publish this project to a Codio assignment. You’ll use [GitHub Actions](https://docs.github.com/en/actions/get-started/quickstart) to run the publish step.

---

## Part 1: Codio (Admin Only)

These steps require **Codio organization admin** rights.

### 1.1 Create a GitHub API integration in Codio

1. In Codio, go to **Organization → Integrations**.
2. Find **GitHub API** (or similar) and click **Add Integration**.
3. Give it a name (e.g. `Minimal_Banking_Agent_production`).
4. After creation, open the integration and copy:
   - **Client ID**
   - **Secret ID**  
   Keep these for Part 2. The Secret ID can be regenerated later if needed.

### 1.2 Get your course and assignment IDs

1. In Codio, open the **assignment** that should receive this repo’s content.
2. Go to the assignment’s **Overview** tab.
3. Look at the browser URL. It will look roughly like:
   ```text
   https://codio.com/.../course/<course-id>/assignment/<assignment-id>
   ```
4. Copy the **course-id** and **assignment-id** (long hex-like strings).  
   You’ll paste these into the workflow file in Part 2.

---

## Part 2: GitHub (This Repository)

Do this in the **Minimal_Banking_Agent** repo on GitHub (and optionally in your local clone).

### 2.1 Add Codio credentials as repository secrets

1. On GitHub, open **deesumblip/Minimal_Banking_Agent** (or your fork).
2. Go to **Settings → Secrets and variables → Actions**.
3. Click **New repository secret** and add two secrets:

   | Name                             | Value              |
   |----------------------------------|--------------------|
   | `CODIO_PRODUCTION_CLIENT_ID`     | Codio Client ID    |
   | `CODIO_PRODUCTION_SECRET_ID`     | Codio Secret ID    |

   Use these exact names so the workflow (below) can reference them.

### 2.2 Add the workflow file

A workflow file is already in this repo:

- **Path:** `.github/workflows/codio-publish.yml`

It runs on every **push to `main`**, checks out the repo, and runs the Codio publish action. You only need to **insert your Codio IDs** into it.

**Option A – Edit on GitHub**

1. In the repo, open **.github/workflows/codio-publish.yml**.
2. Click **Edit** (pencil icon).
3. Replace the placeholders:
   - `YOUR_COURSE_ID` → your actual **course-id** from step 1.2.
   - `YOUR_ASSIGNMENT_ID` → your actual **assignment-id** from step 1.2.
4. Commit directly to `main` (or create a branch and merge to `main`).

**Option B – Edit locally**

1. Open `.github/workflows/codio-publish.yml` in your editor.
2. Replace `YOUR_COURSE_ID` and `YOUR_ASSIGNMENT_ID` with your real IDs.
3. Commit and push to `main`:
   ```bash
   git add .github/workflows/codio-publish.yml
   git commit -m "Configure Codio publish workflow with course and assignment IDs"
   git push origin main
   ```

### 2.3 Confirm workflows are enabled

1. In the repo, open the **Actions** tab.
2. If you see workflows listed (e.g. “codio-publish”), Actions is enabled.
3. If Actions is disabled, go to **Settings → Actions → General** and allow workflows for this repository.

---

## Part 3: Verify It Works

1. Make a small change (e.g. edit `PROJECT_SUMMARY.md` or a comment in the workflow).
2. Commit and push to `main`.
3. On GitHub, go to **Actions** and open the **codio-publish** workflow run.
4. Confirm the job **succeeds** (green check). If it fails, open the run and read the logs (e.g. wrong secrets, wrong IDs, or Codio API errors).
5. In Codio, open the assignment and confirm the latest project content (and guide, if applicable) is updated.

---

## Summary Checklist

- [ ] **Codio:** GitHub API integration created; Client ID and Secret ID copied.
- [ ] **Codio:** Course ID and Assignment ID copied from the assignment URL (Overview tab).
- [ ] **GitHub:** Secrets `CODIO_PRODUCTION_CLIENT_ID` and `CODIO_PRODUCTION_SECRET_ID` added.
- [ ] **GitHub:** `.github/workflows/codio-publish.yml` updated with real `course-id` and `assignment-id`.
- [ ] **GitHub:** Workflow committed and pushed to `main`.
- [ ] **Verify:** A push to `main` triggers the workflow and the Codio assignment updates.

---

## If You Get 404 NOT_FOUND

If the workflow fails with `404 NOT_FOUND` on the Codio API:

1. **Confirm the IDs from the URL**
   - In Codio, open **Rasa University** → **Minimal_Banking_Agent** and go to the **Overview** tab.
   - Copy the **course-id** and **assignment-id** directly from the browser address bar (they appear in the path; format may be `.../courses/<course-id>/assignments/<assignment-id>/...` or similar).
   - Paste them into `.github/workflows/codio-publish.yml` (replace the existing `course-id` and `assignment-id`). Even one wrong character will cause 404.

2. **Integration and organization**
   - The GitHub API integration must be created under the **same Codio organization** that owns the course. In Codio: **Organization → Integrations** is where you created it; the course “Rasa University” must belong to that org. If the course is in a different org, create an integration in that org and use its Client ID and Secret ID in GitHub secrets.

3. **Try the other domain**
   - If you use **codio.co.uk** (not codio.com), in the workflow set `domain: codio.co.uk`. Wrong domain leads to 404.

4. **Try names instead of IDs**
   - In the workflow you can use `course-name: Rasa University` and `assignment-name: Minimal_Banking_Agent` instead of `course-id` and `assignment-id` (remove the id lines). Names must match Codio exactly.

---

## Optional: Publishing to Multiple Assignments

If one repo should publish to **several** Codio assignments (e.g. one per chapter), use Codio’s **mapping** approach:

1. Create a folder (e.g. `.github/yaml_map/`) and add one `.yml` file per assignment, each defining `assignment`, `section`, and `paths` (see [Codio’s “Publishing projects into multiple assignments”](https://docs.codio.com/develop/develop/ide/tools/ghapi.html#publishing-projects-into-multiple-assignments)).
2. In the workflow, **remove** `assignment-id` and add:
   ```yaml
   yml: ./.github/yaml_map
   ```
3. Keep `course-id` (or switch to `course-name` if you prefer).

For a single assignment, the existing `codio-publish.yml` (with one `course-id` and one `assignment-id`) is enough.
