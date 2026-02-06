#!/usr/bin/env python3
"""
Convert CODIO_IMPLEMENTATION_GUIDE*.md files to HTML with GitHub-style CSS.

Converts both CODIO_IMPLEMENTATION_GUIDE_OPTIMISED.md and CODIO_IMPLEMENTATION_GUIDE_LINEAR.md.

Usage:
    python convert_codio_guide_to_html.py
    python convert_codio_guide_to_html.py --open
"""

import markdown
from pathlib import Path
import sys
import webbrowser
import argparse

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

def convert_md_to_html(md_file, html_file, title=None, open_browser=False):
    """Convert a single Markdown file to HTML."""
    if not md_file.exists():
        print(f"[ERROR] {md_file.name} not found")
        return False

    if title is None:
        title = md_file.stem.replace("_", " ").replace("-", " ").title()

    print(f"Reading {md_file.name}...")
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            md_content = f.read()
        print(f"   [OK] Read {len(md_content)} characters")
    except Exception as e:
        print(f"   [ERROR] Error reading file: {e}")
        return False
    
    print(f"   Converting markdown to HTML...")
    try:
        html_content = markdown.markdown(
            md_content,
            extensions=['extra', 'codehilite', 'tables', 'fenced_code', 'nl2br', 'sane_lists']
        )
        print(f"   [OK] Converted to HTML")
    except Exception as e:
        print(f"   [ERROR] Error converting markdown: {e}")
        return False
    
    print(f"   Creating HTML document...")
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
    
    print(f"   Saving HTML file...")
    try:
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html_document)
        file_size = html_file.stat().st_size / 1024
        print(f"   [OK] Saved to {html_file.name} ({file_size:.1f} KB)")
        
        return html_file
    except Exception as e:
        print(f"   [ERROR] Error saving file: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(
        description='Convert CODIO_IMPLEMENTATION_GUIDE*.md to HTML with GitHub-style CSS',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python convert_codio_guide_to_html.py          # Convert both guides to HTML
  python convert_codio_guide_to_html.py --open   # Convert and open first HTML in browser
        """
    )
    parser.add_argument(
        '--open',
        action='store_true',
        help='Open first HTML file in browser after conversion'
    )
    
    args = parser.parse_args()
    
    script_dir = Path(__file__).parent
    guides = [
        ("CODIO_IMPLEMENTATION_GUIDE_OPTIMISED.md", "Level 1: Codio Course Guide (Optimised)"),
        ("CODIO_IMPLEMENTATION_GUIDE_LINEAR.md", "Level 1: Codio Course Guide (Linear)"),
    ]
    
    converted = []
    for md_name, title in guides:
        md_file = script_dir / md_name
        html_file = script_dir / md_name.replace(".md", ".html")
        print(f"\nConverting {md_name}...")
        result = convert_md_to_html(md_file, html_file, title=title)
        if result:
            converted.append(result)
    
    if converted:
        print(f"\nConversion complete! Generated {len(converted)} file(s).")
        if args.open and converted:
            webbrowser.open(f"file://{converted[0].absolute()}")
            print(f"Opened {converted[0].name} in browser.")
        print(f"\nNext steps:")
        for html_path in converted:
            print(f"   - {html_path.name}")
        print(f"   1. Open HTML in your browser")
        print(f"   2. Press Ctrl+P to print")
        print(f"   3. Choose 'Save as PDF' or 'Microsoft Print to PDF'")
    else:
        print(f"\nConversion failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()
