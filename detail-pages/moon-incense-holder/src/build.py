"""Build index.html from src/template.html.

- Injects a deterministic star-field SVG into the hero.
- Downloads Google Fonts subset to exactly the characters used and embeds them
  as base64 @font-face rules, so the page renders identically offline.
Usage: python3 src/build.py
"""
import base64, random, re, subprocess, urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
tpl = (ROOT / "src" / "template.html").read_text(encoding="utf-8")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/130.0 Safari/537.36")


def sky_svg(w=780, h=1020):
    rnd = random.Random(7)
    dots = []
    for _ in range(90):
        x, y = rnd.uniform(0, w), rnd.uniform(0, h * 0.86)
        r, o = rnd.uniform(0.6, 1.9), rnd.uniform(0.18, 0.8)
        dots.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.2f}" fill="#fff" opacity="{o:.2f}"/>')
    def sparkle(cx, cy, s, o):
        p = (f"M{cx} {cy-s} Q{cx+s*.18} {cy-s*.18} {cx+s} {cy} Q{cx+s*.18} {cy+s*.18} {cx} {cy+s} "
             f"Q{cx-s*.18} {cy+s*.18} {cx-s} {cy} Q{cx-s*.18} {cy-s*.18} {cx} {cy-s}Z")
        return f'<path d="{p}" fill="#e6cd96" opacity="{o}"/>'
    sparks = [sparkle(*a) for a in [(92, 168, 13, .9), (688, 318, 8, .75), (148, 420, 7, .6),
                                     (636, 812, 9, .7), (66, 700, 7, .55), (720, 560, 6, .5)]]
    orbit = ('<circle cx="390" cy="640" r="318" stroke="#e6cd96" stroke-opacity=".10" fill="none"/>'
             '<circle cx="390" cy="640" r="372" stroke="#e6cd96" stroke-opacity=".06" fill="none" stroke-dasharray="2 7"/>')
    return (f'<svg class="sky" width="{w}" height="{h}" viewBox="0 0 {w} {h}" aria-hidden="true">'
            + orbit + "".join(dots) + "".join(sparks) + "</svg>")


def fonts_css(text):
    chars = "".join(sorted(set(text + "0123456789")))
    families = ["Noto Sans KR:wght@400;500;700", "Noto Serif KR:wght@500;700",
                "Cormorant Garamond:wght@600"]
    q = "&".join("family=" + urllib.parse.quote(f, safe=":;@") for f in families)
    url = f"https://fonts.googleapis.com/css2?{q}&text={urllib.parse.quote(chars)}&display=block"
    css = subprocess.run(["curl", "-sSf", "-A", UA, url], capture_output=True, text=True, check=True).stdout
    def embed(m):
        data = subprocess.run(["curl", "-sSfL", "-A", UA, m.group(1)], capture_output=True, check=True).stdout
        return f"url(data:font/woff2;base64,{base64.b64encode(data).decode()}) format('woff2')"
    out, n = re.subn(r"url\((https://[^)]+)\)\s*format\('woff2'\)", embed, css)
    if n == 0:
        raise SystemExit("font download failed:\n" + css[:500])
    print(f"embedded {n} font files for {len(chars)} glyphs")
    return out


html = tpl.replace("<!--SKY-->", sky_svg())
visible = re.sub(r"<style>.*?</style>|<[^>]+>", " ", html, flags=re.S)
html = html.replace("/*FONTS*/", fonts_css(visible))
(ROOT / "index.html").write_text(html, encoding="utf-8")
print("wrote", ROOT / "index.html", f"{len(html)/1024:.0f} KB")
