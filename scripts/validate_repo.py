"""Minimal zero-dependency local/CI validation of repository navigation links."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import sys

root = Path(__file__).resolve().parent.parent
required = [
    "README.md", "AGENTS.md", "WORKFLOW.md",
    "drafts/ORIGINAL-REQUEST-BRIEF.md", "drafts/AGENT-REVIEW-PROMPT.md",
    "contracts/work-item.md", "contracts/evidence.md",
    "playbooks/README.md", ".agents/skills/README.md",
]
problems = [f"Missing required document: {x}" for x in required if not (root / x).is_file()]
# Inline Markdown references; not a full Markdown parser.
pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
for md in root.rglob("*.md"):
    if ".git" in md.parts:
        continue
    text = md.read_text(encoding="utf8")
    for target in pattern.findall(text):
        target = target.strip().split(" ", 1)[0].strip("<>")
        if not target or target.startswith(("#", "http://", "https://", "mailto:", "data:")):
            continue
        url = urlsplit(target)
        local = unquote(url.path)
        if not local:
            continue
        resolved = (md.parent / local).resolve()
        if not resolved.is_relative_to(root) or not resolved.exists():
            problems.append(f"{md.relative_to(root)}: broken link -> {target}")

for item in problems:
    print("ERROR:", item)
print(f"Checked {len(list(root.rglob('*.md')))} Markdown files")
sys.exit(1 if problems else 0)
