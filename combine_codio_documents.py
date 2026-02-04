#!/usr/bin/env python3
"""
Combine each level's implementation guide and playbook into a single markdown file.

Creates CODIO_IMPLEMENTATION_MASTER.md per level with this structure:
1. Title/header
2. Full text of CODIO_IMPLEMENTATION_GUIDE.md
3. Separator + full text of CODIO_IMPLEMENTATION_PLAYBOOK.md
"""

from pathlib import Path


def _level_title(level_dir: Path) -> str:
    return level_dir.name.replace("level", "Level ").title()


def combine_for_level(level_dir: Path) -> None:
    guide_path = level_dir / "CODIO_IMPLEMENTATION_GUIDE.md"
    playbook_path = level_dir / "CODIO_IMPLEMENTATION_PLAYBOOK.md"
    output_path = level_dir / "CODIO_IMPLEMENTATION_MASTER.md"

    if not guide_path.exists():
        raise FileNotFoundError(f"Missing guide at {guide_path}")
    if not playbook_path.exists():
        raise FileNotFoundError(f"Missing playbook at {playbook_path}")

    guide_text = guide_path.read_text(encoding="utf-8").rstrip()
    playbook_text = playbook_path.read_text(encoding="utf-8").rstrip()

    level_label = _level_title(level_dir)

    header = f"# {level_label}: Integrated Codio Course Manual\n\n"
    intro = (
        "This single reference combines the comprehensive implementation guide "
        "with the Codio-specific playbook so both student-facing content and platform "
        "execution steps live in one place.\n\n"
    )
    usage = (
        "## How to Use This Document\n\n"
        "- **Students & instructors**: Read Part 1 for all curriculum content, labs, and technical specs.\n"
        "- **Codio implementers**: Use Part 2 for environment setup, Guides authoring, auto-grading, "
        "Virtual Coach, Code Playback, analytics/LMS integration, and the two-week timeline slice.\n"
        "- **Quick reference**: The table below highlights where to look based on the task at hand.\n\n"
        "| Need | Section |\n"
        "| --- | --- |\n"
        "| Full curriculum, step-by-step labs, technical specs | Part 1: Implementation Guide |\n"
        "| Codio setup tasks, auto-grader recipes, timelines | Part 2: Implementation Playbook |\n"
        "| Day-by-day rollout targets | Part 2 → Timeline |\n\n"
    )

    part_guide = "## Part 1: Complete Implementation Guide\n\n"
    separator = "\n\n---\n\n"
    part_playbook = "## Part 2: Codio Implementation Playbook\n\n"

    output = (
        header
        + intro
        + usage
        + part_guide
        + guide_text
        + separator
        + part_playbook
        + playbook_text
        + "\n"
    )
    output_path.write_text(output, encoding="utf-8")


def main() -> None:
    repo_root = Path(__file__).resolve().parent
    for level in range(1, 6):
        level_dir = repo_root / f"level{level}"
        combine_for_level(level_dir)
        print(f"[OK] Combined documents for {level_dir}")


if __name__ == "__main__":
    main()
