"""Build index.html (premium editorial version) from src/template.html.

- Generates the six scent chapters, index and spec line from SCENTS.
- Draws incense smoke (SVG turbulence) for the cover and the ritual section.
- Embeds a film-grain tile and Google Fonts subset to exactly the characters used.
Usage: python3 src/build.py
"""
import base64, io, re, subprocess, sys, urllib.parse
from pathlib import Path
import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
from smoke import smoke_svg  # noqa: E402

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/130.0 Safari/537.36")

# order = top-to-bottom order of the packs photo; "pack" = tagline printed on the pack itself
SCENTS = [
    dict(key="lavender", en="LAVENDER", ko="라벤더", pack="Energy and harmony",
         poem="하루를 내려놓는 저녁,<br>보랏빛 허브 향이 천천히 번져요.",
         desc="편안하게 감싸는 라벤더 허브 향", mood="편안한 · 허브 · 부드러운", moment="하루를 마무리하는 저녁"),
    dict(key="moon-dreams", en="MOON DREAMS", ko="문 드림", pack="Sensualidad, placer y buenos sueños",
         poem="불을 끈 방 안으로<br>고요한 달빛이 스며드는 밤.",
         desc="고요한 달밤의 무드를 담은 블렌드", mood="고요한 · 차분한 · 깊은", moment="불을 끈 늦은 밤"),
    dict(key="rain-forest", en="RAIN FOREST", ko="레인 포레스트", pack="Refreshing and purifying",
         poem="비가 그친 숲길,<br>젖은 잎 사이로 맑은 공기가 흘러요.",
         desc="비 내린 숲의 싱그러운 그린 향", mood="싱그러운 · 그린 · 맑은", moment="창을 여는 아침"),
    dict(key="white-musk", en="WHITE MUSK", ko="화이트 머스크", pack="Energy and harmony",
         poem="햇볕에 잘 마른 하얀 리넨처럼<br>깨끗하고 포근한 잔향.",
         desc="깨끗하고 포근한 머스크 향", mood="깨끗한 · 포근한 · 은은한", moment="샤워를 마친 오후"),
    dict(key="coconut", en="COCONUT", ko="코코넛", pack="Cleanses evil, attracts good fortune",
         poem="느긋한 주말 오후,<br>달콤한 코코넛이 공간을 감싸요.",
         desc="달콤하고 부드러운 코코넛 향", mood="달콤한 · 부드러운 · 여유로운", moment="여유로운 주말 오후"),
    dict(key="baby-powder", en="BABY POWDER", ko="베이비 파우더", pack="Gentle, calming and clean",
         poem="갓 세탁한 이불 속처럼<br>보송하고 포근한 시간.",
         desc="보송하고 포근한 파우더리 향", mood="보송한 · 포근한 · 순한", moment="낮잠 같은 휴식"),
]


def field_tone(key):
    a = np.asarray(Image.open(ROOT / "assets" / f"field-{key}.jpg").convert("RGB")).astype(np.float32)
    return "tone-dark" if float((a @ np.array([.2126, .7152, .0722])).mean()) < 150 else "tone-light"


def chapters():
    out = []
    for i, s in enumerate(SCENTS, 1):
        side = "odd" if i % 2 else "even"
        out.append(f'''<section class="sec chapter {side} {field_tone(s["key"])}" id="s-ch{i}">
  <div class="visual" style="background-image:url(assets/field-{s["key"]}.jpg)">
    <span class="no">{i:02d}</span>
    <figure class="card"><img src="assets/card-{s["key"]}.jpg" alt="{s["ko"]} 팩 일러스트"></figure>
  </div>
  <div class="text">
    <div class="name"><div class="nm"><h3>{s["en"]}</h3><span>{s["ko"]}</span></div>
      <p class="pk"><small>ON THE PACK</small><q>{s["pack"]}</q></p></div>
    <p class="poem">{s["poem"]}</p>
    <p class="desc">{s["desc"]}</p>
    <dl class="meta"><div><dt>MOOD</dt><dd>{s["mood"]}</dd></div><div><dt>MOMENT</dt><dd>{s["moment"]}</dd></div></dl>
  </div>
</section>''')
    return "\n".join(out)


def index():
    return "\n    ".join(f'<li><span class="n">{i:02d}</span><span class="t"><b>{s["en"]}</b><span>{s["ko"]}</span></span></li>'
                           for i, s in enumerate(SCENTS, 1))


def stick_svg():
    x, top = 190, 600
    art = f'''<svg class="stick" width="780" height="1100" viewBox="0 0 780 1100" aria-hidden="true">
  <defs>
    <radialGradient id="emb"><stop offset="0" stop-color="#ffc98a" stop-opacity=".95"/><stop offset=".35" stop-color="#ff8a3d" stop-opacity=".55"/><stop offset="1" stop-color="#ff8a3d" stop-opacity="0"/></radialGradient>
    <linearGradient id="dish" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4a524c"/><stop offset="1" stop-color="#1f2521"/></linearGradient>
  </defs>
  <ellipse cx="{x}" cy="984" rx="118" ry="16" fill="#000" opacity=".35"/>
  <path d="M{x - 86} 958 Q{x - 80} 990 {x} 992 Q{x + 80} 990 {x + 86} 958 Z" fill="url(#dish)"/>
  <ellipse cx="{x}" cy="958" rx="86" ry="15" fill="#3c433e" stroke="#59625b" stroke-width="1.2"/>
  <ellipse cx="{x}" cy="958" rx="66" ry="10" fill="#7a746a" opacity=".55"/>
  <path d="M{x} 958V908" stroke="#b8925f" stroke-width="2.6" stroke-linecap="round"/>
  <path d="M{x} 908V{top + 12}" stroke="#4b3527" stroke-width="5" stroke-linecap="round"/>
  <path d="M{x} {top + 12}V{top + 3}" stroke="#9a948b" stroke-width="4.6" stroke-linecap="round"/>
  <circle cx="{x}" cy="{top + 1}" r="22" fill="url(#emb)"/>
  <circle cx="{x}" cy="{top + 2}" r="3.4" fill="#ffd2a0"/>
</svg>'''
    return art + smoke_svg("rit", 780, 1100, x, top - 2, ey=30, seed=2, amp=58, drift=34)


def grain_uri(size=180, sigma=26, seed=3):
    rng = np.random.default_rng(seed)
    g = np.clip(rng.normal(128, sigma, (size, size)), 0, 255).astype(np.uint8)
    buf = io.BytesIO(); Image.fromarray(g, "L").save(buf, "PNG", optimize=True)
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()


def fonts_css(text):
    chars = "".join(sorted(set(text + "0123456789“”")))
    families = ["Noto Sans KR:wght@300;400;500", "Noto Serif KR:wght@400;500",
                "Cormorant Garamond:ital,wght@0,300;0,500;0,600;1,300;1,400"]
    q = "&".join("family=" + urllib.parse.quote(f, safe=":;@,") for f in families)
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
parts = {
    "<!--CHAPTERS-->": chapters(),
    "<!--INDEX-->": index(),
    "<!--SPECSCENTS-->": "<br>".join([" · ".join(s["ko"] for s in SCENTS[:3]), " · ".join(s["ko"] for s in SCENTS[3:])]),
    "<!--SMOKE:cover-->": smoke_svg("cov", 780, 1300, 560, 790, ey=40, seed=5, amp=76, drift=-46),
    "<!--STICK-->": stick_svg(),
    "/*GRAIN*/": grain_uri(),
}
for k, v in parts.items():
    assert k in html, k
    html = html.replace(k, v)
visible = re.sub(r"<style>.*?</style>|<svg.*?</svg>|<[^>]+>", " ", html, flags=re.S)
html = html.replace("/*FONTS*/", fonts_css(visible))
(ROOT / "index.html").write_text(html, encoding="utf-8")
print("wrote", ROOT / "index.html", f"{len(html)/1024:.0f} KB")
