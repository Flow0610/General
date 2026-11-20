# 다르샨 그린 컬렉션 인센스 스틱 6종 — 쿠팡·네이버 상세페이지

기존 상세페이지(`src/originals/old-detail-page.jpg`)의 내용만 활용해 새 레이아웃으로 만든 페이지입니다.
제품 사진은 새로 촬영한 원본(`photo-box-raw.jpg`, `photo-packs-raw.jpg`)을 보정해서 사용했습니다.

## 업로드용 결과물 (`output/`)

| 폴더 | 용도 | 가로 |
|---|---|---|
| `coupang_780/` | 쿠팡 상세 이미지 | 780px |
| `naver_860/` | 네이버 스마트스토어 상세 이미지 | 860px (장당 세로 2,500px 이하) |
| `retouched_photos/` | 보정한 제품 사진 원본 | — |

각 플랫폼 폴더: `00_full.jpg`(전체 1장) + 분할 7장(01~07, 순서대로 업로드)

| 분할 | 내용 |
|---|---|
| 01_hero | 메인 비주얼 + 핵심 수치(6종 · 20×6 · 120개입) |
| 02_6scents-inside | 박스 안 6가지 향 (팩 사진 + 범례) |
| 03_scent-guide | 향별 카드 6개 (팩 일러스트 · 설명 · 해시태그) |
| 04_mood-howto | 기분별 추천 + 사용 방법 3단계 |
| 05_gift-package | 선물 패키지 (박스 · 디테일) |
| 06_recommend-info | 추천 대상 + 제품 정보 |
| 07_notice | 구매 전 안내 · 사용 시 주의사항 |

`retouched_photos/`: `box_retouched.jpg`(보정 박스), `box_cutout.png`(누끼), `box_square_1000.jpg`(흰 배경 1000×1000),
`packs_retouched.jpg`(보정 6팩), `before_after.jpg`(보정 전후 비교)

## 사진 보정 내용
- 배경 조명 평탄화(플랫필드): 왼쪽은 밝고 오른쪽은 어둡던 조명 차이와 노란 색 틀어짐을 함께 보정
- 박스 4개 모서리 기준 원근·기울기 보정, 대비·채도·선명도 소폭 보정
- 박스 누끼(걸이 구멍은 투명 유지), 6팩 사진에서 향별 일러스트 크롭

## 다시 만들기
```bash
python3 src/build.py && python3 src/export.py
```
문구 수정은 `src/template.html`, 향 정보(이름·설명·태그·색)는 `src/build.py`의 `SCENTS`에서 합니다.
