#!/usr/bin/env python3
"""Extract lightweight style signals from a PPTX template.

This helper is intentionally conservative: it never modifies the input PPTX and
uses only OOXML package reads plus optional Pillow image analysis when available.
It is meant to support style-card drafting, not to perfectly reverse-engineer a
PowerPoint theme.
"""

from __future__ import annotations

import argparse
import collections
import io
import json
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


NS = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
}


def text_of(node: ET.Element) -> str:
    return "".join(t.text or "" for t in node.findall(".//a:t", NS)).strip()


def slide_number(name: str) -> int:
    match = re.search(r"slide(\d+)\.xml$", name)
    return int(match.group(1)) if match else 0


def maybe_image_palette(zf: zipfile.ZipFile, media_names: list[str], limit: int = 10) -> list[dict]:
    try:
        from PIL import Image  # type: ignore
    except Exception:
        return []

    palettes = []
    for name in media_names[:limit]:
        try:
            image = Image.open(io.BytesIO(zf.read(name))).convert("RGB")
        except Exception:
            continue
        small = image.resize((120, 68))
        counts = collections.Counter()
        for r, g, b in small.getdata():
            if r > 245 and g > 245 and b > 245:
                continue
            bucket = (round(r / 16) * 16, round(g / 16) * 16, round(b / 16) * 16)
            counts[bucket] += 1
        palettes.append(
            {
                "media": name,
                "size": [image.width, image.height],
                "dominant": [f"#{r:02X}{g:02X}{b:02X}" for (r, g, b), _ in counts.most_common(6)],
            }
        )
    return palettes


def extract(path: Path) -> dict:
    result: dict = {"source": str(path), "warnings": []}
    with zipfile.ZipFile(path) as zf:
        names = zf.namelist()
        slides = sorted(
            [n for n in names if re.match(r"ppt/slides/slide\d+\.xml$", n)],
            key=slide_number,
        )
        result["slide_count"] = len(slides)

        pres_xml = zf.read("ppt/presentation.xml").decode("utf-8", errors="ignore")
        size_match = re.search(r'<p:sldSz[^>]*cx="(\d+)"[^>]*cy="(\d+)"', pres_xml)
        if size_match:
            cx, cy = map(int, size_match.groups())
            result["slide_size_emu"] = [cx, cy]
            result["aspect_ratio"] = round(cx / cy, 4) if cy else None

        media = [n for n in names if n.startswith("ppt/media/")]
        result["media_count"] = len(media)
        result["media_palette"] = maybe_image_palette(zf, media)

        colors: collections.Counter[str] = collections.Counter()
        fonts: collections.Counter[str] = collections.Counter()
        shape_geometries: collections.Counter[str] = collections.Counter()
        slide_summaries = []

        for idx, slide_name in enumerate(slides, 1):
            xml = zf.read(slide_name).decode("utf-8", errors="ignore")
            root = ET.fromstring(xml)
            texts = [text_of(p) for p in root.findall(".//p:sp", NS)]
            texts = [t for t in texts if t]
            colors.update(f"#{c.upper()}" for c in re.findall(r'<a:srgbClr val="([0-9A-Fa-f]{6})"', xml))
            fonts.update(re.findall(r'<a:latin typeface="([^"]+)"', xml))
            shape_geometries.update(re.findall(r'<a:prstGeom prst="([^"]+)"', xml))
            slide_summaries.append(
                {
                    "slide": idx,
                    "text_items": len(texts),
                    "text_sample": texts[:8],
                    "color_sample": [c for c, _ in colors.most_common(8)],
                }
            )

        result["top_colors"] = [{"hex": c, "count": n} for c, n in colors.most_common(20)]
        result["top_fonts"] = [{"font": f, "count": n} for f, n in fonts.most_common(20)]
        result["shape_geometries"] = [{"geometry": g, "count": n} for g, n in shape_geometries.most_common(20)]
        result["slides"] = slide_summaries

    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract style signals from a PPTX template.")
    parser.add_argument("pptx", type=Path)
    parser.add_argument("--output", "-o", type=Path, help="Write JSON to this path.")
    parser.add_argument("--pretty", action="store_true", help="Print a compact human summary before JSON.")
    args = parser.parse_args()

    data = extract(args.pptx)
    payload = json.dumps(data, ensure_ascii=False, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload + "\n", encoding="utf-8")
    if args.pretty:
        print(f"source: {data['source']}")
        print(f"slides: {data.get('slide_count')} ratio: {data.get('aspect_ratio')}")
        print("top colors:", ", ".join(c["hex"] for c in data.get("top_colors", [])[:8]))
        print("top fonts:", ", ".join(f["font"] for f in data.get("top_fonts", [])[:8]))
    else:
        print(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
