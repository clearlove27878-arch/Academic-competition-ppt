#!/usr/bin/env python3
"""Scan visible PPTX slide text for Chinese encoding loss.

This intentionally scans only ppt/slides/slide*.xml text runs, not OOXML
metadata/theme files, to avoid noisy false positives.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


MOJIBAKE_RE = re.compile(r"(?:\?{2,}|�|閳|鐎|鐮|鍩|鈹|瀹炶|缁|涓|鍥|鑳)")


def iter_visible_text(pptx: Path):
    with zipfile.ZipFile(pptx) as archive:
        slide_names = sorted(
            name
            for name in archive.namelist()
            if name.startswith("ppt/slides/slide") and name.endswith(".xml")
        )
        for name in slide_names:
            try:
                root = ET.fromstring(archive.read(name))
            except ET.ParseError:
                continue
            for element in root.iter():
                if element.tag.endswith("}t") and element.text:
                    yield name, element.text


def find_issues(pptx: Path):
    issues = []
    total = 0
    for slide_name, text in iter_visible_text(pptx):
        total += 1
        stripped = text.strip()
        if not stripped:
            continue
        if MOJIBAKE_RE.search(stripped):
            issues.append({"slide_xml": slide_name, "text": stripped})
    return total, issues


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pptx", type=Path)
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    args = parser.parse_args()

    if not args.pptx.exists():
        print(f"PPTX not found: {args.pptx}", file=sys.stderr)
        return 2

    total, issues = find_issues(args.pptx)
    result = {
        "pptx": str(args.pptx),
        "visible_text_nodes": total,
        "issue_count": len(issues),
        "issues": issues[:50],
    }

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"visible_text_nodes={total}")
        print(f"encoding_issue_count={len(issues)}")
        for issue in issues[:20]:
            print(f"{issue['slide_xml']}: {issue['text']}")

    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
