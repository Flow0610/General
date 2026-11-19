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
