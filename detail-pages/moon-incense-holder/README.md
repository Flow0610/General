# 박스형 달문양 인센스 홀더 — 쿠팡 상세페이지

기존 상세 이미지(`src/original-detail.jpg`)의 텍스트·사진을 정보로만 활용해 새 레이아웃으로 재구성한 쿠팡용 상세페이지입니다.

## 업로드용 결과물 (`output/`, 가로 780px JPG)

| 파일 | 내용 |
|---|---|
| `00_full.jpg` | 전체 1장 (780×9940) |
| `01_hero-checkpoint.jpg` | 메인 비주얼 + CHECK POINT |
| `02_point1-moon-pattern.jpg` | POINT 01 금색 달문양 + 디테일 |
| `03_point2-cover-howto.jpg` | POINT 02 덮개 구조 + 사용 방법 3단계 |
| `04_point3-storage.jpg` | POINT 03 하단 스틱 수납 |
| `05_size-info.jpg` | 사이즈 도면 + 제품 정보표 |
| `06_notice.jpg` | 구매 전 안내 (수작업 특성 · 유격 발생 가능 · 사용 주의) |

쿠팡에는 분할 이미지(01~06)를 순서대로 올리는 것을 권장합니다. 한 장으로 올릴 때는 `00_full.jpg`를 사용하세요.

## 최상단 안내 배너 — 구매 전 확인하세요 (`output/top-notice/`)

쿠팡이 전달한 판매자로켓 안내 배너 가이드(`src/coupang-guide/`)에 맞춰 만든, 상세페이지 **맨 위**에 넣는 배너입니다.

| 파일 | 용도 |
|---|---|
| `top-notice_1000.jpg` | 쿠팡 가이드 규격(가로 1000px) — 상세 이미지 첫 장으로 업로드 |
| `top-notice_780.jpg` | 같은 배너를 다른 이미지와 같은 780px로 맞춘 버전 |
| `preview_full-page.jpg` | 배너를 기존 상세페이지 위에 붙인 미리보기(업로드용 아님) |

- 가이드 그대로: 고정 타이틀 이미지(PSD의 판매자용 2p 버전, 쿠팡 로고 없음), Noto Sans CJK KR 30px, 자간 -35, 행간 44, 글머리 점, 테두리, 하단 여백 65px/30px
- 가이드 권장 사항 반영: 반품 원인이 되는 내용을 구체적으로 적고, 관련 사진(금색 문양, 덮개·본체 이음 부분)을 함께 넣음
- 다시 만들기: `python3 src/build_top_notice.py` (문구는 `src/top-notice.html`에서 수정)

## 구성
- `index.html` — 빌드된 페이지 (폰트 내장). 브라우저에서 바로 열 수 있습니다.
- `src/template.html` — 편집용 원본. 문구 수정은 이 파일에서 합니다.
- `src/build.py` — 별 배경 SVG 삽입 + 사용 글자만 담은 Google Fonts(Noto Serif KR / Noto Sans KR / Cormorant Garamond) 내장.
- `src/render.js` — Playwright로 780px 전체 렌더링.
- `src/export.py` — 섹션별 JPG 분할 저장.
- `assets/` — 원본에서 잘라낸 제품 사진 (Real-ESRGAN 4배 업스케일, 메인컷 배경 제거, 사진 위 글자 제거).
- `src/asset-prep/` — 위 사진 가공에 쓴 스크립트 (참고용).

## 다시 만들기
```bash
python3 src/build.py && node src/render.js 1 && python3 src/export.py
```
