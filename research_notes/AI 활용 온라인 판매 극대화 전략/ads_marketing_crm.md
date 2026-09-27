# AI 활용 광고·마케팅·CRM — 온라인 셀러용 리서치 노트 (기준일 2026-09-27)

> **조사 한계 (보고서 작성자 필독).** 이 세션에서는 WebFetch가 모든 외부 도메인에서 네트워크 egress proxy에 막혔다(시도한 도메인: ppc.live, byline.network, inside.ampm.co.kr, campaignasia.com, navercorp.com, blog.google, facebook.com, airbridge.io, support.google.com, s21.q4cdn.com, haus.io, kakaocorp.com, ads.tiktok.com). 세션 공유 WebSearch 한도(200회)도 조사 도중 소진되었다(본 연구자는 약 40회 사용). 따라서 **아래 수치는 모두 검색엔진 결과 요약에서 가져왔고, 원문을 열어 문맥을 확인하지 못했다.** 링크는 검색 결과가 반환한 URL이다. 인플루언서 AI 툴, CRM 툴(Klaviyo·Braze·Attentive·빅인·채널톡·스티비·카페24 앱), 라이브커머스 AI 호스트, SNS 오가닉 활용 사례, SMB 대상 독립 설문은 해당 검색을 하기 전에 한도가 소진되어 대부분 Gaps로 남았다.
>
> **출처 등급 표기:** [VENDOR]=플랫폼·툴사 자체 주장 / [3P]=대행사·툴사·블로그(이해관계가 있거나 방법론 불명) / [IND]=플랫폼과 독립된 측정(단, Haus·Optmyzr도 측정·툴 판매사임) / [ACAD]=학술 논문·워킹페이퍼 / [PRESS]=언론 보도 / [UNVERIFIED]=원출처 미확인·요약 과정의 왜곡 가능성

## 1. 플랫폼 AI 광고 상품(Meta·Google·TikTok·네이버·쿠팡·카카오): 소상공인 활용법, 보고된 성과, 함정

### Takeaway
6개 플랫폼 모두 "상품·예산·목표만 넣으면 AI가 타깃·소재·입찰·지면을 운영"하는 캠페인을 기본값으로 밀고 있다. 해당 캠페인은 Advantage+ Sales, Meta의 2026-06 칸 end-to-end 크리에이티브, PMax·AI Max, GMV Max, ADVoost 쇼핑·오디언스·AI 브리핑 광고, 쿠팡 AI 스마트·매출최적화, 카카오모먼트AI다. 플랫폼 주장 성과는 전환·ROAS 기준 +14~32%다. 반면 독립 증분 측정(Haus 640건)과 실무자 보고는 "단기 성과와 플랫폼 귀속 지표는 좋지만, 장기 증분과 상품 단위 통제력은 약하다"는 쪽이다. 소상공인은 자동화를 기본으로 쓰되 가드레일을 쳐야 한다: 브랜드 제외, 예산 상한, 주력 상품용 수동 캠페인 병행, 홀드아웃 테스트.

### Cited Findings

**상태 요약표 (확인된 범위만; 공란·"미확인"은 Gaps 참조)**

| 상품 | 출시/상태 | 한국 이용 | 별도 이용료 | 출처 |
|---|---|---|---|---|
| Meta Advantage+ Sales 캠페인 | 2025년 Advantage+ Shopping에서 명칭 변경. 2026년에는 구 Shopping 형식 생성 불가. 2026-02 수동/Advantage+ 생성 흐름 통합 [3P] | Meta 광고 자체는 한국 이용 가능. 기능별 한국어 지원은 미확인 | 소스에 언급 없음(매체비) | [topgrowthmarketing](https://topgrowthmarketing.com/advantage-plus-shopping-campaigns/) |
| Meta end-to-end AI 크리에이티브 솔루션(Brand Memory) | 2026-06-23 칸 라이언즈에서 **발표**. 시장별 출시 상태 미확인 | 미확인 | 미확인 | [Campaign US](https://www.campaignlive.com/article/meta-launches-complete-ai-creative-ad-ecosystem/1962693) |
| Google AI Max for Search | 기존 검색 캠페인 안의 옵션 레이어. 자동 생성 애셋·캠페인 단위 확장검색 사용 캠페인은 2026-09부터 자동 업그레이드, DSA 일몰·자동 업그레이드는 2027-02로 연기 | 미확인 | 매체비 | [Google blog](https://blog.google/products/ads-commerce/dsa-upgrade-to-ai-max-2026/) |
| Google GML 2026 발표(AI Brief, 멀티모달 Asset Studio, Ask Advisor, 1-click 실험) | 발표. 단계별 출시 상태 미확인 | 미확인 | 미확인 | [Google GML 2026](https://blog.google/products/ads-commerce/google-marketing-live-2026-collection/) |
| TikTok GMV Max | 2025년 중반 TikTok Shop 광고의 유일한 캠페인 유형으로 의무화(날짜는 시장별로 상충, 아래 참조). Seller Center·Ads Manager 전면 지원 2026-02-25 [3P] | TikTok Shop의 한국 운영 여부 미확인(크로스보더 셀러에 해당) | 매체비 | [TikTok help](https://ads.tiktok.com/help/article/gmv-max-migration-tiktok-shop-ads), [dataslayer](https://www.dataslayer.ai/blog/tiktok-shop-gmv-max-30-higher-gmv-vs-manual-ads-2026-complete-guide) |
| 네이버 ADVoost 쇼핑 | 2025-05-22 오픈베타. '부스트 업' 별도 캠페인 분리 2026-04-28 예정 | 한국 | 미확인 | [머니투데이](https://www.mt.co.kr/tech/2025/05/22/2025052209125860746), [마케팅인사이드](https://inside.ampm.co.kr/insight/58820) |
| 네이버 ADVoost 오디언스 | 2025-11 출시 보도 | 한국 | 미확인 | [전자신문](https://www.etnews.com/20251119000289) |
| 네이버 AI 브리핑 광고(ADVoost 검색·쇼핑) | 테스트 2026-05-07~07-02. 광고주센터 2026-07-15, 정식 노출 2026-07-21 | 한국 | 미확인 | [나스미디어](https://blog.nasmedia.co.kr/entry/2605naspick) |
| 쿠팡 AI 스마트 광고 / 매출최적화 광고 | 운영 중. 2026년 광고센터가 AI 스마트·매출최적화·수동 성과형으로 구분 [3P] | 한국 | 매체비 | [OSC](https://oscsnm.com/coupang-ads-center-guide-2026/), [쿠팡 광고](https://ads.coupang.com/settings/mps) |
| 카카오모먼트AI | 2025-12-11 출시 | 한국 | 요금 명시 없음 | [뉴시스](https://www.newsis.com/view/NISX20251211_0003437038) |

#### Meta
- [PRESS] Meta는 2026년 말까지 브랜드가 AI로 광고 제작과 타깃팅을 완전히 자동화할 수 있게 하는 것을 목표로 한다고 보도되었다(WSJ 원보도, Reuters 인용. 보도 시점은 2025년으로 알려졌으나 정확한 날짜는 원문 미확인). — [Yahoo Finance/Reuters](https://finance.yahoo.com/news/meta-looking-fully-automate-ad-113056107.html)
  - 구상: 브랜드가 상품 이미지와 예산 목표를 올리면 AI가 이미지·영상·문구를 생성하고, 타깃을 정하고, 예산 배분을 제안한다. 사용자별 실시간 개인화도 포함된다(예: 같은 자동차 광고가 사용자 위치에 따라 설산 배경 또는 도심 도로 배경). 일부 대형 브랜드는 브랜드 보이스 희석과 AI 이미지의 왜곡·품질 문제를 우려했다. — [Campaign Asia](https://www.campaignasia.com/article/meta-aims-to-fully-automate-ad-creation-with-ai-by-2026/502831)
- [PRESS/VENDOR] **2026-06-23 칸 라이언즈(Meta Beach)**: 글로벌 비즈니스 총괄 Nicola Mendelsohn이 AI 광고 제작 "end-to-end creative solution"을 발표했다. 핵심 기능은 **Brand Memory**로, 기존 광고에서 브랜드 정체성과 톤을 학습해 생성형 광고에 적용한다. 크리에이티브팀과 미디어팀의 공유 작업 공간이 있고, 성과 좋은 광고를 확인한 뒤 새 광고를 생성·테스트하는 흐름이다. — [Campaign US](https://www.campaignlive.com/article/meta-launches-complete-ai-creative-ad-ecosystem/1962693); [MM+M](https://www.mmm-online.com/news/meta-launches-complete-ai-creative-ad-ecosystem/)
  - [3P] 제3자 설명: 상품 이미지나 사업자 URL과 예산을 넣으면 AI가 이미지·영상·카피를 생성하고, 오디언스 선택, 지면 최적화, 예산 배분 제안까지 한다. 즉 2025년 보도된 "완전 자동화" 구상을 제품으로 발표한 것이다. 한국 출시나 한국어 지원은 확인하지 못했다. — [Digital Applied](https://www.digitalapplied.com/blog/meta-ai-creative-ads-cannes-lions-2026-advertiser-guide)
- [3P] Advantage+ Shopping은 2025년 Advantage+ Sales로 이름이 바뀌었고, 2026년에는 구 Shopping 형식을 새로 만들 수 없다. 2026-02 광고관리자 개편으로 수동 캠페인과 Advantage+ 생성 흐름이 하나로 통합되었다. — [topgrowthmarketing](https://topgrowthmarketing.com/advantage-plus-shopping-campaigns/); [AdNabu](https://blog.adnabu.com/facebook/meta-advantage-plus-sales-campaigns/)
- [3P, UNVERIFIED — Meta 공식 문서 미확인] Advantage+ 최소 주간 전환 요건이 **2026-04부터 50건에서 25건으로 완화**되어 소형 스토어도 쓸 수 있게 되었다고 한다. — [1ClickReport](https://www.1clickreport.com/blog/advantage-plus-shopping-25-conversions-2026-guide); [topgrowthmarketing](https://topgrowthmarketing.com/advantage-plus-shopping-campaigns/)
- [3P] 광고세트당 광고 최대 50개, 캠페인당 150개. 제품군에는 Advantage+ Leads, Advantage+ Audience, 생성형 AI 소재 변형(Creative suite)이 포함된다. — [Benly](https://benly.ai/learn/meta-ads/advantage-plus-updates-2026)
- [VENDOR, 3P 경유] "글로벌 테스트에서 Advantage+ Sales를 쓴 광고주는 수동 전용 대비 평균 **ROAS +32%, CPA −17%**." 테스트 방법과 기간은 공개되지 않았고 Meta 원문도 확인하지 못했다. 다른 요약에는 Meta 자체 보고 Advantage+ ROAS가 "약 $4.52"로 나와 수치 계열이 상충한다. — [Birch](https://bir.ch/blog/advantage-plus-sales-campaigns-guide); [AdNabu](https://blog.adnabu.com/facebook/meta-advantage-plus-sales-campaigns/)
- [VENDOR] **Meta 2026년 2분기 실적 발표**(2026-07 말, MediaPost 2026-07-31 보도). 검색 요약 기준 수치이며 transcript 원문은 열지 못했다.
  - Advantage+ end-to-end 솔루션 연 매출 런레이트 **$750억 초과**
  - **900만 개 이상 소규모 사업자**가 생성형 AI 광고 소재 도구를 1개 이상 사용
  - 이미지 생성 도구 채택이 분기 중 2배 이상 증가했고, 영상 애셋으로 이미지 생성 가능
  - GEM 랭킹 모델과 사용자 이해 모델로 Facebook 광고 클릭 +8.3%, 전환 +15.7%
  - 인스타그램 LLM 파일럿으로 앱 이벤트 전환 +1%
  - Meta가 제시한 사례: 온라인 의류 브랜드 "Underneat"이 Advantage+ Sales 도입 후 증분 구매 +13%, 장바구니 담기 +16%
  - 출처: [Meta Q2 2026 transcript PDF](https://s21.q4cdn.com/399680738/files/doc_financials/2026/q2/META-Q2-2026-Earnings-Call-Transcript.pdf); [Alpha Spread](https://www.alphaspread.com/security/nasdaq/meta/investor-relations/earnings-call/q2-2026); [MediaPost](https://www.mediapost.com/publications/article/416925/meta-boosts-advertising-in-q2-tries-to-reassure-i.html)
- [3P, UNVERIFIED] Advantage+를 Meta 광고주의 82%가 사용하고, value optimization 제품군 런레이트는 $200억 초과로 전년 대비 2배 이상이라고 한다. — [VectorShift](https://vectorshift.ai/research/companies/meta-platforms/earnings/2026-q2-summary); [AdsUploader](https://adsuploader.com/blog/meta-earnings-for-advertisers)
- [IND] **Haus "The Meta Report"**: 18개월간 Meta 증분 실험 640건. 평균 브랜드는 Meta에 월 약 $100만 이상(연 약 $1,400만) 지출하는 대형 광고주다.
  - Meta의 핵심 KPI 평균 lift는 약 19%다.
  - Haus 역대 상위 100개 고증분 실험 중 77개가 Meta였다.
  - 옴니채널 브랜드는 Meta 효과의 32%가 자사몰(DTC) 밖, 즉 리테일·마켓플레이스 매출로 나타났다.
  - **58%의 브랜드는 Advantage+보다 직접 운영한 수동 캠페인의 iROAS(증분 ROAS)가 더 높았다.**
  - Advantage+는 실험 중간 시점에는 수동보다 9% 좋았지만 **종료 시점에는 12% 나빴다.** 고의도 사용자를 빨리 잡아 단기 성과는 좋지만, 기간을 길게 보면 수동 캠페인이 실제 증분 가치를 더 만드는 경우가 많다는 해석이다.
  - 출처: [Haus](https://www.haus.io/blog/the-meta-report-lessons-from-640-haus-incrementality-experiments); [AdExchanger](https://www.adexchanger.com/measurement/for-meta-marketers-automation-isnt-always-the-advantage-but-its-complicated/); [MediaCat](https://mediacat.uk/marketers-best-metas-black-box-report-shows/)
- [UNVERIFIED — 원 데이터 출처 불명] "Meta 캠페인 5.5만 개 이상 분석 결과, Advantage+ 신규고객 획득비용이 2024-05에서 2025-05 사이 $257에서 $528로 2배 이상 올랐는데도 Meta 보고 ROAS는 약 $4.52로 유지되었다." — [Pixis](https://pixis.ai/blog/advantage-vs-performance-max-head-to-head-2026/) 경유 검색 요약

#### Google
- [VENDOR] **AI Max for Search**는 새 캠페인 유형이 아니라 기존 검색 캠페인에서 켜는 최적화 레이어다. 구성 요소는 검색어 매칭 확장, 텍스트 맞춤화, 최종 URL 확장이다. Google 주장: 켜면 비슷한 CPA/ROAS에서 **전환(가치) +14%**, 완전일치·구문일치 위주 캠페인은 **최대 +27%**. — [Google Ads Help](https://support.google.com/google-ads/answer/15910187?hl=en); [ALM Corp](https://almcorp.com/blog/google-ai-max-search-campaigns-complete-checklist-performance-analysis/)
- [3P, UNVERIFIED] 독립 테스트를 종합하면 "**광고주의 84%가 중립 또는 부정적 결과**"를 보고했다고 한다. 표본과 원 조사는 확인하지 못했다. — [PPC Live](https://ppc.live/library/strategy/googles-ai-max-for-search-what-the-data-actually-shows-in-2026/)
- [3P] Brainlabs가 23개 테스트를 분석한 결과, AI Max 기능 3개를 모두 켠 캠페인이 검색어 매칭만 켠 캠페인보다 "성공률"이 40% 높았다. — [PPC Live](https://www.ppc.live/post/google-s-ai-max-for-search-what-the-data-actually-shows-in-2026)
- [3P] 성과가 좋은 광고주의 공통점: AI Max를 "통제된 확장 레이어"로 취급한다. 계정 구조가 깔끔하고, 전환 데이터가 충분하고, 검색어를 적극 모니터링하고, 사전에 성공 기준을 정해 둔다. — [PPC Live](https://ppc.live/library/strategy/googles-ai-max-for-search-what-the-data-actually-shows-in-2026/)
- [VENDOR] DSA(동적 검색광고)의 AI Max 전환: 일몰과 자동 업그레이드는 **2027-02 시작으로 연기**되었다. 다만 자동 생성 애셋(ACA)이나 캠페인 단위 확장검색 설정을 쓰는 캠페인은 **2026-09부터** 계속 자동 업그레이드된다. — [Google blog](https://blog.google/products/ads-commerce/dsa-upgrade-to-ai-max-2026/)
- [VENDOR] **GML 2026 발표** (출시 단계와 한국 제공 여부는 미확인)
  - AI Max가 Google AI 캠페인 최적화의 주력 프레임워크가 된다.
  - 자연어 가드레일인 "AI Brief"로 AI Max와 PMax를 조정한다(사업 맥락, 강조 메시지, 금지 사항, 맞추고 싶은 검색어).
  - 멀티모달 Asset Studio: 프롬프트 하나로 텍스트·이미지·영상을 생성한다("Gemini Omni"). 브리프나 브랜드 가이드 PDF를 올려 스타일 기준으로 쓴다.
  - PMax 애셋 수정을 바로 A/B 테스트로 바꾸는 1-click "Save and Set Experiment"가 생긴다.
  - Google Ads·GA·Merchant Center·GMP를 아우르는 Gemini 에이전트 "Ask Advisor"가 나온다.
  - 출처: [Google GML 2026](https://blog.google/products/ads-commerce/google-marketing-live-2026-collection/); [Think with Google](https://business.google.com/us/think/search-and-video/google-marketing-live-2026-collection/); [Brainlabs](https://www.brainlabsdigital.com/google-marketing-live-2026-brainlabs-review/); [Strike Social](https://strikesocial.com/blog/google-marketing-live-2026/)
- [3P] PMax 통제 기능. 가이드들은 "2026 업데이트"로 표기하지만 실제 출시일은 미확인이다(Gaps 참조).
  - 캠페인·계정 단위 제외 키워드(PMax 캠페인당 최대 10,000개)
  - 채널별 리포트(Search·Shopping·Display·YouTube·Discover·Gmail·Maps)
  - 브랜드 제외는 캠페인 시작 전에 설정해야 한다.
  - 계정 단위 제외 키워드에 브랜드명을 넣으면 검색·쇼핑·PMax 전체에 적용된다.
  - PMax의 검색어 인사이트 리포트에서 브랜드어가 차지하는 전환 비중을 보고 잠식 정도를 추정할 수 있다.
  - 출처: [Benly](https://benly.ai/learn/google-ads/pmax-2026-updates); [PaidMediaWorld](https://paidmediaworld.com/performance-max-brand-cannibalization/)
- [3P, UNVERIFIED — 대행사 추정, 방법론 없음] PMax가 원래 자연 전환될 브랜드 검색어에 입찰하면 겉보기 ROAS가 15~30% 부풀고 PMax 예산의 8~15%가 소진된다고 한다. — [Growthspree](https://www.growthspreeofficial.com/blogs/branded-search-cannibalization-pmax-b2b-saas-2026); [Supermetric](https://www.super-metric.com/performance-max-cannibalizing-branded-search)
- [IND(툴사)] Optmyzr 조사(2025-02, 503개 계정): **91.45%의 계정에서 검색 캠페인과 PMax의 키워드가 겹쳤다.** — [Optmyzr](https://www.optmyzr.com/blog/is-pmax-cannibalizing-search/)
- [IND(툴사)] Optmyzr 조사(9,199개 계정, PMax 24,702개 캠페인): 92%가 오디언스 신호를 쓰는데 요약에 따르면 이 계정들은 "모든 지표에서 고전"했다. 71%는 검색 테마를 쓰지만 결과가 혼재하거나 개선이 없었다. 요약 표현이므로 원문 확인이 필요하다. — [Optmyzr](https://www.optmyzr.com/blog/performance-max-2025-updates-study-analysis/)
- [IND(툴사)] Optmyzr 2026년 1분기 벤치마크(2.1만 개 이상 계정): 참여 지표는 올랐지만 효율은 정체였다. — [Search Engine Journal](https://www.searchenginejournal.com/optmyzr-report-finds-google-ads-engagement-rising-while-efficiency-holds/573718/); [Optmyzr](https://www.optmyzr.com/blog/google-ads-benchmark-report-q1-2026/)
- [IND] Haus도 PMax 내 브랜드어 분석을 발표했으나 세부 내용은 확보하지 못했다. — [PPC Land](https://ppc.land/haus-analysis-reveals-insights-on-brand-terms-in-google-performance-max/)

#### TikTok (크로스보더 셀러 해당)
- [3P/VENDOR] GMV Max는 Product·LIVE·Video Shopping Ads를 하나로 합친 자동화 형식으로, 노출·클릭이 아니라 GMV를 최적화한다. 2025년에 TikTok Shop 광고의 기본이자 유일한 캠페인 유형이 되었다.
  - 제3자가 정리한 일정: 6/1 신규 셀러의 기존 광고 생성 차단 → 6/25 기존 광고 기능 제거 → 7/15 전 셀러 전환.
  - **상충:** CedCommerce는 "9/1부터 의무"라고 보도했다(시장별 차이로 보인다). TikTok 공식 마이그레이션 도움말 페이지는 있지만 열지 못했다.
  - 출처: [TikTok Ads help](https://ads.tiktok.com/help/article/gmv-max-migration-tiktok-shop-ads); [Agentative](https://agentative.ai/blog/tiktok-shop-gmv-max-sellers-guide); [TBA Global](https://tbaglobal.com/tiktok-shop-replaces-traditional-ads-with-gmv-max-what-sellers-must-know-in-2025/); [CedCommerce](https://cedcommerce.com/blog/tiktok-shop-mandates-gmv-max-use-for-ads-what-this-means-for-your-strategy/)
- [3P] 두 가지 유형이 있다. 셀러는 상품, 예산, ROI 목표만 정하고 타깃·소재 최적화·예산 배분은 알고리즘이 한다.
  - **Product GMV Max**: 글로벌 제공. For You 피드, 검색, Shop 탭, Pangle에 영상과 상품카드 형식으로 노출된다.
  - **LIVE GMV Max**: 인도네시아·베트남·태국·필리핀·말레이시아·싱가포르에서만 제공되며, 작성 시점 기준 미국은 미제공이다.
  - 출처: [MADA](https://wearemada.com/resources/tiktok-shop-gmv-max/); [Polici](https://polici.net/guides/gmv-max-tiktok-shop); [TBA Global](https://tbaglobal.com/tiktok-shop-replaces-traditional-ads-with-gmv-max-what-sellers-must-know-in-2025/)
- [VENDOR, 3P 경유] "GMV Max는 수동 광고 대비 GMV +30%." Seller Center(데스크톱·모바일)와 Ads Manager 전면 지원은 2026-02-25에 시작되었다. — [Dataslayer](https://www.dataslayer.ai/blog/tiktok-shop-gmv-max-30-higher-gmv-vs-manual-ads-2026-complete-guide)
- [3P 추정치] TikTok Shop 시장 규모: 2026년 상반기 글로벌 GMV $503억(전년 대비 +92%), 2026년 연간 전망 $1,235억, 셀러 1,500만 명 이상. 미국은 등록 스토어 80.35만 개 중 절반 이상이 매출 0이다. 2026년 상반기 GMV $100만을 넘긴 미국 스토어는 5,700개 이상이고, 상위 1% 셀러가 GMV의 약 60%를 차지한다. — [SmartScout](https://www.smartscout.com/blog/tiktok-shop-statistics-2026); [Branvas](https://branvas.com/blogs/news/tiktok-shop-statistics)

#### 네이버
- [PRESS] ADVoost(애드부스트)는 AI로 타깃 설정부터 소재 제작, 운영 자동화까지 지원하는 네이버 광고 솔루션 브랜드다. — [인사이트코리아](https://www.insightkorea.co.kr/news/articleView.html?idxno=250345); [매일일보](https://www.m-i.kr/news/articleView.html?idxno=1392419)
- [PRESS] **ADVoost 쇼핑**: 2025-05-22 오픈베타. 쇼핑 광고주 특화 상품으로, 캠페인 설정·운영, 상품 연동·소재 선별, 지면 선정·노출 전 과정을 AI가 자동화한다. — [머니투데이](https://www.mt.co.kr/tech/2025/05/22/2025052209125860746); [ZDNet Korea](https://zdnet.co.kr/view/?no=20250522220303); [바이라인네트워크](https://byline.network/2025/05/22-437/)
  - [3P] 구조상 GFA(성과형 디스플레이)의 AI 전자동 캠페인이다(타깃·소재·입찰·지면을 AI가 운영). — [이노빈](https://www.inobean.com/blog/post.php?slug=%EB%84%A4%EC%9D%B4%EB%B2%84-%EB%94%94%EC%8A%A4%ED%94%8C%EB%A0%88%EC%9D%B4%EA%B4%91%EA%B3%A0-advoost-%EC%87%BC%ED%95%91%EC%9D%B4%EB%9E%80-ai-%EC%A0%84%EC%9E%90%EB%8F%99-%EC%BA%A0%ED%8E%98%EC%9D%B8-%EC%9E%91%EB%8F%99%EC%9B%90%EB%A6%AC-%EC%B2%B4%ED%81%AC%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EB%B3%91%ED%96%89%EC%A0%84%EB%9E%B5)
  - [VENDOR] 출시 전 약 1개월간 가전·화장품·패션·식음료 광고주 40곳 대상 비공개 테스트(CBT)를 진행했다. 결과는 "평균 ROAS·CVR이 도입 전보다 **유의미하게 향상**"이라고만 발표했고 **구체 수치는 공개하지 않았다.** — [ZDNet Korea](https://zdnet.co.kr/view/?no=20250522220303); [디지털투데이](https://www.digitaltoday.co.kr/news/articleView.html?idxno=567413); [AI매터스](https://aimatters.co.kr/news-report/ai-news/21804/)
  - [VENDOR 공지, 3P 경유] 네이버 밖의 검증된 광고 영역으로 도달을 넓히는 '부스트 업' 기능이 별도 '부스트 업' 캠페인으로 분리되고 관리·리포트 환경도 개선된다(2026-04-28 예정). — [마케팅인사이드](https://inside.ampm.co.kr/insight/58820)
- [PRESS] **ADVoost 오디언스**: AI가 광고 타깃팅을 자동 설정한다(2025-11 보도). — [전자신문](https://www.etnews.com/20251119000289)
- [VENDOR] **ADVoost Screen**: AI를 접목한 DOOH(옥외 디지털 광고) 솔루션. — [네이버 보도자료](https://navercorp.com/media/pressReleasesDetail?seq=33507)
- [PRESS] **AI 브리핑 광고** (ADVoost 검색광고·쇼핑 광고 중심)
  - 일정: 2026-05-07~07-02 약 8주간 일부 키워드·트래픽 대상 테스트 → 2026-07-15 광고주센터 오픈 → **2026-07-21 정식 노출**.
  - 작동 방식: 광고주가 등록한 문안을 그대로 쓰지 않는다. 네이버 광고 에이전트가 광고주 등록 정보나 랜딩페이지 정보를 바탕으로 **문안을 새로 생성하고 관련 상품을 선별**한다.
  - AI 브리핑 월 이용자는 약 3,000만 명(네이버 발표).
  - 출처: [나스미디어](https://blog.nasmedia.co.kr/entry/2605naspick); [아이뉴스24](https://www.inews24.com/view/1978190); [전자신문](https://www.etnews.com/20260618000242); [AI 파이낸셜뉴스](https://www.aifnlife.co.kr/news/articleView.html?idxno=27287); [네이트](https://m.news.nate.com/view/20260506n28647)
- [3P] 에이전시 분석: 애드부스트 도입이 네이버 검색광고의 패러다임 전환이라는 해석(세부 내용은 확보하지 못함). — [InterAd](https://www.interad.com/insights/naver-advoost-strategic-shift)

#### 쿠팡
- [3P] 2026년 쿠팡 광고센터는 AI 스마트 광고, 매출최적화 광고, 수동 성과형 광고로 나뉜다. 캠페인-그룹 구조가 강화되었고, 매출 기회가 있는 캠페인 추천과 공유 예산 기능이 있다. — [OSC(쿠팡광고파트너 대행사)](https://oscsnm.com/coupang-ads-center-guide-2026/)
- [3P] **AI 스마트 광고** 작동 방식
  - 판매자는 목표만 설정하고, 쿠팡이 광고에 적합한 상품을 자동으로 고른다.
  - 상품명·카테고리·태그를 기반으로 가능한 키워드를 계속 자동 추가한다.
  - 7~14일의 최적화(학습) 기간이 있다.
  - 출처: [오픈애즈](https://www.openads.co.kr/content/contentDetail?contsId=16147); [아이보스](https://www.i-boss.co.kr/ab-6141-67264)
- [3P] **AI 스마트 광고 단점**
  - 계정당 캠페인을 1개만 운영할 수 있다.
  - 상품별 ON/OFF가 안 되어 주력 상품에 예산을 몰거나 특정 상품을 빼기 어렵다.
  - 광고비 낭비를 알면서도 시간 절약 때문에 쓰는 셀러가 많고, 설정 제한과 낮은 ROAS 때문에 기피하는 셀러도 있다.
  - 출처: [오픈애즈](https://www.openads.co.kr/content/contentDetail?contsId=16147); [Savvy](https://intro.savvy.ing/15bc2402-752c-8182-88fd-c9ef5f3bba6f)
- [3P, UNVERIFIED — 대행사 주장, 방법론 없음] "AI 스마트 광고 자동화로 클릭률 평균 30% 상승, 광고비 약 10% 절감." — [OSC](https://oscsnm.com/coupang-ads-center-guide-2026/)
- [3P 실무자 사례] 수동 광고는 ROAS 2000%까지도 나오지만 AI 스마트 광고는 200~300%까지 떨어질 수 있다. **AI 70% + 수동 30%** 병행으로 ROAS를 180%에서 330%로 올렸다는 사례도 있다. — [아이보스 커뮤니티](https://www.i-boss.co.kr/ab-1486505-51369); [Windly](https://www.windly.cc/blog/coupang-ad-types-and-settings)
- [VENDOR] 매출최적화 광고 공식 설정 페이지와, 두 유형을 비교하는 쿠팡 공식 비디오클래스('AI스마트광고 vs 매출 최적화 광고')가 있다. 세부 내용(목표 ROAS 설정 등)은 확보하지 못했다. — [쿠팡 광고 매출최적화](https://ads.coupang.com/settings/mps); [쿠팡 광고 비디오클래스](https://ads.coupang.com/videoclass/youtube03)
- [3P] 2026년 쿠팡 광고 유형 비교(5종, 자동 입찰과 수동 입찰): [실무팩](https://silmupack.com/%EC%BF%A0%ED%8C%A1-%EA%B4%91%EA%B3%A0-%EC%A2%85%EB%A5%98/); [올라](https://allra.co.kr/blogs/106)

#### 카카오
- [VENDOR/PRESS] **카카오모먼트AI** (2025-12-11 출시)
  - 대상: 모먼트를 쓰고 싶지만 운영이 어려운 자영업자·중소상공인.
  - 기능: 광고 데이터를 해석하고 운영 방향을 제안한다. 캠페인 데이터를 분석해 **최적화 점수(18~100점)**를 매기는데, 최근 성과 변화, 경쟁 상황, **소재 피로도**를 종합한다. 점수를 올리기 위한 실행 제안('신규 소재 추가', '타겟 범위 확장' 등)도 함께 준다.
  - 요금: 명시되지 않았다.
  - 출처: [뉴시스](https://www.newsis.com/view/NISX20251211_0003437038); [카카오](https://www.kakaocorp.com/page/detail/11845); [플래텀](https://platum.kr/archives/276979); [뉴데일리](https://biz.newdaily.co.kr/site/data/html/2025/12/11/2025121100099.html)
- [PRESS] 2026-04-23 카카오 광고 컨퍼런스(광고주 약 1,000명)에서 캠페인 기획, 타깃 설정, 소재 운영까지 전 과정을 AI로 자동화하는 방향을 발표했다. — [머니투데이](https://www.mt.co.kr/tech/2026/04/24/2026042409313714033); [뉴스핌](https://www.newspim.com/news/view/20260424000482); [카카오](https://www.kakaocorp.com/page/detail/12006)
- [VENDOR 문서] 카카오모먼트 한 곳에서 비즈보드, 디스플레이, 동영상, 메시지 광고를 함께 운영한다. — [카카오비즈니스 가이드](https://kakaobusiness.gitbook.io/main/ad/moment)
- [3P] '커머스 광고자산 자동연동 / 상품 카탈로그 캠페인' 관련 공지가 있다(세부 내용 미확보). — [아이디어키](https://www.ideakey.co.kr/html/customer/notice_detail.html?no=1383)

### Inferences
- **공통 구조.** 플랫폼들이 "상품 피드 + 예산 + 목표 + 소재 풀"만 받고 나머지를 AI가 정하는 구조로 수렴했다. 셀러에게 남는 레버는 다섯 가지다: ① 상품 피드와 상세페이지 품질, ② 소재의 양과 다양성(2장), ③ 전환 추적 정확도, ④ 예산·목표 ROAS 설정, ⑤ 제외 설정(브랜드어, 저마진 상품). 네이버 AI 브리핑 광고는 랜딩페이지 정보로 문안을 새로 쓰므로 **상세페이지 문구가 곧 광고 문안의 원재료**가 된다. 따라서 과장·부정확한 표현이 AI 문안으로 증폭될 위험이 있다.
- **플랫폼 ROAS는 상한선으로 보라.** Haus 결과(단기 우위가 종료 시점에 역전, 58% 브랜드가 수동 우위)와 Optmyzr의 검색·PMax 중복 91%를 보면, 자동화 캠페인의 플랫폼 ROAS에는 원래 샀을 고객(브랜드 검색, 재방문)이 섞여 있을 가능성이 높다. 자사몰, 쿠팡, 스마트스토어를 함께 운영하는 셀러는 Haus가 보고한 교차채널 효과(DTC 밖 32%)까지 고려해야 한다. 채널별 ROAS보다 **전체 매출 ÷ 전체 광고비(MER)**와 **신규고객 비중**을 기준 지표로 삼는 것이 안전하다.
- **1인 셀러 시작 순서(추론).**
  1. 구매 의도가 가장 강한 곳부터 시작한다. 쿠팡은 AI 스마트 광고로 키워드를 발굴(학습 7~14일)한 뒤, 성과 키워드와 주력 상품을 수동 성과형으로 옮긴다. 실무자가 보고한 70:30 혼합이 출발점이다.
  2. 스마트스토어는 네이버 검색·쇼핑 광고를 기본으로 하고, ADVoost 쇼핑은 소액으로 테스트한다. '부스트 업'(외부 지면)은 분리된 캠페인이므로 따로 평가한다.
  3. Meta는 주간 구매 약 25건 이상일 때(제3자 주장 기준) Advantage+ Sales를 쓴다. 그 미만이면 학습 신호가 부족할 수 있다.
  4. 카카오모먼트는 모먼트AI 최적화 점수와 제안을 체크리스트로 쓴다.
- **중소 브랜드(자사몰) 가드레일(추론).**
  - Google: PMax와 AI Max 전에 브랜드 제외와 계정 단위 브랜드 제외 키워드를 걸고, 검색어 인사이트와 채널 리포트를 주간으로 점검한다.
  - Google: AI Max는 전환 데이터가 깔끔한 캠페인에만 켠다. Google 자체 실험 기능이나 GML의 "Save and Set Experiment"로 켠 것과 끈 것을 비교한다.
  - Meta: Advantage+와 수동 캠페인을 충분한 기간 병행 비교한다. 중간 시점 결과로 판단하지 않는다.
- **비용.** 수집한 출처 어디에도 이 AI 기능들에 별도 이용료가 있다는 언급은 없다. 비용은 매체비이며, 학습 기간에 생기는 비효율과 소재 제작비가 숨은 비용이다.

### Gaps
- Google Demand Gen, TikTok Smart+(Shop 외 일반 광고), 네이버 쇼핑검색광고 자동입찰, 네이버 GFA의 ADVoost 외 AI 기능, 쿠팡 매출최적화 광고 세부(목표 ROAS 범위, 최소 예산), 카카오 비즈보드 AI 소재 기능은 검색 한도 소진으로 데이터를 확보하지 못했다.
- 한국 제공 여부와 한국어 지원(AI Max, Asset Studio·Gemini 기반 생성, Meta Brand Memory·end-to-end 솔루션, Meta 생성형 영상)은 미확인이다.
- Meta Advantage+ Sales 공식 성과 주장 수치가 상충한다(+32%/−17% 대 "$4.52" 계열). 25건 기준 완화도 Meta 공식 문서로 확인하지 못했다.
- 출시일 미확인:
  - AI Max의 베타에서 정식 출시(GA) 시점.
  - PMax 제외 키워드·채널 리포트 출시일. 제3자는 "2026 업데이트"로 쓰지만 모델 배경지식으로는 2025년 출시 가능성이 있어 검증이 필요하다.
  - WSJ의 Meta 자동화 보도일.
- TikTok Shop의 한국 운영 여부, 한국 셀러가 TikTok Shop 미국·동남아·일본에 입점할 때의 요건은 미확인이다.
- 네이버·쿠팡·카카오 모두 정량 성과를 공개하지 않았다. 네이버는 "유의미한 향상"만 발표했다. 한국 플랫폼 대상 독립 증분 실험은 찾지 못했다.
- 추가 확인 권장 단서(미검증): Meta 2026년 2분기 광고 단가(price per ad) 상승률. 검색 결과 제목에 "+12% price per ad"가 있었다([Digital Applied](https://www.digitalapplied.com/blog/meta-ads-price-per-ad-planning-after-q2)). 원문이나 10-Q로 확인해야 한다.

## 2. AI 크리에이티브 제작·대량 테스트 (브이캣, AdCreative.ai, Meta/Google 생성형, Canva, 이미지·UGC 영상 툴)

### Takeaway
자동화 캠페인 안에서는 **소재의 양보다 '진짜로 다른' 소재의 수**가 핵심 레버다. Meta Andromeda는 거의 같은 소재를 하나로 묶어 처리한다. 대행사 권고는 광고세트당 개념적으로 다른 소재 8~20개, Reels 비중이 큰 지면은 2~3주마다 교체다. 학술 현장실험에서는 AI 생성 광고가 CTR에서 사람 제작 광고와 같거나 더 높았다(GDN +19%, 3.69억 노출에서 불이익 없음). 다만 **"AI 생성" 표시가 붙으면 CTR이 약 31% 떨어진다.** 한국은 2026-06-01부터 AI 가상인물 광고에 '가상인물' 표시가 의무이고, 가짜 경험담은 표시해도 불법이다.

### Cited Findings
**툴별 (기능, 가격, 대상)**
- **브이캣(VCAT.AI)** [VENDOR]
  - 기능: AI(ChatGPT 포함)가 상품 이미지와 설명을 분석해 광고 콘셉트를 제안하고, 이미지를 고르고, 문구를 쓰고, 음악을 넣는다.
  - 요금: 셀프 결제 스타터·프로 요금제와 엔터프라이즈가 있다. 회원가입만 하면 영상·이미지 제작을 무제한으로 체험할 수 있지만 **다운로드는 유료 사용자만** 가능하다.
  - 정확한 KRW 가격은 확보하지 못했다.
  - 출처: [VCAT 요금제 차이](https://vcat.ai/help/ko/articles/7901577-%EC%9A%94%EA%B8%88%EC%A0%9C-%EB%B3%84-%EC%B0%A8%EC%9D%B4%EA%B0%80-%EA%B6%81%EA%B8%88%ED%95%B4%EC%9A%94-%EC%8A%A4%ED%83%80%ED%84%B0-%ED%94%84%EB%A1%9C-%EC%97%94%ED%84%B0); [VCAT 무료 사용](https://vcat.ai/help/ko/articles/7901571-%EB%B8%8C%EC%9D%B4%EC%BA%A3%EC%9D%80-%EB%AC%B4%EB%A3%8C%EB%A1%9C-%EC%82%AC%EC%9A%A9%ED%95%A0-%EC%88%98-%EC%9E%88%EB%82%98%EC%9A%94); [G2](https://www.g2.com/products/vcat-ai/reviews)
- **AdCreative.ai** [3P 가격 정리, 2026]
  - 가격 범위: 월 $20~$1,399.
  - 플랜(크레딧 수): $29(10), $59(25), $99(50), $149(100), $189(100), $249(200), $399(500), 커스텀.
  - Starter: 월간 결제 $39, 분기 결제 $29, 연간 결제 $20.
  - Professional: $249, 영상 기능이 열린다.
  - 할인: 연간 결제 50%, 분기 결제 25%.
  - 7일 무료체험(10크레딧, 카드 등록 필요, 8일째 자동 유료 전환).
  - 출처: [Atria](https://www.tryatria.com/blog/adcreative-ai-pricing); [TrustRadius](https://www.trustradius.com/products/adcreative-ai/pricing)
- **Arcads** (AI UGC 영상) [3P]: 월 $110에 8,000크레딧, AI UGC 영상 최대 50개로 영상당 약 $11이다. 공개 가격 페이지가 없다(2026-07 기준 /pricing이 404). 캐주얼하고 AI처럼 보이지 않는 대량 TikTok·Meta UGC 광고용이다. — [Wireflow](https://www.wireflow.ai/blog/arcads-pricing); [AdMake](https://admakeai.com/blog/best-ai-ugc-video-tools)
- **Creatify** [3P]: 연간 결제 시 월 $39부터, 30초 영상당 약 $3.90. 상품 URL을 넣으면 페이지를 읽어 스크립트를 쓰고 UGC형 광고를 4분 안에 생성한다(SKU가 많은 이커머스용). — [AdMake](https://admakeai.com/blog/best-ai-ugc-video-tools); [shhots](https://shhots.ai/blog/heygen-vs-arcads/)
- **HeyGen** [3P]: Creator $29(600크레딧), Pro $49(1,000크레딧), Business $149(1,500크레딧, 추가 좌석 $20). 175개 이상 언어 현지화 아바타 영상이 강점으로, 설명 영상이나 다국어 크로스보더 광고에 맞다. — [shhots](https://shhots.ai/blog/heygen-vs-arcads/); [Playcut](https://playcut.ai/blog/heygen-vs-arcads/)
- **Meta 생성형 소재 도구** [VENDOR]: 2026년 2분기 기준 900만 개 이상 소규모 사업자가 사용하고, 이미지 생성 채택이 분기 중 2배가 되었다(1장 참조). — [Alpha Spread](https://www.alphaspread.com/security/nasdaq/meta/investor-relations/earnings-call/q2-2026)
- **Google Asset Studio** [VENDOR]: GML 2026에서 멀티모달(텍스트·이미지·영상) 생성과 브랜드 가이드 업로드 기능이 발표되었다(1장 참조). — [Brainlabs](https://www.brainlabsdigital.com/google-marketing-live-2026-brainlabs-review/)

**몇 개를 테스트하나 (Andromeda 시대)**
- [3P] Andromeda는 소재 다양성을 보상하지만 중복은 하나로 묶는다. "문구만 조금 다른 제품컷 5개는 소재 5개가 아니라 1개로 취급된다." 훅, 포맷, 앵글이 개념적으로 달라야 한다. — [Jon Loomer](https://www.jonloomer.com/meta-andromeda-creative-diversification/); [Confect](https://confect.io/tactics/meta-andromeda-2026)
- [3P] 권고 범위
  - 광고세트당 10~20개 이상. 대행사들은 Meta가 권하는 방식이라고 설명한다.
  - 캠페인당 개념적으로 다른 콘셉트 8~12개.
  - 이커머스 계정은 15~50개를 한 세트에 쌓는다.
  - 출처: [Confect](https://confect.io/tactics/meta-andromeda-2026); [Segwise](https://segwise.ai/blog/meta-andromeda-update-creative-strategy-2026)
- [3P, UNVERIFIED — 서로 상충]
  - 다양한 소재 25개를 넣은 광고세트 1개가 소재 5개씩 넣은 광고세트 5개보다 전환 17% 많고 비용 16% 낮았다고 한다.
  - 반면 활성 소재 4~6개가 1~2개 대비 CTR +22%이고, 7개를 넘으면 CTR이 정체되고 CPM이 8~12% 오른다는 주장도 있다.
  - 출처: [AdScale](https://adscale.com/blog/how-many-ad-creatives-per-ad-set/); [Confect](https://confect.io/tactics/meta-andromeda-2026)

**크리에이티브 피로도**
- [3P 데이터] AdSpyder 2026-05 표본(광고 24,650개)
  - 관측된 소재 수명 중앙값: Meta 4일, YouTube 5.1일, LinkedIn 43.3일.
  - 54%가 7일 안에 사라졌고, 30일 이상 남은 것은 22%, 90일 이상은 9.4%였다.
  - 광고 라이브러리 관측 기간이므로 테스트 후 중단한 소재도 포함된다.
  - 출처: [AdSpyder](https://adspyder.io/blog/ad-fatigue-benchmarks/)
- [3P] Motion 2026 Creative Benchmarks(광고비 $13억 규모): 소재의 약 절반이 28일 전에 교체되었다. — [The Interconnections](https://www.theinterconnections.com/benchmarks/meta-creative-fatigue)
- [VENDOR 연구, 3P 경유, 원문 미확인] Meta Analytics 연구: 같은 시각 요소에 반복 노출되면 광고 효율이 떨어지고, 이는 오디언스 포화와 구별된다. Meta의 피로도 가이드를 따랐을 때 피로도가 높은 경우 전환율이 평균 8% 올랐다. "4회 반복 노출 후 CTR 45% 하락"이라는 Meta 연구 인용도 있다. — [The Interconnections](https://www.theinterconnections.com/benchmarks/meta-creative-fatigue); [GoodMorning](https://goodmorningco.com/blog/how-often-refresh-meta-ads-creative)
- [3P 경험칙]
  - Andromeda가 소진 기간을 줄여 Reels 비중이 큰 지면에서는 한 콘셉트가 2~3주면 소진된다.
  - 7일 빈도 기준 상단 퍼널 약 2.5, 중간 퍼널 약 3.5를 교체 신호로 본다.
  - 4분기 성수기에는 상단 퍼널 소재를 5~7일, 하단 퍼널 소재를 10~14일마다 교체한다.
  - 출처: [GoodMorning 주기](https://goodmorningco.com/blog/how-often-refresh-meta-ads-creative); [GoodMorning 빈도](https://goodmorningco.com/blog/what-is-creative-fatigue-meta-ads-frequency-thresholds)
- [VENDOR] 카카오모먼트AI 최적화 점수에도 '소재 피로도'가 포함된다(1장). — [뉴시스](https://www.newsis.com/view/NISX20251211_0003437038)

**학술·독립 근거 (AI 소재 성과)**
- [ACAD] NYU·Emory 연구진의 Google Display Network 현장실험: 처음부터 생성형 AI로 만든 광고의 CTR이 사람 제작 광고보다 **19% 높았다.** AI로 처음부터 만든 광고("Gen AI created")가 사람 디자인을 AI로 수정만 한 광고("Gen AI modified")보다 성과가 좋았다. 논문 원문은 확인하지 못했다. — [Eric Seufert X 게시물](https://x.com/eric_seufert/status/1996981773389963357); [The Decoder](https://the-decoder.com/telling-consumers-an-ad-is-ai-generated-cuts-clicks-by-31-percent-study-finds/)
- [ACAD] **공개 효과:** 광고에 AI 생성이라고 표시하자 CTR이 표시 없는 사람 광고 대비 약 **31.5% 낮아졌다.** — [The Decoder](https://the-decoder.com/telling-consumers-an-ad-is-ai-generated-cuts-clicks-by-31-percent-study-finds/)
- [ACAD] "AI in Disguise" (Exner, Hartmann, Ding, Zhang, Netzer): AI 생성 광고를 대규모로 실제 집행한 사례를 준실험으로 분석했다. 노출 3.69억 회, 클릭 250만 회 기준으로 AI 이미지의 평균 CTR 열위는 **발견되지 않았다.** 사람이 만든 것처럼 보이는 AI 광고는 사람 제작 광고와 인공적으로 보이는 AI 광고보다 CTR이 유의하게 높았다. — [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5096969); [TUM](https://www.msl.mgt.tum.de/en/dm/news/article/new-working-paper-ai-in-disguise/)
- [ACAD] Hartmann·Exner·Domdey "The power of generative marketing": 생성형 AI가 사람을 넘어서는 시각 마케팅 콘텐츠를 만들 수 있는지 검증한 연구(세부 수치는 확보하지 못함). — [SSRN](https://dx.doi.org/10.2139/ssrn.4597899)
- [ACAD] X(트위터) 현장실험(노출 490만 회): 사람-AI 팀은 사람-사람 팀보다 텍스트 품질이 높고 이미지 품질이 낮았다. 이미지 품질은 CPC를 낮추고 텍스트 품질은 CTR을 올리는데, 두 효과가 상쇄되어 광고 성과는 비슷했다. — [arXiv 2503.18238](https://arxiv.org/html/2503.18238v3)

**한국 규제 (AI 소재·AI 모델·UGC형 광고)**
- [PRESS] 공정위가 '추천·보증 등에 관한 표시·광고 심사지침' 개정을 확정해 **2026-06-01부터 시행**한다.
  - 생성형 AI 가상인물을 쓴 광고는 실제 인물로 오인하지 않도록 **'가상인물'임을 명확히 표시**해야 한다.
  - 가상인물이라고 밝혀도 **가짜 경험담을 늘어놓으면 불법 광고**다.
  - 출처: [서울신문 2026-05-31](https://www.seoul.co.kr/news/economy/2026/05/31/20260531500033)
- [3P 법률 칼럼] **AI 기본법(2026-01 시행)**: AI 사업자는 생성형 AI 기반 제품·서비스임을 이용자에게 사전 고지하고 생성물을 표시해야 한다. 위반하면 과기정통부 시정명령을 받고, 불이행 시 **최대 3,000만 원 과태료**가 부과된다. — [법률사무소 번화](https://bh-law.kr/ko/news/column/ai-content-labeling-obligation-guide); [디센트로](https://decentlaw.io/en/news/670); [KOCCA](https://www.kocca.kr/trendott/vol02/spotlight_4.html)
- [3P 해석, 법률 확인 필요] AI 기본법의 표시 의무 대상은 'AI 사업자'이고, AI 툴로 소재를 만들기만 한 광고주는 대상이 아니라는 해석이 있다. 다만 공정위 지침(가상인물 표시·가짜 후기 금지)은 광고주에게 적용된다. — [GI Corp](https://www.gi-corp.co.kr/post/ai-content-labeling-ads)
- [PRESS] AI 생성 이미지를 광고에 쓰면 허위광고가 되는지에 대한 팩트체크 기사가 있다(세부 내용 미확보). — [단비뉴스](https://www.danbinews.com/news/articleView.html?idxno=31761)

### Inferences
- **1인 셀러 제작 스택(추론).**
  1. 먼저 무료인 플랫폼 내장 생성 기능을 쓴다: Meta 생성형 도구, Google Asset Studio, 네이버 ADVoost 쇼핑의 소재 선별.
  2. 양이 필요하면 월 $20~50대 툴을 하나 추가한다: AdCreative Starter, HeyGen Creator, Creatify.
  3. 목표는 "소재 50개"가 아니라 **서로 다른 콘셉트 8~12개**다(문제 제기형, 비교형, 사용 장면, 리뷰 요약, 가격·혜택, 언박싱). 콘셉트마다 변형 2~3개를 만든다.
  4. 2~4주마다 콘셉트를 교체하고, 7일 빈도 2.5~3.5를 교체 신호로 쓴다.
- **중소 브랜드(추론).** 주간 소재 파이프라인을 운영한다: 기획 → AI 초안 → 사람 검수(법규, 브랜드 톤) → A/B 테스트 → 콘셉트 단위 성과 기록. Meta Brand Memory나 Google 브랜드 가이드 업로드처럼 브랜드 일관성 기능이 한국에 풀리면 활용한다.
- **AI 아바타 UGC 광고의 국내 적용(추론).**
  - 2026-06-01부터 '가상인물' 표시가 의무다. 연구상 AI 공개는 CTR을 약 31% 낮추므로 성과 불이익을 감안해야 한다.
  - '후기·경험담' 형식은 불법 위험이 있다. 제품 시연, 사용법, 스펙 설명 형식으로 쓰는 편이 안전하다.
  - 화장품·건강식품은 별도 표시광고 규제가 있으므로 AI 문구를 반드시 검수해야 한다(규제 세부는 Gaps).
- AI 이미지가 "사람이 만든 것처럼 자연스러울 때" 성과가 높았다는 연구 결과가 있다. 따라서 어색한 AI 티(손가락, 왜곡된 텍스트)를 걸러내는 품질 관리가 CTR에 직접 영향을 준다.

### Gaps
- 브이캣의 KRW 요금표와 벤더 사례 수치(CTR·ROAS 개선율), Canva AI(Magic Studio)의 한국 가격·기능, ChatGPT 이미지 생성·Midjourney 요금, Google 이미지·영상 생성 모델의 광고 연동 현황은 검색 한도 소진으로 확보하지 못했다.
- Arcads·Creatify·HeyGen 아바타의 한국어 품질과 한국 셀러 사례, AI UGC 광고의 독립 성과 연구는 확보하지 못했다.
- 네이버 GFA·쿠팡·카카오의 공식 소재 개수·교체 가이드는 없음 또는 미확인이다.
- 화장품·건강기능식품 AI 광고 문구 관련 식약처·공정위 제재 사례는 미조사다.

## 3. 오가닉 콘텐츠·SNS(인스타·틱톡·쇼츠·네이버 블로그·스레드), 검색엔진의 AI 콘텐츠 입장, AI 가상인간·라이브커머스

### Takeaway
Google과 네이버 모두 "AI를 썼다는 사실 자체는 제재하지 않는다." 제재 대상은 검수 없는 대량 생산 콘텐츠다. Google에서는 scaled content abuse, 네이버에서는 AI 초안 복붙, 반복어, 환각이 포함된 저품질 문서다. 2026년 업데이트는 경험과 신뢰할 수 있는 출처를 더 우대하는 방향이다. 따라서 셀러는 AI를 초안·구조화 도구로 쓰고 직접 경험, 실사진, 팩트체크는 사람이 채워야 한다. 한국 라이브커머스 AI 쇼호스트 성과와 SNS 콘텐츠 캘린더 AI 활용 근거는 이 세션에서 확보하지 못했다.

### Cited Findings
- [VENDOR, 2023-02 — 오래된 자료] Google 공식 입장: AI로 만든 콘텐츠도 유용하면 가이드라인 위반이 아니다. 제작 방식보다 품질을 본다. — [Google 검색 센터(한국어)](https://developers.google.com/search/blog/2023/02/google-search-and-ai-content?hl=ko)
- [3P] Google은 2024-03 스팸 정책의 "자동 생성 스팸" 조항을 "scaled content abuse(대량 생성 콘텐츠 악용)"로 바꿨다. 순위 조작 목적의 저품질 대량 페이지를 겨냥하며, **AI가 만들었든 사람이 만들었든 똑같이 적용**된다. — [RankAI](https://rankai.ai/articles/google-policy-on-ai-content-seo-compliance-guide); [Quillly](https://quillly.com/blogs/scaled-content-abuse)
- [3P, 수치 UNVERIFIED] 2026-03 코어 업데이트가 AI 대량 페이지를 주 표적으로 삼아, 편집 감독 없이 수백~수천 개 AI 페이지를 발행한 사이트는 트래픽이 50~80% 줄었다고 한다. Google이 공식 발표한 수치는 아니다. — [Digital Applied](https://www.digitalapplied.com/blog/scaled-content-abuse-google-march-update-ai-pages-decimated)
- [3P] 2026 검색 품질 평가 가이드라인(QRG)은 AI 사용 여부와 관계없이 E-E-A-T(경험·전문성·권위·신뢰), 독창성, 실제 사용자 가치를 우선한다. — [Broworks](https://www.broworks.net/blog/googles-2026-search-quality-rater-guidelines-what-you-need-to-know)
- [UNVERIFIED — 원출처 불명, 사실로 인용 비권장] "사람이 편집한 AI 글 50~100개를 발행하면 트래픽 +30~80%, 편집 없는 AI 글 1,000개 이상은 −40~90%"라는 SEO 블로그 주장이 있다. — [Maintouch](https://maintouch.com/blogs/does-google-penalize-ai-generated-content)
- [3P 블로그, 네이버 공식 문서 미확인] 네이버의 AI 글 대응
  - AI 사용 자체는 막지 않는다.
  - 제재 대상: 팩트체크나 수정 없이 AI 초안을 그대로 붙여넣은 글, 무의미한 단어 반복, 기계적인 문장과 환각(오류)이 들어간 문서.
  - 저품질 원인: 유사 문서, 무차별 키워드, 짧거나 상업성이 짙은 글, 부자연스러운 활동.
  - 2026년부터 "문서 유형에 관계없이 신뢰할 수 있는 출처의 문서를 우선 노출"하는 기술을 적용했다고 한다.
  - 출처: [행머니 판별 기준](https://moneyroan.com/naver-ai-content-detection-criteria/); [행머니 체크리스트](https://moneyroan.com/ai-blog-low-quality-checklist-2026/); [TILNOTE](https://tilnote.io/en/pages/69ce9379a5dad016ee58c5b9); [근거픽](https://geungeopick.com/2026-naver-blog-start-guide/)
- [3P] 권장 방식: 경험과 근거는 사람이 책임지고 AI는 정리와 표현을 돕는다. AI 초안에 팩트체크, 개인 경험 한 줄, 비교표나 체크리스트 하나만 더해도 노출 경쟁력이 달라진다. — [행머니](https://moneyroan.com/naver-ai-blog-not-exposed-reason-2026/); [TILNOTE](https://tilnote.io/en/pages/69ce9379a5dad016ee58c5b9)
- [VENDOR/PRESS] 네이버 AI 브리핑(AI 검색 요약)의 월 이용자는 약 3,000만 명이다(1장). AI 브리핑에 인용되는 조건을 다룬 대행사 글도 있다(세부 미확보). — [나스미디어](https://blog.nasmedia.co.kr/entry/2605naspick); [원플랜](https://blog.oneplan.co.kr/naver-ai-search-optimization/)
- [PRESS] AI 가상인물을 광고에 쓰면 '가상인물' 표시가 의무이고(2026-06-01~), 가짜 경험담은 금지다(2장). 라이브커머스 AI 쇼호스트나 AI 인플루언서 영상이 광고 성격을 띠면 적용될 가능성이 높다(추론은 아래). — [서울신문](https://www.seoul.co.kr/news/economy/2026/05/31/20260531500033)

### Inferences
- **스마트스토어·자사몰 셀러의 블로그·SEO 운영(추론).**
  - AI는 구조화와 초안에 쓴다: 키워드 조사, 목차, FAQ, 비교표.
  - 사람이 넣을 것: 실사용 사진, 직접 써본 경험, 수치 검증.
  - 대량 자동 발행은 Google과 네이버 모두에서 가장 큰 위험 요인이다.
  - 네이버 AI 브리핑과 Google AI 개요처럼 요약형 검색이 커질수록, 사실관계가 명확하고 구조화된 문서(스펙표, FAQ)가 인용되기 유리할 것으로 보인다. 원플랜 글이 이 방향을 시사하지만 세부는 미확인이다.
- **AI 쇼호스트·가상인간.** 공정위 개정 지침의 '가상인물 표시'와 '가짜 경험담 금지'가 라이브커머스와 숏폼 광고에도 적용될 것으로 보는 것이 안전하다. 따라서 가상인간을 "써보니 좋았다"는 후기형 진행자로 쓰는 것은 피해야 한다(추론, 법률 확인 필요).

### Gaps
- **라이브커머스 AI 호스트 근거 없음:**
  - 네이버 쇼핑라이브, 그립, 쿠팡라이브의 AI 쇼호스트·가상인간 도입 현황과 성과.
  - 쿠팡라이브의 현재 운영 상태.
  - 2025년 중국 사례(JD 창업자 AI 아바타 라이브, 바이두의 뤄융하오 AI 디지털휴먼 라이브 GMV 등)는 널리 보도된 것으로 알고 있으나 이 세션에서 검증하지 못했다.
- 인스타그램·스레드·틱톡·유튜브 쇼츠의 AI 콘텐츠 표시 정책(AI 라벨), 재업로드·독창성 알고리즘 변경, AI 콘텐츠 캘린더·스크립트 툴 활용 사례와 성과는 확보하지 못했다.
- 네이버 공식 검색 블로그의 AI 콘텐츠 관련 공지 원문(신뢰 출처 우선 노출 기술의 정확한 명칭과 시행일)은 미확인이다. 위 내용은 제3자 블로그 기반이다.

## 4. AI 인플루언서 마케팅 (탐색·매칭 툴: 피처링, 레뷰 등 / Modash, CreatorIQ 등)

### Takeaway
이 주제는 검색 한도가 소진되기 전에 조사하지 못해 **검증된 툴 정보(기능, 가격, 성과)가 없다.** 확인된 것은 규제 한 가지다. 2026-06-01 시행된 공정위 추천·보증 심사지침은 AI 가상인물(가상 인플루언서) 광고에 '가상인물' 표시를 요구하고, 가짜 경험담을 금지한다.

### Cited Findings
- [PRESS] 공정위 '추천·보증 등에 관한 표시·광고 심사지침' 개정(2026-06-01 시행): 생성형 AI 가상인물 광고는 '가상인물'임을 명확히 표시해야 하고, 표시해도 가짜 경험담은 불법이다. — [서울신문](https://www.seoul.co.kr/news/economy/2026/05/31/20260531500033)
- [ACAD] AI임을 공개하면 광고 CTR이 약 31% 낮아진다는 실험 결과가 있다. 가상 인플루언서 콘텐츠의 성과 기대치를 잡을 때 참고할 수 있다. — [The Decoder](https://the-decoder.com/telling-consumers-an-ad-is-ai-generated-cuts-clicks-by-31-percent-study-finds/)

### Inferences
- 가상 인플루언서나 AI 아바타 협찬 콘텐츠를 쓴다면 표시 의무와 경험담 금지 때문에 '후기·추천'형보다 '정보·시연'형이 적합하다. 기존 뒷광고(협찬 미표시) 규제와 함께 적용된다고 보는 것이 안전하다(추론).

### Gaps
- 한국 툴의 기능(AI 탐색, 가짜 팔로워 탐지, 매칭), 요금, 벤더 사례, 독립 성과 모두 미확보: 피처링(Featuring), 레뷰(REVU), 기타 체험단·인플루언서 매칭 플랫폼.
- 글로벌 툴 미확보: Modash, CreatorIQ, TikTok One·Creator Marketplace, Meta 크리에이터 마켓플레이스(Instagram 파트너십 광고).
- 인플루언서 콘텐츠를 광고 소재로 재활용하는 방식(파트너십 광고, Spark Ads)의 성과 데이터가 없다.
- 크리에이터 마케팅 산업 보고서(예: CreatorIQ의 연례 보고서)의 2025~26 수치를 확보하지 못했다.

## 5. CRM·리텐션 자동화 (세분화, 이탈·LTV 예측, 발송 시간 최적화, 알림톡·브랜드 메시지, 채널톡, 빅인, 스티비, 카페24 앱, Klaviyo, Braze, Attentive)

### Takeaway
확인된 가장 큰 2025~26년 변화는 카카오 **친구톡 → 브랜드 메시지** 전환이다. 친구톡은 2025-12-31 종료되었고 2026-01-01부터 브랜드 메시지가 대체한다. 브랜드 인증을 받은 발신자는 채널 친구가 아니어도 **마케팅 수신동의 고객 전원**에게 보낼 수 있어서, 합법적으로 모은 퍼스트파티 DB와 수신동의가 CRM의 핵심 자산이 되었다. AI CRM 툴들의 기능, 가격, 재구매·LTV 개선 수치는 이 세션에서 검증하지 못했다.

### Cited Findings
- [3P/VENDOR 공지] **친구톡은 2025-12-31 종료, 2026-01-01부터 브랜드 메시지로 대체.** 브랜드 메시지는 사전 브랜드 인증으로 발신 주체를 분명히 하는 신규 비즈니스 메시지 상품이다. — [솔라피](https://solapi.com/blog/kakaotalk-brand-message-notice); [스피디](https://www.speedykorea.com/blog/kakao-friendtalk-end-brand-message); [센드고](https://sendgo.io/announcements/friendtalk-discontinued-brand-message); [Omago](https://www.omago.ai/ko/blog/kakaotalk-brand-message-2026)
- [3P] '친구'에게만 보낼 수 있던 폐쇄형 친구톡이 사라지고, **마케팅 수신동의 고객이면 채널 친구가 아니어도 발송**할 수 있게 되었다. "2026년 카카오 마케팅의 핵심은 '친구 추가'가 아니라 합법적으로 수집한 퍼스트파티 데이터와 마케팅 수신동의의 질이다." — [아이보스](https://www.i-boss.co.kr/ab-6141-69665); [버클](https://vircle.co.kr/blog/%EC%B9%B4%EC%B9%B4%EC%98%A4-%EC%B1%84%EB%84%90-%EB%B8%8C%EB%9E%9C%EB%93%9C-%EB%A9%94%EC%8B%9C%EC%A7%80-%EC%A0%84%EB%9E%B5); [마케팅인사이드](https://inside.ampm.co.kr/insight/59098)
- [VENDOR PR] 핵클(Hackle)은 추가 개발 없이 브랜드 메시지로 전환할 수 있게 지원한다고 밝혔다(2025-12-17). — [모비인사이드](https://www.mobiinside.co.kr/2025/12/17/press-hackle/)
- [VENDOR 문서] 카카오 메시지 광고도 카카오모먼트에서 함께 운영한다. — [카카오비즈니스 가이드](https://kakaobusiness.gitbook.io/main/ad/moment)
- [VENDOR] 카카오모먼트AI는 '소재 피로도'를 점수화한다(1장). 메시지 캠페인에 적용되는지는 미확인이다. — [뉴시스](https://www.newsis.com/view/NISX20251211_0003437038)

### Inferences
- **자사몰(카페24·아임웹·식스샵·고도몰·Shopify) 셀러 우선순위(추론).**
  1. 회원가입과 결제 단계에서 **마케팅 수신동의를 명확하게 받는 설계**를 한다.
  2. 카카오 채널을 개설하고 브랜드 인증을 받는다.
  3. 브랜드 메시지와 알림톡을 CRM 툴에 연동한다.
  4. 첫 구매 후 재구매 유도, 장바구니 이탈, 휴면 복귀 시나리오를 자동화한다.
  - 브랜드 메시지가 비친구 발송을 허용하면서 수신동의 DB의 규모와 질이 곧 도달 범위가 되었다.
- **마켓플레이스 셀러(추론).** 스마트스토어·쿠팡 셀러는 고객 연락처를 직접 활용하는 데 제약이 있을 가능성이 크다. 따라서 채널 친구 추가, 톡톡 같은 플랫폼 내 CRM이나 자사몰 유입 전환이 과제가 된다. 플랫폼별 고객정보 활용 정책은 미확인이다.
- AI 세분화, 이탈·LTV 예측, 발송 시간 최적화의 가치는 발송 대상 DB가 있어야 생긴다. 수신동의 DB가 작은 1인 셀러는 고급 AI CRM보다 기본 자동화 시나리오 3~4개가 먼저다(추론).

### Gaps
- **툴별 데이터 미확보(검색 한도 소진):** 채널톡(마케팅 기능, AI 상담 에이전트, 요금), 빅인(자사몰 CRM·예측 세분화, 요금, 사례), 스티비(이메일, AI 기능, 무료 플랜), 카페24 앱스토어 CRM·알림톡 앱, Klaviyo(K:AI·예측 분석·발송 시간 최적화, 무료 한도, 가격), Braze(AI 의사결정 기능), Attentive(AI 기반 SMS).
- 브랜드 메시지의 세부 규칙: 건당 단가, 발송 유형(타깃 유형), 야간 발송 제한, 광고 표기 요건, 알림톡과의 가격 차이.
- 재구매율·LTV 개선에 대한 벤더 사례와 독립 연구: 국내외 모두 확보하지 못했다.
- 정보통신망법의 광고성 정보 전송 규정(수신동의 2년 재확인 등)과 브랜드 메시지의 관계는 미조사다.

## 6. SMB AI 마케팅 ROI: 독립 근거 vs 플랫폼 주장

### Takeaway
플랫폼 주장은 대부분 플랫폼이 자체 측정한 +14~32%(전환·ROAS)에 몰려 있다. 반면 독립적이거나 제3자인 근거는 네 갈래다.
- 증분 실험(Haus): 자동화는 단기에 이기지만 58% 브랜드에서 장기 iROAS는 수동이 우세했다.
- 계정 감사(Optmyzr): 검색과 PMax 중복이 91%였고, 오디언스 신호·검색 테마는 효과가 미미했다.
- 실무자 보고: AI Max는 84%가 중립 또는 부정 결과(원출처 불명), 쿠팡 AI 광고 ROAS가 수동보다 낮았다.
- 학술 현장실험: AI 소재는 사람 소재와 대등하거나 우세했다.

SMB만 대상으로 하거나 한국 셀러를 대상으로 한 엄밀한 ROI 연구는 찾지 못했다.

### Cited Findings

**주장 vs 독립 근거 대조표**

| 영역 | 플랫폼·벤더 주장 | 독립·제3자 근거 |
|---|---|---|
| Meta Advantage+ | ROAS +32%, CPA −17% (Meta 주장, 제3자 경유) — [Birch](https://bir.ch/blog/advantage-plus-sales-campaigns-guide). Underneat 증분 구매 +13% (Meta 선정 사례) — [Alpha Spread](https://www.alphaspread.com/security/nasdaq/meta/investor-relations/earnings-call/q2-2026) | 640개 실험 중 58%가 수동 iROAS 우위. 중간 시점 +9%에서 종료 시점 −12%로 역전 — [Haus](https://www.haus.io/blog/the-meta-report-lessons-from-640-haus-incrementality-experiments). 신규고객 획득비용 $257→$528 (UNVERIFIED) — [Pixis](https://pixis.ai/blog/advantage-vs-performance-max-head-to-head-2026/) |
| Google AI Max | 전환 +14%, 완전·구문일치 위주는 최대 +27% — [ALM Corp](https://almcorp.com/blog/google-ai-max-search-campaigns-complete-checklist-performance-analysis/) | 84% 중립·부정 (원출처 불명). Brainlabs 23개 테스트에서 기능 3개 전부 켠 쪽의 성공률이 40% 높음 — [PPC Live](https://ppc.live/library/strategy/googles-ai-max-for-search-what-the-data-actually-shows-in-2026/) |
| Google PMax | (본 세션에서 최신 공식 lift 수치 미확보) | 검색·PMax 키워드 중복 91.45% (503개 계정) — [Optmyzr](https://www.optmyzr.com/blog/is-pmax-cannibalizing-search/). 브랜드 잠식으로 ROAS 15~30% 과대 (대행사 추정) — [Supermetric](https://www.super-metric.com/performance-max-cannibalizing-branded-search) |
| TikTok GMV Max | 수동 대비 GMV +30% — [Dataslayer](https://www.dataslayer.ai/blog/tiktok-shop-gmv-max-30-higher-gmv-vs-manual-ads-2026-complete-guide) | 찾지 못함 |
| 네이버 ADVoost 쇼핑 | 광고주 40곳 CBT에서 ROAS·CVR "유의미한 향상" (수치 비공개) — [ZDNet Korea](https://zdnet.co.kr/view/?no=20250522220303) | 찾지 못함 |
| 쿠팡 AI 스마트 | CTR +30%, 광고비 −10% (대행사 주장) — [OSC](https://oscsnm.com/coupang-ads-center-guide-2026/) | 실무자: AI ROAS 200~300% vs 수동 최대 2000%. 70:30 혼합으로 180%→330% — [아이보스](https://www.i-boss.co.kr/ab-1486505-51369) |
| 카카오모먼트AI | 성과 수치 발표 없음 | 찾지 못함 |
| AI 생성 소재 | Meta 생성형 도구 사용 SMB 900만 이상 (채택률이며 성과 수치 아님) | GDN 현장실험 CTR +19% — [Seufert](https://x.com/eric_seufert/status/1996981773389963357). 3.69억 노출에서 CTR 열위 없음 — [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5096969). AI 공개 시 CTR −31% — [The Decoder](https://the-decoder.com/telling-consumers-an-ad-is-ai-generated-cuts-clicks-by-31-percent-study-finds/). X 실험에서 사람-AI 팀과 사람 팀의 성과 비슷 — [arXiv](https://arxiv.org/html/2503.18238v3) |

- [IND] Haus 표본의 평균 브랜드는 Meta에 월 $100만 이상을 쓴다. **1인 셀러나 소형 셀러에 그대로 일반화하기 어렵다.** — [Haus](https://www.haus.io/blog/the-meta-report-lessons-from-640-haus-incrementality-experiments)
- [IND] Meta는 Haus 상위 증분 실험 100개 중 77개를 차지할 만큼 증분 효과가 큰 채널이다(평균 lift 약 19%). 즉 "Meta가 효과 없다"가 아니라 "Advantage+ 자동화의 장기 증분이 수동보다 나은지는 브랜드마다 다르다"는 결론이다. — [Haus](https://www.haus.io/blog/the-meta-report-lessons-from-640-haus-incrementality-experiments); [AdExchanger](https://www.adexchanger.com/measurement/for-meta-marketers-automation-isnt-always-the-advantage-but-its-complicated/)
- [IND(툴사)] Optmyzr 2026년 1분기(2.1만 개 이상 계정): 참여 지표는 올랐으나 효율은 정체. AI 자동화가 늘어도 계정 전반의 효율 개선은 뚜렷하지 않다는 신호다. — [Search Engine Journal](https://www.searchenginejournal.com/optmyzr-report-finds-google-ads-engagement-rising-while-efficiency-holds/573718/)

### Inferences
- **이해관계 주의.** Haus는 증분 측정 서비스를, Optmyzr는 PPC 관리 툴을 판다. 플랫폼 자체 측정을 비판할 유인이 있다는 뜻이다. 그래도 방법론(무작위 지역·홀드아웃 실험, 대규모 계정 집계)이 공개되어 있어 플랫폼이 스스로 보고한 ROAS보다 신뢰도가 높다.
- **플랫폼 보고 ROAS와 증분 ROAS의 차이**가 가장 큰 곳은 브랜드 검색, 리타깃팅, 기존고객 구매다. 자동화 캠페인은 이 영역을 기본으로 포함하므로 과대평가 위험이 체계적으로 있다.
- **증분 테스트 예산이 없는 소상공인의 대안(추론):**
  - 지역이나 기간 단위로 광고를 껐다 켜서 비교한다(on/off 테스트).
  - 전체 매출 ÷ 전체 광고비(MER)와 신규고객 비율을 추적한다.
  - 자동 캠페인과 수동 캠페인을 같은 기간에 병행 비교하되, Haus 결과처럼 중간 시점이 아니라 종료 시점까지 본다.
- 한국 플랫폼(네이버, 쿠팡, 카카오)은 정량 성과를 공개하지 않고, 독립 검증도 사실상 없다. 셀러가 직접 측정해야 할 몫이 글로벌 플랫폼보다 크다.

### Gaps
- SMB 대상 AI 마케팅 도입과 ROI 설문(Salesforce, HubSpot, McKinsey, eMarketer, 중기부, 소진공, 대한상의, KISDI 등)을 확보하지 못했다(검색 한도 소진).
- Google PMax·Demand Gen의 최신 공식 성과 주장과 독립 증분 연구(Haus의 PMax 브랜드어 분석 세부 포함)를 확보하지 못했다.
- 한국 플랫폼(네이버 ADVoost, 쿠팡 AI 광고, 카카오)에 대한 독립 증분 실험이나 학술 연구를 찾지 못했다.
- Meta의 Advantage+ 공식 주장 원문(수치 상충 해소)과 Haus 보고서 발표일을 확인하지 못했다.
- AI CRM(Klaviyo, Braze, Attentive, 국내 툴)의 재구매·LTV 개선에 대한 독립 검증을 찾지 못했다.
