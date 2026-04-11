"""Check Level 5 unit index.json order matches .md and .json page files."""
import json
from pathlib import Path

base = Path(__file__).resolve().parent / "content" / "Level-5---Tool-Calling-f9e0"
issues = []
for unit_dir in sorted(base.iterdir()):
    if not unit_dir.is_dir() or not unit_dir.name.startswith("Unit-"):
        continue
    idx = unit_dir / "index.json"
    if not idx.exists():
        issues.append((str(unit_dir), "NO index.json"))
        continue
    try:
        data = json.loads(idx.read_text(encoding="utf-8"))
        order = data.get("order", [])
    except Exception as e:
        issues.append((str(unit_dir), f"Invalid index.json: {e}"))
        continue
    md_files = {f.stem for f in unit_dir.glob("*.md")}
    page_jsons = {f.stem for f in unit_dir.glob("*.json") if f.name != "index.json"}
    in_order = set(order)
    for pid in order:
        if pid not in md_files:
            issues.append((str(unit_dir), f'order has "{pid}" but no .md'))
        if pid not in page_jsons:
            issues.append((str(unit_dir), f'order has "{pid}" but no .json'))
    for stem in md_files:
        if stem not in in_order:
            issues.append((str(unit_dir), f'orphan .md "{stem}" not in order'))
    for stem in page_jsons:
        if stem not in in_order:
            issues.append((str(unit_dir), f'orphan .json "{stem}" not in order'))

for loc, msg in issues:
    print(f"{loc}: {msg}")
if not issues:
    print("OK: Level 5 all units coherent (order matches .md and .json)")
