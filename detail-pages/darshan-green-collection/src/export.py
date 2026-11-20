"""Render the page for each platform and slice it into upload-ready JPGs.

coupang_780 : 780px wide (CSS 1x)
naver_860   : 860px wide (same layout rendered at 860/780 scale -> crisp text, no resampling)
Every slice stays under 2,500px tall at 860px.
Usage: python3 src/build.py && python3 src/export.py
"""
import json, shutil, subprocess
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "output"
PLATFORMS = {"coupang_780": 780, "naver_860": 860}
GROUPS = [
    ("01_hero", ["s-hero"]),
    ("02_6scents-inside", ["s-inside"]),
    ("03_scent-guide", ["s-guide"]),
    ("04_mood-howto", ["s-mood", "s-how"]),
    ("05_gift-package", ["s-pkg"]),
    ("06_recommend-info", ["s-rec", "s-info"]),
    ("07_notice", ["s-notice", "s-footer"]),
]
for name, width in PLATFORMS.items():
    scale = width / 780
    for stale in OUT.glob("_full@*x.png"):
        stale.unlink()
    subprocess.run(["node", str(ROOT / "src" / "render.js"), repr(scale)], check=True, capture_output=True)
    full_png = next(OUT.glob("_full@*x.png"))
    full = Image.open(full_png).convert("RGB")
    assert full.width == width, (full.width, width)
    secs = {s["id"]: s for s in json.loads((OUT / "_sections.json").read_text())}
    d = OUT / name
    shutil.rmtree(d, ignore_errors=True); d.mkdir(parents=True)
    starts = [round(secs[ids[0]]["top"] * scale) for _, ids in GROUPS] + [full.height]
    for gi, (gname, ids) in enumerate(GROUPS):
        top, bottom = starts[gi], starts[gi + 1]          # contiguous: no gaps, no duplicated rows
        part = full.crop((0, top, width, bottom))
        assert part.height <= 2500, (gname, part.height)
        part.save(d / f"{gname}.jpg", quality=92, subsampling=0, optimize=True)
        print(f"{name}/{gname}.jpg  {part.width}x{part.height}")
    full.save(d / "00_full.jpg", quality=90, subsampling=0, optimize=True)
    print(f"{name}/00_full.jpg  {full.width}x{full.height}")
    full_png.unlink()
(OUT / "_sections.json").unlink()
