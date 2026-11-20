"""Slice the rendered page into Coupang-ready JPGs (780px wide).
Run after: python3 src/build.py && node src/render.js 1
"""
import json
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "output"
full = Image.open(OUT / "_full@1x.png").convert("RGB")
secs = {s["id"]: s for s in json.loads((OUT / "_sections.json").read_text())}
groups = [
    ("01_hero-checkpoint", ["s-hero", "s-check"]),
    ("02_point1-elephant-pattern", ["s-p1"]),
    ("03_point2-cover-howto", ["s-p2"]),
    ("04_point3-storage", ["s-p3"]),
    ("05_size-info", ["s-size"]),
    ("06_notice", ["s-notice", "s-footer"]),
]
for old in OUT.glob("*.jpg"):
    old.unlink()
for name, ids in groups:
    top = secs[ids[0]]["top"]
    bottom = secs[ids[-1]]["top"] + secs[ids[-1]]["height"]
    part = full.crop((0, top, full.width, bottom))
    part.save(OUT / f"{name}.jpg", quality=92, subsampling=0, optimize=True)
    print(f"{name}.jpg  {part.size[0]}x{part.size[1]}")
full.save(OUT / "00_full.jpg", quality=90, subsampling=0, optimize=True)
print(f"00_full.jpg  {full.size[0]}x{full.size[1]}")
(OUT / "_full@1x.png").unlink()
(OUT / "_sections.json").unlink()
