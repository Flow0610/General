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


def _petals(n, r1, r2, w, rot=0.0):
    out = []
    for i in range(n):
        a = rot + i * 360 / n
        m = (r1 + r2) / 2
        out.append(f'<path transform="rotate({a:.2f})" d="M0 {-r1:.1f}Q{w:.1f} {-m:.1f} 0 {-r2:.1f}Q{-w:.1f} {-m:.1f} 0 {-r1:.1f}Z"/>')
    return "".join(out)


def mandala(cx, cy, R, color, op, sw):
    dots = "".join(
        f'<circle transform="rotate({i * 360 / 36:.1f})" cx="0" cy="{-R * .79:.1f}" r="{R * .009:.2f}" fill="{color}" stroke="none"/>'
        for i in range(36))
    return (f'<g transform="translate({cx} {cy})" stroke="{color}" stroke-opacity="{op}" fill="none" stroke-width="{sw}">'
            f'<circle r="{R * .16:.1f}"/>' + _petals(8, R * .16, R * .42, R * .1)
            + f'<circle r="{R * .46:.1f}"/>' + _petals(16, R * .46, R * .72, R * .075, 11.25)
            + f'<g fill-opacity="{op}">{dots}</g>'
            + f'<circle r="{R * .86:.1f}"/>' + _petals(32, R * .86, R * .98, R * .04)
            + f'<circle r="{R:.1f}" stroke-dasharray="2 6"/></g>')


def sky_svg(w=780, h=1044):
    rnd = random.Random(11)
    dust = []
    for _ in range(60):
        x, y = rnd.uniform(0, w), rnd.uniform(0, h * 0.88)
        dust.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{rnd.uniform(.6, 1.6):.2f}" fill="#e6cd96" opacity="{rnd.uniform(.12, .45):.2f}"/>')
    return (f'<svg class="sky" width="{w}" height="{h}" viewBox="0 0 {w} {h}" aria-hidden="true">'
            + mandala(390, 650, 360, "#e6cd96", .11, 1.2) + "".join(dust) + "</svg>")


def ornament_svg():
    small = (f'<g transform="translate(30 30)" stroke="#e6cd96" fill="none" stroke-width="1.3">'
             f'<circle r="4" fill="#e6cd96"/>' + _petals(8, 6, 17, 4.2)
             + '<circle r="19"/>' + _petals(16, 19, 28, 2.6, 11.25) + '</g>')
    return f'<svg class="orn" viewBox="0 0 60 60" aria-hidden="true">{small}</svg>'


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


html = tpl.replace("<!--SKY-->", sky_svg()).replace("<!--ORN-->", ornament_svg())
visible = re.sub(r"<style>.*?</style>|<[^>]+>", " ", html, flags=re.S)
html = html.replace("/*FONTS*/", fonts_css(visible))
(ROOT / "index.html").write_text(html, encoding="utf-8")
print("wrote", ROOT / "index.html", f"{len(html)/1024:.0f} KB")
