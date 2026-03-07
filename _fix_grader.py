path = ".guides/secure/level1_graders/lab_2.2_grader.py"
with open(path, "r", encoding="utf-8") as f:
    s = f.read()

# Remove the duplicate fallback block (lines 55-64 in the current file)
old = """        else:
            block_text = rest.strip()
    # Fallback: if block detection missed (e.g. different indent/line endings), get section from full content
    if "- text:" not in block_text and "text:" not in block_text:
        idx = content.find("utter_goodbye")
        if idx >= 0:
            rest = content[idx:]
            # End at next utter_ that isn't utter_goodbye (start of next response)
            match = re.search(r"\\nutter_(?!goodbye\\s*:)[a-z_]+\\s*:", rest)
            block_text = rest[: match.start()] if match else rest
        else:
            block_text = ""
    if "- text:" not in block_text and "text:" not in block_text:"""

new = """        else:
            block_text = rest.strip()
    if "- text:" not in block_text and "text:" not in block_text:"""

if old in s:
    s = s.replace(old, new, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(s)
    print("Removed duplicate fallback")
else:
    print("Pattern not found - file may already be clean")
