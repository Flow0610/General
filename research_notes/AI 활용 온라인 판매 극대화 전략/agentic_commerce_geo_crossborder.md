# AI 쇼핑 에이전트·에이전틱 커머스, GEO/AEO, AI 기반 해외판매 — 한국 온라인 셀러 관점 리서치 노트 (기준일 2026-09-27)

> **조사 방법·신뢰도 표기 (보고서 작성자 필독)**
> - 이번 세션에서 WebSearch 33회 수행 후 세션 전체 검색 한도(200회, 병렬 리서처 공유)가 소진됐고, WebFetch는 egress 정책으로 거의 모든 도메인(openai.com, blog.google, cnbc.com, 국내 언론사 등)이 차단됐다. 따라서 대부분의 항목은 **검색엔진 결과 요약(원문 미열람)**에 근거한다. 요약 과정에서 날짜·수치가 뒤섞였을 수 있으니 핵심 수치는 가능하면 재확인할 것.
> - 원문을 직접 읽은 1차 자료: (1) Adobe Digital Insights "Q3 AI Traffic Trends Report"(2026-06, PDF 53쪽, S3 미러), (2) ACP GitHub 저장소(README·changelog·RFC·JSON Schema, HEAD 커밋 2026-07-17), (3) UCP GitHub 저장소 release/2026-08-25 브랜치(announcements·roadmap·glossary, 최종 커밋 2026-09-21), (4) AP2 저장소 README, (5) llms.txt 제안서 v2(2026-08-10 수정), (6) Princeton GEO 논문 저장소 README.
> - 표기: **[원문확인]** = 1차 문서 직접 확인 / **[검색요약]** = 검색 결과 요약만 확인 / **[벤더·자체발표]** = 이해관계자 발표 / **[독립]** = 제3자 조사 / **[2차]** = 대행사·블로그 등 2차 출처.
> - (d) 해외판매(역직구·크로스보더) 질문은 검색 한도 소진으로 **거의 조사하지 못했다**. 5번 섹션의 Gaps를 참고해 후속 조사 필요.

## 1. 글로벌 에이전틱 커머스 현황(2026-09): ChatGPT·Google·Perplexity·Amazon·Microsoft·Walmart/Shopify — 프로토콜, 머천트 프로그램, 요건·수수료·자격(비미국·한국 셀러 포함)

### Takeaway
2025년 하반기에 "AI 대화창 안에서 바로 결제"가 대대적으로 발표됐지만, 2026년 9월 현재 실제로 자리 잡은 패턴은 **"AI에서 발견 → 셀러 자체 결제(사이트·앱)"**이다. OpenAI는 Instant Checkout을 2026년 3월 사실상 접고 상품 피드·광고·머천트 앱으로 방향을 바꿨다. 반면 Google(UCP·Universal Cart·AP2), Microsoft(Copilot Checkout), Perplexity(PayPal Instant Buy), Amazon(Alexa for Shopping/Buy for Me)은 에이전틱 결제를 계속 넓히고 있다. 다만 거의 모두 **미국 한정**(Google은 CA·AU 다음 UK 예정)이고, 한국 사업자가 한국 법인·한국 스토어로 직접 참여할 수 있는 경로는 확인하지 못했다. 현재 에이전트 전용 추가 수수료는 대체로 없다. 수익화는 광고(ChatGPT Ads 등) 쪽으로 옮겨 가고 있다.

### Cited Findings

**OpenAI / ChatGPT: Instant Checkout의 부침**
- 2025-09-29 Instant Checkout과 Agentic Commerce Protocol(ACP)을 출시했다. 미국 Etsy 셀러부터 시작했고 Shopify 머천트(Glossier, SKIMS, Spanx, Vuori 등 100만+)는 "곧 합류" 예정이었다. Stripe가 결제 인프라를 맡았다. [벤더·자체발표][검색요약] — [OpenAI](https://openai.com/index/buy-it-in-chatgpt/); [Stripe newsroom](https://stripe.com/newsroom/news/stripe-openai-instant-checkout)
- ACP 스펙 최초 버전 날짜는 2025-09-29이다. 이후 2025-12-12(fulfillment), 2026-01-16(capability negotiation), 2026-01-30(extensions·discounts·payment handlers), 2026-04-17(cart·feed·orders·authentication·MCP) 버전이 나왔다. 현재 상태는 "beta"이며 OpenAI·Stripe가 공동 관리한다. [원문확인] — [ACP GitHub](https://github.com/agentic-commerce-protocol/agentic-commerce-protocol)
- ACP 저장소의 미출시 changelog와 MAINTAINERS.md에 **Meta가 lead maintainer이자 TSC 3번째 석**으로 추가돼 있다("merchants worldwide" 참여 지원 목적). 저장소 HEAD는 2026-07-17이며, 공식 발표 여부는 확인하지 못했다. [원문확인] — [ACP GitHub](https://github.com/agentic-commerce-protocol/agentic-commerce-protocol)
- 수수료: Shopify 머천트는 ChatGPT Checkout 매출의 **4%**를 OpenAI에 낸다(상품가+배송비+세금 기준). 첫 적격 주문 후 30일 무료 체험이 있고, Shopify 자체 수수료와 별도이며, opt-in 방식이다. 같은 기사에 "Google AI Mode/Gemini와 Microsoft Copilot은 AI 경유 구매에 추가 수수료가 없다"는 비교가 실렸다. 2026년 초 보도이며, Instant Checkout 종료로 현재는 **역사적 참고치**다. [검색요약] — [PYMNTS 2026](https://www.pymnts.com/news/ecommerce/2026/shopify-merchants-to-pay-4percent-fee-on-sales-made-through-chatgpt-checkout/)
- Walmart는 2025년 10월 ChatGPT Instant Checkout 제휴를 발표했다. [검색요약] — [eMarketer](https://www.emarketer.com/content/walmart-openai-partnership-chatgpt-instant-commerce)
- 채택 부진: 2026년 2월 기준 Instant Checkout으로 실제 판매 가능한 Shopify 머천트가 "약 30곳"에 그쳤다는 보도가 있다. [2차·벤더 블로그, 미검증] — [Laioutr](https://www.laioutr.com/en/blog/chatgpt-instant-checkout-merchant-adoption-agentic-readiness-2026)
- Walmart 측정치로, ChatGPT 내부 결제의 전환율은 Walmart.com 클릭아웃보다 **약 3배 낮았다**. 반면 ChatGPT가 데려온 신규고객 비율은 검색엔진 대비 약 2배였다. [2차, Walmart 원 발언 미확인] — [Hypotenuse AI](https://www.hypotenuse.ai/blog/chatgpts-instant-checkout-the-next-phase-of-agentic-commerce); [Digital Applied](https://www.digitalapplied.com/blog/ai-agentic-commerce-discover-in-ai-buy-on-site-2026)
- 2026년 3월 OpenAI는 Instant Checkout을 무기한 중단했다. OpenAI 입장: "initial version of Instant Checkout did not offer the level of flexibility that we aspire to provide, so we're allowing merchants to use their own checkout experiences while we focus our efforts on product discovery." [검색요약] — [CNBC 2026-03-24](https://www.cnbc.com/2026/03/24/openai-revamps-shopping-experience-in-chatgpt-after-instant-checkout.html); [CNBC 2026-03-20](https://www.cnbc.com/2026/03/20/open-ai-agentic-shopping-etsy-shopify-walmart-amazon.html); [Forrester](https://www.forrester.com/blogs/what-it-means-that-the-leader-in-agentic-commerce-just-pulled-back/); [Agentic Commerce Feed 2026-03-16](https://www.agenticcommercefeed.com/blog/2026-03-16-openai-kills-instant-checkout); [Modern Retail](https://www.modernretail.co/technology/what-went-wrong-with-chatgpts-instant-checkout/)
- 전환 이후 모델은 두 갈래다. (a) **상품 피드**가 ChatGPT 노출을 좌우한다. (b) 구매는 개별 **머천트 앱**(Instacart, Target, Expedia, Booking.com 등)이나 머천트 사이트에서 일어난다. 앱은 선택 사항이며 통제권을 원하는 대형 머천트에 적합하다. OpenAI는 셀프서브 머천트 플랫폼을 "2026년 하반기"에 내놓을 계획이다. [검색요약] — [Exploding Topics](https://explodingtopics.com/blog/agentic-commerce-protocol); [chatgpt.com/merchants](https://chatgpt.com/merchants/)
- 상품 피드 요건: CSV·TSV·XML·JSON 형식을 받고, 최대 15분 간격으로 갱신할 수 있다. chatgpt.com/merchants에서 신청한다. **Shopify·Etsy 판매자는 카탈로그가 이미 연동돼 있어 별도 신청이 필요 없다.** 쇼핑은 **미국 사용자 대상**으로 운영 중이며, 머천트·지역 확대는 "over time"으로만 언급됐다. [검색요약] — [chatgpt.com/merchants](https://chatgpt.com/merchants/); [Lengow](https://www.lengow.com/get-to-know-more/chatgpt-product-feed/); [OpenAI Help Center](https://help.openai.com/en/articles/11128490-shopping-with-chatgpt-search)
- ChatGPT "shopping research"는 쇼핑 질의에 대해 상위 선택지와 핵심 차이, 구매 고려사항을 담은 심층 가이드를 만들어 준다. [2차] — [WPConsults](https://www.wpconsults.com/chatgpt-shopping-research/); [Profound blog(제목만 확인)](https://www.tryprofound.com/blog/chatgpt-shopping-deep-dive)
- **ChatGPT Ads 일정**:
  - 2026-02-09 미국 출시, 2026년 3월 캐나다·호주·뉴질랜드로 확대. Free·Go 요금제 사용자에게만 상업적 의도 답변 아래 sponsored card로 노출되며, 다음 확대 대상은 브라질·멕시코.
  - 2026-05-05 최소 집행액 폐지, 2026-06-02 Ads Manager에 Feeds 섹션 신설. Google Merchant Center와 같은 형식의 피드를 그대로 받는다.
  - 입찰은 CPC와 CPM 모두 가능하다. "권장 시작 CPC $3~5", "기본 최대 CPM $60, 일부 $25에 낙찰" 수치는 대행사 관찰치다.
  - 2026-09-16 광고에서 광고주 에이전트와 대화로 이어지는 **Sponsored Agents**를 미국에서 테스트 시작. 미국 Shopify 머천트용 ChatGPT Ads 앱도 나왔다.
  - [2차·대행사 출처, 수치 미검증] — [Passionfruit](https://www.getpassionfruit.com/blog/chatgpt-product-feed-ads-what-retailers-need-to-know); [ai.nl](https://www.ai.nl/en/advertising-in-chatgpt); [Digiday](https://digiday.com/marketing/openai-makes-it-easier-to-run-shopping-ads-in-chatgpt/); [Novadata](https://novadata.io/resources/news/chatgpt-ads-manager-product-feeds-june-2026); [Digital Applied](https://www.digitalapplied.com/blog/chatgpt-sponsored-agents-shopify-app-what-changes); [ARWriter](https://arwriterai.com/en/blog/openai-sponsored-agents-chatgpt-ads-2026/)
- 2026-02-16 기사에 따르면 OpenAI는 Instacart 연동(레시피에서 장보기 결제까지)으로 식료품 영역을 넓혔고, PayPal ACP 서버가 2026년 "수천만 소상공인"을 연결할 예정이라고 했다. 이는 **벤더 전망**이다. 같은 요약은 "Buy it in ChatGPT가 2026-02-16 출시"라고 적었는데, 2025-09-29 출시와 **충돌하므로 오류로 보인다**. [검색요약] — [Digital Commerce 360](https://www.digitalcommerce360.com/2026/02/16/openai-expands-agentic-commerce-push/)

**Google: AI Mode·Gemini·UCP·Universal Cart·AP2**
- UCP(Universal Commerce Protocol)는 2026년 1월 발표된 에이전틱 커머스 개방 표준이다(GitHub 첫 릴리스 v2026-01-11). Shopify, Etsy, Wayfair, Target, Walmart와 공동 개발했고 Adyen, AmEx, Best Buy, Flipkart, Macy's, Mastercard, Stripe, Home Depot, Visa, Zalando 등 20+ 곳이 지지한다. 할인코드, 로열티, 구독, Google Pay 결제를 다룬다. [벤더·자체발표][검색요약] — [Google blog](https://blog.google/products/ads-commerce/agentic-commerce-ai-tools-protocol-retailers-platforms/); [Google Developers Blog](https://developers.googleblog.com/under-the-hood-universal-commerce-protocol-ucp/); [Semrush 해설](https://www.semrush.com/blog/universal-commerce-protocol/)
- UCP 결제(AI Mode·Gemini 상품 목록의 checkout 버튼) 요건은 두 가지다. 활성 **Google Merchant Center 계정**과 **checkout 적격 상품**이 있어야 한다. 현재는 **"eligible U.S.-based merchants"만** 대상이며 "2026년 중 글로벌 확대 계획"이 있다. [검색요약] — [Merchant Center Help: About UCP](https://support.google.com/merchants/answer/16837055?hl=en); [UCP 온보딩](https://support.google.com/merchants/answer/16992327?hl=en); [Google for Developers UCP 가이드](https://developers.google.com/merchant/ucp/guides)
- 2026년 3월 UCP 업데이트로 여러 상품을 한 번에 담는 cart와, 실시간 가격·재고를 읽는 카탈로그 접근이 추가됐다. [검색요약] — [Google blog: UCP updates](https://blog.google/products-and-platforms/products/shopping/ucp-updates/)
- 미국 적격 리테일러는 Merchant Center에서 브랜드 에이전트를 켜고 커스터마이즈할 수 있다. 자사 데이터 학습, 고객 인사이트, 연관상품 제안, 에이전틱 체크아웃은 "coming months"로 예고됐다. [검색요약] — [Talon.One](https://www.talon.one/blog/google-ai-shopping-assistant); [Google blog](https://blog.google/products/ads-commerce/agentic-commerce-ai-tools-protocol-retailers-platforms/)
- **Google I/O(2026-05-19)** 발표 내용:
  - **Universal Cart**: Search·Gemini·YouTube·Gmail을 가로지르는 통합 장바구니로, 가격 인하·재입고를 자동 추적한다.
  - UCP 결제를 **캐나다·호주로 "coming months" 확대, 이후 영국**.
  - 미국 YouTube에 UCP 적용, 호텔·음식배달 버티컬 추가.
  - Merchant Center 신규 속성 스키마 **"Conversational Attributes"**.
  - [벤더·자체발표][검색요약] — [Google blog: Universal Cart](https://blog.google/products-and-platforms/products/shopping/google-shopping-cart/); [Search Engine Journal](https://www.searchenginejournal.com/google-announces-new-universal-cart-at-i-o/575301/); [Digital Commerce 360 2026-05-20](https://www.digitalcommerce360.com/2026/05/20/google-universal-cart-for-agentic-commerce/); [eMarketer](https://www.emarketer.com/content/google-expands-push-agentic-shopping-with-universal-cart); [Azoma](https://www.azoma.ai/insights/google-i-o-2026-what-the-agentic-commerce-announcements-mean-for-brands)
- **UCP 거버넌스와 버전** [원문확인]:
  - 프로토콜 릴리스: v2026-01-11, v2026-01-23, v2026-04-08. release/2026-08-25 브랜치도 존재한다(릴리스 노트는 미확인).
  - 2026-04-24 Tech Council을 16석으로 늘리며 Amazon, Meta, Microsoft, Stripe, Salesforce 인사를 영입했다.
  - 2026-04-28 Stripe가 Governing Council에 합류했다(상임은 Google·Shopify).
  - 로드맵에는 인도·인도네시아·중남미 등으로의 단계적 확대, 로열티, 교차·상향 판매, 음식·숙박 버티컬이 있다. **한국은 언급이 없다.**
  - 용어집은 "Business = Merchant of Record, retaining financial liability and ownership of the order"로 정의한다.
  - 출처: [UCP GitHub](https://github.com/Universal-Commerce-Protocol/ucp)
- AP2(Agent Payments Protocol)는 2025-09-16 60+ 파트너(Mastercard, PayPal, Coinbase, AmEx, Salesforce 등)와 함께 발표됐다. 2026년 4월 v0.2를 내고 **FIDO Alliance에 기증**했으며, FIDO는 Agentic Authentication TWG와 Payments TWG(Mastercard·Visa 공동의장)를 신설했다. I/O 2026에서 AP2 통제 기능을 갖춘 첫 제품 "Gemini Spark"를 발표했다. AP2는 브랜드·상품·지출 한도를 정해 두고 조건이 맞을 때만 구매하는 가드레일을 제공한다. [검색요약·2차] — [Google blog: AP2 → FIDO](https://blog.google/products-and-platforms/platforms/google-pay/agent-payments-protocol-fido-alliance/); [The Next Web](https://thenextweb.com/news/google-universal-cart-agent-payments-shopping-io-2026); [Eco(2차)](https://eco.com/support/en/articles/15192002-ap2-protocol-explained-google-s-agentic-commerce-standard-2026). AP2 저장소 README는 ADK와 Gemini 기반 샘플을 제공하며 "AP2는 둘 다 요구하지 않는다"고 명시한다. [원문확인] — [AP2 GitHub](https://github.com/google-agentic-commerce/AP2)
- UCP 문서는 UCP가 AP2와 완전 호환이라고 밝힌다. 판매자는 checkout 상태에 서명한 checkoutSignature(JWT)를 발급하고, 결제 mandate는 checkout 해시에 묶여 토큰 재사용이나 금액 조작을 막는다. [원문확인] — [UCP GitHub docs/ucp-and-ap2](https://github.com/Universal-Commerce-Protocol/ucp)
- 한국: Google AI 모드는 **2025-09-08부터 한국어로 순차 제공**됐다. 수십억 개 상품의 쇼핑 데이터를 활용한다. UCP 결제나 에이전틱 체크아웃의 한국 제공 발표는 찾지 못했다. 일부 국내 블로그가 "AI 모드에서 검색→비교→결제 완료"라고 쓰지만 미국 기능 설명을 옮긴 것으로 보인다. [검색요약] — [Google 코리아 블로그](https://blog.google/intl/ko-kr/products/explore-get-answers/ai-mode-in-korean/); [AI포스트](https://www.aipostkorea.com/news/articleView.html?idxno=9372); [designcompass 2025-09-12](https://designcompass.org/en/2025/09/12/google-ai-mode/)

**Microsoft Copilot**
- 2025-04-18 Copilot Merchant Program을 시작했다. [벤더·자체발표] — [Microsoft Copilot Blog](https://www.microsoft.com/en-us/microsoft-copilot/blog/2025/04/18/introducing-the-copilot-merchant-program/)
- 2026-01-08 **Copilot Checkout**을 출시했다. PayPal, Shopify, Stripe와 함께하며 **머천트가 Merchant of Record를 유지**한다. 온보딩 방식은 다음과 같다.
  - Shopify 머천트는 **자동 등록**되고 Shopify admin에서 제어한다.
  - PayPal·Stripe 머천트는 신청해서 합류한다.
  - 출시 파트너는 Urban Outfitters, Anthropologie, Ashley Furniture, 일부 Etsy 셀러다. 함께 발표된 Brand Agents는 브랜드 자체 대화형 에이전트다.
  - [검색요약] — [Microsoft Source 2026-01-08](https://news.microsoft.com/source/2026/01/08/microsoft-propels-retail-forward-with-agentic-ai-capabilities-that-power-intelligent-automation-for-every-retail-function/); [Microsoft Advertising blog](https://about.ads.microsoft.com/en/blog/post/january-2026/conversations-that-convert-copilot-checkout-and-brand-agents); [gHacks 2026-01-09](https://www.ghacks.net/2026/01/09/microsoft-and-paypal-launch-copilot-checkout-for-in-chat-purchases/); [ALM Corp](https://almcorp.com/blog/microsoft-copilot-checkout-brand-agents-guide/)
- 이후 Copilot Checkout은 **50만+ 머천트**로 확대되고 모바일 앱 체크아웃이 추가됐다(기사 날짜 미확인). [검색요약] — [Windows Central](https://www.windowscentral.com/microsoft/windows-11/copilots-shopping-upgrade-brings-checkout-to-the-mobile-app-with-deeper-data-from-half-a-million-merchants)

**Perplexity**
- 2025년 11월 PayPal과 **Instant Buy**를 출시했다. 미국 사용자가 대상이고 PayPal 신원확인과 구매자·판매자 보호가 적용된다. 초기 머천트는 Abercrombie & Fitch, Ashley Furniture, Fabletics, Adorama, Newegg이며, PayPal 머천트가 Perplexity에서 발견 가능해진다. 2026년 초 카탈로그 연결 강화와 카테고리 확대를 예고했다. [벤더·자체발표][검색요약] — [PayPal Newsroom](https://newsroom.paypal-corp.com/2025-11-PayPal-and-Perplexity-Launch-Instant-Buy); [PYMNTS](https://www.pymnts.com/news/artificial-intelligence/2025/paypal-and-perplexity-debut-instant-buy-ahead-of-black-friday-shopping/); [Perplexity Help Center](https://www.perplexity.ai/help-center/en/articles/12932923-instant-buy-buy-with-paypal)
- Perplexity는 미국 사용자에게 무료 AI 쇼핑을 제공한다(날짜 미확인). [검색요약] — [Yahoo Tech](https://tech.yahoo.com/ai/perplexity-ai/articles/perplexity-rolls-free-ai-shopping-093700080.html)
- 2026-01-22 PayPal이 Cymbio를 인수했다. Cymbio는 드롭십·커머스 자동화 업체로, 브랜드 카탈로그를 Copilot·Perplexity 등 여러 AI 채널에 한 번에 동기화한다. [2차] — [SecNews](https://www.secnews.gr/en/725171/paypal-perplexity-instant-buy-agentic-commerce-2026/)

**Amazon**
- **2026-05-13 미국에서 Rufus가 "Alexa for Shopping"으로 개편**돼 Alexa+와 통합됐다. 특징은 다음과 같다.
  - 로그인한 모든 미국 고객에게 앱·웹 기본으로 제공되며 Prime이나 Echo가 필요 없다.
  - 가격 추적 자동구매와 예약 실행(Scheduled Actions)을 지원한다.
  - **Buy for Me**로 아마존 밖 타사 사이트에서도 대신 구매한다.
  - [검색요약] — [CNBC 2026-05-13](https://www.cnbc.com/2026/05/13/amazon-ditches-rufus-ai-chatbot-in-favor-of-alexa-shopping-agent.html); [GeekWire](https://www.geekwire.com/2026/amazon-unifies-alexa-and-rufus-as-ai-rivals-move-into-online-shopping/); [Canopy Management](https://canopymanagement.com/amazon-alexa-for-shopping-sellers-guide/); [Amalytix](https://www.amalytix.com/en/knowledge/ai/amazon-rufus-guide-2026/); [Flipflow](https://www.flipflow.io/en/blog-en/amazon-launches-alexa-for-shopping/)

**Walmart / Target / Shopify**
- 2026-01-11 Walmart와 Google Gemini가 제휴했다. Gemini 답변에 Walmart·Sam's Club 상품이 나오고, 결제는 **Walmart 자체 결제 환경**에서 이뤄진다. [검색요약] — [CNBC 2026-01-11](https://www.cnbc.com/2026/01/11/walmart-partners-with-google-gemini-on-shopping-tool.html); [Retail Dive](https://www.retaildive.com/news/walmart-google-gemini-ai-assisted-shopping/809307/); [Retail Brew](https://www.retailbrew.com/stories/2026/01/15/what-does-walmart-s-agentic-ai-partnership-with-google-mean-for-online-shopping)
- Walmart는 OpenAI Instant Checkout 파일럿을 끝내고 **자체 쇼핑 에이전트 Sparky를 Gemini와 ChatGPT에 탑재**하는 쪽으로 전환했다. [2차] — [MLQ](https://mlq.ai/news/walmart-shifts-to-self-developed-ai-shopping-in-gemini-after-ending-openai-partnership/)
- Target은 ChatGPT 머천트 앱으로 들어가 있다. [검색요약] — [Exploding Topics](https://explodingtopics.com/blog/agentic-commerce-protocol)
- Shopify의 위치: ChatGPT 상품 발견에 카탈로그가 자동 연동되고, Copilot Checkout에 자동 등록되며, UCP 공동개발사이자 Governing Council 상임 멤버다. 위 인용 출처들을 종합한 결과다.

### Inferences
- **소규모 셀러에게 실제로 열린 문**은 네 가지다. 모두 미국 소비자 대상이다.
  - (1) Shopify나 Etsy에 상점을 두면 ChatGPT 상품 발견과 Copilot Checkout 노출이 자동이다.
  - (2) Google Merchant Center 무료 리스팅 품질을 관리한다. UCP 결제는 미국 사업자 한정이다.
  - (3) PayPal 머천트 경로로 Perplexity에 노출될 수 있다.
  - (4) Amazon US 입점 셀러는 Alexa for Shopping 추천 로직에 자동으로 편입된다.
- 한국 법인·한국 결제로 운영하는 네이버·쿠팡·카페24 상점은 이 프로그램들의 직접 대상이 아니다. 비미국 사업자의 자격 조건은 공식 문서로 확인하지 못했다(Gaps).
- **수수료 구조의 방향**: 에이전트 전용 수수료는 OpenAI 4% 이후 확산되지 않았다. Google과 Microsoft는 추가 수수료가 없다고 보도됐고, 네이버도 추가 수수료가 없다(2번 섹션). 대신 ChatGPT Ads와 Sponsored Agents처럼 **광고 기반 유료 노출**로 수익화가 이동하고 있다. 중기적으로는 "오가닉 추천 + 유료 노출" 구조를 전제로 예산을 계획하는 편이 합리적이다.
- **"AI에서 발견, 자사에서 결제"가 당분간 기본값이다.** Instant Checkout 실패와 Walmart가 자체 에이전트로 옮겨 간 사례를 보면, 결제·고객데이터 통제를 포기하는 모델은 대형 머천트도 받아들이지 않았다. 셀러에게 당장 급한 것은 결제 연동보다 **피드 품질, 상품 정보의 기계 판독성, 랜딩 전환율**이다.
- 프로토콜은 ACP(OpenAI·Stripe·Meta), UCP(Google·Shopify·Stripe, Amazon·Meta·MS·Salesforce 참여), AP2(→FIDO)로 나뉘어 있다. 그러나 Stripe와 Meta가 양쪽에 모두 들어가 있어 **수렴 신호**가 보인다. 한국 중소 셀러가 프로토콜을 직접 구현할 필요는 거의 없고, Shopify·Stripe·PayPal 같은 플랫폼 레이어가 이를 흡수할 것으로 보인다.

### Gaps
- 한국에 등록된 Shopify 스토어나 한국 사업자 PayPal·Stripe 계정이 ChatGPT 상품 피드, Copilot Checkout, Perplexity Instant Buy, Google UCP 결제 대상인지 공식 문서로 확인하지 못했다(원문 접근 차단).
- Amazon Rufus/Alexa for Shopping의 이용자 수와 매출 기여도(Amazon 실적발표 수치)를 확보하지 못했다.
- Google Merchant Center "Conversational Attributes"의 구체 필드와 checkout 적격 속성(예: 반품정책·배송 요건)의 세부 목록, Google의 UCP 결제 수수료 공식 문구를 확인하지 못했다.
- Stripe Agentic Commerce Suite 요금, Shopify의 비Shopify 브랜드용 에이전틱 플랜, Visa Intelligent Commerce와 Mastercard Agent Pay의 2026년 현황을 조사하지 못했다.
- ChatGPT Ads의 CPC·CPM 수치는 대행사 관찰치이며 OpenAI 공식 단가는 확인하지 못했다.

## 2. 한국: 네이버·카카오·쿠팡·11번가·G마켓의 AI 쇼핑 에이전트 — 상품 노출 방식 변화와 셀러 대응

### Takeaway
2026년 한국 커머스 플랫폼은 모두 "대화형 탐색·비교·요약 → (연내~2027 초) 에이전트 내 결제"로 가고 있다. 네이버는 2026-02 네이버플러스 스토어에 '쇼핑 AI 에이전트' 베타를 냈고, 연내 일부 상품군에서 에이전트 내 결제를 시범 적용할 예정이다. 광고는 없고 추가 수수료도 없으며, 판매자 서비스 품질(주문이행·배송·CS)이 추천에 반영된다. 카카오는 ChatGPT for Kakao(약 800만 명)와 카나나의 A2A 연동으로 파트너 에이전트를 붙이는 방식이다. 쿠팡은 수억 개 상품 데이터를 AI가 읽을 수 있는 구조로 다시 짰다. 결국 셀러 경쟁력의 축은 **"키워드 광고·상품명 최적화"에서 "구조화된 속성·리뷰·배송·CS 품질 데이터"로** 옮겨 가고 있다.

### Cited Findings

**네이버(네이버플러스 스토어)**
- 2026-02-26 네이버플러스 스토어 앱에 **'쇼핑 AI 에이전트' 베타**를 출시했다(결제는 아직 미지원). 쇼핑 키워드를 넣으면 탐색 가이드를 제시하고 상품 정보 요약, 비교, 리뷰 분석을 해 준다. 개인 쇼핑 이력을 분석해 예컨대 '소파'라면 인원·공간·소재별 구매 팁과 적합 브랜드를 알려 준다. 베타 1.0은 디지털·리빙·생활 중심이며 상반기 중 뷰티·식품으로 넓힐 계획이었다. [벤더·자체발표][검색요약] — [네이버 보도자료](https://navercorp.com/media/pressReleasesDetail?seq=34353); [네이트/뉴스 2026-02-26](https://m.news.nate.com/view/20260226n32167); [나스미디어 블로그](https://blog.nasmedia.co.kr/entry/2603mediaissue-naveraiagent); [네이트 2026-02-26 체험기](https://m.news.nate.com/view/20260226n37405)
- **현재 쇼핑 에이전트에는 광고 상품이 노출되지 않는다.** 에이전트를 통한 판매에는 **일반 스마트스토어 판매수수료만 적용되고 추가 수수료는 없다.** 네이버 책임리더는 "탐색 과정에서 소비자의 노동을 쇼핑 지면 내에서 얼마나 감소시킬 수 있을지가 출발점"이라고 말했다. [검색요약] — [바이라인네트워크 2026-03-15](https://byline.network/2026/03/15_19298383/)
- 네이버는 **주문이행, 배송품질, CS만족도 등 판매자의 서비스 품질 데이터를 입체적으로 알고리즘에 반영**해 추천의 공정성과 투명성을 관리한다고 밝혔다. [벤더·자체발표][검색요약, 기사 특정 불확실] — [바이라인네트워크](https://byline.network/2026/03/15_19298383/); [블로터](https://www.bloter.net/news/articleView.html?idxno=662604)
- 2026년 8월 기준, 에이전트는 사용자에게 먼저 대화를 제안하는 방향으로 업데이트됐다. 기사는 네이버 커머스가 "AI가 제안하고 여기서 사는" 구조로 바뀌는 중이며 **"이미 앱 거래액의 절반이 AI 추천을 경유"**한다고 전했다. [자체발표 추정, 정의 불명확] — [Daum 게재 기사 '[쇼핑AI 上]' 2026-08-17(언론사 미확인)](https://v.daum.net/v/20260817130257886); [네이트](https://m.news.nate.com/view/20260817n07242)
- 사용자 주소지 기준으로 원하는 날짜에 도착 가능한 상품을 추천하는 **배송 특화 기능**이 추가됐다. [검색요약] — [MSN](https://www.msn.com/ko-kr/news/other/%EB%84%A4%EC%9D%B4%EB%B2%84-%EC%87%BC%ED%95%91%EC%95%B1-ai-%EC%87%BC%ED%95%91-%EC%97%90%EC%9D%B4%EC%A0%84%ED%8A%B8-%EB%B0%B0%EC%86%A1-%ED%8A%B9%ED%99%94-%EA%B8%B0%EB%8A%A5-%EA%B3%A0%EB%8F%84%ED%99%94/ar-AA2couyE)
- **2026-09-27 보도**: 네이버는 AI 쇼핑 에이전트 안에서 추천부터 결제까지 가능한 기능을 **연내 일부 상품군에 시범 적용**할 예정이다. 2026-09-17에는 쇼핑·지도로 '에이전트'를 넓혀 검색을 넘어 구매·예약까지 하겠다고 했다. [검색요약] — [파이낸셜뉴스 2026-09-27](https://www.fnnews.com/news/202609270633124595); [브릿지경제 2026-09-27](https://www.viva100.com/article/20260927500328); [네이트 2026-09-17](https://m.news.nate.com/view/20260917n17934)
- 머니투데이 단독(2026-09-21)은 "내년 설(2027년 2월) 쇼핑은 AI 대전"이라며 네이버와 다음의 AI 쇼핑결제 일정을 보도했다. **다음(Daum)은 결제 파트너와 수익 모델을 아직 정하지 않았고, 2027년 초 베타에서 검색·비교·구매 연결 경험을 먼저 검증할 전망**이다. [검색요약] — [머니투데이](https://www.mt.co.kr/tech/2026/09/21/2026092109174890300); [네이트 전재](https://m.news.nate.com/view/20260921n14503)
- 관련 해설로는 네이버 커머스 2026 전략(2차) — [슈퍼레이블](https://super-label.com/blog/naver-commerce-strategy-2026), 그리고 AI 쇼핑 에이전트 시대 전문몰 생존 전략(의견) — [모비인사이드 2026-05-06](https://www.mobiinside.co.kr/2026/05/06/ai-shoppingmall/)이 있다.

**카카오(카카오톡·ChatGPT for Kakao·카나나)**
- **2025-10-28 'ChatGPT for Kakao'**를 출시했다. 카카오톡 안에서 ChatGPT를 쓰고, Kakao Tools로 카카오맵, 예약하기, **카카오톡 선물하기**, 멜론을 자동 연결한다. [벤더·자체발표] — [카카오 공식](https://www.kakaocorp.com/page/detail/11780); [바이라인네트워크 2025-10-28](https://byline.network/2025/10/28-544/)
- 2026-03-24 보도: 카톡 ChatGPT에서 **올리브영·무신사** 쇼핑이 가능해졌다. [검색요약] — [네이트](https://news.nate.com/view/20260324n37195)
- 2026-09-11 보도: ChatGPT for Kakao 이용자는 **약 800만 명**으로 알려졌다('알려졌다' 수준, 공식 여부 미확인). Kakao Tools 연동 서비스는 **28개**이며, 이번에 다이소몰, 룩스루, 스페이스클라우드, 신세계면세점, 신한카드, LF몰, 청연 7곳을 더해 상품·카드 추천을 시작했다. [검색요약] — [아시아경제 2026-09-11](https://view.asiae.co.kr/article/2026091110363804383)
- 2026-05-07 보도: 카카오는 "검색부터 결제까지 카톡 안에서" 처리하는 AI 에이전트를 예고했다. 주요 버티컬과 협력한 엔드투엔드 프로액티브 에이전트를 준비 중이며, 음식배달부터 시작해 커머스·예약·여행으로 넓힌다. [검색요약] — [MTN](https://news.mtn.co.kr/news-detail/2026050711360865784); [파이낸셜포스트](https://www.financialpost.co.kr/news/articleView.html?idxno=275191)
- 2026-08-06: **'카나나 인 카카오톡'의 첫 외부 에이전트 간 연동(A2A) 파트너로 쿠팡이츠**를 선정했다. AI 에이전트로 주문·결제까지 하는 방향이다. [검색요약] — [더빅데이터](https://www.thebigdata.co.kr/view.php?ud=202608061337554175bbceadc3c9_23); [Daum 2026-08-17](https://v.daum.net/v/20260817130257886); [시사저널e](https://www.sisajournal-e.com/news/articleView.html?idxno=422823)
- 선물하기에서 판매한 'ChatGPT Pro 1개월 이용권' 2만9000원이 2026년 2월 3일 만에 소진됐다. 카카오는 이후 비공식 경로 등록을 제한했다. 플랫폼 간 결합 프로모션 사례다. [검색요약] — [한국경제 2026-02-13](https://www.hankyung.com/article/202602134325g); [전자신문 2026-02-19](https://www.etnews.com/20260219000287)

**쿠팡**
- 2026-08-07 쿠팡은 AI로 탐색→비교→구매 결정을 다시 설계했다고 발표했다. 올해 AI 상품 비교, 상품 한눈에 보기, AI 인포그래픽 등 **5개+ AI 기능**을 적용했다. 가전 로켓배송 상품은 화면 크기·소비전력 같은 사양을 AI가 이미지·도표로 바꿔 보여 준다. 리뷰 요약 기능 '고객들은 이렇게 리뷰했어요'도 운영한다. [벤더·자체발표] — [쿠팡 뉴스룸](https://news.coupang.com/archives/65494/); [바이라인네트워크 2026-08-07](https://byline.network/2026/08/07_2928173/); [아시아경제](https://view.asiae.co.kr/article/2026080708430912018); [헤럴드경제](https://biz.heraldcorp.com/article/10833854); [녹색경제신문](https://www.greened.kr/news/articleView.html?idxno=347113)
- 2026-07-15 보도: 쿠팡은 **수억 개 상품의 이미지·설명·세부 속성값을 AI가 읽을 수 있는 형태로 재구조화**하고 있다. 제각각인 대표이미지, 상세설명, 규격, 재질, 용도를 일정한 형식으로 맞추는 작업이다. [검색요약] — [한국경제](https://www.hankyung.com/article/202607156887g)

**11번가 / G마켓 / 기타**
- 11번가는 AI 검색을 도입했다. 가격, 배송비, 배송속도, 리뷰를 분석해 조건에 맞는 상품 **5개 안팎**을 추천하고, '집들이 선물' 같은 일상 표현도 처리한다. 11번가에 따르면 출시 첫 달 **AI 검색 구매전환율이 기존 통합검색 대비 2배 이상**이었다. [자체발표][검색요약] — [Daum 2026-08-18](https://v.daum.net/v/20260818144548537); [뉴스1](https://www.news1.kr/industry/distribution/6261262)
- G마켓은 상품명뿐 아니라 이미지, 가격, 리뷰, 이용 경험을 분석해 숨은 의도를 파악하는 **'초개인화 AI 에이전트'**를 "내년" 출시 목표로 준비 중이다. 기사 날짜를 확인하지 못해 '내년'이 2026년인지 2027년인지 불확실하다. [검색요약] — [Daum](https://v.daum.net/v/5qJzY02uE6); [네이트 2026-07-27 'AI쇼핑 경쟁 불붙었다…쿠팡·G마켓 등 가세'](https://m.news.nate.com/view/20260727n28610)
- 네이버, 무신사, 11번가, 롯데온 등이 생성형 AI 쇼핑을 고도화하고 있다. 현대백화점과 신세계도 '제로클릭' 경쟁에 합류했다. [검색요약] — [코리아리포트](https://www.koreareport.co.kr/news/articleView.html?idxno=53101); [네이트 2026-03-15](https://m.news.nate.com/view/20260315n13660); [전자신문 2026-07-01 '플랫폼 패싱하는 에이전틱 커머스'](https://www.etnews.com/20260701000423)

### Inferences
- **노출 로직 변화 (네이버)**: 에이전트 추천은 (a) 구조화된 상품정보·스펙, (b) 리뷰 내용(요약·비교에 쓰임), (c) 판매자 서비스 지표(주문이행·배송·CS), (d) 사용자 개인화 이력을 섞는 것으로 보인다. 에이전트 지면에는 아직 광고가 없어서 **오가닉 품질 지표의 비중이 광고 지면보다 크다**.
- **1인 셀러 → 네이버 체크리스트**: 무료이고 바로 할 수 있는 것부터 정리하면 다음과 같다.
  - 상품 속성(카테고리별 필수·선택 속성)을 빠짐없이 채운다.
  - 상세페이지 핵심 정보를 이미지가 아닌 **텍스트로도** 병기한다. 4번 섹션 Adobe 판독성 결과와 같은 논리다.
  - 리뷰 수와 질을 관리한다(사용 맥락이 드러나는 리뷰 유도).
  - 도착보장이나 빠른 발송 설정, 출고 준수율, CS 응답 시간을 관리한다.
  - 함정: 이미지 위주 상세페이지는 AI가 스펙을 못 읽어 비교에서 빠질 수 있다(추론).
- **쿠팡 (윙·로켓그로스)**: 쿠팡이 상품 데이터를 표준 속성 체계로 다시 짜고 있으므로, 셀러가 등록하는 속성값(규격·재질·용도)의 정확성과 완결성이 AI 비교표·인포그래픽 노출의 전제가 된다. 로켓배송·로켓그로스 상품에 AI 기능이 먼저 적용되는 패턴(가전 로켓배송)이 보여 **로켓그로스 입고 상품이 유리할 가능성**이 있다(추론, 미검증).
- **11번가**: AI가 가격·배송비·배송속도·리뷰로 5개 안팎을 고르므로, 경쟁 단위는 표시가가 아니라 **"배송비 포함 총액 + 도착 속도"**다.
- **카카오**: 현재 에이전트 연동은 대형 파트너(쿠팡이츠, 올리브영, 무신사, 다이소몰, LF몰, 신세계면세점 등) 중심의 A2A다. 중소 셀러가 노출되는 현실적 경로는 **(1) 선물하기 입점**(Kakao Tools 기본 연동)과 **(2) 이미 연동된 대형 플랫폼(무신사·올리브영 등)에 입점하는 것**이다(추론).
- **결제 내재화의 의미**: 네이버(연내 시범), 카카오(쿠팡이츠 A2A), 다음(2027 초 베타)이 에이전트 내 결제를 붙이면, 국내에서는 미국과 달리 **"발견과 결제가 모두 플랫폼 안에서 끝나는" 모델이 표준**이 될 가능성이 크다. 자사몰로의 유입은 더 줄어들 수 있다. 네이버·쿠팡이 이미 결제·물류를 쥐고 있어서, 외부 LLM 앱 위주인 미국보다 성공 확률이 높아 보인다(추론).

### Gaps
- 네이버의 공식 판매자 가이드(에이전트 노출 요인, 스마트스토어센터 공지)와 'AI 브리핑' 쇼핑 결과 노출 기준, 연내 결제 시범 대상 상품군을 확인하지 못했다.
- "앱 거래액의 절반이 AI 추천 경유"에서 'AI 추천'의 정의(기존 개인화 추천 포함 여부)가 불명확하다.
- 카카오톡 선물하기와 톡스토어 상품이 ChatGPT for Kakao에서 어떤 기준으로 노출되는지, 중소 셀러 노출 사례가 있는지 확인하지 못했다.
- 무신사, 29CM, 에이블리, 지그재그, 오늘의집, 컬리, 롯데온의 AI 쇼핑 기능과 셀러 영향은 검색 한도 소진으로 조사하지 못했다.
- 쿠팡 AI 기능이 검색 순위와 아이템위너에 어떤 영향을 주는지, 로켓그로스와 일반 윙 상품 간 적용 차이는 확인하지 못했다.

## 3. 소비자 채택·트래픽 근거: 생성형 AI 쇼핑 이용률, AI 유입 트래픽·전환율, 에이전트의 매출 영향, 시장 전망

### Takeaway
미국 데이터 기준으로 AI 유입은 **규모는 아직 작지만(절대 비중 미공개) 빠르게 늘고, 질은 이제 다른 채널보다 높다**. Adobe 집계로 2026년 5월 미국 리테일 AI 유입은 전년 대비 +138%였고, 전환율은 비AI 대비 **+54%**, 방문당 매출은 **+53%**였다. 1년 전에는 AI 쪽이 열위였으니 방향이 뒤집힌 셈이다. 2030 시장 전망은 미국 기준 $190B~$1T로 편차가 크다. 한국 소비자는 기대(69%)는 크지만 불신(64%)도 크다.

### Cited Findings

**Adobe Analytics / Adobe Digital Insights (미국, 1조+ 리테일 방문 기반, 벤더 데이터)**
- 2025 홀리데이 시즌: 생성형 AI발 미국 리테일 트래픽은 **전년 대비 +693.4%**(11월 +769%, 12월 +673%)였다. AI 유입의 전환율은 추수감사절에 **+54%**, 블랙프라이데이에 **+38%**로 비AI보다 높았다. 체류시간 +45%, 페이지뷰 +13%, 즉시이탈 확률 -33%였고 AI 유입 방문당 매출은 +254%(시즌 누계, 정의 불명확)였다. 같은 기간 미국 온라인 홀리데이 매출은 $257.8B(+6.8%)였다. [벤더][검색요약] — [Digital Commerce 360 2026-01-13](https://www.digitalcommerce360.com/2026/01/13/generative-ai-online-holiday-shopping-traffic-2025/); [Adobe blog](https://business.adobe.com/blog/ai-driven-traffic-surges-across-industries); [Adobe blog: GenAI-powered shopping](https://business.adobe.com/blog/generative-ai-powered-shopping-rises-with-traffic-to-retail-sites)
- 2026년 1분기: AI발 미국 리테일 트래픽은 **전년 대비 +393%**(2026년 1~3월)였다. 2026년 3월 AI 유입 전환율은 비AI 대비 **+42%**로 역대 최고였는데, 2025년 3월에는 -38%였다. 참여율 +12%, 체류 +48%, 페이지 +13%였다. Adobe는 "많은 리테일 사이트가 기계가 완전히 읽을 수 없는 상태"라고 지적하며 자사 AI Content Visibility Checker(100점 척도)를 소개했다. [벤더, 이해관계 있음][검색요약] — [Adobe blog](https://business.adobe.com/blog/ai-traffic-surge-retail-sites-not-machine-readable); [Marketing Week](https://www.marketingweek.com/ai-traffic-is-surging-but-many-retail-sites-arent-readable/); [DesignRush](https://news.designrush.com/adobes-393-ai-traffic-surge-exposes-visibility-gap)
- **Adobe Q3 AI Traffic Trends Report(2026-06 발행, 2026-05 데이터)** [원문확인][벤더] — [Adobe PDF(S3 미러)](https://s3.amazonaws.com/media.mediapost.com/uploads/ADOBE_q3-2026-ai-sourced-traffic-insights.pdf); [Digital Commerce 360 2026-06-17](https://www.digitalcommerce360.com/2026/06/17/adobe-ai-referred-traffic-to-retail-sites-doubles-in-a-year/)
  - 2026년 5월 AI 유입 리테일 트래픽은 전년 대비 **+138%**로, 2024년 10월 추적 시작 이래 전체 리테일 방문 중 AI 비중이 가장 높았다. 여행 +194%, 금융 +105%였다.
  - 2026년 5월 AI 유입 전환율은 비AI보다 **54% 높았다**. 1년 전에는 AI 쪽이 비AI의 절반 수준이었다.
  - 방문당 매출(RPV)은 AI가 **+53%**로 3월(+37%)보다 올랐다. 12개월 전에는 비AI 방문이 128% 더 가치 있었다.
  - 참여율 +15%, 체류시간 +53%(4월 +55%), 페이지뷰 +23%, 이탈 가능성 -36%였다. AI 이탈률은 17~20%대, 비AI는 약 27%다.
  - 3월 설문(미국 5,000+명): **39%가 온라인 쇼핑에 AI 어시스턴트를 써 봤고**, 그중 85%는 경험이 개선됐다고 답했다. 66%가 "생성형 AI 결과가 정확하다", 38%가 "예전보다 더 신뢰한다"고 했다. 79%는 구매 확신이 커졌고 69%는 반품 가능성이 낮아졌다고 답했다. **50%가 AI가 준 링크를 클릭하고 27%는 그 링크로 구매까지 한다.** 55%는 영감·아이디어를 얻으려고 AI를 쓰며, 대개 쇼핑 시작 전이다. 54%는 AI 사용이 늘었다고, 58%는 지난주에 AI를 썼다고 답했다.
  - 세대별 AI 쇼핑 경험: Gen Z 53%, 밀레니얼 48%, Gen X·베이비부머 34%.
  - 2026년 3월 AI 유입 증가가 강했던 카테고리는 장난감, 유아용품, 의류, 반려동물, 홈&가든, 퍼스널케어 등이다.
- 참고(오래된 데이터): 2025-03 Adobe는 생성형 AI발 미국 리테일 트래픽 +1,200%를 발표했다(2024-07 대비 2025-02). — [Adobe blog 2025-03-17](https://blog.adobe.com/en/publish/2025/03/17/adobe-analytics-traffic-to-us-retail-websites-from-generative-ai-sources-jumps-1200-percent)

**Salesforce (벤더 자체 플랫폼 데이터 기반 추정. 모집단 규모는 이번 세션에서 미확인)**
- 2025 홀리데이(11/1~12/31) 온라인 매출은 글로벌 **$1.29T**(+7%), 미국 **$294B**(+4%)였다. **AI와 에이전트가 글로벌 온라인 매출의 20%, 약 $262B에 영향을 줬다.** 반품·배송조회 같은 에이전트 처리 업무는 142% 늘었다. 쇼퍼 에이전트를 도입한 브랜드의 매출 성장률은 6.2%로 미도입(3.9%)보다 59% 높았다. **AI 검색 유입 전환율은 소셜 유입의 9배**였다. 사이버위크 글로벌 매출은 $336.6B로 사상 최대였다. [벤더, "influenced" 정의가 넓음] — [Salesforce 2025 Holiday Data](https://www.salesforce.com/news/stories/2025-holiday-shopping-data/); [MarTech](https://martech.org/how-ai-agents-shaped-the-record-breaking-2025-holiday-season/); [Salesforce 2025-12-05 PR](https://www.salesforce.com/news/press-releases/2025/12/05/cyber-week-ai-agents-sales/)
- **충돌**: 2025 미국 홀리데이 온라인 매출을 Adobe는 $257.8B(+6.8%), Salesforce는 $294B(+4%)로 집계했다. 방법론 차이 때문이다.

**시장 전망 (컨설팅·IB, 독립이지만 전망치)**
- McKinsey(2025-10): 에이전틱 커머스가 2030년까지 **글로벌 $3~5T**, **미국 B2C 리테일에서 최대 $1T**의 "orchestrated" 매출을 만들 수 있다고 본다. 요약에 따르면 미국 수치는 B2C 매출의 약 30% 수준이나 미검증이다. 글로벌 수치는 B2B·물류·결제까지 포괄한다. — [Digital Commerce 360 2025-10-20](https://www.digitalcommerce360.com/2025/10/20/mckinsey-forecast-5-trillion-agentic-commerce-sales-2030/); [Retail Dive](https://www.retaildive.com/news/agentic-commerce-us-one-trillion-2030/818936/); [McKinsey](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-automation-curve-in-agentic-commerce)
- Morgan Stanley(2025-12): 2030년 미국 이커머스에서 에이전틱 쇼퍼 지출을 **$190B~$385B**(온라인 리테일의 10~20%)로 추정한다. 미국인 약 **23%가 지난 한 달간 AI로 무언가를 구매**했다고 답했고(MS 설문), 식료품·CPG가 선두다. 2030년 1억2,600만 명이 쓸 것이라는 전망은 2차 출처다. — [Morgan Stanley](https://www.morganstanley.com/insights/articles/agentic-commerce-market-impact-outlook); [Digital Commerce 360 2025-12-09](https://www.digitalcommerce360.com/2025/12/09/morgan-stanley-ai-agentic-shoppers-385-billion-online-sales/); [FourWeekMBA(2차)](https://fourweekmba.com/morgan-stanleys-agentic-commerce-projection-126-million-ai-shopping-agents-by-2030-while-traditional-e-commerce-halves/)
- Bain(2025 하반기): 2030년 미국 에이전틱 커머스를 **$300~500B**(이커머스의 15~25%)로 본다. 소비자 **약 50%는 완전 자율 구매에 신중**하다. 미국 소비자 30~45%가 제품 조사·비교에 생성형 AI를 쓰고, 17%는 홀리데이 쇼핑을 AI 플랫폼에서 시작하겠다고 답했다. 스펙 중심 생필품이 먼저 옮겨 가고, 의류·여행 같은 재량 소비는 느리게 옮겨 갈 것으로 본다. 소비자가 **리테일러 자체 에이전트를 제3자 에이전트보다 3배 더 신뢰**한다는 수치도 있으나 검색요약상 출처가 Bain으로 추정될 뿐이다. — [Bain snap chart](https://www.bain.com/insights/2030-forecast-how-agentic-ai-will-reshape-us-retail-snap-chart/); [Bain PR](https://www.bain.com/about/media-center/press-releases/20252/agentic-ai-poised-to-disrupt-retail-even-with-50-of-consumers-cautious-of-fully-autonomous-purchasesbain--company/); [Bain: trust](https://www.bain.com/insights/agentic-ai-commerce-hinges-on-consumer-trust/); [Digital Commerce 360 2025-12-22](https://www.digitalcommerce360.com/2025/12/22/bain-agentic-ai-us-ecommerce-sales-2030/)

**한국 소비자 조사**
- 크리테오 '2026 커머스와 AI 트렌드 리포트':
  - 한국인 **76%**가 AI 쇼핑 환경에서도 브랜드 차별성을 중시한다.
  - **69%**가 AI 에이전트가 쇼핑 시간·비용을 크게 줄일 것이라고 기대한다(글로벌 58%).
  - AI 쇼핑의 최대 우려인 '허위·편향 정보에 오도될 가능성'은 **한국 64%**, 글로벌 52%다.
  - AI 어시스턴트 활용은 한국 **7%**, 글로벌 14%다(정확한 문항은 미확인).
  - [벤더(광고기술사)][검색요약] — [매드타임스](https://www.madtimes.co.kr/news/articleView.html?idxno=27972); [디지털인사이트](https://ditoday.com/%ED%95%9C%EA%B5%AD%EC%9D%B8-69-ai%EB%A1%9C-%EC%87%BC%ED%95%91-%ED%9A%A8%EC%9C%A8-%EB%86%92%EC%95%84%EC%A7%88-%EA%B2%83/); [오픈애즈](https://www.openads.co.kr/content/contentDetail?contsId=19176)
- 온라인 쇼핑에서 AI 서비스를 써 본 소비자는 **60%**다. 주요 용도는 제품별 장단점 비교(54.4%)와 쇼핑몰별 최저가·혜택 비교(46.2%)다. [검색요약, 출처 특정 불확실. 오픈서베이 '온라인 쇼핑 트렌드 리포트 2026'으로 추정] — [오픈서베이](https://blog.opensurvey.co.kr/trendreport/online_shopping-2026/)
- 오픈서베이 'AI 검색 트렌드 리포트 2026': 최근 3개월 ChatGPT 검색 이용 경험은 **39.6%(2025-03) → 54.5%(2025-12)**, Gemini는 9.5% → 28.9%다. 지식 습득 검색에서는 생성형 AI가 자리 잡았고, 뉴스·생활정보는 여전히 네이버가 강하다. 2026 하반기판과 한·일 비교판도 있다. [독립 조사사][검색요약] — [오픈서베이 AI 검색 2026](https://blog.opensurvey.co.kr/trendreport/ai-search-2026/); [하반기판](https://blog.opensurvey.co.kr/trendreport/ai-search-2-2026/); [일본판](https://blog.opensurvey.co.kr/trendreport/ai-search-jp-ko-2026/); [한국경제 2026-01-27](https://www.hankyung.com/article/202601275738g)

### Inferences
- AI 유입의 **"양은 작고 질은 높다"**는 결론은 Adobe(전환 +54%, RPV +53%)와 Salesforce(소셜 대비 9배)가 같은 방향을 가리킨다. 둘 다 AI 가시성 솔루션을 파는 벤더라는 점은 할인해서 봐야 한다. 절대 비중이 공개되지 않았으니 "AI가 매출의 몇 %"라는 식의 과장은 피해야 한다.
- 한국은 네이버·쿠팡 **앱 내부 AI**가 주 무대다. 외부 LLM 유입보다 플랫폼 내 AI 추천 비중이 결정적이다. 네이버 '거래액 절반'은 정의가 불명확하다.
- 전망치 편차($190B~$1T)는 "영향(influenced)"과 "에이전트가 완결한 거래"의 정의 차이에서 온다. 보고서에는 범위와 정의를 함께 적어야 한다.
- 한국 소비자는 기대와 불신이 모두 크다(69%/64%). 그래서 AI가 인용할 수 있는 **검증 가능한 근거**(성분·인증·실측 스펙·실사용 리뷰)를 갖춘 셀러가 유리할 것이다.

### Gaps
- AI 유입이 미국·한국 리테일 전체 트래픽에서 차지하는 **절대 비중**(Adobe 캡처본에 수치 없음).
- 한국 외부 LLM(ChatGPT·Gemini·Perplexity)에서 한국 쇼핑몰로 들어오는 유입·전환 데이터. 카페24나 네이버 등의 공식 통계를 찾지 못했다.
- Salesforce "AI influenced" 방법론의 세부.
- 한국 정부나 공공 조사(과기정통부·KISDI 등)의 AI 쇼핑 이용률 데이터는 미조사.

## 4. GEO/AEO 플레이북: LLM 쇼핑 답변이 상품을 고르는 방식, 피드·구조화데이터·리뷰·콘텐츠, llms.txt 논쟁, 측정 도구, 근거 연구

### Takeaway
확인된 근거를 종합하면, AI 쇼핑 답변 노출은 네 가지로 좌우된다. **(1) 구조화된 상품 피드**(ChatGPT·Google Merchant Center·ACP/UCP 카탈로그), **(2) 페이지의 기계 판독성**(텍스트화된 스펙·FAQ·가이드 콘텐츠), **(3) 리뷰와 서비스 품질 신호**, **(4) 외부 언급**이다. Adobe 자료상 AI 유입이 많은 상위 20% 기업은 홈페이지·검색결과·가이드 콘텐츠의 AI 판독성 점수가 23~52% 높았다. llms.txt는 제안자 쪽 채택 주장은 있으나 쇼핑 노출 효과를 보여 주는 근거는 찾지 못했다.

### Cited Findings

**피드·카탈로그 (1순위)**
- ChatGPT 노출은 상품 피드가 좌우한다. 형식은 CSV·TSV·XML·JSON이고 최대 15분 주기로 갱신할 수 있다. Shopify·Etsy는 자동 연동되고 그 외는 chatgpt.com/merchants에서 신청한다. 미국 전용이다. [검색요약] — [chatgpt.com/merchants](https://chatgpt.com/merchants/); [Lengow](https://www.lengow.com/get-to-know-more/chatgpt-product-feed/)
- ChatGPT Ads는 Google Merchant Center 피드 형식을 그대로 받는다. [2차] — [Passionfruit](https://www.getpassionfruit.com/blog/chatgpt-product-feed-ads-what-retailers-need-to-know)
- **ACP Product Feed 스키마(2026-04-17)** [원문확인] — [ACP GitHub](https://github.com/agentic-commerce-protocol/agentic-commerce-protocol)
  - 푸시 모델이다. 머천트가 에이전트 측 피드 서비스로 `POST /feeds`와 `PATCH /feeds/{id}/products`를 호출하고, 파일로 넣을 때는 metadata.json과 products.jsonl을 쓴다.
  - Product 필수 필드는 id와 variants다. 선택 필드는 title, description, url, media다.
  - Variant 필드: id, title(필수), barcodes, price, list_price, unit_price, availability, categories, condition, variant_options(색상·사이즈), media(첫 번째가 대표), seller, marketplace.
  - FeedMetadata에는 **target_country**(ISO 3166-1)가 있다. 가격은 ISO 4217 통화와 최소단위 정수로 표기한다.
  - RFC는 "피드는 발견·머천다이징 면이고 가격·세금·배송·결제의 권위 있는 원천은 checkout"이라고 규정한다. 미출시 제안으로는 `/.well-known/acp.json` 디스커버리 문서와 `suggested_price`(SEP #197, 피드 가격과 결제 가격 일치용)가 있다.
- UCP도 catalog_search·catalog_lookup·cart·checkout·order 스키마를 정의한다(release/2026-08-25). [원문확인] — [UCP GitHub](https://github.com/Universal-Commerce-Protocol/ucp)
- Google은 I/O 2026에서 Merchant Center 신규 속성 스키마 **"Conversational Attributes"**를 발표했다. 대화형 질의에 맞춘 속성으로 보이나 필드 세부는 미확인이다. [검색요약] — [Azoma](https://www.azoma.ai/insights/google-i-o-2026-what-the-agentic-commerce-announcements-mean-for-brands); [Verity Score](https://verityscore.io/en/kb/google-ai-ecommerce-updates/); [Paz.ai GMC for AI Mode 가이드](https://www.paz.ai/guides/google-merchant-center-for-ai-mode)
- 한국: 쿠팡은 수억 개 상품을 AI가 읽을 수 있는 표준 속성 체계로 재구조화하고 있다([한국경제](https://www.hankyung.com/article/202607156887g)). 네이버는 주문이행·배송품질·CS만족도를 추천 알고리즘에 반영한다([바이라인네트워크](https://byline.network/2026/03/15_19298383/)).

**페이지 판독성·콘텐츠 (Adobe, 2026-02·05 분석)** [원문확인][벤더] — [Adobe Q3 2026 PDF](https://s3.amazonaws.com/media.mediapost.com/uploads/ADOBE_q3-2026-ai-sourced-traffic-insights.pdf)
- AI 방문 점유율 상위 20% 기업과 하위 기업의 "AI Citation Readability" 점수 차이는 **홈페이지 +52%**, **사이트 내 검색결과 페이지 +32%**, **블로그·구매가이드·교육 콘텐츠 +23~30%**, 브랜드 랜딩과 PDP +14~15%, 카테고리·컬렉션 +5%, 매장 위치 페이지 +29%였다. FAQ 페이지는 그룹 간 차이가 작았는데, 구조화된 Q&A는 누구에게나 효과적이기 때문이라고 Adobe는 해석한다.
- 상위 기업은 기계가 읽지 못하는 "missing words"가 적었다. 홈페이지 -53%, 브랜드 랜딩 -38%, 반품·교환 -35%, 콘텐츠 -28%다.
- 업종별 평균 판독성은 **화장품 63%**(1위, 성분 교육·튜토리얼 등 에디토리얼 덕분), 전자 56%, 스포츠·의류 51%, 식료품 48%, 가구·홈 47%다.
- PDP 판독성은 식료품 70%, 스포츠 68%, 전자 65%, 가구 52%, 화장품 51%, **의류 50%**다. 의류 PDP는 텍스트보다 이미지에 치우쳐 있다.

**AI 인용·추천 요인 연구**
- Princeton 등 "GEO: Generative Engine Optimization"(arXiv 2311.09735, KDD 2024): 최적화 전략으로 생성형 엔진 답변에서 출처 가시성을 **최대 40%** 높일 수 있었다. GEO-bench 공개. [독립·학술][원문확인(README)] — [GEO GitHub](https://github.com/GEO-optim/GEO); [arXiv](https://arxiv.org/abs/2311.09735)
- Profound는 ChatGPT 쇼핑이 무엇을 보고 상품을 인용하는지 분석한 글을 냈다. 제목만 확인했고 내용은 미확인이다. [벤더] — [Profound blog](https://www.tryprofound.com/blog/chatgpt-shopping-deep-dive)

**llms.txt 논쟁**
- 제안서 v2(Jeremy Howard, 2026-08-10 수정)는 다음을 주장한다.
  - 수천 개 사이트가 llms.txt를 게시하고, 문서 플랫폼(Mintlify)은 자동 생성한다.
  - **Chrome Lighthouse가 "agentic browsing" 점검 항목으로 llms.txt 유무를 감사**한다.
  - OpenAI·Anthropic·Gemini가 자사 개발자 문서용 llms.txt를 게시했다.
  - 주 용도는 **소프트웨어 문서**이고, 비즈니스 구조·정책 안내에도 쓸 수 있다.
  - 페이지별 .md 버전 제공과 `rel="alternate" type="text/markdown"` 링크를 권고한다.
  - WordPress 플러그인(Yoast, AIOSEO)이 자동 생성한다.
  - [제안자 측 자료=옹호 입장][원문확인] — [llms.txt 제안서(GitHub)](https://github.com/AnswerDotAI/llms-txt)
- 반대 측 근거(검색엔진·LLM 업체가 쇼핑 노출에 llms.txt를 쓰지 않는다는 공식 입장 등)는 이번 세션에서 확보하지 못했다(Gaps).

### Inferences — 셀러 실행 카드 (무엇 / 누구에게 / 비용 / 시작 방법 / 확인된 효과 / 함정)
- **A. 피드 위생 (Google Merchant Center → ChatGPT·광고 재사용)**
  - 무엇: 제목·설명·GTIN(바코드)·가격·재고·배송비·반품정책·variant(색상·사이즈)·이미지를 정확히 채운 단일 피드.
  - 누구: 해외(미국) 판매 자사몰(Shopify·카페24 글로벌) 셀러. 1인 셀러도 가능하다.
  - 비용: GMC 등록·무료 리스팅은 무료다. ChatGPT 피드 연동도 무료(Shopify·Etsy는 자동)이며, ChatGPT Ads는 유료(CPC 관찰치 $3~5, 대행사 추정)다.
  - 시작: GMC 계정 → 피드 등록 → 진단 오류 0 만들기 → (미국 대상이면) chatgpt.com/merchants 신청. ACP 스키마상 variant별 id, 가격, 재고, 바코드, 대표이미지가 핵심이다.
  - 효과: 피드 자체의 효과를 독립적으로 측정한 수치는 없다. 간접 근거로 AI 유입 전환율 +54%(Adobe)가 있다.
  - 함정: 피드 가격과 결제 가격 불일치(ACP가 suggested_price를 따로 제안할 만큼 흔한 문제), 품절 미반영, 미국 외 사업자 자격 불명확.
- **B. 국내 플랫폼 속성·리뷰·서비스지표 (네이버·쿠팡·11번가)**
  - 무엇: 카테고리 속성 100% 입력, 스펙 텍스트 병기, 리뷰 관리, 도착보장·출고준수·CS 응답시간 관리.
  - 누구: 모든 국내 셀러. 1인 셀러가 가장 먼저 할 일이다.
  - 비용: 무료. 네이버 에이전트는 추가 수수료가 없다.
  - 시작: 스마트스토어·윙 상품 속성 점검 → 상세 이미지 속 스펙을 텍스트로 옮기기 → 리뷰 요청 흐름 만들기 → 배송 리드타임 단축.
  - 효과: 11번가 AI 검색 전환율 2배+(플랫폼 자체발표). 셀러 단위 효과 수치는 없다.
  - 함정: 이미지 위주 상세페이지(Adobe의 의류 PDP 판독성 50%와 같은 논리), 배송비 포함 총액 경쟁력 부족.
- **C. 기계 판독 가능한 콘텐츠 (자사몰·브랜드)**
  - 무엇: 구매가이드, 성분·소재 설명, 사용법, FAQ, 반품·교환 페이지를 텍스트 HTML로 작성하고 schema.org Product·Offer·Review·FAQ 구조화데이터를 붙인다.
  - 누구: 자사몰(카페24·아임웹·식스샵·고도몰·Shopify)을 운영하는 중소 브랜드, 특히 화장품·전자처럼 설명 콘텐츠가 강점인 카테고리.
  - 비용: 내부 작업 또는 AI 작성 도구 비용. 구조화데이터는 대부분 솔루션 기본 기능이나 앱으로 처리된다(솔루션별 지원 여부는 미확인).
  - 시작: 홈페이지·카테고리·PDP의 핵심 정보가 JS나 이미지 속에만 있지 않은지 점검 → FAQ·가이드 페이지 신설 → 반품정책 텍스트화.
  - 효과: Adobe 상위 20% 기업은 홈 +52%, 가이드 +23~30% 판독성 우위(상관관계이며 인과는 아님).
  - 함정: 판독성 점수는 벤더 지표이고, 이미지 중심 한국형 상세페이지는 대개 불리하다.
- **D. 외부 언급·리뷰 생태계**
  - 무엇: 리뷰 플랫폼, 커뮤니티, 언론·블로그 비교 기사에 등장하는 것.
  - 근거: GEO 논문(최대 40% 가시성)과 Salesforce(AI 검색 유입 전환 = 소셜의 9배)는 간접 근거다. 외부 언급이 추천 확률에 얼마나 기여하는지는 이번 세션에서 확보하지 못했다(Gaps).
- **E. llms.txt**
  - 비용: 거의 0(플러그인·수작업).
  - 효과: 쇼핑 노출에 대한 근거는 없다. 제안자 측은 Lighthouse 점검 항목이 됐다고 주장한다.
  - 판단: 비용이 낮으니 "해도 되지만 우선순위는 낮게". 피드·판독성보다 뒤다.
- **F. 측정**
  - 무엇: GA4 등에서 chatgpt.com, perplexity.ai, gemini.google.com, copilot 리퍼러 유입을 세그먼트로 보고 전환율과 방문당 매출을 비교한다. 핵심 질의 20~50개를 정해 주기적으로 AI 답변 노출을 수동 점검한다.
  - 도구: Profound, Semrush AI toolkit, Ahrefs Brand Radar 같은 유료 AI 가시성 도구는 가격 미확인(Gaps). 1인 셀러는 수동 점검으로 충분하다.

### Gaps
- AI 가시성 측정 도구 요금·무료 플랜(Profound, Semrush AI Visibility Toolkit, Ahrefs Brand Radar, Peec AI, Otterly 등)과 한국형 도구의 존재 여부를 조사하지 못했다(검색 한도 소진).
- 무엇이 AI 인용·추천을 이끄는지에 대한 독립 대규모 연구(Ahrefs의 브랜드 언급 상관, Semrush·Search Engine Land 연구 등)의 수치를 확보하지 못했다.
- OpenAI 상품 피드 공식 스펙의 필드 목록(enable_search 등)은 developers.openai.com 접근이 차단돼 확인하지 못했다. ACP 스키마로만 대체했다.
- Google의 llms.txt·AI 기능 관련 공식 입장("별도 AI 파일·특수 스키마 불필요" 취지)을 확인하지 못했다.
- 네이버 AI 브리핑이나 쇼핑 에이전트의 인용 기준(블로그·카페 리뷰의 영향)도 확인하지 못했다.
- 카페24·아임웹·식스샵·고도몰의 구조화데이터, GMC 연동, ChatGPT 피드 지원 현황도 확인하지 못했다.

## 5. AI 기반 해외판매(크로스보더): 번역·현지화, 마켓플레이스 AI 도구, 다국어 자사몰, K-뷰티·K-패션 사례, 정부·KOTRA 지원

### Takeaway
**이번 세션에서는 이 질문을 거의 조사하지 못했다**(검색 한도 소진, 원문 접근 차단). 확보된 근거로 말할 수 있는 것은 구조적 사실뿐이다. 글로벌 AI 쇼핑·결제 프로그램이 대부분 미국 사용자와 미국 사업자 기준이므로, 한국 셀러가 이 흐름에 올라타는 현실적 경로는 **미국 소비자 대상 채널**(Shopify 해외몰, Etsy, Amazon US)이다. 또 화장품은 AI 판독성 1위 카테고리여서 K-뷰티가 콘텐츠 기반 GEO에 유리한 위치에 있다.

### Cited Findings
- 지역 제한 현황:
  - ChatGPT 쇼핑은 미국 사용자 대상이다. [chatgpt.com/merchants](https://chatgpt.com/merchants/)
  - ChatGPT Ads는 미국·캐나다·호주·뉴질랜드에서 시작해 브라질·멕시코가 다음이다. [ai.nl](https://www.ai.nl/en/advertising-in-chatgpt)
  - Google UCP 결제는 미국 사업자 대상이며 캐나다·호주, 이후 영국으로 확대된다. [Merchant Center Help](https://support.google.com/merchants/answer/16837055?hl=en); [Google blog](https://blog.google/products-and-platforms/products/shopping/google-shopping-cart/)
  - UCP 로드맵의 확대 지역은 인도·인도네시아·중남미다. [UCP GitHub](https://github.com/Universal-Commerce-Protocol/ucp)
  - Alexa for Shopping은 미국용이다. [CNBC](https://www.cnbc.com/2026/05/13/amazon-ditches-rufus-ai-chatbot-in-favor-of-alexa-shopping-agent.html)
  - Perplexity Instant Buy는 미국 사용자용이다. [PayPal](https://newsroom.paypal-corp.com/2025-11-PayPal-and-Perplexity-Launch-Instant-Buy)
- ACP 피드는 feed 단위로 target_country를 지정하고 가격을 ISO 4217 통화로 표기한다. 국가별·통화별 피드를 따로 운영하는 구조가 가능하다. Meta의 ACP 합류 명분은 "enable merchants worldwide"다. [원문확인] — [ACP GitHub](https://github.com/agentic-commerce-protocol/agentic-commerce-protocol)
- Shopify·Etsy 판매자의 카탈로그는 ChatGPT 상품 발견에 자동 연동된다. Shopify 머천트는 Copilot Checkout에 자동 등록된다. [검색요약] — [chatgpt.com/merchants](https://chatgpt.com/merchants/); [Microsoft Advertising blog](https://about.ads.microsoft.com/en/blog/post/january-2026/conversations-that-convert-copilot-checkout-and-brand-agents)
- 미국 리테일 AI 판독성에서 **화장품이 63%로 1위**다. 성분 교육, 튜토리얼, 고객서비스 콘텐츠가 이유다. 반면 화장품 PDP는 51%로 중간이다. [원문확인][벤더] — [Adobe Q3 2026 PDF](https://s3.amazonaws.com/media.mediapost.com/uploads/ADOBE_q3-2026-ai-sourced-traffic-insights.pdf)
- 2026년 3월 Adobe 기준 AI 유입 증가가 두드러진 카테고리에 퍼스널케어, 의류, 유아용품이 들어 있다. — [Adobe Q3 2026 PDF](https://s3.amazonaws.com/media.mediapost.com/uploads/ADOBE_q3-2026-ai-sourced-traffic-insights.pdf)
- 오픈서베이는 한·일 AI 검색 행태를 비교한 '일본 AI 검색 트렌드 리포트 2026'을 냈다(수치 미확인). 일본 진출 셀러의 참고자료가 될 수 있다. — [오픈서베이](https://blog.opensurvey.co.kr/trendreport/ai-search-jp-ko-2026/)

### Inferences
- 미국 대상 판매는 **Shopify(또는 Etsy) 해외몰 + GMC 피드 + 영문 텍스트 콘텐츠(성분·사용법·FAQ)** 조합으로 ChatGPT, Copilot, Google AI Mode 발견 흐름에 추가 비용 없이 올라탈 수 있다. 결제 자격은 별도 확인이 필요하다.
- 한국 자사몰 솔루션(카페24 등)으로 해외몰을 운영한다면, 해당 솔루션이 GMC나 ChatGPT 피드를 지원하는지가 관건이다(미확인).
- K-뷰티는 AI가 가장 잘 인용하는 콘텐츠 유형(성분 교육·루틴 가이드)을 원래 갖고 있다. 이를 **텍스트 HTML·다국어**로 옮기는 것이 이미지 중심 상세페이지를 번역하는 것보다 AI 노출에 유리할 것이다. Adobe 판독성 결과에서 끌어낸 추론이다.
- 일본·동남아처럼 에이전틱 결제가 아직 없는 시장에서는 AI의 역할이 번역·현지화·CS 자동화로 한정된다. 마켓플레이스(Qoo10, Shopee 등) 내부 AI 도구가 핵심이 될 것으로 보이나, 이 판단은 근거 미확보다.

### Gaps (후속 조사 필요. 아래 항목명은 조사 대상이며 사실 주장이 아님)
- **번역·현지화 도구** DeepL, 파파고, GPT·Claude의 2026년 요금, 상세페이지·CS 적용 사례, 오역·규제 표현(화장품 효능 표현 등) 리스크.
- **마켓플레이스 AI 도구**: Amazon 글로벌 셀링(생성형 AI 리스팅 생성 등 셀러 도구), Shopee·Lazada, Qoo10 Japan, TikTok Shop(미국·일본), Etsy의 2026년 AI 기능, 한국 셀러 적용 방법, 비용.
- **다국어 자사몰**: 카페24 다국어·해외몰과 AI 기능, Shopify Markets·번역 앱, 아임웹 등의 AI 번역과 해외결제 지원.
- **K-뷰티·K-패션 성공 사례의 수치**: 브랜드별 아마존·큐텐·틱톡샵 매출, 2025~2026 화장품 수출 통계(식약처·관세청·KITA).
- **정부 지원**: KOTRA와 중소벤처기업부·중진공의 2026년 온라인 수출 지원사업(해외 온라인몰 입점, 물류·마케팅 바우처, 고비즈코리아 등)의 공고, 지원 한도, 신청 시기.
- 비미국 사업자(한국 법인)가 Shopify Payments·Stripe·PayPal 기반으로 미국 AI 결제 프로그램에 참여할 수 있는지 여부.

## 6. 리스크: 플랫폼 종속, 수수료, 고객관계·데이터 상실, 프로토콜 파편화, 에이전트 구매의 사기·차지백 책임

### Takeaway
에이전틱 커머스의 비용은 "추가 수수료"보다 **고객관계·데이터·통제권 상실**과 **광고형 유료 노출로의 이동**으로 나타나고 있다. 주요 프로토콜(UCP·ACP)과 Copilot Checkout은 모두 **셀러가 Merchant of Record로 재무 책임(차지백 포함)을 진다**는 전제 위에 있다. 에이전트가 결제를 대신해도 사기·분쟁 리스크는 셀러에게 남는다. 프로토콜은 여러 갈래지만 Stripe·Meta의 중복 참여와 AP2의 FIDO 이관으로 수렴 조짐이 있다.

### Cited Findings
- **책임 주체**:
  - UCP 용어집: "Business … act as the Merchant of Record (MoR), retaining financial liability and ownership of the order." UCP 문서는 "You remain the Merchant of Record … full ownership of customer relationships"를 내세운다(마케팅 문구). [원문확인] — [UCP GitHub](https://github.com/Universal-Commerce-Protocol/ucp)
  - ACP는 에이전트가 "without being the merchant of record"라고 명시하며 거래한다. 2026-04-17 버전에 3DS 인증 결과 예시(denied, frictionless)가 들어갔고 delegate_payment의 risk_signals 최소 개수 요건을 없앴다. [원문확인] — [ACP GitHub](https://github.com/agentic-commerce-protocol/agentic-commerce-protocol)
  - Copilot Checkout은 머천트가 MoR을 유지한다. [검색요약] — [Microsoft Advertising blog](https://about.ads.microsoft.com/en/blog/post/january-2026/conversations-that-convert-copilot-checkout-and-brand-agents)
- **사기 방지 장치**: AP2 mandate는 checkout 해시에 묶여 토큰 재사용과 금액 조작을 막고, 양측에 암호학적 합의 증거를 남긴다(UCP-AP2 문서, [원문확인] — [UCP GitHub](https://github.com/Universal-Commerce-Protocol/ucp)). FIDO Alliance는 Agentic Authentication·Payments 작업반을 신설했고 Payments 작업반은 Mastercard·Visa가 공동의장이다. Mastercard의 Verifiable Intent 프레임워크도 함께 논의된다. [2차] — [Eco](https://eco.com/support/en/articles/15192002-ap2-protocol-explained-google-s-agentic-commerce-standard-2026); [Google blog](https://blog.google/products-and-platforms/platforms/google-pay/agent-payments-protocol-fido-alliance/)
- **고객관계·데이터 상실** [원문확인] — [ACP GitHub rfcs](https://github.com/agentic-commerce-protocol/agentic-commerce-protocol)
  - ACP 'Marketing Consent' RFC는 동기로 "When buyers purchase through ACP-integrated agents instead of merchant storefronts, this opt-in opportunity is lost"와 "Merchants lose a key acquisition channel"을 든다.
  - 'Intent Traces' RFC는 에이전트가 결제를 취소한 이유(가격·배송비 등)를 구조화 코드로 머천트에 전달하자고 제안한다.
  - 'Affiliate Attribution' RFC는 에이전틱 커머스에서 클릭 경로가 사라져 제휴 기여 측정이 깨진다고 진단한다.
  - 세 문서 모두 Status: Proposal이다.
- **통제권을 둘러싼 대형 머천트의 선택**: Walmart는 ChatGPT 내부 결제의 전환이 3배 낮았다고 보도됐다. 이후 OpenAI 결제 파일럿을 끝내고 자체 에이전트 Sparky를 Gemini·ChatGPT에 넣었으며, Gemini 제휴에서도 결제는 Walmart 환경에서 한다. [2차·검색요약] — [Digital Applied](https://www.digitalapplied.com/blog/ai-agentic-commerce-discover-in-ai-buy-on-site-2026); [MLQ](https://mlq.ai/news/walmart-shifts-to-self-developed-ai-shopping-in-gemini-after-ending-openai-partnership/); [CNBC 2026-01-11](https://www.cnbc.com/2026/01/11/walmart-partners-with-google-gemini-on-shopping-tool.html)
- **수수료·유료 노출**:
  - OpenAI의 4% 수수료는 폐지된 모델이지만 선례로 남아 있다. — [PYMNTS](https://www.pymnts.com/news/ecommerce/2026/shopify-merchants-to-pay-4percent-fee-on-sales-made-through-chatgpt-checkout/)
  - ChatGPT Ads(2026-02 출시)와 Sponsored Agents(2026-09 테스트). — [Digital Applied](https://www.digitalapplied.com/blog/chatgpt-sponsored-agents-shopify-app-what-changes)
  - 네이버 에이전트는 현재 광고와 추가 수수료가 없다. — [바이라인네트워크](https://byline.network/2026/03/15_19298383/)
  - 국내 언론은 "맞춤 추천일까, 광고일까"를 문제로 제기했다. — [Daum](https://v.daum.net/v/5qJzY02uE6)
- **플랫폼 우회와 종속**: 전자신문은 "플랫폼 패싱하는 에이전틱 커머스"를 짚었다. 기존 검색·몰 방문 없이 에이전트가 거래를 중개하는 구조를 말한다. — [전자신문 2026-07-01](https://www.etnews.com/20260701000423). Amazon Buy for Me는 타사 사이트에서도 대신 구매한다. — [Canopy Management](https://canopymanagement.com/amazon-alexa-for-shopping-sellers-guide/)
- **프로토콜 파편화와 수렴** [원문확인·검색요약]:
  - ACP의 maintainer는 OpenAI, Stripe, Meta다.
  - UCP의 Governing Council은 Google, Shopify, Stripe이고, Tech Council에는 Amazon, Meta, Microsoft, Stripe, Salesforce가 들어 있다.
  - AP2는 FIDO로 이관됐다.
  - 이 밖에 Visa Intelligent Commerce, Mastercard Agent Pay, Stripe·PayPal의 자체 레이어가 병존한다. — [ACP GitHub](https://github.com/agentic-commerce-protocol/agentic-commerce-protocol); [UCP GitHub](https://github.com/Universal-Commerce-Protocol/ucp); [Internet Pros 개관(2차)](https://internet-pros.com/blog/agentic-commerce-ai-payments-visa-mastercard-2026/)
- **소비자 신뢰 리스크**: 미국 소비자 약 50%가 완전 자율 구매에 신중하다(Bain). 한국 소비자 64%는 AI의 허위·편향 정보를 우려한다(Criteo). — [Bain PR](https://www.bain.com/about/media-center/press-releases/20252/agentic-ai-poised-to-disrupt-retail-even-with-50-of-consumers-cautious-of-fully-autonomous-purchasesbain--company/); [매드타임스](https://www.madtimes.co.kr/news/articleView.html?idxno=27972)

### Inferences
- **셀러 관점 리스크 순위(추론)**:
  - (1) **노출 알고리즘 블랙박스와 종속**: 에이전트가 5개 안팎만 추천하는 구조(11번가 사례)에서는 승자독식이 심해진다.
  - (2) **고객데이터·재구매 채널 상실**: 에이전트 내 결제가 붙으면 마케팅 수신동의와 CRM 접점이 약해진다.
  - (3) **광고형 노출 비용 상승**.
  - (4) **사기·차지백**: MoR로서 책임은 그대로인데, 에이전트 경유 주문의 이상거래 패턴은 셀러가 통제하기 어렵다.
  - (5) **파편화**: 중소 셀러는 플랫폼 레이어(Shopify·Stripe·PayPal·네이버페이)가 흡수해 주므로 상대적으로 영향이 작다.
- **대응 원칙(추론)**: 추천 알고리즘이 쓰는 품질 데이터(배송·CS·리뷰)를 관리하는 일, 구매 후 접점(패키지 인서트, 멤버십, 카카오 채널)으로 재구매를 자사로 되돌리는 일, 에이전트 경유 주문의 이상거래·반품 모니터링이 필요하다. 한 플랫폼 AI 지면에 매출이 쏠리지 않게 채널 포트폴리오도 관리해야 한다.
- 국내에서는 네이버·카카오가 결제(네이버페이·카카오페이)까지 쥔 상태로 에이전트를 붙인다. 따라서 셀러의 협상력은 미국(여러 에이전트가 경쟁)보다 약할 가능성이 크다.

### Gaps
- Visa·Mastercard의 에이전트 결제 차지백 규칙과 책임 전환(liability shift) 조건, 국내 카드사·PG의 에이전트 결제 분쟁 처리 기준을 확인하지 못했다.
- 한국 전자상거래법(청약철회, 표시·광고)이 AI 에이전트 추천·결제에 어떻게 적용되는지, 공정위의 자사우대·광고 표시 규율 동향을 확인하지 못했다.
- 에이전트 경유 주문의 실제 사기율·반품률 데이터는 없다. Adobe 설문의 "69%가 반품 가능성 낮아짐"은 소비자 자기보고일 뿐이다.
