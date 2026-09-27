# AI로 상품 콘텐츠를 만들고 클릭·전환을 높이는 법 — 이미지·영상·상세페이지·리스팅 SEO·개인화·리뷰·CRO (기준일 2026-09-27)

> **조사 방법·신뢰도 주의 (보고서 작성자 필독).** (1) 이번 세션에서는 WebFetch가 egress 프록시에 막혔다(draph.art, photoroom.com, etnews, mtn, daum, imweb, frontiersin, korea.kr, openai, aboutamazon 등 시도한 도메인 전부). 그래서 원문 페이지를 열지 못했고, **WebSearch 결과 요약(검색엔진이 만든 요약)과 링크에 의존**했다. 요약 속 문장이 여러 링크 중 정확히 어느 페이지에서 나왔는지 확인할 수 없는 경우에는 후보 링크를 모두 달았다. (2) 세션 전체 WebSearch 한도(200회)가 조사 도중 소진되었다. 그 결과 **Q4(리스팅 SEO), Q5(개인화·검색), Q6(리뷰), Q7(CRO)는 이번 세션 검색 결과가 거의 없다.** 해당 부분은 [PK] 항목과 Gaps의 "검증 필요 단서"로 채웠다.
> **태그:** [I]=독립 출처(규제기관·학술지·중립 언론), [P]=기업 보도자료 기반 언론 기사, [V]=벤더/플랫폼 자체 주장, [A]=제3자 블로그·가격비교 사이트(원문 미검증), [S]=설문(자기보고), [H]=제목/헤드라인만 확인(본문 미확인), [PK]=작성자 사전지식(2026-06 학습 기준, 이번 세션 재검증 못 함 → 사용 전 확인 필요).

---

## Q1. AI 상품 사진 — 배경 교체·연출컷·AI 모델/가상 피팅·팩샷: 도구, 비용, 품질 한계, 측정된 성과 (+ 한국 플랫폼·법규)

### Takeaway
AI 상품 사진의 확실한 효용은 실물 사진 1장을 누끼 딴 뒤 배경·연출·모델을 합성하는 방식으로 **촬영비와 제작 시간을 크게 줄이는 것**이다(벤더 사례: 제작비 −45%, 제작시간 약 −90%). 반면 "전환율 상승" 근거는 대부분 벤더 자료이거나 "연출컷 vs 단순 제품컷" 비교(Amazon 광고 CTR 최대 +40%)여서 "AI컷이 실사보다 낫다"는 증거로 쓰면 안 된다. 2026년 한국 셀러에게 가장 중요한 변화는 규제다. **네이버쇼핑은 2026-07-10부터 AI 생성·변형 이미지·영상의 표기를 의무화하고 건강·식품 등 일부 카테고리에서 AI 사용 자체를 금지**했다. 공정위는 2026-06-01부터 광고 속 AI 가상인물 표시를 의무화했다. 이 때문에 "썸네일은 실사, 보조컷·광고소재는 AI"가 기본 전략이 되었다.

### Cited Findings

**한국 도구**
- **드랩아트(Draph Art)**: ㈜드랩(2022년 창업, 대표 이주완)이 개발한 생성형 AI 상품사진 솔루션. 2023년 7월 정식 출시(GA). 가입하면 배경 제거는 무료이고, 나머지 기능은 5회 무료 이용 후 유료 — [나무위키](https://namu.wiki/w/%EB%93%9C%EB%9E%A9%EC%95%84%ED%8A%B8), [드랩 출시 보도](https://draph.ai/%EB%93%9C%EB%9E%A9-ai-%EC%83%81%ED%92%88-%EC%82%AC%EC%A7%84-%EC%83%9D%EC%84%B1-%EC%84%9C%EB%B9%84%EC%8A%A4-%EB%93%9C%EB%9E%A9%EC%95%84%ED%8A%B8-%EA%B3%B5%EA%B0%9C%EC%9A%A9-%EC%B6%9C/) [V]
- 드랩아트 요금제는 "제품 사진, AI 모델샷, 광고 영상, 상세페이지" 등 기능별 플랜이며 월간/연간 결제를 지원한다. 연간은 선결제 할인이고, 추가 충전("배터리팩")과 무료 체험이 있다. **구체적 원화 가격은 이번 세션에서 확인하지 못했다** — [드랩아트 요금제](https://draph.art/ko/pricing) [V]
- 드랩아트 기능: "원본 사진 한 장으로 배경, 소품, 조명, 그림자, 모델까지" 새로 연출하고, 누끼 작업 없이 제품을 다양한 공간에 합성한다 — [드랩아트 배경 생성](https://draph.art/overview/bg_generation), [드랩 블로그](https://draph.art/blog/aimodel/2024_ai_ad_success_90percent_time_reduction) [V]
- 드랩아트 자체 사례: ① AI 광고 모델로 주방 사용 장면을 연출해 **광고 클릭률 150% 상승**, ② 가구 브랜드가 **월 광고 제작 건수 3배, 제작 비용 45% 절감**. 블로그 URL 슬러그는 "90percent_time_reduction"(제작시간 약 90% 단축 주장) — [드랩 블로그 "2025 AI 광고 성공사례"](https://draph.art/blog/aimodel/2024_ai_ad_success_90percent_time_reduction) [V — 벤더 마케팅 주장, 비교 기준·표본 불명]
- 드랩아트는 쿠팡 상세페이지("사진 한 장으로 끝내는 쿠팡 상세페이지")와 스마트스토어 배너용 가이드를 운영한다 — [드랩 블로그(쿠팡)](https://draph.art/blog/insights/create-coupang-page-with-draphart), [드랩 블로그(스마트스토어 배너)](https://draph.art/blog/insights/ai_banner_creation_guide_for_smartstoresellers) [V/H]
- 도입 비교 자료(기능·가격·도입 사례 정리) — [임팩트플로우: 드랩아트](https://impactflow.kr/product/draph-art) [A/H]
- 기타 한국어 셀러용 이미지·등록 자동화 서비스(이름·포지셔닝만 확인): **키픽AI**("셀러 상품등록 자동화 | 상품명·키워드·속성·이미지 AI") — [kipic-ai.com](https://www.kipic-ai.com/) [V/H]; **셀러비서**("쿠팡 스마트스토어 상세페이지 AI 자동 생성") — [sellerbiseo.com](https://sellerbiseo.com/ko/) [V/H]; 쿠팡 썸네일용 AI 배경 제거 가이드 — [Tenorshare PixPretty](https://pixpretty.tenorshare.ai/ko/ai-generator/making-coupang-product-thumbnail.html), [ADai](https://adai.tw/ko/blog/coupang-product-image-ai) [A/H]

**글로벌 도구·가격** (모두 제3자 요약 기반 [A]. 벤더 가격 페이지 원문은 확인하지 못함)
- **Photoroom**: Pro는 연간 결제 시 약 $7.50/월, 월간 결제 시 약 $12.99–15. 연간 결제로 33% 절약. 일괄(batch) 편집(최대 500장), 템플릿 1,000+개, 월 약 1,000건 export. 팀 좌석은 최대 50석까지 좌석당 요금이 없고, 플랜 가격만큼의 "API/MCP 크레딧 지갑"이 포함된다고 요약됨. 리셀러·1인 사업자·소상공인 대상 — [Photoroom Pricing](https://www.photoroom.com/pricing), [Photoroom Help](https://help.photoroom.com/en/articles/6976012-what-are-photoroom-s-plans), [Pikes 2026](https://pikes.ai/blog/photoroom-pricing-2026), [eesel](https://www.eesel.ai/blog/photoroom-pricing), [API 가격](https://www.photoroom.com/api/pricing) [A] (월간가 $12.99 vs $15는 출처마다 다름)
- **Claid.ai**: 크레딧제. Essential $15/월(500크레딧), Pro $49/월(2,000크레딧, 영상 생성·커스텀 AI 모델 포함). 셀프서브 API는 $59/1,000크레딧부터. 무료 가입 시 웹 50 + API 50크레딧(카드 불필요). 크레딧 소모: 기본 보정 1, 배경 제거 2, AI 배경 생성 3, **5초 영상 35** — [Claid Pricing](https://claid.ai/pricing), [WizCommerce](https://wizcommerce.com/blog/claid-ai-pricing/), [Pikes 리뷰 2026](https://pikes.ai/blog/claid-ai-review-2026-best-ai-tool-for-product-photos-or-overrated), [Claid for business](https://claid.ai/business) [A/V]
- **Pebblely**: 월 $9–39. 크레딧이 아니라 "완성 이미지" 단위로 판매(월 30/200/500장, $9부터). 2026 리뷰 기준 무료체험·환불 없음. 원리는 "업로드한 제품 사진을 기반으로 배경을 만들고 그림자·반사를 추가"하는 방식 — [Pikes Pebblely 리뷰 2026](https://pikes.ai/blog/pebblely-review-2026), [WizCommerce](https://wizcommerce.com/blog/pebblely-pricing/), [Allo](https://www.withallo.com/blog/ai-product-photography-ecommerce) [A]
- **Pixelcut**: Pro $9.99/월. 배경 제거가 강하고 일괄 처리는 최대 100장. 일일 제한 무료 데모 — [Allo](https://www.withallo.com/blog/ai-product-photography-ecommerce), [Rewarx](https://www.rewarx.com/blogs/flair-ai-vs-pixelcut-pricing-comparison) [A]
- **Flair.ai**: 무료 플랜 5장, 유료 $10–55/월(생성 장수 기준). 캔버스형이라 아트디렉션이 들어간 연출컷에 적합 — [Rewarx](https://www.rewarx.com/blogs/flair-ai-vs-pixelcut-pricing-comparison), [tasarim.ai](https://tasarim.ai/en/compare/flair-ai-vs-pebblely-vs-booth-ai) [A]
- 용도 구분: Photoroom·Pixelcut 같은 **누끼 중심 툴은 리스팅용**, Flair 같은 캔버스 툴과 Presti 같은 에이전트형 툴은 **아트디렉션 연출컷·광고 영상용** — [Allo](https://www.withallo.com/blog/ai-product-photography-ecommerce) [A]
- **Botika**(AI 패션 모델): 가격 정보가 출처마다 충돌한다. "Lite $22/월 = 30크레딧", "Lite ~$33 ~ Advanced ~$40", "Starter ~$29/월"이 모두 보고됨. 경쟁사 Photta(100크레딧 $6.95)와 비교하면 재생성이 잦을 때 크레딧 소모가 부담이라는 지적 — [Botika Pricing](https://botika.com/pricing), [Photta](https://www.photta.app/pricing-and-reviews/botika), [Modelia](https://modelia.ai/blog/botika-pricing), [Rewarx](https://www.rewarx.com/blogs/botika-alternative-ai-fashion-models) [A — **가격 충돌**, 경쟁사 작성 자료 포함]
- **Google Nano Banana Pro(Gemini 3 Pro Image) API**: 2026년 8월 기준 공식 가격은 1K/2K 출력 $0.134/장, 4K $0.24/장(Standard). Batch API는 약 절반(2K 1,000장 = $67 vs 표준 $134). 제3자 재판매는 ~$0.05/장. Magic Hour 경유 시 1K/2K/4K 장당 100/150/200크레딧(플랜 $19/$39/$99). Shopify 앱 **Phora AI**는 2K 25장 $15(1회) — [AI Free API](https://www.aifreeapi.com/en/posts/nano-banana-pro-cost-per-image), [AI Free API(해상도별)](https://www.aifreeapi.com/en/posts/nano-banana-pro-pricing), [Magic Hour](https://magichour.ai/api/nano-banana-pro), [PiAPI(from $0.105)](https://piapi.ai/nano-banana-pro), [Rogue Marketing(2026-05)](https://the-rogue-marketing.github.io/google-nano-banana-imagen-4-image-generation-pricing-may-2026/), [Phora AI](https://apps.shopify.com/phora-ai), [PhotoAI Shopify 앱](https://apps.shopify.com/image-generator) [A]
- [PK] Nano Banana(Gemini 2.5 Flash Image)는 2025-08-26 Gemini 앱·API에 공개, Nano Banana Pro(Gemini 3 Pro Image)는 2025-11-20 공개 — [Google 블로그(2025-08)](https://blog.google/products/gemini/updated-image-editing-model/), [Google 블로그(Nano Banana Pro)](https://blog.google/technology/ai/nano-banana-pro/) [PK — URL·날짜 재검증 필요]
- [PK] ChatGPT(GPT-4o) 네이티브 이미지 생성은 2025-03-25 출시 — [OpenAI](https://openai.com/index/introducing-4o-image-generation/) [PK]
- **Amazon Ads 이미지 생성기**: 2023년 10월 베타 출시. 광고 콘솔에서 상품 선택 → Generate → 짧은 프롬프트로 수정 → 여러 버전 테스트 순서로 쓴다. 이후 화면비(aspect ratio) 기능이 추가됨 — [About Amazon](https://www.aboutamazon.com/news/innovation-at-amazon/amazon-ads-ai-powered-image-generator), [Amazon Ads 블로그](https://advertising.amazon.com/blog/ai-image-generation), [About Amazon(화면비 추가)](https://www.aboutamazon.com/news/innovation-at-amazon/amazon-ads-image-generator-adds-aspect-ratio-capability), [Search Engine Land](https://searchengineland.com/amazon-ai-image-generator-advertisers-434302) [V/P]

**측정된 성과 (신뢰도 표시)**
- Amazon: **라이프스타일 연출 광고의 CTR이 일반 제품 이미지 광고보다 "최대 40% 높다"**(예: 모바일 Sponsored Brands 광고에서 주방 조리대 위 토스터와 크루아상 연출) — [About Amazon](https://www.aboutamazon.com/news/innovation-at-amazon/amazon-ads-ai-powered-image-generator), [Benzinga 2023-10](https://www.benzinga.com/news/23/10/35445781/amazons-new-ai-powered-ad-imagery-boosts-click-through-rates-by-40) [V, 2023 자료. "연출 vs 단순컷" 비교이며 AI vs 실사 비교가 아님]
- 프랑스 마켓플레이스 Label Emmaus: 아마추어 배경을 AI 최적화 배경으로 바꾼 뒤 **전환율 패션 +56%, 홈 +34%** — [Fibr/Rewarx 등 CRO 사례 모음](https://www.rewarx.com/blogs/ab-testing-ecommerce-product-images), [Fibr](https://fibr.ai/conversion-rate-optimization/cro-case-studies) [A→V: 벤더(Photoroom 추정) 사례 재인용, 원문 미확인]
- "Photoroom 2024 리포트: AI 생성 상품 이미지가 의류·뷰티·홈 A/B 전환 테스트에서 **스튜디오 촬영 대비 3% 이내 성과**" — [검색결과 내 제3자 블로그들: BlendNow](https://www.blendnow.com/blog/do-better-product-photos-really-increase-sales), [PixelPanda](https://pixelpanda.ai/blog/2026/03/25/how-to-a-b-test-product-images-to-increase-conversion-rates-2/) [A→V: 원 리포트 미확인]
- "Shopify 조사: 전문가 품질 사진 상품의 전환율이 저품질 대비 평균 33% 높음" / "적절한 상품사진이 전환을 ~30% 올림" — [SellHound](https://www.sellhound.com/learn/conversion-rate-product-photos), [BlendNow](https://www.blendnow.com/blog/do-better-product-photos-really-increase-sales) [A: 원 조사 출처·연도 불명확 → 마케팅 인용 통계로 취급]
- Wayfair: Facebook/Instagram에서 라이프스타일 광고 이미지로 전환 21% 증가 — [Rewarx 47 tests](https://www.rewarx.com/blogs/ab-testing-ecommerce-product-images) [A: 오래된 Meta 사례로 추정, 연도 불명]
- 실무 블로그 주장: 50달러 이상이거나 생활 속 사용을 상상해야 하는 상품(가구·홈데코·의류·피트니스)은 라이프스타일 이미지가 20–30% 전환 우위. 스킨케어·보충제는 정면보다 살짝 위 3/4 각도가 12–18% 우위 — [Nightjar](https://nightjar.so/blog/how-to-ab-test-product-images-and-what-weve-learned), [adcreator.ai](https://adcreator.ai/blog/ab-testing-ai-product-photos-conversion-rate-2026) [A — 방법론 불명, 낮은 신뢰도]

**소비자 신뢰·AI 표기 연구**
- Frontiers in Computer Science(2026) "Beyond the label itself: how disclosed content shapes consumer responses to AI-generated product imagery in E-commerce": **실용재(utilitarian) 맥락에서는 AI 표기 라벨이 무표기 대비 지각된 진정성·미적 매력·사회적 실재감을 낮췄다. 쾌락재(hedonic) 맥락에서는 이 부정 효과가 검출되지 않았다.** 선행연구는 AI 표기를 인지 비용과 신뢰 이득을 동시에 가진 "양날의 검"으로 본다 — [Frontiers 2026](https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2026.1860932/full) [I, 동료심사. 표본 수·효과 크기는 원문 미확인]
- AI 광고는 효율·개인화를 높일 수 있지만 진정성·신뢰성 지각을 해칠 수 있다(AI vs 인간 제작 광고 비교 연구) — [Equilibrium 저널](https://economic-policy.pl/index.php/eq/article/view/4038?articlesBySimilarityPage=2), [Academia 사본](https://www.academia.edu/165561421/AI_generated_versus_human_created_advertising_Effects_on_consumer_trust_and_purchase_intent) [I/H]. 관련: [Manchester대 AI 광고 표기 연구](https://research.manchester.ac.uk/en/publications/transparent-technology-evaluating-the-impact-of-ai-generated-ad-d/) [H], [AI 마케팅 콘텐츠 신뢰 체계적 문헌고찰 2026](https://americanimpactreview.com/article/e2026024) [H]
- AI 상품사진 업체 블로그의 2025 설문: 쇼핑객 59%가 AI 이미지 사용 시 표기를 원하고 표기를 정직함의 신호로 해석했다. 약 60%는 AI 생성이라는 말을 듣고도 중립/긍정 반응. 신뢰 손상은 라벨이 아니라 **디테일 색상 오류, 부자연스러운 원단 표현, 비율 불일치 같은 정확성 실패**에서 온다는 주장 — [Shotova](https://shotova.com/blog/how-buyers-react-to-ai-product-photos) [V/S — 이해상충 벤더, 방법론 불명]

**한국 플랫폼·법규: AI 생성물 표시와 과장 금지 (Q1–Q3 공통 적용)**
- **네이버쇼핑(스마트스토어·네이버플러스 스토어), 2026-07-10 시행 "AI 생성물 사용 기준"**:
  - 표기 의무: 썸네일(대표이미지)이나 상세페이지에 AI로 제작·변형한 이미지·영상을 올리면 AI 활용 사실을 알려야 한다. 문구·아이콘 모두 허용. 썸네일은 이미지·영상 내부에, 상세페이지는 해당 콘텐츠 내부 또는 최대한 가까운 위치에 표기.
  - AI 사용 제한 카테고리(생명·신체·건강 직결): 의료기기, 건강기능식품, 유아식품, 신선식품(농·축·수산물), 의약외품, 위험 화학물질, 반려동물용 건강식품·간식·건강관리용품, 이미용 가전 → AI 활용 자체가 제한됨.
  - 금지 행위: 미표기 AI 이미지·영상, 의사·약사 등 전문가로 오인될 수 있는 가상인물, 유명인·실존인물을 모방한 AI 이미지, 실제 상품과 다른 색상·크기·구성 표현.
  - 제재: 네이버쇼핑 페이지 미노출 등 상품 조치와 "클린 프로그램" 적용. 정책 취지는 AI 금지가 아니라 오인 유발 AI의 제한.
  - 출처: [MTN 2026-07-24 "쇼핑은 의무·블로그는 자율"](https://news.mtn.co.kr/news-detail/2026072417015682342), [다음/언론 "지나친 과장상품은 AI 표시해도 금지"](https://v.daum.net/v/yeaHDbb0Zi), [세하컴퍼니 정리](https://sehacompany.onch3.co.kr/bbs_view.php?num=13&vnum=16026) [P/A — 네이버 공지 원문 미확인]
- 네이버 블로그는 AI 생성물 표기가 **자율**이라 쇼핑과 기준이 이중이라는 비판이 있다 — [MTN 2026-07-24](https://news.mtn.co.kr/news-detail/2026072417015682342) [H]
- **카카오(쇼핑)**: 판매자 대상 "AI 생성물 관련 표시·광고 안내"를 공지했다. AI 생성·변형 콘텐츠가 실제 상품과 현저히 다르거나 품질·효능·크기·구성을 오인하게 하면 허위·과장 광고나 소비자 기만에 해당할 수 있다는 내용 — [KPI뉴스 "이커머스업계 'AI 양면전략'"](https://www.kpinews.kr/newsView/1065598689138238), [고구마팜](https://gogumafarm.kr/ai-%EA%B8%B0%EB%B3%B8%EB%B2%95-%EB%A7%88%EC%BC%80%ED%84%B0%EB%8F%84-%EC%A0%81%EC%9A%A9-%EB%8C%80%EC%83%81%EC%9D%BC%EA%B9%8C-ai-%EC%83%9D%EC%84%B1-%EC%BD%98%ED%85%90%EC%B8%A0-%ED%91%9C%EA%B8%B0/) [P/A — 공지일 미확인]
- **쿠팡**: 판매자 대상 "생성 AI 콘텐트 활용 가이드" 공지. ① 실제 사람·제품·공간처럼 보이는 AI 생성물은 소비자가 쉽게 알아보도록 명확히 표시, ② 실제 상품과 다른 형태를 AI로 만들어 대표 이미지로 쓰지 말 것, ③ 위법·부당 표시광고로 판단되면 **책임은 판매자에게 귀속** — [오픈애즈 "2026 AI 저작권 가이드"](https://www.openads.co.kr/content/contentDetail?contsId=19836), [레이메이커(쿠팡 상세페이지 검수)](https://www.laymaker.com/coupang-detail-page) [A — **쿠팡 WING 공지 원문·공지일 미확인**. 두 번째 검색에서는 원 공지를 찾지 못함]
- **오늘의집**: 파트너센터에 "[정책] 생성형 AI 사용에 대한 가이드", "[정책] 오늘의집 생성형 AI 사용 가이드 안내" 문서가 있다(내용 미확인) — [오늘의집 파트너센터 1](https://www.partnerbucketplace.com/hc/ko/articles/55423122367897--%EC%A0%95%EC%B1%85-%EC%83%9D%EC%84%B1%ED%98%95-AI-%EC%82%AC%EC%9A%A9%EC%97%90-%EB%8C%80%ED%95%9C-%EA%B0%80%EC%9D%B4%EB%93%9C), [파트너센터 2](https://www.partnerbucketplace.com/hc/ko/articles/55424188349593--%EC%A0%95%EC%B1%85-%EC%98%A4%EB%8A%98%EC%9D%98%EC%A7%91-%EC%83%9D%EC%84%B1%ED%98%95-AI-%EC%82%AC%EC%9A%A9-%EA%B0%80%EC%9D%B4%EB%93%9C-%EC%95%88%EB%82%B4) [H]
- **공정위 「추천·보증 등에 관한 표시·광고 심사지침」 개정, 2026-06-01 시행**:
  - 추천·보증 주체에 "가상인물"(인공지능 등 기반으로 실제와 구분하기 어려운 가상의 인물)을 추가하고, AI 가상인물 광고에는 "가상인물"임을 명확히 표시하도록 했다.
  - 표시 위치: 블로그·카페 등 문자 매체는 제목이나 첫 부분(예: "AI를 기반으로 생성된 가상인물이 포함된 게시물입니다", "가상인물 포함"). 유튜브·인스타그램 등 영상 매체는 가상인물이 등장하는 동안 인접 위치.
  - **가상인물임을 밝혀도 가짜 경험담(사용후기)을 늘어놓으면 불법 광고.**
  - 출처: [서울신문 2026-05-31](https://www.seoul.co.kr/news/economy/2026/05/31/20260531500033), [세종 뉴스레터](https://www.shinkim.com/kor/media/newsletter/3230), [김·장](https://www.kimchang.com/ko/insights/detail.kc?sch_section=4&idx=34590), [법률신문](https://www.lawtimes.co.kr/news/articleView.html?idxno=219837), [네이트 2026-09-01](https://m.news.nate.com/view/20260901n32916) [I/P]
- **AI기본법(인공지능 발전과 신뢰 기반 조성 등에 관한 기본법), 2026-01-22 시행**:
  - 생성형 AI 결과물 워터마크(가시·가청 표시 또는 메타데이터 등 기계판독 방식) 표시 의무가 있다. 서비스 밖으로 다운로드·공유될 때 적용된다.
  - 과태료는 최소 1년 계도기간.
  - 다수 법률 해설은 **제31조 표시 의무가 "AI사업자"(도구 제공자)에게 부과되고, AI 도구로 만든 결과물을 광고·상품 설명에 쓰는 광고주·쇼핑몰 판매자는 원칙적으로 직접 의무 대상이 아니라고** 본다.
  - 반대로 "AI로 제품·서비스를 제공하는 모든 사업자"에게 적용된다는 요약도 있어 **해석이 충돌**한다.
  - 출처: [정책브리핑](https://www.korea.kr/news/policyNewsView.do?newsId=148958380), [지아이코퍼레이션(광고주는 대상 아님)](https://www.gi-corp.co.kr/post/ai-content-labeling-ads), [고구마팜](https://gogumafarm.kr/ai-%EA%B8%B0%EB%B3%B8%EB%B2%95-%EB%A7%88%EC%BC%80%ED%84%B0%EB%8F%84-%EC%A0%81%EC%9A%A9-%EB%8C%80%EC%83%81%EC%9D%BC%EA%B9%8C-ai-%EC%83%9D%EC%84%B1-%EC%BD%98%ED%85%90%EC%B8%A0-%ED%91%9C%EA%B8%B0/), [아임웹 블로그](https://imweb.me/blog?idx=486), [법률사무소 번화](https://bh-law.kr/ko/news/column/ai-content-labeling-obligation-guide), [헬프미](https://www.help-me.kr/blog/article/korea-ai-act-2026-compliance-guide/), [국민일보](https://www.kmib.co.kr/article/view.asp?arcid=1768984300), [디센트로](https://decentlaw.io/en/news/670) [I/A — **적용범위 해석 충돌**]
- 2026 하반기 달라지는 것: "AI가상인물 광고표시 의무화…쇼핑몰 사용후기 조작방지" — [이데일리 2026-06-30](https://edaily.co.kr/News/Read?mediaCodeNo=257&newsId=03981926645486968), [다음](https://v.daum.net/v/20260630100311911) [H — 후기 조작방지 조치의 근거 법령·내용 미확인]
- 규제 공백 보도: "'AI 착용샷 보고 사세요' 'AI 번역본 팝니다'…이런 사업자, 규제할 방법이 없다" — [네이트 2026-08-04](https://m.news.nate.com/view/20260804n22813) [H]

### Inferences
- **실무 순서(1인 셀러 기준, 추론):**
  1. 스마트폰으로 균일한 조명에서 실제 색이 나오게 원본을 촬영한다.
  2. 무료 누끼(드랩아트 무료 배경 제거 / Photoroom·Pixelcut)로 배경을 딴다.
  3. 보조컷·광고소재부터 AI 연출컷을 만든다(드랩아트 5회 무료, Claid 50크레딧 무료, Flair 5장 무료로 품질 테스트).
  4. 네이버 등록 시 AI 표기(문구/아이콘)를 이미지 안에 넣는다.
  5. 쇼핑검색광고·쿠팡 광고로 "실사 vs AI 연출" CTR을 비교한 뒤 대표이미지 교체 여부를 정한다.
- **썸네일은 실사를 유지하는 편이 안전하다.** 네이버는 AI로 "변형"한 썸네일에도 이미지 내부 표기를 요구한다. Frontiers 연구상 실용재에서는 AI 라벨 자체가 진정성 지각을 떨어뜨릴 수 있어 CTR 손실 가능성이 있다. 쾌락재(패션·인테리어 무드컷)는 라벨 부담이 상대적으로 작을 수 있다.
- **카테고리 체크가 먼저다.** 건강기능식품·신선식품·유아식품·의료기기·의약외품·반려동물 건강식품/간식·이미용 가전 셀러는 네이버에서 AI 이미지·영상을 사실상 쓰지 않는 것으로 계획해야 한다(실사 촬영 예산 유지).
- **충실도(fidelity) 원칙:** text-to-image(Midjourney 등) 대신 실제 제품 사진을 입력으로 하는 합성/편집형(드랩아트, Photoroom, Nano Banana 편집)을 쓴다. 라벨 문구·로고·색상·크기감·구성품을 실물과 대조하는 QA를 거친다. 신뢰 손상은 라벨보다 정확성 실패에서 온다.
- **AI 모델·가상 피팅:** 광고(SNS·블로그 포함)에 쓰면 공정위 지침에 따라 "가상인물" 표시가 필요하다. AI 모델이 "써보니 좋았다"는 식으로 체험을 말하게 하면 위법이다. 의사·약사 연출이나 연예인 닮은꼴은 네이버에서 금지된다.
- **비용 감각:** 1인 셀러는 월 $10–15급(Photoroom Pro, Pixelcut, Pebblely, Claid Essential) 또는 한국어 UI의 드랩아트로 충분하다. SKU가 수백~수천 개인 중소 브랜드는 Nano Banana Pro API(2K 약 $0.13/장, Batch 약 $0.067/장)나 Claid API로 일괄 처리하는 편이 단가상 유리하다(개발 인력 필요).
- 드랩아트의 "CTR 150%↑", Label Emmaus의 "+56%" 같은 수치는 비교군·기간이 불명확한 벤더 사례다. 보고서에서는 "가능성의 예시"로만 쓰고 기대치로 제시하지 않는 것이 적절하다.

### Gaps
- 드랩아트·브이캣 등 **한국 도구의 2026년 원화 요금표**: 가격 페이지가 WebFetch 차단으로 열리지 않았고 검색 요약에도 금액이 없었다.
- 드랩아트 외 한국 AI 상품사진 서비스(예: 젠시, 스냅플, 포토룸 한국어 지원 현황 등): 검색 한도 소진으로 조사하지 못했다.
- Adobe Firefly(상업적 안전성·면책 정책·가격), Midjourney(V7·비디오, 무료 없음), ChatGPT 이미지 최신 모델·요금, Pixelcut/Flair/Botika의 한국어 지원·원화 결제 여부: 미검증.
- 네이버 기준에서 **단순 누끼(배경 제거)·보정도 "AI 변형"으로 표기 대상인지**: 네이버 공지 원문 미확인.
- AI기본법 표시의무 위반 과태료 상한: 최대 3,000만 원으로 알려져 있으나(사전지식) 이번 세션에서 검증하지 못함. 계도기간 종료 시점도 확인 필요.
- 쿠팡 "생성 AI 콘텐트 활용 가이드"의 원문, 공지일, 대표이미지 규정(흰 배경 등)과의 관계: 미확인.
- AI 상품사진이 실사 대비 전환에 미치는 **독립적(비벤더) 필드 실험**은 찾지 못했다. Frontiers 연구도 설문 실험 기반으로 보인다(원문 미확인).
- 11번가·G마켓/옥션·무신사·29CM·에이블리·지그재그·컬리의 AI 이미지 정책: 미조사.

---

## Q2. AI 상품 영상·숏폼 — 브이캣, Veo, Sora, Runway, Kling, 아바타(HeyGen/Creatify), CapCut: 활용법과 영상의 전환 효과 근거

### Takeaway
한국 셀러에게 가장 실용적인 경로는 **"상세페이지 URL → 자동 영상/배너"형(브이캣, Creatify)**과 **"실제 상품 사진 → image-to-video"형(Veo 3.1 via Flow/Gemini, Kling, Runway)** 두 가지다. OpenAI Sora는 2026-04-26에 앱이 종료되고 API도 2026-09-24에 제거되어 **더 이상 선택지가 아니다.** "영상이 전환을 높인다"는 근거는 대부분 설문(Wyzowl)·벤더·플랫폼 자료이고, 독립적 인과 근거는 이번 조사에서 확인하지 못했다. 영상에도 Q1의 AI 표기(네이버)와 가상인물 표시(공정위) 규칙이 똑같이 적용된다.

### Cited Findings

**한국 도구**
- **브이캣(VCAT.AI)**: 상품 URL을 넣으면 마케팅 영상과 배너 이미지를 약 1분 만에 자동 제작한다. AI가 상품페이지에서 이미지와 상품정보를 분류하고, 베스트 컷과 상품 설명을 편집해 자동 완성한다 — [브이캣](https://vcat.ai/), [NHN커머스(고도몰) 앱스토어](https://apps.nhn-commerce.com/apps/499) [V]
- 브이캣 배너 자동제작: 상세페이지 주소 입력 후 수 초 내에 제품명·할인율 등을 넣은 이미지를 여러 장 일괄 제작한다. 쇼핑몰 배너와 구글·인스타그램·네이버·카카오용 이미지를 한 번에 만든다 — [한국면세뉴스](https://www.kdfnews.com/news/articleView.html?idxno=112296), [다음(ChatGPT 붐 시기 보도)](https://v.daum.net/v/03AmrhD73X?f=p) [P, 출시 시점은 2023년 초로 추정·미확인]
- 브이캣 템플릿: 카테고리별로 "상세페이지 전용 영상", "상품·할인·리뷰 강조형 광고" 등 — [브이캣](https://vcat.ai/) [V]
- 브이캣 요금: 월간/연간 구독. 무료로도 사용할 수 있지만 **다운로드는 Starter 플랜 이상**. 금액은 미확인 — [임팩트플로우: 브이캣](https://impactflow.kr/product/vcat), [브이캣 헬프센터 "무료로 사용할 수 있나요?"](https://vcat.ai/help/ko/articles/7901571-%EB%B8%8C%EC%9D%B4%EC%BA%A3%EC%9D%80-%EB%AC%B4%EB%A3%8C%EB%A1%9C-%EC%82%AC%EC%9A%A9%ED%95%A0-%EC%88%98-%EC%9E%88%EB%82%98%EC%9A%94), [테크뷰](https://www.techview.best/software/291) [A/V]
- 브이캣 블로그 "네이버 숏클립으로 어떻게 매출 6배를 올릴 수 있었을까요?" — [브이캣 블로그](https://vcat.ai/blog/insight/navershortclip/) [V/H — 벤더 사례, 조건 미확인]
- 네이버 쇼핑라이브 "숏클립" 거래액 2배 증가(2023-05 보도) — [네이트 2023-05-12](https://news.nate.com/view/20230512n13314) [P, **2023년 자료**]
- 샵라이브(Shoplive, 한국 비디오커머스 SaaS)의 "AI Clip 생성" 기능 문서 — [Shoplive Docs](https://docs.shoplive.cloud/docs/creating-ai-clips) [V/H]
- "쇼핑몰 상세페이지가 마케팅 영상으로 변신, AI 숏폼 시대 시작" — [모노프로 AI 뉴스](https://monopro.kr/AINEWS/?bmode=view&idx=171983233) [H]; 2026 네이버 쇼핑라이브 전략 — [아이보스](https://www.i-boss.co.kr/ab-6141-71418) [H]
- 네이버 7/10 기준의 영상 적용: AI 생성 영상 미표기, 전문가 오인 가상인물, 실존인물 모방, 색상·크기·구성 왜곡이 금지된다 — [세하컴퍼니](https://sehacompany.onch3.co.kr/bbs_view.php?num=13&vnum=16026) [A]

**글로벌 영상 생성·아바타 도구**
- **OpenAI Sora — 종료:** Sora 2는 2025-09-30 공개 — [OpenAI "Sora 2 is here"](https://openai.com/index/sora-2/) [V]. 2025년에는 한국에서도 한시적으로 직접 다운로드가 열렸다 — [GlobalGPT](https://www.glbgpt.com/hub/openai-sora-2-availability/), [Medium](https://medium.com/@CherryZhouTech/openai-expands-global-access-to-sora-2-in-strategic-time-limited-rollout-334a5676c7a6) [A]. OpenAI는 2026-03-24 종료를 발표했고, **앱·웹은 2026-04-26 종료, Sora 2 API는 2026-09-24 제거** 예정이었다 — [TechCrunch 2026-03-24](https://techcrunch.com/2026/03/24/openais-sora-was-the-creepiest-app-on-your-phone-now-its-shutting-down/), [The Decoder](https://the-decoder.com/openai-sets-two-stage-sora-shutdown-with-app-closing-april-2026-and-api-following-in-september/), [OpenAI Help](https://help.openai.com/en/articles/20001152-what-to-know-about-the-sora-discontinuation) [I/V]. WSJ 보도를 인용한 2차 자료에 따르면 운영비는 하루 약 100만 달러, 인앱 매출은 210만 달러 수준이었다 — [MindStudio](https://www.mindstudio.ai/blog/openai-shutting-down-sora-what-happened), [TechJournal](https://techjournal.org/what-happened-to-sora-openai-shutdown) [A, WSJ 원문 미확인]
- **Google Flow / Veo 3.1:**
  - Flow는 Veo 3.1·Nano Banana·"Gemini Omni"를 묶은 크리에이티브 스튜디오이며, 무료로 매일 50크레딧을 준다.
  - 요금: AI Plus $4.99/월, **AI Pro $19.99/월(월 1,000 Flow 크레딧 ≈ Veo 3.1 Lite 약 100편 / Fast 약 50편 / Quality 약 10편)**, AI Ultra $99.99–199.99/월.
  - AI Pro는 150개국 이상에서 제공된다(한국 원화 가격·Flow 한국 제공 여부는 미확인).
  - 출처: [Magic Hour: Google Flow](https://magichour.ai/blog/google-flow), [CostGoat Flow(2026-09)](https://costgoat.com/pricing/google-flow), [CostGoat Veo](https://costgoat.com/pricing/google-veo), [Google AI 구독](https://gemini.google/subscriptions/), [DIYAI](https://diyai.io/ai-tools/video-generation/google-veo-pricing/) [A/V]
- **Kling 3.0**: Standard $10 / Pro $37 / Premier $92 / Ultra $180(월간). 연간 결제 시 앞의 세 플랜은 34% 할인. 다른 출처는 Standard를 $6.99/월로 제시하고, Pro 연간 환산 $25.99로 Runway Pro($28)보다 싸며 네이티브 4K를 지원한다고 함 — [AI Tool Analysis](https://aitoolanalysis.com/kling-ai-pricing/), [CloudZero](https://www.cloudzero.com/blog/kling-ai-pricing/), [Rangy](https://rangy.ai/blog/veo-vs-kling-vs-runway/), [TechSifted](https://techsifted.com/comparisons/kling-ai-vs-runway-2026/) [A — **가격 충돌**]
- **Runway(Gen-4.5)**: 연간 결제 시 $12/월부터. Standard 625 / Pro 2,250 / Max 9,500 월 크레딧. **2026년 6월 Unlimited 플랜을 폐지하고 Max($95/월, 9,500크레딧 ≈ 플래그십 출력 약 790초, 1개월 이월)로 대체** — [Somake](https://www.somake.ai/blog/runway-ai-pricing) [A]
- **Creatify**(URL→영상 광고, AI 아바타): Shopify·Amazon 등 상품 URL을 넣으면 스크립트·아바타·상품 데이터로 숏폼 광고를 만든다. Starter $39/월(100크레딧, 워터마크 제거, AI 배우 300명), Pro $99/월(300크레딧, AI 배우 1,500명+커스텀 아바타 3, 경쟁사 광고 트래커). 영상 1편은 2–20크레딧이고 미사용 크레딧은 2개월마다 소멸 — [Creatify Pricing](https://creatify.ai/pricing), [Creatify URL-to-video](https://creatify.ai/features/url-to-video), [Fast.io 리뷰 2026](https://fast.io/resources/creatify-ai-review-2026/), [Superscale](https://superscale.ai/alternatives/creatify/pricing) [V/A]
- Claid.ai도 5초 상품 영상 생성을 제공한다(35크레딧/클립) — [WizCommerce](https://wizcommerce.com/blog/claid-ai-pricing/) [A]
- API 단가 비교 자료(Veo 3.1, Kling 3.0, Seedance, Runway; 2026-07) — [BuildMVPFast](https://www.buildmvpfast.com/api-costs/ai-video) [A/H]

**"상품 영상이 전환을 높이는가" 근거**
- Wyzowl 2026: 응답자 85%가 영상을 보고 제품·서비스 구매를 설득당한 적이 있다. 63%는 제품을 알아볼 때 짧은 영상을 가장 선호한다. 89%는 영상 품질이 브랜드 신뢰에 영향을 준다고 답했다. 마케터 82%가 영상 ROI가 좋다고 답했다(전년 93%에서 하락) — [Wyzowl Video Marketing Statistics 2026](https://wyzowl.com/video-marketing-statistics/) [S — 영상 제작사가 수행한 자기보고 설문, 인과 근거 아님]
- "영상을 본 쇼핑객은 장바구니 담기 가능성이 144% 높다", "88%가 영상이 구매에 영향" — [NetSolutions](https://www.netsolutions.com/insights/how-product-videos-are-important-for-your-e-commerce-business/) [A — **원출처·연도 불명의 반복 인용 통계, 사용 비권장**]
- 학술: 상품 소개 영상은 지각된 진단성(perceived diagnosticity)과 심상(mental imagery)을 거쳐 구매의도에 영향을 주며, 상품 평점이 조절 변수다 — [PMC8891234](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8891234/) [I/H — 제목 기반, 수치 미확인]
- 반대 방향 근거: 라이브커머스의 "과도한 설득"이 반품 증가와 연관된다는 실증 연구(POMS, 2025) — [Feng et al. 2025](https://journals.sagepub.com/doi/10.1177/10591478231224949) [I/H — 제목 기반]

### Inferences
- **상세페이지용 AI 영상은 "실물 사진 기반 image-to-video 5–10초 클립"이 적정선이다**(질감·사용 장면·360° 느낌 등). 텍스트만으로 만든 영상(text-to-video)은 형태·로고·구성이 달라질 위험이 크다. 네이버의 "색상·크기·구성 왜곡 금지"를 위반하기 쉽다.
- **시작 경로(추론):**
  - 자사몰(카페24·고도몰): 브이캣 무료로 템플릿을 확인한 뒤 Starter 이상 구독해 다운로드하고, 상세페이지 상단 GIF/MP4와 숏클립·릴스 광고에 재사용한다.
  - 글로벌/크로스보더: Creatify URL-to-video로 아바타 광고를 A/B 테스트한다.
  - 고품질 연출: Google AI Pro($19.99)로 Flow에서 Veo 3.1 Fast를 쓴다(월 약 50편).
- **아바타·AI 인물 영상은 공정위 "가상인물" 표시 대상이다.** AI 인물이 사용 후기를 말하는 광고는 표시해도 위법이다. 아바타는 "제품 설명자" 역할로 한정한다.
- Sora 종료 사례는 **특정 모델에 워크플로를 고정하지 말아야 한다**는 교훈이다. 템플릿·프롬프트·원본 소스는 도구 중립적으로 보관해야 한다.
- 영상 효과 수치는 설문·벤더 자료뿐이므로, 셀러는 네이버 숏클립 조회→유입, 상세페이지 영상 유무의 체류시간·전환을 직접 비교해야 한다(Q7 참고).

### Gaps
- HeyGen(제품 아바타·가격), CapCut(커머스 기능·AI 상품 영상, 한국 제공 여부), Runway·Kling의 원화 결제·한국어 지원: 검색 한도 소진으로 미조사.
- 브이캣 원화 가격, 운영사, 출시일, 2025–26 신기능(AI 상세페이지 등): 미확인.
- 네이버 숏클립·쇼핑라이브의 2025–26 AI 편집/자동생성 기능, 쿠팡의 상품 영상 등록 정책: 미조사.
- "상품 영상 → 전환율" 독립 실증(플랫폼 A/B, 학술 자연실험)의 수치: 찾지 못함. 인용 가능한 수치는 설문뿐.
- "Gemini Omni" 모델의 정체·출시일: 제3자 요약에만 등장하고 미확인.

---

## Q3. AI로 상세페이지 기획·카피·디자인 — 전용 도구(카페24 등), LLM 카피 워크플로, 과장·허위표시 Do/Don't

### Takeaway
2025–26년 한국 자사몰 솔루션은 **"상품 이미지만 넣으면 상세페이지 자동 생성 + SEO/AI 검색용 구조화 데이터 자동 적용"** 쪽으로 발전했다(카페24 PRO "데코", 2025-12-31). 마켓 셀러용으로는 셀러비서·레이메이커·키픽AI 같은 한국어 자동 생성 서비스가 나왔다. 가장 큰 리스크는 **AI가 만든 과장 문구·이미지가 표시광고법과 플랫폼 기준(네이버·카카오·쿠팡)을 위반하는 것**이다. 쿠팡은 책임이 판매자에게 있다고 명시했다.

### Cited Findings
- **카페24 PRO "데코(Deco)" 상세페이지 테마**(2025-12-31 발표):
  - 상품 이미지 등록만으로 SEO가 적용된 상세페이지를 자동 제작한다.
  - 타이틀·디스크립션·저자·키워드 등을 검색엔진과 AI가 인식하기 쉬운 "프로덕트 스키마"로 자동 구조화한다.
  - 사용자 사례: 주얼리 브랜드 "미코페"가 "과거 하루 몇 개 등록도 부담 → 3시간에 10개 이상 제작"했다고 말함.
  - 출처: [네이트(2025-12-30)](https://m.news.nate.com/view/20251230n27644), [네이트(2026-01-09) "사진만 있으면 3분 완성"](https://m.news.nate.com/view/20260109n20992) [P — 카페24 보도자료 기반, 사용자 인용은 선별 사례]
- 카페24 "커머스 AX": "쇼핑몰 운영부터 AI 쇼핑까지" 확장(2026-09-10 보도) — [전자신문](https://www.etnews.com/20260910000398) [H — 본문 미확인]
- 카페24의 이전 AI 기능: 에디봇 AI 썸네일 자동 크롭(2022-10) — [ZDNet Korea](https://zdnet.co.kr/view/?no=20221006085626), [더밸류뉴스](https://www.thevaluenews.co.kr/news/172048). AI 상세페이지 제작(CMTS 2023) — [블로터](https://www.bloter.net/news/articleView.html?idxno=603584). 상세페이지 제작 도구 안내 — [카페24](https://www.cafe24.com/commerce/manage/productdetail.html), [카페24 스토리 "AI로 고객을 사로잡는 상세페이지 작성하기"](https://store.cafe24.com/us/story/1896) [P/V, **2022–23 자료 포함**]
- 마켓 셀러용 한국어 AI 상세페이지·등록 도구(포지셔닝만 확인, 가격 미확인): 셀러비서(쿠팡·스마트스토어 상세페이지 AI 자동 생성) — [셀러비서](https://sellerbiseo.com/ko/). 레이메이커(쿠팡 상세페이지 AI 제작·등록 검수) — [레이메이커](https://www.laymaker.com/coupang-detail-page). 키픽AI(상품명·키워드·속성·이미지) — [키픽AI](https://www.kipic-ai.com/) [V/H]
- 드랩아트: 사진 한 장으로 쿠팡 상세페이지 제작 가이드. 요금제에 "상세페이지" 기능 플랜 포함 — [드랩 블로그](https://draph.art/blog/insights/create-coupang-page-with-draphart), [드랩 요금제](https://draph.art/ko/pricing) [V]
- 섹션별 이미지 생성 프롬프트 가이드("스마트스토어 상세페이지 이미지, 섹션별로 뽑는 AI 프롬프트 가이드") — [allmyuniverse](https://allmyuniverse.com/image-prompt-guide-smartstore-product-detail-page-v1/) [A/H]
- Shopify 생태계의 AI 설명 생성 앱 예시: Content Generator, SmartCopy AI — [Shopify 앱](https://apps.shopify.com/content-generator?locale=ko), [SmartCopy AI](https://apps.shopify.com/smartcopyai?locale=ko) [V/H]
- [PK] Shopify Magic(관리자 내 AI 상품 설명 생성 등)은 Shopify 플랜에 무료 포함 — [Shopify Magic](https://www.shopify.com/magic) [PK]
- **Do/Don't의 규범 근거:** 네이버 7/10 기준(미표기 AI, 전문가 오인 가상인물, 실존인물 모방, 색상·크기·구성 왜곡 금지, 건강·식품 등 AI 금지 카테고리), 카카오 안내(실제와 현저히 다르거나 품질·효능·크기·구성 오인 → 허위·과장/기만), 쿠팡 가이드(판매자 책임). 상세 내용과 출처는 Q1의 "한국 플랫폼·법규" 참조 — [MTN](https://news.mtn.co.kr/news-detail/2026072417015682342), [KPI뉴스](https://www.kpinews.kr/newsView/1065598689138238), [오픈애즈](https://www.openads.co.kr/content/contentDetail?contsId=19836) [P/A]
- "지나친 과장상품은 AI 표시해도 금지" — 즉 **AI 표기가 과장 광고의 면책 사유가 아님** — [다음/언론](https://v.daum.net/v/yeaHDbb0Zi) [H/P]

### Inferences
- **한국형 상세페이지 LLM 워크플로(추론·실무 관행, 출처 미검증):**
  1. 입력 자료를 모은다: 실제 스펙표, 성분/소재, 인증서, 시험성적서, 고객 리뷰 원문, 경쟁상품 상세 3–5개(구조 참고용).
  2. LLM에 섹션 구조를 지정한다: 후킹 헤드라인 → 고객 문제·공감 → 해결/USP 3개 → 근거(성분·스펙·인증·수치) → 사용법/사용 장면 → 비교표 → 실제 리뷰 발췌 → FAQ → 배송·교환·A/S → CTA.
  3. **"모든 효능·수치 주장 옆에 근거 자료를 표기하라, 근거 없는 최상급(최고·유일·1위·100%) 금지"를 프롬프트 규칙으로 명시**한다.
  4. 섹션별 이미지 프롬프트를 뽑아 드랩아트/Nano Banana로 제작한다(실물 사진 입력).
  5. AI 표기를 삽입한다(네이버).
  6. 사람이 사실을 검수한 뒤 모바일 가독성(짧은 문단·큰 글씨)을 확인한다.
- **건강기능식품·화장품·식품은 AI 카피가 가장 위험하다.** LLM은 질병 예방·치료 뉘앙스의 표현을 쉽게 만든다. 네이버는 이 카테고리 다수에서 AI 이미지 자체를 금지한다. 카피도 식약처 기준으로 검수가 필수다(Gaps 참조).
- 자사몰은 카페24 PRO 데코처럼 **구조화 데이터(Product schema)가 자동 적용되는 테마**를 쓰는 편이 구글·AI 검색 노출 면에서 유리할 가능성이 있다. 다만 효과 수치는 제시되지 않았다.
- AI 표기는 "정직 신호"가 될 수도 있지만(벤더 설문), 실용재에서는 매력도를 떨어뜨릴 수 있다(Frontiers 2026). 그래서 **AI 이미지는 무드·사용장면 섹션에 쓰고, 스펙·구성·사이즈 섹션은 실사로** 구성하는 분리 전략이 합리적이다.

### Gaps
- 미리캔버스 AI, Canva Magic Studio(한국어), 망고보드, Figma AI의 상세페이지 기능·가격: 검색 한도 소진으로 미조사.
- 아임웹·식스샵·고도몰(NHN커머스)·샵바이의 AI 상세페이지/상품설명 기능과 출시일: 미조사.
- 11번가·G마켓/옥션·쿠팡(WING)·네이버 자체의 판매자용 AI 상세페이지/상품등록 도우미: 미조사.
- 식약처(건기식·화장품·식품 부당광고 기준)와 표시광고법상 AI 카피 관련 최신 가이드·제재 사례: 미조사.
- 셀러비서·레이메이커·키픽AI의 가격·출시일·사용자 규모: 미확인.
- AI 상세페이지 도입의 전환율 효과에 대한 독립 수치: 찾지 못함(카페24 사례는 제작시간 절감만).

---

## Q4. AI로 리스팅 SEO — 네이버쇼핑 상품명, 쿠팡 검색, Amazon 생성형 AI 리스팅, Google Merchant Center: 플랫폼 공식 입장

### Takeaway
**이번 세션에서는 검색 한도 소진으로 플랫폼 공식 가이드(네이버 상품명 SEO, 쿠팡 검색 랭킹, Amazon 제목 정책, Google Merchant Center의 AI 생성 제목 속성)를 직접 확인하지 못했다.** 확인된 것은 한국 셀러용 "상품명·키워드·속성 AI" 도구(키픽AI 등)가 있다는 점과, 카페24가 AI 검색 대응용 구조화 데이터를 자동 적용한다는 점 정도다. 아래 Gaps에 검증이 필요한 단서를 정리했다.

### Cited Findings
- 키픽AI: "셀러 상품등록 자동화 | 상품명·키워드·속성·이미지 AI" — [키픽AI](https://www.kipic-ai.com/) [V/H]
- 카페24 PRO 데코: 상품 정보를 검색엔진과 **AI가 인식하기 쉬운 "프로덕트 스키마"로 자동 구조화**해 "검색 노출 경쟁력"을 높인다는 주장 — [네이트(2025-12-30)](https://m.news.nate.com/view/20251230n27644) [P]
- 쿠팡 썸네일 승인 전략(광고대행사 자료) — [OSC](https://oscsnm.com/coupang-thumbnail-design/) [A/H]
- [PK] Amazon은 2023년 9월 판매자용 생성형 AI 리스팅 도구를 발표했다. 짧은 설명이나 키워드만 넣으면 제목·불릿·상품설명 초안을 생성한다 — [About Amazon](https://www.aboutamazon.com/news/small-business/amazon-sellers-generative-ai-tool) [PK — 이후 2024–26 확장(URL 기반 리스팅 생성, 에이전트형 Seller Assistant 등)은 미검증]

### Inferences
- AI 도구로 상품명을 만들 때는 **"키워드를 많이 넣기"보다 플랫폼 규칙 준수 + 속성·태그 정확 입력**을 우선해야 한다. 네이버·쿠팡은 모두 상품명 어뷰징을 제재 대상으로 다루는 것으로 알려져 있으나 이번 세션 미검증이다. AI는 대량 생성 속도 때문에 어뷰징 패턴을 SKU 전체로 복제하는 위험이 있다.
- 자사몰에서는 LLM 기반 AI 검색(ChatGPT·Gemini·네이버 AI 브리핑 등)의 노출을 위해 구조화 데이터(Product schema), 정확한 속성, FAQ형 텍스트가 중요해지는 추세로 보인다(카페24의 포지셔닝 근거). 효과 수치는 없다.

### Gaps (검증 필요 단서 — 모두 이번 세션 미확인)
- **네이버쇼핑:** 검색 랭킹은 "적합도·인기도·신뢰도" 3요소로 공개되어 있다고 알려져 있다. 상품명 가이드로는 대략 공백 포함 50자 이내 권장, 브랜드→제품명→모델/속성 순서, 중복·무관 키워드·특수문자·판매조건 문구(무료배송·할인 등) 사용 시 신뢰도 감점("상품명 SEO")이 알려져 있다. 쇼핑파트너센터/스마트스토어센터 원문과 2025–26 개정 여부를 확인해야 한다. 네이버플러스 스토어 앱의 AI 개인화 추천이 노출에 미치는 영향도 미조사.
- **쿠팡:** 노출상품명(브랜드+제품명+주요 속성) 규칙, 쿠팡의 상품명 수정 권한, 공개된 랭킹 요소(판매실적·사용자 선호·상품정보 충실도·검색 정확도 등으로 알려짐), 아이템위너 구조에서의 이미지·상품명 통합 규칙: 윙 헬프센터 원문 미확인.
- **Amazon:** 2025년 1월 제목 정책 강화(200자 이하, 동일 단어 2회 초과 금지, 장식용 특수문자·홍보 문구 금지로 알려짐)와 2024–26 생성형 AI 리스팅 도구 확장: 미검증.
- **Google Merchant Center:** 생성형 AI로 만든 제목·설명은 `structured_title` / `structured_description` 속성에 `digital_source_type = trained_algorithmic_media`를 표시해 제출하는 방식이 안내되어 있다고 알려져 있다. Product Studio(AI 이미지 편집)의 한국 제공 여부와 함께 미확인.
- 한국 키워드 도구(아이템스카우트, 판다랭크, 셀러라이프 등)의 AI 상품명 추천 기능·가격: 미조사.
- AI 작성 상품명이 CTR·검색순위에 미친 **측정 결과**: 미조사.

---

## Q5. 자사몰 온사이트 개인화·검색·AI 쇼핑 어시스턴트 — 그루비·빅인·레코벨·카페24 앱, Shopify Search & Discovery·Nosto·Klevu·Algolia·Dynamic Yield·Rebuy: 측정된 전환/AOV 효과

### Takeaway
**검색 한도 소진으로 이 질문은 거의 조사하지 못했다.** 인용 가능한 것은 McKinsey(2021, 개인화 매출 10–15% 상승)와 Amazon Rufus(벤더 발표) 같은 사전지식 [PK] 항목뿐이다. 한국 솔루션(그루비·빅인·레코벨·크리마 등)의 기능·가격·성과는 전부 Gaps로 남는다.

### Cited Findings
- 카페24는 2026년 9월 "쇼핑몰 운영부터 AI 쇼핑까지" 커머스 AX를 확장한다고 보도됨 — [전자신문 2026-09-10](https://www.etnews.com/20260910000398) [H]
- [PK] McKinsey(2021-11) "The value of getting personalization right—or wrong—is multiplying": 소비자 71%가 개인화를 기대하고 76%는 개인화가 없으면 불만을 느낀다. **개인화는 대개 매출 10–15% 상승을 만들며(기업별 5–25%)**, 빠르게 성장하는 기업은 느린 기업보다 개인화에서 40% 더 많은 매출을 얻는다 — [McKinsey](https://www.mckinsey.com/capabilities/growth-marketing-and-sales/our-insights/the-value-of-getting-personalization-right-or-wrong-is-multiplying) [PK. 컨설팅사 자료이며 대기업 중심, **2021년 자료**]
- [PK] Amazon은 2025년 3분기 실적(2025-10-30)에서 AI 쇼핑 어시스턴트 Rufus에 대해 "올해 2억5천만 명 사용, 쇼핑 중 Rufus를 쓴 고객은 구매 완료 가능성이 60% 높음, 연환산 100억 달러 이상 증분 매출 전망"이라고 밝힌 것으로 기억함 — [Amazon IR](https://ir.aboutamazon.com/quarterly-results/default.aspx) [PK/V — **자기선택 편향**(구매의도 높은 고객이 Rufus를 씀)으로 인과 효과 아님, 수치 재검증 필요]
- [PK] Shopify Search & Discovery 앱(필터·동의어·상품 추천·부스트)은 무료 — [Shopify App Store](https://apps.shopify.com/search-and-discovery) [PK]

### Inferences
- 트래픽이 적은 1인·소규모 자사몰은 추천 엔진이 학습할 데이터가 부족하다. 그래서 유료 개인화 SaaS보다 **검색 개선(동의어·오타·필터)과 규칙 기반 추천(함께 산 상품·최근 본 상품)**의 비용 대비 효과가 클 가능성이 높다(추론).
- 벤더가 제시하는 "전환 +X%" 수치는 대개 도입 전후 비교나 추천 클릭자와 비클릭자 비교라서 자기선택 편향이 있다. 도입 시 **홀드아웃(A/B) 조건으로 계약·평가**할 것을 권고한다(추론).

### Gaps (전부 미조사 — 우선 재조사 대상)
- 그루비(Groobee), 빅인(Bigin), 레코벨(Recobell), 크리마(크리마 핏 등), 카페24 앱스토어 AI 추천/검색 앱의 2026 기능·가격(원화)·도입 사례·측정 성과.
- Nosto, Klevu, Algolia, Dynamic Yield, Rebuy의 가격대·한국 쇼핑몰(카페24/아임웹) 연동 가능 여부·케이스 스터디 수치.
- 온사이트 AI 쇼핑 어시스턴트(자사몰용 챗봇형 검색, 네이버플러스 스토어 AI 쇼핑 가이드/에이전트, Shopify의 AI 기능 등)의 2025–26 출시 현황과 성과.
- 사이트 검색 이용자의 전환율 배수(흔히 인용되는 "검색 이용자 전환 2배" 류)와 Baymard의 검색 UX 벤치마크 원문 수치.

---

## Q6. 리뷰·소셜 프루프와 AI — 리뷰 수집 자동화(크리마리뷰·브이리뷰·알파리뷰), AI 리뷰 요약, AI 답글, UGC, 법적 한계

### Takeaway
이번 세션에서 확인한 것은 **법적 한계 쪽**뿐이다.
- 공정위 지침상(2026-06-01 시행) AI 가상인물이 가짜 경험담을 말하면 표시 여부와 관계없이 위법이다.
- 2026 하반기에 쇼핑몰 사용후기 조작방지 조치가 예고되었다.
- 공정위는 쿠팡 임직원 리뷰·검색순위 조작 사건을 제재했다(2024 의결).
- 미국은 FTC가 AI 생성 가짜 리뷰를 명시적으로 금지한다(2024 규칙, [PK]).

리뷰 솔루션별 기능·성과는 Gaps다.

### Cited Findings
- 공정위 추천·보증 심사지침 개정(2026-06-01): 가상인물임을 밝혀도 가짜 경험담은 명백한 불법 광고 — [네이트 2026-09-01](https://m.news.nate.com/view/20260901n32916), [서울신문](https://www.seoul.co.kr/news/economy/2026/05/31/20260531500033) [P/I]
- "쇼핑몰 사용후기 조작방지" — 2026 하반기부터 달라지는 제도로 보도 — [이데일리 2026-06-30](https://edaily.co.kr/News/Read?mediaCodeNo=257&newsId=03981926645486968) [H — 세부 미확인]
- 공정위 2024-08-05 의결 제2024-284호 [쿠팡(주) 및 씨피엘비] — [케이스노트](https://casenote.kr/%EA%B3%B5%EC%A0%95%EA%B1%B0%EB%9E%98%EC%9C%84%EC%9B%90%ED%9A%8C/%EC%9D%98%EA%B2%B02024-284) [I/H — 결정 존재만 확인, 본문 미확인]
- [PK] 미국 FTC "가짜 리뷰·추천 금지 최종 규칙"(2024-08-14 발표, 2024-10 시행): 존재하지 않는 사람이나 **AI가 생성한 가짜 리뷰**, 리뷰 매수(긍정·부정 조건부 인센티브), 미공개 내부자 리뷰, 리뷰 억압 등을 금지하고 위반당 민사벌금을 부과한다 — [FTC 보도자료](https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials) [PK — 크로스보더(미국) 판매자 해당]
- [PK] Amazon은 2023년 8월 상품 상세페이지에 **AI 생성 리뷰 하이라이트(리뷰 요약)**를 도입했다 — [About Amazon](https://www.aboutamazon.com/news/amazon-ai/amazon-improves-customer-reviews-with-generative-ai) [PK]

### Inferences
- **허용되는 AI 활용(추론):** 구매확정 후 리뷰 요청 자동화, 포토/영상 리뷰 인센티브(조건 없이 제공하고 공개), 리뷰 요약·키워드 하이라이트(실제 리뷰 기반), AI 답글 초안(사람 검수), 리뷰에서 USP·불만을 추출해 상세페이지 FAQ에 반영.
- **금지 영역:** AI로 리뷰 본문 생성·대량 작성, 긍정 리뷰 조건부 보상, 임직원·지인 리뷰 미표시, 부정 리뷰 숨김, AI 가상인물 사용 후기.
- 리뷰 요약은 플랫폼(네이버·쿠팡)이 자체 제공하는 추세로 보인다(미검증). 따라서 자사몰에서만 리뷰 솔루션의 AI 요약이 차별 요소가 된다.

### Gaps (미조사 — 재조사 필요)
- 크리마리뷰, 브이리뷰(AI 리뷰 요약·영상 리뷰), 알파리뷰의 2026 기능·가격(원화)·카페24/아임웹 연동, 도입 효과 수치(리뷰 작성률·전환율).
- 네이버 스마트스토어 "AI 리뷰 요약"과 쿠팡 리뷰 요약 기능의 출시 시점과 셀러 영향.
- 한국 "사용후기 조작방지" 제도의 근거(전자상거래법 개정/고시?), 시행일, 판매자 의무.
- 공정위 쿠팡 사건(의결 2024-284)의 세부: 사전지식으로는 검색순위 알고리즘 조작으로 PB 상품을 우대하고 임직원을 동원해 PB 리뷰를 작성한 건이며, 과징금은 약 1,628억 원으로 기억한다. 이번 세션에서 검증하지 못했으므로 인용 전 공정위 보도자료로 확인해야 한다.
- 리뷰 수·평점이 전환에 미치는 독립 연구 수치(예: Spiegel Research Center 등): 미조사.

---

## Q7. AI 기반 A/B 테스트·CRO — AI 실험, AI 히트맵·세션 분석

### Takeaway
**이번 세션 근거는 상품 이미지 A/B 테스트 관련 실무 블로그뿐이며 신뢰도가 낮다.** 도구 측면에서는 사전지식상 Google Optimize 종료(2023-09) 이후 무료 대안이 줄었고, Microsoft Clarity(무료, AI 세션 요약)가 소규모 셀러의 기본 선택지다 [PK]. 마켓플레이스 셀러는 광고 소재 CTR 테스트가 사실상 유일한 A/B 수단이다.

### Cited Findings
- 상품 이미지 A/B 테스트 방법론·사례 모음(실무 블로그): [Nightjar](https://nightjar.so/blog/how-to-ab-test-product-images-and-what-weve-learned), [adcreator.ai "12개 AI 상품사진 A/B 테스트"](https://adcreator.ai/blog/ab-testing-ai-product-photos-conversion-rate-2026), [Rewarx "47 Tests"](https://www.rewarx.com/blogs/ab-testing-ecommerce-product-images), [PixelPanda](https://pixelpanda.ai/blog/2026/03/25/how-to-a-b-test-product-images-to-increase-conversion-rates-2/), [Fibr CRO 사례 2026](https://fibr.ai/conversion-rate-optimization/cro-case-studies) [A — 벤더 블로그, 방법론 불명]
- 이 블로그들의 주장: 라이프스타일 이미지가 고가·생활맥락 상품에서 20–30% 우위, 3/4 각도가 12–18% 우위(Q1 참조) [A, 낮은 신뢰도]
- Amazon Ads 이미지 생성기는 "여러 버전을 만들어 테스트해 성과를 최적화"하도록 설계됨 — [About Amazon](https://www.aboutamazon.com/news/innovation-at-amazon/amazon-ads-ai-powered-image-generator) [V]
- [PK] Google Optimize는 2023-09-30 종료 — [Google Optimize 도움말](https://support.google.com/optimize/answer/12979939) [PK]
- [PK] Microsoft Clarity는 무료 히트맵·세션 녹화 도구이며, Copilot 기반 AI 세션 요약·인사이트를 제공한다 — [Microsoft Clarity](https://clarity.microsoft.com/) [PK]

### Inferences
- **1인 셀러 CRO 루틴(추론):**
  1. 자사몰에 Clarity(무료)를 설치하고, AI 요약으로 모바일 이탈 구간(상세페이지 스크롤 깊이)을 찾는다.
  2. 이탈이 몰리는 섹션을 AI로 재작성·재디자인한다.
  3. 마켓(네이버·쿠팡)은 대표이미지·상품명 A/B를 직접 할 수 없는 경우가 많으므로, 쇼핑검색광고·쿠팡 광고에서 소재별 CTR을 1–2주 비교해 승자를 대표이미지로 채택한다.
  4. 변경은 한 번에 하나만 하고 기간과 결과를 기록한다.
- 트래픽이 적은 셀러는 전환율 A/B가 통계적 유의성을 갖기 어렵다. 그래서 CTR(표본이 큼)을 선행지표로 쓰는 것이 현실적이다(추론).
- AI는 "테스트할 변형을 싸게 많이 만드는 것"에서 가장 큰 가치를 낸다(이미지·카피 변형). 반면 "AI가 알아서 최적화"한다는 주장은 검증이 어렵다.

### Gaps
- 한국 도구(뷰저블 Beusable, 빅인·그루비 A/B 기능), 글로벌 AI 실험 도구(VWO, Optimizely, AB Tasty, Shopify 네이티브 테스트 기능 등)의 2026 기능·가격: 미조사.
- Amazon "Manage Your Experiments"(브랜드 등록 판매자용 제목·메인이미지·A+ A/B 테스트)의 현재 조건과 Amazon이 제시하는 효과 수치: 미검증.
- Hotjar·Clarity AI 기능의 출시일과 무료 한도: 미검증.
- AI 기반 CRO의 독립 측정 사례: 찾지 못함.

---

## Q8. 정량 벤치마크 모음 (출처·날짜·독립/벤더 구분)

### Takeaway
이번 세션에서 확보한 수치는 대부분 **벤더 사례나 설문, 또는 "연출컷 vs 단순컷" 비교**다. "AI 콘텐츠가 전환을 X% 올린다"는 독립적 인과 근거는 확인하지 못했다. 보고서에서는 **비용·시간 절감(비교적 확실)**과 **전환 효과(불확실, 직접 테스트 필요)**를 분리해 제시해야 한다.

### Cited Findings
| 지표 | 수치 | 출처·날짜 | 신뢰도 |
|---|---|---|---|
| 라이프스타일 연출 광고 CTR (vs 일반 제품컷) | 최대 +40% | Amazon Ads, 2023-10 — [About Amazon](https://www.aboutamazon.com/news/innovation-at-amazon/amazon-ads-ai-powered-image-generator), [Benzinga](https://www.benzinga.com/news/23/10/35445781/amazons-new-ai-powered-ad-imagery-boosts-click-through-rates-by-40) | [V] 2023, AI vs 실사 비교 아님 |
| AI 모델 연출 광고 CTR | +150% | 드랩아트 블로그(2025 사례) — [Draph](https://draph.art/blog/aimodel/2024_ai_ad_success_90percent_time_reduction) | [V] 비교군 불명 |
| 광고 제작 건수 / 제작비 | 3배 / −45% | 드랩아트(가구 브랜드) — [Draph](https://draph.art/blog/aimodel/2024_ai_ad_success_90percent_time_reduction) | [V] |
| 제작시간 | 약 −90% | 드랩아트 블로그 URL 슬러그 — [Draph](https://draph.art/blog/aimodel/2024_ai_ad_success_90percent_time_reduction) | [V/H] |
| 상세페이지 제작 속도 | 하루 몇 개 → 3시간 10개+ | 카페24 PRO 데코 사용자 인용, 2026-01 — [네이트](https://m.news.nate.com/view/20260109n20992) | [P] 선별 사례 |
| AI 배경 전환 (Label Emmaus) | 패션 +56%, 홈 +34% | 제3자 재인용 — [Rewarx](https://www.rewarx.com/blogs/ab-testing-ecommerce-product-images) | [A→V] 원문 미확인 |
| AI 이미지 vs 스튜디오 사진 전환 | 3% 이내 차이 | "Photoroom 2024 리포트" 재인용 — [BlendNow](https://www.blendnow.com/blog/do-better-product-photos-really-increase-sales) | [A→V] 원문 미확인 |
| 전문 사진 vs 저품질 전환 | +33% | "Shopify 조사" 재인용 — [SellHound](https://www.sellhound.com/learn/conversion-rate-product-photos) | [A] 원조사 불명 |
| 라이프스타일 광고 전환 (Wayfair) | +21% | 재인용 — [Rewarx](https://www.rewarx.com/blogs/ab-testing-ecommerce-product-images) | [A] 오래된 자료 추정 |
| 영상 보고 구매 설득 경험 | 85% | Wyzowl 2026 — [Wyzowl](https://wyzowl.com/video-marketing-statistics/) | [S] |
| 영상 ROI 긍정 마케터 | 82% (전년 93%) | Wyzowl 2026 — [Wyzowl](https://wyzowl.com/video-marketing-statistics/) | [S] |
| 영상 시청 후 장바구니 | +144% | 재인용 — [NetSolutions](https://www.netsolutions.com/insights/how-product-videos-are-important-for-your-e-commerce-business/) | [A] 출처 불명, 사용 비권장 |
| 숏클립 거래액 | 2배 | 네이버 쇼핑라이브, 2023-05 — [네이트](https://news.nate.com/view/20230512n13314) | [P] 2023 |
| 숏클립 활용 매출 | 6배 | 브이캣 블로그 — [VCAT](https://vcat.ai/blog/insight/navershortclip/) | [V/H] |
| AI 이미지 표기 원하는 쇼핑객 | 59% | Shotova 설문, 2025 — [Shotova](https://shotova.com/blog/how-buyers-react-to-ai-product-photos) | [V/S] |
| AI 라벨 효과 (실용재) | 진정성·미적 매력·사회적 실재감 하락, 쾌락재는 유의하지 않음 | Frontiers in Computer Science, 2026 — [Frontiers](https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2026.1860932/full) | [I] 수치 미확인 |
| 개인화 매출 효과 | 10–15% (5–25%) | McKinsey, 2021-11 — [McKinsey](https://www.mckinsey.com/capabilities/growth-marketing-and-sales/our-insights/the-value-of-getting-personalization-right-or-wrong-is-multiplying) | [PK] 컨설팅, 2021 |
| AI 쇼핑 어시스턴트 이용자 구매완료 가능성 | +60% | Amazon Rufus, 2025-10 실적 — [Amazon IR](https://ir.aboutamazon.com/quarterly-results/default.aspx) | [PK/V] 자기선택 편향 |
| 생성 단가 (이미지) | Nano Banana Pro 2K $0.134, 4K $0.24, Batch 약 50% | 2026-08 — [AI Free API](https://www.aifreeapi.com/en/posts/nano-banana-pro-cost-per-image) | [A] |
| 생성 단가 (영상) | Google AI Pro $19.99 = 1,000크레딧 ≈ Veo 3.1 Fast 약 50편 | 2026-09 — [CostGoat](https://costgoat.com/pricing/google-flow) | [A] |

### Inferences
- 수치의 방향성(연출·라이프스타일 이미지가 단순컷보다 CTR이 높고, 영상이 구매 판단을 돕는다)은 여러 출처에서 일관된다. 크기는 출처마다 다르고 대부분 이해상충이 있다. 보고서에서는 "범위·방향"만 제시하고 셀러별 자체 테스트를 권고하는 것이 적절하다.
- 가장 방어 가능한 주장은 **"AI가 콘텐츠 제작 단가·시간을 크게 낮춰 더 많은 변형을 테스트할 수 있게 한다"**이다. 전환 상승은 그 테스트의 결과로 나오는 것이지 AI 사용 자체의 효과가 아니다.

### Gaps
- Baymard Institute(상품 이미지·사이트 검색 UX), Salesforce Shopping Index(AI·에이전트 영향 매출), Adobe(생성형 AI 유입 트래픽 전환), Spiegel(리뷰 효과) 등의 원 수치: 검색 한도 소진으로 미확보.
- 한국 플랫폼(네이버·쿠팡·카페24)이 공개한 AI 기능의 전환 효과 공식 수치: 미확보.
- 상품 영상 → 전환의 독립 실험 수치: 미확보.
