#!/usr/bin/env python3
"""
Convert TUTORIAL.md files to HTML with GitHub-style CSS.

Usage:
    python convert_tutorials_to_html.py          # Convert all levels (1-5)
    python convert_tutorials_to_html.py 1         # Convert only Level 1
    python convert_tutorials_to_html.py 2 3 5    # Convert Levels 2, 3, and 5
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

def convert_tutorial(level_num, open_browser=False):
    """Convert a single tutorial to HTML."""
    root_dir = Path(__file__).parent
    level_dir = root_dir / f"level{level_num}"
    md_file = level_dir / "TUTORIAL.md"
    html_file = level_dir / "TUTORIAL.html"
    
    if not md_file.exists():
        print(f"[ERROR] Level {level_num}: TUTORIAL.md not found in {level_dir}")
        return False
    
    print(f"\nLevel {level_num}: Reading {md_file.name}...")
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
    <title>Level {level_num} Tutorial</title>
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
        
        if open_browser:
            webbrowser.open(f"file://{html_file.absolute()}")
            print(f"   [OK] Opened in browser")
        
        return True
    except Exception as e:
        print(f"   [ERROR] Error saving file: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(
        description='Convert TUTORIAL.md files to HTML with GitHub-style CSS',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python convert_tutorials_to_html.py          # Convert all levels (1-5)
  python convert_tutorials_to_html.py 1        # Convert only Level 1
  python convert_tutorials_to_html.py 2 3 5    # Convert Levels 2, 3, and 5
  python convert_tutorials_to_html.py --open   # Convert all and open in browser
        """
    )
    parser.add_argument(
        'levels',
        nargs='*',
        type=int,
        help='Level numbers to convert (1-5). If none specified, converts all levels.'
    )
    parser.add_argument(
        '--open',
        action='store_true',
        help='Open HTML files in browser after conversion'
    )
    
    args = parser.parse_args()
    
    # Determine which levels to convert
    if args.levels:
        # Validate that all provided levels are valid
        invalid_levels = [l for l in args.levels if l not in [1, 2, 3, 4, 5]]
        if invalid_levels:
            print(f"Error: Invalid level numbers: {invalid_levels}")
            print("Valid levels are: 1, 2, 3, 4, 5")
            sys.exit(1)
        levels_to_convert = args.levels
    else:
        levels_to_convert = [1, 2, 3, 4, 5]
    
    print("Converting tutorials to HTML...")
    print(f"   Levels: {', '.join(map(str, levels_to_convert))}")
    
    success_count = 0
    for level in levels_to_convert:
        if convert_tutorial(level, open_browser=args.open):
            success_count += 1
    
    print(f"\nConversion complete!")
    print(f"   Successfully converted: {success_count}/{len(levels_to_convert)} levels")
    
    if success_count > 0:
        print(f"\nNext steps:")
        print(f"   1. Open the HTML files in your browser")
        print(f"   2. Press Ctrl+P to print")
        print(f"   3. Choose 'Save as PDF' or 'Microsoft Print to PDF'")
        print(f"   4. Save your PDF files")

if __name__ == "__main__":
    main()
