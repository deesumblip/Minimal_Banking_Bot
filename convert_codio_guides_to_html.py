#!/usr/bin/env python3
"""
Convert CODIO_IMPLEMENTATION_GUIDE.md to HTML for levels 2-5.

Usage:
    python convert_codio_guides_to_html.py
    python convert_codio_guides_to_html.py --open
"""

import argparse
import sys
import webbrowser
from pathlib import Path

import markdown

# GitHub-style CSS (matching VS Code/Cursor preview) - Dark Reader compatible
GITHUB_CSS = """
<style>
.markdown-body {
    box-sizing: border-box;
    min-width: 200px;
    max-width: 980px;
    margin: 0 auto;
    padding: 45px;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    font-size: 16px;
    line-height: 1.5;
    word-wrap: break-word;
    color: #24292e;
    background-color: #ffffff;
}

@media (max-width: 767px) {
    .markdown-body {
        padding: 15px;
    }
}

.markdown-body h1,
.markdown-body h2 {
    margin-top: 24px;
    margin-bottom: 16px;
    font-weight: 600;
    line-height: 1.25;
    color: #24292e;
    border-bottom: 1px solid #eaecef;
    padding-bottom: .3em;
}

.markdown-body h1 { font-size: 2em; }
.markdown-body h2 { font-size: 1.5em; }
.markdown-body h3 { font-size: 1.25em; margin-top: 24px; margin-bottom: 16px; }
.markdown-body h4 { font-size: 1em; margin-top: 24px; margin-bottom: 16px; }

.markdown-body p {
    margin-top: 0;
    margin-bottom: 16px;
}

.markdown-body ul,
.markdown-body ol {
    margin-top: 0;
    margin-bottom: 16px;
    padding-left: 2em;
}

.markdown-body li {
    margin-top: .25em;
}

.markdown-body code {
    padding: .2em .4em;
    margin: 0;
    font-size: 85%;
    background-color: rgba(27,31,35,.05);
    border-radius: 3px;
    font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace;
}

.markdown-body pre {
    padding: 16px;
    overflow: auto;
    font-size: 85%;
    line-height: 1.45;
    background-color: #f6f8fa;
    border-radius: 6px;
    margin-bottom: 16px;
}

.markdown-body pre code {
    display: inline;
    padding: 0;
    margin: 0;
    background-color: transparent;
    border: 0;
}

.markdown-body blockquote {
    padding: 0 1em;
    color: #6a737d;
    border-left: .25em solid #dfe2e5;
    margin: 0 0 16px 0;
}

.markdown-body table {
    border-spacing: 0;
    border-collapse: collapse;
    margin-top: 0;
    margin-bottom: 16px;
    width: 100%;
    display: block;
    overflow: auto;
}

.markdown-body table th {
    font-weight: 600;
    padding: 6px 13px;
    border: 1px solid #dfe2e5;
    background-color: #f6f8fa;
}

.markdown-body table td {
    padding: 6px 13px;
    border: 1px solid #dfe2e5;
}

.markdown-body table tr {
    background-color: #fff;
    border-top: 1px solid #c6cbd1;
}

.markdown-body table tr:nth-child(2n) {
    background-color: #f6f8fa;
}

.markdown-body hr {
    height: .25em;
    padding: 0;
    margin: 24px 0;
    background-color: #e1e4e8;
    border: 0;
}

.markdown-body a {
    color: #0366d6;
    text-decoration: none;
}

.markdown-body a:hover {
    text-decoration: underline;
}

@media print {
    .markdown-body {
        max-width: 100%;
        padding: 20px;
    }
    
    .markdown-body h1,
    .markdown-body h2 {
        page-break-after: avoid;
    }
    
    .markdown-body pre,
    .markdown-body blockquote {
        page-break-inside: avoid;
    }
}
</style>
"""


LEVEL_TITLES = {
    2: "Level 2: Complete Codio Course Guide",
    3: "Level 3: Complete Codio Course Guide",
    4: "Level 4: Complete Codio Course Guide",
    5: "Level 5: Complete Codio Course Guide",
}


def convert_one(level_dir: Path, open_browser: bool) -> bool:
    md_file = level_dir / "CODIO_IMPLEMENTATION_GUIDE.md"
    html_file = level_dir / "CODIO_IMPLEMENTATION_GUIDE.html"
    level_num = int(level_dir.name.replace("level", ""))

    if not md_file.exists():
        print(f"[ERROR] Missing {md_file}")
        return False

    print(f"Reading {md_file.name} in {level_dir.name}...")
    try:
        md_content = md_file.read_text(encoding="utf-8")
        print(f"   [OK] Read {len(md_content)} characters")
    except Exception as exc:
        print(f"   [ERROR] Error reading file: {exc}")
        return False

    print("   Converting markdown to HTML...")
    try:
        html_content = markdown.markdown(
            md_content,
            extensions=["extra", "codehilite", "tables", "fenced_code", "nl2br", "sane_lists"],
        )
        print("   [OK] Converted to HTML")
    except Exception as exc:
        print(f"   [ERROR] Error converting markdown: {exc}")
        return False

    title = LEVEL_TITLES.get(level_num, f"Level {level_num}: Complete Codio Course Guide")
    html_document = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    {GITHUB_CSS}
</head>
<body>
    <article class="markdown-body">
{html_content}
    </article>
</body>
</html>"""

    print("   Saving HTML file...")
    try:
        html_file.write_text(html_document, encoding="utf-8")
        file_size = html_file.stat().st_size / 1024
        print(f"   [OK] Saved to {html_file.name} ({file_size:.1f} KB)")
        if open_browser:
            webbrowser.open(f"file://{html_file.absolute()}")
            print("   [OK] Opened in browser")
        return True
    except Exception as exc:
        print(f"   [ERROR] Error saving file: {exc}")
        return False


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert Codio guides (levels 2-5) to HTML",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--open",
        action="store_true",
        help="Open HTML files in browser after conversion",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent
    levels = [repo_root / f"level{i}" for i in range(2, 6)]

    print("Converting CODIO_IMPLEMENTATION_GUIDE.md files to HTML...")
    ok = True
    for level_dir in levels:
        ok = convert_one(level_dir=level_dir, open_browser=args.open) and ok
        print()

    if not ok:
        print("One or more conversions failed.")
        sys.exit(1)

    print("All conversions complete!")


if __name__ == "__main__":
    main()
