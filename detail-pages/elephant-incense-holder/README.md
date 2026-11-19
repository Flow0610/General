# 박스형 코끼리문양 인센스 홀더 — 쿠팡 상세페이지

`../moon-incense-holder`(달문양)와 같은 레이아웃에 인도 전통 테마(딥 그린 + 금색 만다라)를 적용한 버전입니다.
기존 상세 이미지(`src/original-detail.jpg`)의 문구와 고해상도 제품 사진(`src/original-product.jpg`)을 사용했습니다.

## 업로드용 결과물 (`output/`, 가로 780px JPG)

| 파일 | 내용 |
|---|---|
| `00_full.jpg` | 전체 1장 (780×10070) |
| `01_hero-checkpoint.jpg` | 메인 비주얼 + CHECK POINT |
| `02_point1-elephant-pattern.jpg` | POINT 01 금색 코끼리문양 + 디테일 |
| `03_point2-cover-howto.jpg` | POINT 02 덮개 구조 + 사용 방법 3단계 |
| `04_point3-storage.jpg` | POINT 03 하단 스틱 수납 |
| `05_size-info.jpg` | 사이즈 도면 + 제품 정보표 |
| `06_notice.jpg` | 구매 전 안내 (수작업 특성 · 유격 발생 가능 · 사용 주의) |

## 구성
- `index.html` — 빌드된 페이지 (폰트 내장)
- `src/derive_template.py` — 달문양 템플릿에서 코끼리 버전 문구·아이콘·테마를 바꿔 `src/template.html` 생성
- `src/build.py` — 만다라 배경 SVG 삽입 + 폰트 내장 / `src/render.js` — 렌더링 / `src/export.py` — 분할 저장
- `assets/` — 메인컷·디테일컷은 고해상도 제품 사진에서 제작, 덮개·수납 사진은 원본 상세페이지 사진(달문양 버전과 동일 컷)

## 다시 만들기
```bash
python3 src/derive_template.py && python3 src/build.py && node src/render.js 1 && python3 src/export.py
```
레이아웃을 바꿀 때는 달문양 버전의 `src/template.html`을 고친 뒤 위 명령을 실행하면 두 페이지가 함께 맞춰집니다.
