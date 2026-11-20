"""Render the page for each platform and slice it into upload-ready JPGs.

coupang_780 : 780px wide
naver_860   : 860px wide (rendered at 860/780 device scale -> crisp text, no resampling)
Sections are packed in order into slices no taller than 2,500px at 860px (2,267px at 780px);
a section is never split.
Usage: python3 src/build.py && python3 src/export.py
"""
import json, shutil, subprocess
import numpy as np
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "output"
PLATFORMS = {"coupang_780": 780, "naver_860": 860}
MAX_CSS = int(2500 * 780 / 860)
SHORT = {"s-cover": "cover", "s-prologue": "prologue", "s-stories": "stories", "s-ritual": "ritual",
         "s-box": "box", "s-foryou": "foryou", "s-details": "details", "s-notice": "notice", "s-footer": "footer",
         **{f"s-ch{i}": f"scent{i}" for i in range(1, 7)}}


def pack(secs):
    groups, cur = [], []
    for s in secs:
        h = sum(x["height"] for x in cur) + s["height"]
        if cur and h > MAX_CSS:
            groups.append(cur); cur = []
        cur.append(s)
    groups.append(cur)
    return groups


groups = None
for name, width in PLATFORMS.items():
    scale = width / 780
    for stale in OUT.glob("_full@*x.png"):
        stale.unlink()
    subprocess.run(["node", str(ROOT / "src" / "render.js"), repr(scale)], check=True, capture_output=True)
    full = Image.open(next(OUT.glob("_full@*x.png"))).convert("RGB")
    assert full.width == width, (full.width, width)
    secs = json.loads((OUT / "_sections.json").read_text())
    groups = groups or pack(secs)
    d = OUT / name
    shutil.rmtree(d, ignore_errors=True); d.mkdir(parents=True)
    starts = [round(g[0]["top"] * scale) for g in groups] + [full.height]
    for gi, g in enumerate(groups):
        part = np.asarray(full.crop((0, starts[gi], width, starts[gi + 1]))).copy()
        # fractional scaling can leave one blended row at a section boundary: replace it with its neighbour
        for edge, nb in ((0, 1), (-1, -2)):
            if np.abs(part[edge].astype(int) - part[nb].astype(int)).mean() > 5:
                part[edge] = part[nb]
        part = Image.fromarray(part)
        assert part.height <= 2500, (gi, part.height)
        fname = f"{gi + 1:02d}_" + "-".join(SHORT[x["id"]] for x in g) + ".jpg"
        part.save(d / fname, quality=92, subsampling=0, optimize=True)
        print(f"{name}/{fname}  {part.width}x{part.height}")
    full.save(d / "00_full.jpg", quality=90, subsampling=0, optimize=True)
    print(f"{name}/00_full.jpg  {full.width}x{full.height}")
for f in OUT.glob("_full@*x.png"):
    f.unlink()
(OUT / "_sections.json").unlink()
