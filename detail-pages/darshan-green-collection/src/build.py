"""Build index.html from src/template.html.

- Fills the scent-driven blocks (legend, cards, mood picks, chips) from SCENTS.
- Embeds Google Fonts subset to exactly the characters used (renders offline).
Usage: python3 src/build.py
"""
import base64, re, subprocess, urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/130.0 Safari/537.36")

# order = top-to-bottom order of the packs photo
SCENTS = [
    dict(key="lavender", en="LAVENDER", ko="라벤더", color="#6a4bc4",
         desc="편안하게 감싸는 라벤더 허브", tags=["편안한", "허브"],
         mood="편안한 허브 향에 기대어 쉬고 싶을 때"),
    dict(key="moon-dreams", en="MOON DREAMS", ko="문 드림", color="#24387a",
         desc="고요한 달밤의 무드를 담은 블렌드", tags=["고요한", "달밤무드"],
         mood="고요한 달밤처럼 차분해지고 싶을 때"),
    dict(key="rain-forest", en="RAIN FOREST", ko="레인 포레스트", color="#2e7d4f",
         desc="비 내린 숲의 싱그러운 그린", tags=["싱그러운", "그린"],
         mood="비 내린 숲처럼 싱그러운 기분이 필요할 때"),
    dict(key="white-musk", en="WHITE MUSK", ko="화이트 머스크", color="#c08378",
         desc="깨끗하고 포근한 머스크", tags=["깨끗한", "포근한"],
         mood="깨끗하고 포근한 향이 좋을 때"),
    dict(key="coconut", en="COCONUT", ko="코코넛", color="#1d82c6",
         desc="달콤하고 부드러운 코코넛", tags=["달콤한", "부드러운"],
         mood="달콤하고 부드러운 향이 당길 때"),
    dict(key="baby-powder", en="BABY POWDER", ko="베이비 파우더", color="#6f9fda",
         desc="보송하고 포근한 파우더리", tags=["보송한", "파우더리"],
         mood="보송하고 포근한 느낌이 그리울 때"),
]
# vertical centre of each pack in the displayed packs photo (552px wide, crop rows scaled 552/1612)
LEGEND_Y = [39.7, 103.4, 165.1, 227.2, 290.2, 353.7]


def blocks():
    legend, cards, picks, chips = [], [], [], []
    for i, s in enumerate(SCENTS, 1):
        c = s["color"]
        legend.append(
            f'<li style="top:{LEGEND_Y[i-1]:.1f}px"><i class="dot" style="background:{c}"></i>'
            f'<span class="t"><span class="en">{i:02d}</span><b>{s["ko"]}</b></span></li>')
        tags = "".join(f'<span style="background:{c}1c;color:{c}">#{t}</span>' for t in s["tags"])
        cards.append(
            f'<article class="scard"><div class="im" style="background-image:url(assets/scent-{s["key"]}.jpg)"></div>'
            f'<div class="bd"><div class="top"><span class="no" style="color:{c}">{i:02d}</span>'
            f'<span class="nm">{s["en"]}</span></div><h3>{s["ko"]}</h3><p>{s["desc"]}</p>'
            f'<div class="tags">{tags}</div></div></article>')
        picks.append(
            f'<li><p class="q">{s["mood"]}</p>'
            '<svg class="ar" viewBox="0 0 24 24" fill="none" stroke="#8fe0d2" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12h15M13 6l6 6-6 6"/></svg>'
            f'<div class="a"><i style="background:{c}"></i><div><b>{s["ko"]}</b><span>{s["en"]}</span></div></div></li>')
        chips.append(f'<span><i style="background:{c}"></i>{s["ko"]}</span>')
    return {"<!--LEGEND-->": "\n      ".join(legend), "<!--CARDS-->": "\n    ".join(cards),
            "<!--PICKS-->": "\n    ".join(picks), "<!--CHIPS-->": "".join(chips)}


def fonts_css(text):
    chars = "".join(sorted(set(text + "0123456789")))
    families = ["Noto Sans KR:wght@400;500;600;700;800", "Cormorant Garamond:wght@600"]
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


html = (ROOT / "src" / "template.html").read_text(encoding="utf-8")
for k, v in blocks().items():
    assert k in html, k
    html = html.replace(k, v)
visible = re.sub(r"<style>.*?</style>|<[^>]+>", " ", html, flags=re.S)
html = html.replace("/*FONTS*/", fonts_css(visible))
(ROOT / "index.html").write_text(html, encoding="utf-8")
print("wrote", ROOT / "index.html", f"{len(html)/1024:.0f} KB")
