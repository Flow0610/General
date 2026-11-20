"""Build the Coupang top notice banner ("구매 전 확인하세요") for the moon box holder page.

Follows Coupang's 판매자로켓 notice-banner template (src/coupang-guide/): 1000px wide, fixed title image,
Noto Sans CJK KR (= Noto Sans KR) 30px body. Outputs:
  output/top-notice/top-notice_1000.jpg   - template size (recommended upload)
  output/top-notice/top-notice_780.jpg    - same banner at 780px, matching the other slices
  output/top-notice/preview_full-page.jpg - 780px banner stacked on top of output/00_full.jpg (preview only)
Usage: python3 src/build_top_notice.py
"""
import base64, re, subprocess, urllib.parse
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "output" / "top-notice"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/130.0 Safari/537.36")


def fonts_css(text):
    chars = "".join(sorted(set(text + "0123456789")))
    q = "family=" + urllib.parse.quote("Noto Sans KR:wght@400;500;700", safe=":;@,")
    url = f"https://fonts.googleapis.com/css2?{q}&text={urllib.parse.quote(chars)}&display=block"
    css = subprocess.run(["curl", "-sSf", "-A", UA, url], capture_output=True, text=True, check=True).stdout
    def embed(m):
        data = subprocess.run(["curl", "-sSfL", "-A", UA, m.group(1)], capture_output=True, check=True).stdout
        return f"url(data:font/woff2;base64,{base64.b64encode(data).decode()}) format('woff2')"
    out, n = re.subn(r"url\((https://[^)]+)\)\s*format\('woff2'\)", embed, css)
    if n == 0:
        raise SystemExit("font download failed:\n" + css[:500])
    return out


src = (ROOT / "src" / "top-notice.html").read_text(encoding="utf-8")
visible = re.sub(r"<style>.*?</style>|<svg.*?</svg>|<[^>]+>", " ", src, flags=re.S)
built = ROOT / "src" / "_top-notice.built.html"
built.write_text(src.replace("/*FONTS*/", fonts_css(visible)), encoding="utf-8")

js = r"""
const { chromium } = require('playwright');
(async () => {
  const [file, out, scale] = process.argv.slice(1);
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1000, height: 800 }, deviceScaleFactor: Number(scale) });
  await p.goto('file://' + file, { waitUntil: 'load' });
  await p.evaluate(() => document.fonts.ready);
  await (await p.$('#s-notice-top')).screenshot({ path: out });
  await b.close();
})();
"""
OUT.mkdir(parents=True, exist_ok=True)
for width in (1000, 780):
    png = OUT / f"_top-notice_{width}.png"
    subprocess.run(["node", "-e", js, str(built), str(png), repr(width / 1000)], check=True)
    im = Image.open(png).convert("RGB")
    assert im.width == width, im.size
    im.save(OUT / f"top-notice_{width}.jpg", quality=93, subsampling=0, optimize=True)
    png.unlink()
    print(f"top-notice_{width}.jpg  {im.width}x{im.height}")
built.unlink()

top = Image.open(OUT / "top-notice_780.jpg"); page = Image.open(ROOT / "output" / "00_full.jpg")
prev = Image.new("RGB", (780, top.height + page.height), "white")
prev.paste(top, (0, 0)); prev.paste(page, (0, top.height))
prev.save(OUT / "preview_full-page.jpg", quality=88, subsampling=0, optimize=True)
print(f"preview_full-page.jpg  {prev.width}x{prev.height}")
