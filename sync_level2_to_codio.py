#!/usr/bin/env python3
"""
Sync Level 2 course content from level2/*.md into Codio .guides/content structure.

Each Level2_Unit*_Content_*.md and each Level2_*_Assessment.md becomes one Codio page.
Run from repo root: python sync_level2_to_codio.py

See CODIO_SYNC_GUIDE.md for how to use this and how Codio content is organized.
"""

import hashlib
import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
LEVEL2_DIR = REPO_ROOT / "level2"
GUIDES_CONTENT = REPO_ROOT / ".guides" / "content"

# Level 2 lives inside this existing Codio chapter (do not create a new chapter)
LEVEL2_CHAPTER_FOLDER = "Chapter-1-2---Custom-Actions-30d6"
# Stable slug ids for lab content pages (so we overwrite same Codio page and preserve assessment JSON)
LAB_CONTENT_SLUG_IDS = {"3.1": "04c0", "4.1": "3406", "5.1": "e512", "6.1": "7710"}
UNIT_TITLES = {
    0: "Recap--What-You-Built-in-Level-1",
    1: "Introduction-to-Actions",
    2: "Understanding-the-Action-Class",
    3: "Creating-Your-First-Action",
    4: "Registering-Actions-in-the-Domain",
    5: "Using-Actions-in-Flows",
    6: "Training-and-Testing-with-Actions",
    7: "Putting-It-All-Together",
    8: "Assessment-and-Next-Steps",
}


def _short_id(s: str, length: int = 4) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:length]


def _slug_from_content_name(name: str) -> str:
    """Level2_Unit4_Content_4.4_Multiple-Actions.md -> 4-4-Multiple-Actions."""
    m = re.match(r"Level2_Unit\d+_Content_([\d.]+)_(.+)\.md$", name, re.IGNORECASE)
    if m:
        num = m.group(1).replace(".", "-")
        rest = m.group(2).replace(" ", "-")
        return f"{num}-{rest}"
    return name.replace(" ", "-").replace(".", "-")[:50]


def _slug_from_assessment_name(name: str, content: str) -> str:
    """From Level2_Lab*_Content.md -> Lab-4-1 or Lab-3-1 (student page). Assessment_Setup -> Lab-Implementation/."""
    if "Lab" in name:
        m = re.match(r"Level2_Lab([\d.]+)_Assessment\.md$", name, re.IGNORECASE)
        if m:
            n = m.group(1).replace(".", "-")
            return f"Lab-{n}"
    m = re.match(r"Level2_Unit(\d+)_Assessment\.md$", name, re.IGNORECASE)
    if m:
        u = m.group(1)
        return f"Lab-{u}-1"
    # Fallback: use first # heading
    for line in content.splitlines():
        if line.startswith("# "):
            t = line[2:].strip()
            return t.replace(" ", "-").replace(".", "-")[:40]
    return name.replace(" ", "-")[:40]


def _page_title_from_content(content: str, fallback: str, prefer_h1: bool = False) -> str:
    """Prefer first ### (h3) for content pages (e.g. '### 0.1 Your Level 1 Banking Bot'); for Lab/Assessment use first # (e.g. 'Lab 4.1: ...')."""
    first_h1 = None
    first_h3 = None
    first_h2 = None
    for line in content.splitlines():
        s = line.strip()
        if s.startswith("# ") and not s.startswith("## "):
            if first_h1 is None:
                first_h1 = s[2:].strip()
        elif s.startswith("### "):
            if first_h3 is None:
                first_h3 = s[4:].strip()
        elif s.startswith("## ") and not s.lower().startswith("## guide"):
            if first_h2 is None:
                first_h2 = s[3:].strip()
    if prefer_h1 and first_h1:
        return first_h1
    return first_h3 or first_h2 or first_h1 or fallback


def collect_level2_pages():
    """Collect (unit_number, sort_key, source_path, slug, title, strip_title_h1) for each page."""
    pages_by_unit = {}  # unit -> list of (sort_key, path, slug, title, strip_title_h1)

    for path in sorted(LEVEL2_DIR.glob("*.md")):
        name = path.name
        if not name.startswith("Level2_"):
            continue
        content = path.read_text(encoding="utf-8")
        # Lab/Assessment pages: use first # heading (e.g. "Lab 4.1: ...") so title is clearly a Lab
        is_assessment = "Assessment" in name or re.search(r"Level2_Lab[\d.]+_Assessment", name, re.I)
        title = _page_title_from_content(content, name, prefer_h1=is_assessment)
        # Strip that heading from the body when syncing so the panel title is not duplicated in the page
        strip_title_h1 = is_assessment  # Labs: strip first #; content: strip first ###

        # Content page: Level2_Unit4_Content_4.4_Multiple-Actions.md
        m = re.match(r"Level2_Unit(\d+)_Content_([\d.]+)_(.+)\.md$", name, re.IGNORECASE)
        if m:
            unit = int(m.group(1))
            sort_key = (float(m.group(2)), 0)
            slug_base = _slug_from_content_name(name)
            short_id = _short_id(str(path))
            slug = f"{slug_base}-{short_id}"
            pages_by_unit.setdefault(unit, []).append((sort_key, path, slug, title, strip_title_h1))
            continue

        # Lab student content (synced to main lab pages): Level2_Lab3.1_Content.md, Level2_Lab4.1_Content.md, etc.
        # Use stable slugs so we overwrite the same Codio pages and preserve assessment JSON.
        m = re.match(r"Level2_Lab([\d.]+)_Content\.md$", name, re.IGNORECASE)
        if m:
            lab_num = m.group(1)
            unit = int(float(lab_num))
            sort_key = (999, 0)  # after all content
            slug_base = f"Lab-{lab_num.replace('.', '-')}"
            stable_id = LAB_CONTENT_SLUG_IDS.get(lab_num, _short_id(str(path)))
            slug = f"{slug_base}-{stable_id}"
            title = _page_title_from_content(content, name, prefer_h1=True)
            strip_title_h1 = True
            pages_by_unit.setdefault(unit, []).append((sort_key, path, slug, title, strip_title_h1))
            continue

        # Skip Assessment_Setup and old Assessment files (they are synced to Lab-Implementation or no longer used)
        if "Assessment_Setup" in name or re.match(r"Level2_Lab[\d.]+_Assessment\.md$", name, re.I) or re.match(r"Level2_Unit\d+_Assessment\.md$", name, re.I):
            continue

    return pages_by_unit


def _strip_title_from_body(content: str, strip_h1: bool) -> str:
    """Remove the first heading from body so the page title is not duplicated in the rendered markdown.
    strip_h1=True: remove first line if it's a single # heading (Labs). False: remove first ### (content)."""
    lines = content.splitlines()
    if not lines:
        return content
    first = lines[0].strip()
    if strip_h1 and first.startswith("# ") and not first.startswith("## "):
        rest = lines[1:]
    elif not strip_h1 and first.startswith("### "):
        rest = lines[1:]
    else:
        return content
    while rest and not rest[0].strip():
        rest.pop(0)
    return "\n".join(rest) + ("\n" if rest else "")


def write_codio_page(unit_dir: Path, slug: str, title: str, md_path: Path, strip_title_h1: bool = False) -> None:
    """Write one page: slug.md (body without title heading) and slug.json (merge to preserve Codio assessments)."""
    unit_dir.mkdir(parents=True, exist_ok=True)
    md_content = md_path.read_text(encoding="utf-8")
    # Remove the title heading from the body so it only appears in the panel, not duplicated in the page
    body_content = _strip_title_from_body(md_content, strip_h1=strip_title_h1)
    (unit_dir / f"{slug}.md").write_text(body_content, encoding="utf-8")

    json_path = unit_dir / f"{slug}.json"
    if json_path.exists():
        # Preserve existing Codio metadata (e.g. assessment links, taskId, files, layout)
        try:
            existing = json.loads(json_path.read_text(encoding="utf-8"))
            existing["title"] = title
            meta = existing
        except (json.JSONDecodeError, OSError):
            meta = _default_page_meta(md_path, slug, title)
    else:
        meta = _default_page_meta(md_path, slug, title)

    json_path.write_text(json.dumps(meta, indent=2), encoding="utf-8")


def _default_page_meta(md_path: Path, slug: str, title: str) -> dict:
    """Default page JSON when no existing file (no assessments to preserve)."""
    page_id = _short_id(str(md_path) + slug, 8)
    return {
        "id": f"{page_id}-xxxx-xxxx-xxxx-xxxxxxxxxxxx"[:36],
        "title": title,
        "files": [],
        "layout": "1-panel",
        "path": [],
        "type": "page",
        "contentType": "markdown",
        "teacherOnly": False,
        "closeTerminalSession": True,
        "learningObjectives": "",
    }


def sync():
    GUIDES_CONTENT.mkdir(parents=True, exist_ok=True)
    pages_by_unit = collect_level2_pages()

    chapter_name = LEVEL2_CHAPTER_FOLDER
    chapter_dir = GUIDES_CONTENT / chapter_name
    chapter_dir.mkdir(parents=True, exist_ok=True)

    unit_folders_order = []
    unit_id_base = _short_id("level2-unit", 4)

    for unit in sorted(pages_by_unit.keys()):
        unit_title = UNIT_TITLES.get(unit, f"Unit-{unit}")
        unit_id = _short_id(f"unit-{unit}-{unit_title}", 4)
        unit_folder_name = f"Unit-{unit}--{unit_title}-{unit_id}"
        unit_dir = chapter_dir / unit_folder_name
        unit_dir.mkdir(parents=True, exist_ok=True)

        entries = pages_by_unit[unit]
        entries.sort(key=lambda x: x[0])
        page_order = []
        for (_sort_key, md_path, slug, title, strip_title_h1) in entries:
            write_codio_page(unit_dir, slug, title, md_path, strip_title_h1=strip_title_h1)
            page_order.append(slug)

        title_clean = unit_title.replace("--", " ").replace("-", " ").title()
        unit_index = {
            "id": f"{unit_id}{unit_id_base}-xxxx-xxxx-xxxx-xxxxxxxxxxxx"[:36],
            "type": "section",
            "title": f"Unit {unit}: {title_clean}",
            "order": page_order,
        }
        (unit_dir / "index.json").write_text(
            json.dumps(unit_index, indent=2), encoding="utf-8"
        )
        unit_folders_order.append(unit_folder_name)

    chapter_index_path = chapter_dir / "index.json"
    if chapter_index_path.exists():
        try:
            chapter_index = json.loads(chapter_index_path.read_text(encoding="utf-8"))
            chapter_index["order"] = unit_folders_order
            chapter_index["title"] = chapter_index.get("title") or "1.2"
        except (json.JSONDecodeError, OSError):
            chapter_index = {"type": "chapter", "title": "1.2", "order": unit_folders_order}
    else:
        chapter_index = {"type": "chapter", "title": "1.2", "order": unit_folders_order}
    chapter_index_path.write_text(
        json.dumps(chapter_index, indent=2), encoding="utf-8"
    )

    # Sync Lab Assessment_Setup files to Lab-Implementation (instructor-only; separate from student pages)
    lab_impl_dir = chapter_dir / "Lab-Implementation"
    lab_impl_dir.mkdir(parents=True, exist_ok=True)
    for path in sorted(LEVEL2_DIR.glob("Level2_Lab*_Assessment_Setup.md")):
        name = path.name
        m = re.match(r"Level2_Lab([\d.]+)_Assessment_Setup\.md$", name, re.IGNORECASE)
        if m:
            lab_num = m.group(1).replace(".", "-")
            out_name = f"Lab-{lab_num}.md"
            (lab_impl_dir / out_name).write_text(path.read_text(encoding="utf-8"), encoding="utf-8")

    # Update root content index to include Level 2 if missing
    root_index_path = GUIDES_CONTENT / "index.json"
    if root_index_path.exists():
        root_index = json.loads(root_index_path.read_text(encoding="utf-8"))
    else:
        root_index = {"title": "Minimal_Banking_Bot", "order": []}
    order = list(root_index.get("order", []))
    if chapter_name not in order:
        order.append(chapter_name)
        root_index["order"] = order
        root_index_path.write_text(
            json.dumps(root_index, indent=2), encoding="utf-8"
        )
        print(f"Added {chapter_name} to root content order.")
    print(f"[OK] Synced Level 2 -> .guides/content/{chapter_name}/ ({len(pages_by_unit)} units)")


if __name__ == "__main__":
    sync()
