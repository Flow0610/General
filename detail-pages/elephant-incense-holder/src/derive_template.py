"""Derive the elephant template from the moon template so both pages share one layout.
Usage: python3 src/derive_template.py   (writes src/template.html)
"""
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
s = (HERE.parent.parent / "moon-incense-holder" / "src" / "template.html").read_text(encoding="utf-8")

def rep(old, new, count=1):
    global s
    n = s.count(old)
    assert n == count, (n, old[:70])
    s = s.replace(old, new)

ELEPHANT = ("M23 33C17 31 12 24 10 13C9.5 9.5 13.5 8.5 14.5 12C16 19 19.5 23.5 24.5 24.5"
            "C26 17 32 13 41 13.5C46 12 52 13 58 14.5C78 14 92 25 92 42C93.5 45 95.5 48.5 97 52.5"
            "L94.5 53.5C93 50.5 91.5 48 90 46.5L88.5 70L79 70L77.5 59C68 61.5 53 61.5 45 59"
            "L44 70L34.5 70L33 53C27 49 24 42 23 33Z")

# ---- meta / theme ----
rep("<title>박스형 달문양 인센스 홀더 | 상세페이지</title>", "<title>박스형 코끼리문양 인센스 홀더 | 상세페이지</title>")
rep("--night:#121628;", "--night:#0f2724;")
rep("background:radial-gradient(130% 75% at 50% 0%,#2b3263 0%,#181d3a 48%,#0e1122 100%)}",
    "background:radial-gradient(130% 75% at 50% 0%,#245850 0%,#143a35 48%,#0a1f1c 100%)}")
rep(".hero{height:1020px;", ".hero{height:1044px;")
rep(".hero .moon{position:absolute;left:612px;top:30px;width:150px;height:150px}",
    ".hero .orn{position:relative;display:block;width:60px;height:60px;margin:64px auto 0}")
rep(".hero .eyebrow{position:relative;padding-top:122px;", ".hero .eyebrow{position:relative;margin-top:22px;")
rep("font:700 66px/1.2 'Noto Serif KR',serif;letter-spacing:-.04em;color:#fbf6ec}",
    "font:700 60px/1.25 'Noto Serif KR',serif;letter-spacing:-.04em;color:#fbf6ec}")
rep(".hero .glow{position:absolute;left:10px;top:420px;", ".hero .glow{position:absolute;left:10px;top:446px;")
rep(".hero .floor{position:absolute;left:120px;top:742px;", ".hero .floor{position:absolute;left:120px;top:770px;")
rep(".hero .prod{position:absolute;left:52px;top:478px;", ".hero .prod{position:absolute;left:52px;top:500px;")
rep("list-style:none}\n.hero .badges li", "list-style:none}\n.hero .badges li")
rep(".hero .badges{position:absolute;left:0;right:0;top:868px;", ".hero .badges{position:absolute;left:0;right:0;top:892px;")
s = s.replace("/* ---------- COMMON ---------- */",
              ".ico-el{display:block;fill:currentColor}\n\n/* ---------- COMMON ---------- */", 1)

# ---- shared elephant symbol ----
rep("<body>\n", '<body>\n<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>'
    f'<symbol id="eleph" viewBox="0 0 100 80"><path d="{ELEPHANT}"/></symbol></defs></svg>\n')

# ---- hero ----
s = re.sub(r'  <svg class="moon".*?</svg>\n', "  <!--ORN-->\n", s, count=1, flags=re.S)
rep('<p class="eyebrow en">MOON &amp; SUN · INCENSE BOX</p>', '<p class="eyebrow en">ELEPHANT · INCENSE BOX</p>')
rep('<p class="pre">밤하늘을 담은 박스형</p>', '<p class="pre">인도의 전통을 담은 박스형</p>')
rep("<h1>달문양 인센스 홀더</h1>", "<h1>코끼리문양 인센스 홀더</h1>")
rep('alt="박스형 달문양 인센스 홀더"', 'alt="박스형 코끼리문양 인센스 홀더"')
rep("<li><b>✦</b> 금색 달·해·별 문양</li>", "<li><b>✦</b> 금색 코끼리 문양</li>")

# ---- check point card 01 ----
rep('<div class="ic"><svg viewBox="0 0 48 48" fill="none" stroke="#b58b45" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round"><path d="M26 9a15 15 0 1 0 13 24A12 12 0 0 1 26 9z"/><path d="M37 5l1.4 4.1L42.5 10.5 38.4 11.9 37 16 35.6 11.9 31.5 10.5 35.6 9.1z" fill="#b58b45" stroke-width="1"/></svg></div>',
    '<div class="ic"><svg class="ico-el" viewBox="0 0 100 80" style="width:56px;height:45px;color:#b58b45"><use href="#eleph"/></svg></div>')
rep("<h3>신비로운 달문양</h3>\n      <p>고급스러운 금색으로 새긴<br>달·해·별 장식</p>",
    "<h3>전통 코끼리문양</h3>\n      <p>고급스러운 금색으로 새긴<br>인도 전통 코끼리 장식</p>")

# ---- point 01 ----
rep('<h2 class="h2">신비로운 달문양,<br>고급스러운 금색 각인</h2>',
    '<h2 class="h2">인도의 전통 코끼리문양,<br>고급스러운 금색 각인</h2>')
rep("<p class=\"body\">신비로운 달문양이 <b>고급스러운 금색</b>으로<br>각인되어 있습니다. 은은하게 빛나는 금빛 포인트가<br>공간에 차분한 분위기를 더해줍니다.</p>",
    "<p class=\"body\">인도의 전통스러운 코끼리문양이 <b>고급스러운 금색</b>으로<br>각인되어 있습니다. 은은하게 빛나는 금빛 포인트가<br>공간에 이국적인 분위기를 더해줍니다.</p>")
rep('alt="금색 달·해·별 문양 디테일"', 'alt="금색 코끼리 문양 디테일"')
rep('<figure class="dt"><div class="circ"><img src="assets/detail-sun.jpg" alt=""></div><span class="en">DETAIL · SUN</span><b>해 문양</b></figure>',
    '<figure class="dt"><div class="circ"><img src="assets/detail-elephant.jpg" alt=""></div><span class="en">DETAIL · ELEPHANT</span><b>코끼리 문양</b></figure>')
rep('<figure class="dt"><div class="circ"><img src="assets/detail-moon.jpg" alt=""></div><span class="en">DETAIL · MOON</span><b>달 문양</b></figure>',
    '<figure class="dt"><div class="circ"><img src="assets/detail-pattern.jpg" alt=""></div><span class="en">DETAIL · PATTERN</span><b>덮개 투각 문양</b></figure>')

# ---- size drawing: three elephants instead of moon motifs ----
s = re.sub(r'      <g fill="#c9a25b">\n        <path d="M180 140.*?</g>\n',
           '      <g fill="#c9a25b">\n'
           '        <use href="#eleph" x="176" y="143" width="44" height="35"/>\n'
           '        <use href="#eleph" x="303" y="147" width="44" height="35"/>\n'
           '        <use href="#eleph" x="430" y="143" width="44" height="35"/>\n'
           '      </g>\n', s, count=1, flags=re.S)
assert 'href="#eleph" x="176"' in s

# ---- spec / footer ----
rep("<tr><th>제품명</th><td>박스형 달문양 인센스 홀더</td></tr>", "<tr><th>제품명</th><td>박스형 코끼리문양 인센스 홀더</td></tr>")
rep('<svg viewBox="0 0 48 48" fill="#e6cd96"><path d="M26 6a18 18 0 1 0 16 28A14 14 0 0 1 26 6z"/></svg>\n  <span class="en">MOON &amp; SUN · INCENSE BOX</span>',
    '<svg class="ico-el" viewBox="0 0 100 80" style="width:44px;height:35px;color:#e6cd96"><use href="#eleph"/></svg>\n  <span class="en">ELEPHANT · INCENSE BOX</span>')
assert "달" not in re.sub(r"<style>.*?</style>", "", s, flags=re.S).replace("달라", "").replace("달리", ""), "moon copy left over"
(HERE / "template.html").write_text(s, encoding="utf-8")
print("template written")
