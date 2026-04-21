# `_dev/` — teacher / author-only content

This folder holds working material for **course authors only**. Its contents
are deliberately **excluded from every Codio publish** (see
`.github/workflows/codio-publish.yml`'s `Strip _dev/ ...` step, which deletes
this folder on the runner before any `codio-assignment-publish-action` step
runs).

## What lives here

- `development_docs/` — design notes, draft lab content, implementation
  overviews, and other authoring material for Levels 1–6.
- `Lauren_Markdown_Edits/` — snapshots of Lauren's markdown edits used as
  reference during review rounds.
- `Screenshots/` — reference images of Codio bugs, phantom files, license
  errors, etc. Used in development notes, not shipped to students.
- `Mini_Banking.code-workspace` — VS Code multi-root workspace file for
  local development. Not used by Codio.

## Adding new author-only content

If you're adding notes, screenshots, rough drafts, or any file that should
**never** appear in a student's Codio workspace, put it under `_dev/`.
Nothing else needs to be configured — the Cleanup step in the workflow
strips the whole folder from every publish.

## What does get published

Student-facing content lives outside `_dev/`:

- `level1/` – `level6/` — per-level bot code.
- `.guides/content/` — Codio Guide pages.
- `.guides/assessments/` — auto-graded questions.
- `.guides/secure/levelN_graders/` — server-side graders.
- `.guides/scripts/`, `.guides/startup.sh` — shared box scripts.
- `.codio`, `.gitignore` — shared box configuration.

See `.github/yaml_map/*.yml` for the per-assignment scoping rules.
