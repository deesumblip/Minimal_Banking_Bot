#!/usr/bin/env python3
"""
Lab 2.2: Creating Your First Response - Grader Script (Codio)
Runs from workspace root. Checks level1/domain/basics.yml for utter_goodbye response.
"""

import os
import sys
from pathlib import Path

WORKSPACE_ROOT = Path(os.environ.get("CODIO_WORKSPACE", os.getcwd()))
if not WORKSPACE_ROOT.is_absolute():
    WORKSPACE_ROOT = Path.cwd()
DOMAIN_FILE = WORKSPACE_ROOT / "level1" / "domain" / "basics.yml"

def main():
    if not DOMAIN_FILE.is_file():
        print("FAIL")
        print("File not found: level1/domain/basics.yml", file=sys.stderr)
        sys.exit(1)

    try:
        import yaml
    except ImportError:
        print("FAIL")
        print("YAML module not available.", file=sys.stderr)
        sys.exit(1)

    try:
        with open(DOMAIN_FILE, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
    except Exception as e:
        print("FAIL")
        print(f"Invalid YAML: {e}", file=sys.stderr)
        sys.exit(1)

    if not data or not isinstance(data, dict):
        print("FAIL")
        print("Domain file has no content or is not a dict.", file=sys.stderr)
        sys.exit(1)

    responses = data.get("responses")
    if not responses or not isinstance(responses, dict):
        print("FAIL")
        print("No responses: section found or it is not a mapping.", file=sys.stderr)
        sys.exit(1)

    goodbye = responses.get("utter_goodbye")
    if goodbye is None:
        print("FAIL")
        print("utter_goodbye not found under responses:.", file=sys.stderr)
        sys.exit(1)

    if not isinstance(goodbye, list) or len(goodbye) == 0:
        print("FAIL")
        print("utter_goodbye must be a list with at least one variation (- text: ...).", file=sys.stderr)
        sys.exit(1)

    first = goodbye[0]
    if not isinstance(first, dict):
        print("FAIL")
        print("Each response variation must be a mapping (e.g. - text: ...).", file=sys.stderr)
        sys.exit(1)

    text = first.get("text")
    if not text or not isinstance(text, str) or not text.strip():
        print("FAIL")
        print("utter_goodbye must have at least one non-empty text variation.", file=sys.stderr)
        sys.exit(1)

    farewell_words = ("goodbye", "bye", "see you", "farewell", "have a great", "take care")
    text_lower = text.strip().lower()
    if not any(w in text_lower for w in farewell_words):
        print("FAIL")
        print("utter_goodbye text should be a farewell message (e.g. Goodbye, See you).", file=sys.stderr)
        sys.exit(1)

    metadata = first.get("metadata")
    if not metadata or not isinstance(metadata, dict):
        print("FAIL")
        print("utter_goodbye should include metadata with rephrase: True.", file=sys.stderr)
        sys.exit(1)
    if metadata.get("rephrase") is not True:
        print("FAIL")
        print("metadata should contain rephrase: True.", file=sys.stderr)
        sys.exit(1)

    print("PASS")
    sys.exit(0)

if __name__ == "__main__":
    main()
