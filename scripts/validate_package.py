#!/usr/bin/env python3
"""Validate the installable eight-skill package using only the standard library."""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "math-paper-rewrite", "paper-structure-planning", "statement-writing",
    "identify-key-steps", "identify-key-ingredients", "paper-style",
    "paper-polish", "outline-file-writing",
}

def main():
    manifest = json.loads((ROOT / "provenance.json").read_text(encoding="utf-8"))
    actual = {p.name for p in (ROOT / "skills").iterdir() if p.is_dir()}
    assert actual == EXPECTED == set(manifest["skills"]), "Skill inventory mismatch"
    license_bytes = (ROOT / "LICENSE").read_bytes()
    for name in sorted(EXPECTED):
        folder = ROOT / "skills" / name
        text = (folder / "SKILL.md").read_text(encoding="utf-8")
        match = re.match(r"^---\nname: ([a-z0-9-]+)\ndescription: (.+)\n---\n", text)
        assert match and match.group(1) == name, "Invalid frontmatter: " + name
        description = json.loads(match.group(2))
        assert isinstance(description, str) and description.strip(), name
        assert not re.search(r"\[TODO|\bTBD\b", text), "Unfinished scaffold: " + name
        for target in set(re.findall(r"(?:\.\./|references/)[A-Za-z0-9_./-]+\.md", text)):
            resolved = (folder / target).resolve()
            assert ROOT in resolved.parents and resolved.is_file(), "Missing reference: " + target
        ui = (folder / "agents" / "openai.yaml").read_text(encoding="utf-8")
        for field in ("display_name", "short_description", "default_prompt"):
            assert re.search(r"^  " + field + r": .+", ui, re.M), "Missing UI field: " + name
        assert "$" + name in ui, "Prompt does not invoke its skill: " + name
        assert (folder / "LICENSE").read_bytes() == license_bytes, "License mismatch: " + name
    for source in manifest["sources"]:
        data = (ROOT / source["local"]).read_bytes()
        assert hashlib.sha256(data).hexdigest() == source["sha256"], source["local"]
    for filename in ("README.md", "NOTICE.md"):
        text = (ROOT / filename).read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^)]+)\)", text):
            if not re.match(r"[a-z]+://", target):
                assert (ROOT / target.split("#")[0]).exists(), "Broken link: " + target
    print("PASS: 8 skills, metadata, local dependencies, licenses, and source hashes")

if __name__ == "__main__":
    main()
