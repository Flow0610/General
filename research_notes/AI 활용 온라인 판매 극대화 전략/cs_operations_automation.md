# AI로 CS·백오피스 자동화하기: 한국·글로벌 온라인 셀러 (2026-09-27 기준 조사 노트)

> **조사 방법·신뢰도 메모 (보고서 작성자 필독)**
> - 조사일: 2026-09-27. 이번 세션에서 **WebFetch가 거의 모든 도메인에서 egress proxy에 막혔다**(channel.io, docs.channel.io, kakaocorp.com, mt.co.kr, byline.network, bizwatch, gartner.com, gorgias.com, fin.ai, cnbc.com, nber.org, chromewebstore 등). 또 **WebSearch 세션 한도(200회, 병렬 리서처와 공유)가 조사 도중 소진**되었다. 그래서 아래 수치 대부분은 **검색엔진 결과 요약(snippet)**에서 가져왔고 원문을 직접 열어 대조하지는 못했다. 인용 URL은 해당 검색 결과 묶음에서 가장 관련이 높은 원문 페이지다. 직접 열람이 가능했던 곳은 GitHub(github.com, raw.githubusercontent.com)뿐이다.
> - 출처 표기: **[VENDOR]** 벤더·자사 발표 또는 마케팅 문구 / **[3P]** 경쟁사·제휴 블로그 등 독립적이지 않은 제3자 / **[PRESS]** 언론 보도(대개 벤더 수치를 그대로 전달) / **[IND]** 독립 출처(학술, Gartner 서베이, 판결) / **[ANEC]** GitHub·커뮤니티 일화(검증 안 됨).
> - 이번 조사 범위에서 **1차 확인하지 못한 항목**(국내 OMS 5사 AI 기능, 네이버·쿠팡·카페24 네이티브 AI, Sendbird, Shopify Sidekick/Inbox, Amazon Project Amelia, ChatGPT agent, Gemini in Sheets, Make/Zapier/n8n 가격 등)은 각 질문의 Gaps에 **"미검증 단서"**로만 적었다. 출처 없이 인용하면 안 된다.

---

## 1. 한국 셀러가 쓸 수 있는 AI CS 에이전트·챗봇: 가격 모델, 자동화율/해결률, CSAT, 사례

### Takeaway
국내 마켓플레이스 셀러에게 현실적인 선택지는 **채널톡 ALF**(스마트스토어 연동, 주문 조회·취소·반품까지 처리, 2024-11 정식 출시, 2025-11 v2)와 **카카오 '카나나 상담매니저'**(톡채널 자동응답, 2025-09-25 정식 출시), 그리고 해피톡·사이드톡이나 월 5만~50만원대 국산 RAG 챗봇이다. Fin(구 Intercom, 2026-09-10 Salesforce 인수 완료), Gorgias, Zendesk, Tidio Lyro 같은 글로벌 도구는 **해결 1건당 $0.90~$2.00를 받는 과금**이 표준이 되었지만, Shopify 중심의 크로스보더 자사몰에 맞는 도구다. 해결률은 벤더 주장(67~80%대)과 제3자 관측(40~60%) 사이에 차이가 크다. 게다가 '해결'의 정의가 벤더마다 달라 수치끼리 직접 비교할 수 없다.

### Cited Findings

**A. 국내 솔루션**

*채널톡 ALF(알프), 채널코퍼레이션*
- **출시·상태**: 2024년 4월 처음 선보였다(2025-11-06 기사 표현은 "지난해 4월 … '알프'를 내놨으며") [PRESS]. [머니투데이/유니콘팩토리 2025-11-06](https://www.unicornfactory.co.kr/article/2025110611161567414). 2024-11-01 '정식 출시'(GA) 공지 [VENDOR]: [채널톡 업데이트 노트 "2024. 11. 01 ALF 정식 출시"](https://docs.channel.io/updates/ko/articles/5cf93bf9-2024-11-01-ALF-%EC%A0%95%EC%8B%9D-%EC%B6%9C%EC%8B%9C-)
- **ALF v2**: 2025-11-06 출시. "자율 업무 수행 능력이 한층 강화된 상담 AI 에이전트", 보도자료 제목은 "완전 자동화 실현" [VENDOR]. [채널톡 보도자료](https://channel.io/ko/blog/articles/alf-v2-press-f03760de), [머니투데이 2025-11-06](https://www.mt.co.kr/future/2025/11/06/2025110611161567414)
- **도입 규모**: 출시 1년 만에 약 2,000여 개 기업, 누적 **130만 건** 상담 처리 [PRESS, 벤더 수치]. [머니투데이 2025-11-06](https://www.mt.co.kr/future/2025/11/06/2025110611161567414). 그 전 마일스톤은 "누적 도입 고객사 500개 돌파"(게시일 미확인) [VENDOR]: [채널톡 블로그](https://channel.io/ko/blog/articles/d980c1e4)
- **해결률(자사 CS에 직접 적용한 결과)**: ALF v2 도입 약 1개월 만에 평균 해결률 **80%**. v1보다 "약 20% 상승"했다는데 %p인지 %인지는 원문에서 불명확하다. 추석 연휴 기간에는 **85%** [VENDOR, 자사 데이터]. [채널톡 블로그 "채널톡이 먼저 써본 ALF v2, 해결률 80% 달성"](https://channel.io/ko/blog/articles/alfv2-cx-case-02942123)
- **고객 사례(여행사)**: 도입 첫 달 홈페이지 문의 **23%↓**, 전화 문의 **19%↓**, 6개월 후 홈페이지 문의 **44%↓** [VENDOR 사례, 언론 인용]. 출처는 2025-11 ALF 보도의 검색 요약이며 원문 대조는 못 했다: [머니투데이](https://www.mt.co.kr/future/2025/11/06/2025110611161567414), [바이라인네트워크 2025-11 "AI의 실효성이 의심되면 '채널톡'을 보라"](https://byline.network/2025/11/1106-4/)
- **과금 기준(해결당)**: '해결된 상담'은 ALF가 커맨드·FAQ·답변 생성(FAQ·도큐먼트 기반 RAG)으로 유의미한 답변을 보냈고, 고객이 **24시간 안에 상담원 연결을 요청하지 않은** 상담이다. "ALF가 해결한 유저챗에 대해서만 과금" [VENDOR]. [채널톡 도움말: ALF 통계](https://docs.channel.io/help/ko/articles/dd674698-ALF-%ED%86%B5%EA%B3%84), [채널톡 도움말: 서비스 구독](https://docs.channel.io/help/ko/articles/df0f42a5)
- **과금 기준 충돌·변경 가능성**: 다른 도움말에는 "**상담 참여당 과금**: ALF가 최초 답변을 시작하고 ALF가 답변을 종료할 때까지를 1건으로 과금"이라는 문구가 있다 [VENDOR]. [채널톡 도움말: 채널톡 구독 이해하기](https://docs.channel.io/help/ko/articles/%EC%B1%84%EB%84%90%ED%86%A1-%EA%B5%AC%EB%8F%85-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0-0c124e99). 2025-11-28자 "[중요 공지] 채널톡 가격제 개편 안내"가 있으므로 해결당 과금이 참여당 과금으로 바뀌었을 수 있다. **원문 미확인이고 KRW 단가도 미확인.** [채널톡 공지 25.11.28](https://docs.channel.io/updates/ko/articles/%EC%A4%91%EC%9A%94-%EA%B3%B5%EC%A7%80-%EC%B1%84%EB%84%90%ED%86%A1-%EA%B0%80%EA%B2%A9%EC%A0%9C-%EA%B0%9C%ED%8E%B8-%EC%95%88%EB%82%B4251128--8bd5ddd0)
- **스마트스토어 연동**: 판매자는 스마트스토어센터를 따로 열지 않고 채널톡 안에서 고객 문의에 답할 수 있다. ALF로 **주문 조회, 취소, 반품**까지 처리한다 [VENDOR]. [채널톡 도움말: 네이버 스마트스토어](https://docs.channel.io/help/ko/articles/%EB%84%A4%EC%9D%B4%EB%B2%84-%EC%8A%A4%EB%A7%88%ED%8A%B8%EC%8A%A4%ED%86%A0%EC%96%B4-6d4e4039)
- **AI 전화상담 '전화 알프' 베타 출시**(출시일 미확인) [VENDOR]. [채널톡 보도자료](https://channel.io/kr/blog/articles/call-alf-press-2d90bbb6)
- **Shopify 앱으로도 제공**되어 크로스보더 Shopify 자사몰에서 쓸 수 있다: [Shopify App Store: channel io](https://apps.shopify.com/channel-io?locale=ko)
- **마케팅 문구**: "고객상담의 80%를 자동화하는 AI 에이전트 ALF" [VENDOR 마케팅 문구를 리뷰 사이트가 인용]. [모켓 도구 리뷰](https://www.moket.kr/tools/channel)

*카카오 '카나나 상담매니저'(카카오톡 채널)*
- **2025-09-25 정식 출시(GA)** [VENDOR/PRESS]: [카카오 보도자료](https://www.kakaocorp.com/page/detail/11719), [비즈워치 2025-09-25](https://news.bizwatch.co.kr/article/mobile/2025/09/25/0044), [CIO Korea](https://www.cio.com/article/4062884/%EC%B9%B4%EC%B9%B4%EC%98%A4-%EA%B3%A0%EA%B0%9D-%EC%9D%91%EB%8C%80%EC%9A%A9-ai-%EC%B1%84%ED%8C%85-%EC%84%9C%EB%B9%84%EC%8A%A4-%EC%B9%B4%EB%82%98%EB%82%98-%EC%83%81%EB%8B%B4%EB%A7%A4%EB%8B%88.html)
- **기능**: 톡채널 고객 문의에 자동으로 답한다. 근거는 사업자가 직접 쓴 답변과 톡채널에 올린 매장 정보·메뉴·최근 소식이다. 1:1 채팅에서 주문·예약 신청을 자동으로 접수하고, 운영 시간 모드('채팅 가능 시간만 응대' / '채팅 불가 시간만 응대' / '24시간 응대')를 고를 수 있다. 소상공인을 포함한 사업자의 응대 부담을 덜어 주는 것이 목적이다 [VENDOR]. [AI매터스](https://aimatters.co.kr/news-report/ai-news/32123/), [비즈워치](https://news.bizwatch.co.kr/article/mobile/2025/09/25/0044)
- **가격**: 이번 조사에서 미확인. 참고로 카카오는 톡채널 '챗봇' 이용요금을 무료로 전환한 적이 있다(시점 미확인): [카카오 보도자료](https://www.kakaocorp.com/page/detail/9756)
- 파트너 상담 솔루션을 톡채널에 연결하는 **상담톡** 가이드: [kakao business 가이드: 상담톡](https://kakaobusiness.gitbook.io/main/ad/cstalk)
- (맥락) 2026-06-16 카카오톡 대화 중 바로 질문하는 **'챗GPT 챗봇'**이 출시되었다. 판매자용이 아니라 소비자용 기능이다 [PRESS]. [아시아경제 2026-06-16](https://view.asiae.co.kr/article/2026061611122365853)

*해피톡(블룸에이아이)*
- AI 에이전트·채팅상담·챗봇·전화상담을 하나로 묶은 **통합 AICC**다. "채널톡 대비 약 50% 비용 절감"을 주장한다 [VENDOR 마케팅]. [해피톡](https://www.happytalk.io/). 챗봇 상품명은 '챗봇 다해줌': [해피톡 챗봇 다해줌](https://home.happytalk.io/chatbot-all)
- 2026-04-30 '브랜드 고객충성도 대상' AI 고객상담 플랫폼 부문에서 2년 연속 1위. 브랜드 어워드일 뿐 성과 지표는 아니다 [PRESS]. [서울경제TV](https://www.sentv.co.kr/article/view/sentv202604300096), [네이트뉴스](https://news.nate.com/view/20260430n20960)
- 공개 가격은 미확인.

*사이드톡*: 홈페이지·카카오톡·네이버톡톡의 반복 문의를 자동화하는 AI 고객상담 챗봇 [VENDOR]. [sidetalk.kr](https://sidetalk.kr/)

*국산 소형 RAG 챗봇 SaaS 가격(카탈로그에 올라온 정가) [VENDOR]*. 출처: GitHub에 공개된 '모두의창업 AI Solution Pack' 카탈로그([aghoc/modoAI-Solution-Pack goal-branding.md](https://github.com/aghoc/modoAI-Solution-Pack/blob/3d0c582ab6ddfb7fbc9c3e9df2a0bb8e96c80623/public/packs/goal-branding.md))
- Do:Namu-Agent **월 50,000원**(15M 토큰): 홈페이지·문서 업로드만으로 구축하는 범용 SaaS형 AI 챗봇
- Chatum AI **월 99,000원**: 소상공인·1인 업장용 다국어 문의 응대(인스타그램, WhatsApp, LINE)
- FELIQ RAG **월 399,000원**: 자체 데이터를 학습해 24시간 응답
- '다국어 AI Chatbot' **월 500,000원**: 매장·상품 정보를 학습한 24시간 다국어 상담, 카카오톡 연동
- AskMind: 문서 업로드형 AI 상담원, 2개월 맞춤 지원 방식
- Conma AI **월 12,900원**(Plus): 소셜미디어를 '마케팅+세일즈+CS 채널'로 바꿔 준다는 범용 AI

**B. 글로벌(주로 Shopify 계열) 솔루션**

*Fin(구 Intercom)*
- **가격 $0.99/outcome**, 대화당 1회 과금 [VENDOR]. [Intercom Pricing](https://www.intercom.com/pricing), [Fin Help Center: "Fin pricing: Outcomes"](https://fin.ai/help/en/articles/13975800-fin-pricing-outcomes)
- Intercom 외에 Zendesk·Salesforce·Freshworks·HubSpot 헬프데스크 위에서도 돈다. Intercom 밖에서 쓰면 **월 최소 50 outcomes** [3P]. [Macha: Fin pricing](https://www.getmacha.com/blog/intercom-fin-pricing)
- **회사·상태 변화**: Intercom은 2026-05-12 사명을 Fin으로 바꿨다(헬프데스크 제품명은 Intercom 유지) [3P/PRESS]. [Richpanel](https://www.richpanel.com/learn/fin-salesforce-acquisition-what-it-means-for-support-teams), [MarTech](https://martech.org/salesforce-acquires-fin-formerly-known-as-intercom/). **Salesforce 인수 계약 2026-06-15(약 $3.6B)**: [Salesforce 보도자료 2026-06-15](https://www.salesforce.com/news/press-releases/2026/06/15/salesforce-signs-definitive-agreement-to-acquire-fin/), [CNBC 2026-06-15](https://www.cnbc.com/2026/06/15/salesforce-ai-customer-service-fin-acquistion.html). **인수 완료 2026-09-10**: [Salesforce 보도자료 2026-09-10](https://www.salesforce.com/news/press-releases/2026/09/10/salesforce-completes-acquisition-of-fin/)
- **고객사 30,000곳 이상**, "업계 최고 수준 **평균 해결률 76%**" [VENDOR]. [Salesforce 2026-09-10](https://www.salesforce.com/news/press-releases/2026/09/10/salesforce-completes-acquisition-of-fin/), [Salesforce Ben](https://www.salesforceben.com/salesforce-acquires-fin-formerly-intercom-adding-30k-ai-customers/)
- **반론**: "Fin claims 76%; production lands at **45–53%**". 해결률은 지식베이스가 얼마나 완비·구조화되어 있는지에 거의 전적으로 좌우된다는 주장이다 [3P, 경쟁 제품 블로그라 독립 출처 아님]. [CloneDesk](https://clonedesk.ai/blog/intercom-fin-limitations)
- 인수 이후에도 $0.99 단가 유지 [3P]. [Macha](https://www.getmacha.com/blog/intercom-fin-explained)

*Gorgias AI Agent(Shopify 중심 헬프데스크)*
- 대부분 플랜은 해결 인터랙션당 **$0.90**, Starter(월결제)는 **$1.00** [VENDOR/3P]. [Gorgias 블로그: AI Agent Pricing](https://www.gorgias.com/blog/ai-agent-pricing), [Lindy](https://www.lindy.ai/blog/gorgias-pricing)
- 플랜별로 월 **90~2,500+** 자동화 인터랙션이 포함되고, 초과분은 **$1.50** [3P]. [Chatarmin](https://chatarmin.com/en/blog/gorgias-pricing), [MyAskAI](https://myaskai.com/blog/gorgias-ai-agent-pricing-explained)
- AI가 해결하면 **헬프데스크 티켓 요금과 AI 요금이 이중으로** 붙는다. 자동 해결 후 **72시간 안에** 고객이 사람 상담으로 넘어가면 헬프데스크 티켓으로만 과금 [3P]. [Chatarmin](https://chatarmin.com/en/blog/gorgias-pricing), [Macha](https://www.getmacha.com/blog/gorgias-ai-agent-explained)

*Zendesk AI agents*
- 해결당 약 **$2(종량제)** 또는 약 **$1.50(약정)** [3P]. [eesel](https://www.eesel.ai/blog/understanding-zendesk-ai-pricing-a-complete-pay-per-resolution-guide), [CorePiper](https://corepiper.com/blog/zendesk-ai-agent-pricing-2026/)
- **2026-05 해결 모델을 3단계로 재편**: Assisted Escalation(무료), Contained Resolution(무료, LLM 검증으로 확인 안 된 건), **Verified Resolution(과금)** [3P 설명, Zendesk 공식 문서로는 미확인]. [CorePiper](https://corepiper.com/blog/zendesk-ai-agent-pricing-2026/), [servicedeskagents](https://servicedeskagents.com/vs-zendesk/)
- Copilot은 상담원당 약 **$50** 추가. 2026-01부터 약정 초과분을 상한·유예 없이 자동 과금한다는 주장 [3P]. [CorePiper](https://corepiper.com/blog/zendesk-ai-agent-pricing-2026/), [Coworker](https://coworker.ai/blog/zendesk-ai-pricing)

*Tidio Lyro(SMB용 라이브챗+AI)*
- Lyro는 **월 $39(100 대화)**부터, 500~1,000 대화는 **$79~149** [3P]. [Featurebase](https://www.featurebase.app/blog/tidio-pricing), [Chatarmin](https://chatarmin.com/en/blog/tidio-pricing)
- Tidio 홈페이지는 **해결률 67%**를 주장한다 [VENDOR]. Premium(월 **$2,999~**)은 **해결률 50%를 보장**하고 미달 시 환불한다 [VENDOR, 3P 경유]. "대부분 스토어의 실제 해결률은 **40~60%**" [3P]. [MyAskAI](https://myaskai.com/blog/tidio-ai-complete-guide-2026), [Chatarmin](https://chatarmin.com/en/blog/tidio-pricing)
- "과금 미터가 3개로 나뉘어 $29 플랜이 월 $200를 넘길 수 있다" [3P]. [Chatarmin](https://chatarmin.com/en/blog/tidio-pricing). Tidio 자체 Lyro 리뷰 글 [VENDOR]: [Tidio blog](https://www.tidio.com/blog/lyro-review/)
- **주의(출처 간 불일치)**: 제3자 글마다 Tidio 플랜 가격 표기가 다르다(예: Chatarmin 제목 "$59 to $749, Nothing In Between", 다른 글은 "$29 플랜", "Premium $2,999~"). 플랜 구성이 자주 바뀌므로 tidio.com에서 재확인해야 한다. [Chatarmin](https://chatarmin.com/en/blog/tidio-pricing), [That Marketing Buddy](https://thatmarketingbuddy.com/pricing/tidio)

*기타*: Shopify 앱스토어에는 한국어로 노출되는 크로스보더용 AI 채팅 앱도 있다(예: 톡바이저 "해외 진출용 인공지능 채팅, 고객 관리"). 존재만 확인했고 성과·가격은 미확인: [Shopify App Store: 톡바이저](https://apps.shopify.com/talkvisor?locale=ko)

**C. 요약표(확인된 범위)**

| 도구 | 출시·상태 | 한국 셀러 적합성 | 최신 확인 가격 | 벤더 주장 성과 | 출처 |
|---|---|---|---|---|---|
| 채널톡 ALF / v2 | 2024-04 첫 출시, 2024-11-01 GA, v2 2025-11-06 | 스마트스토어 연동(주문조회·취소·반품), Shopify 앱 | 해결당 또는 참여당 과금(2025-11-28 개편, 단가 미확인) | 자사 CS 해결률 80%(추석 85%), 2,000사·130만 건 | [업데이트](https://docs.channel.io/updates/ko/articles/5cf93bf9-2024-11-01-ALF-%EC%A0%95%EC%8B%9D-%EC%B6%9C%EC%8B%9C-), [블로그](https://channel.io/ko/blog/articles/alfv2-cx-case-02942123), [MT](https://www.mt.co.kr/future/2025/11/06/2025110611161567414) |
| 카카오 카나나 상담매니저 | 2025-09-25 GA | 톡채널 운영 셀러·소상공인 | 미확인 | 미확인 | [카카오](https://www.kakaocorp.com/page/detail/11719) |
| 해피톡 | 운영 중(AICC) | 채팅·톡상담·전화 통합 | 미공개 | "채널톡 대비 50% 절감"(마케팅) | [해피톡](https://www.happytalk.io/) |
| Fin(구 Intercom) | GA, 2026-09-10 Salesforce 인수 완료 | 크로스보더·자사몰 | $0.99/outcome | 평균 76%(3P 관측 45~53%) | [Salesforce](https://www.salesforce.com/news/press-releases/2026/09/10/salesforce-completes-acquisition-of-fin/), [CloneDesk](https://clonedesk.ai/blog/intercom-fin-limitations) |
| Gorgias AI Agent | GA | Shopify 자사몰 | $0.90~1.00/해결, 초과 $1.50, 티켓비 별도 | 미수집 | [Gorgias](https://www.gorgias.com/blog/ai-agent-pricing) |
| Zendesk AI agents | GA, 2026-05 Verified Resolution 도입(3P) | 중견 이상 | $1.50~2.00/해결 + Copilot $50/인 | 미수집 | [CorePiper](https://corepiper.com/blog/zendesk-ai-agent-pricing-2026/) |
| Tidio Lyro | GA | 소형 Shopify·웹몰 | $39/100대화~, Premium $2,999/월 | 67%(3P 관측 40~60%) | [Chatarmin](https://chatarmin.com/en/blog/tidio-pricing) |

### Inferences
- **비용 감각(가정 기반)**: 월 문의 1,000건, AI 해결 50%, 환율 ₩1,400/$로 가정하면 다음과 같다.
  - Fin: 500×$0.99 ≈ $495(약 69만원) + Intercom 좌석료
  - Gorgias: 500×$0.90 ≈ $450(약 63만원) + 헬프데스크 티켓 요금(이중 과금)
  - Zendesk: 500×$1.5~2 ≈ $750~1,000(약 105만~140만원) + 좌석료
  - Tidio Lyro: 1,000대화 티어 약 $149(약 21만원, 해결 여부와 무관하게 대화당 과금)
  - 국산 정액형 RAG 챗봇: 월 5만~50만원

  1인~소형 셀러에게는 정액형·대화형이 예산을 예측하기 쉽다. 해결당 과금은 볼륨이 커질수록 선형으로 늘어난다.
- **'해결'의 정의가 벤더마다 다르다**: ALF는 24시간 내 상담원 연결 요청이 없으면, Gorgias는 72시간 규칙, Zendesk는 2026-05부터 LLM 검증(3P)으로 판단한다. 그래서 해결률을 서로 직접 비교하면 안 된다. 고객이 포기하고 떠난 대화도 '해결'로 잡힐 수 있으므로 **재문의율·CSAT·클레임 전환율**을 함께 봐야 한다. Zendesk가 '검증된 해결'만 과금하도록 바꾼 것(3P 보고)은 업계도 부풀려진 해결 지표를 인식하고 있다는 신호로 읽힌다.
- ALF의 단순 평균은 130만 건 ÷ 약 2,000사 ≈ **사당 연 650건(월 50여 건)**이다. 저볼륨 중소 도입사가 많다는 뜻으로 읽을 수 있지만, 분포는 알 수 없다.
- 채널톡 자사 CS 해결률 80~85%는 SaaS 기능 문의가 대부분인 환경에서 나온 수치다. 주문·배송·교환 문의가 많은 셀러 환경에 그대로 옮기기는 어렵다.
- 한국 마켓플레이스 셀러에게 핵심은 **문의가 들어오는 창구와의 연동**이다(스마트스토어 Q&A·톡톡, 쿠팡 문의, 카카오 톡채널). Gorgias·Fin 같은 Shopify 중심 도구가 국내 마켓 inbox와 네이티브로 연동된다는 근거는 찾지 못했다. 따라서 국내 셀러에게는 채널톡(스마트스토어 연동 확인), 카카오 카나나(톡채널), API 기반 DIY(2장)가 현실적이다. 글로벌 도구는 **Shopify 기반 크로스보더 자사몰**에 맞다.
- Fin의 Salesforce 편입(2026-09)으로 향후 가격·번들 정책이 바뀔 수 있다. 현재 단가는 유지되고 있다고 3P가 보고한다. 장기 계약 전에 재확인해야 한다.

### Gaps
- 채널톡 ALF의 **KRW 단가**, 2025-11-28 가격제 개편 내용(해결당→참여당 전환 여부), 무료 제공 건수: docs.channel.io가 차단되어 미확인.
- 해피톡·카나나 상담매니저·사이드톡의 가격.
- **네이버 톡톡의 판매자용 AI 답변·챗봇 기능**: 존재 여부, 출시일, 상태를 이번 조사에서 확인하지 못했다(검색 결과에 공식 문서가 나오지 않음).
- **Sendbird AI agent**: 가격, 한국 이커머스 사례 미수집.
- **Shopify Inbox(AI 추천 답변)·Shopify Sidekick**의 한국어 지원과 CS 기능 상태 미확인.
- CSAT, **챗 경유 구매전환율**, 매출 영향에 대한 벤더 사례 수치(Gorgias·Fin·채널톡 커머스 고객사) 미수집.
- Fin, Gorgias, Lyro의 한국어 응답 품질을 평가한 독립 자료 없음.

---

## 2. 마켓플레이스 문의 처리 AI화: 스마트스토어·쿠팡 상품문의 분류와 답변 초안, 리뷰 답글, 교환·반품·환불 triage

### Takeaway
스마트스토어(네이버 커머스API)와 쿠팡(Wing Open API) 모두 **공식 API로 문의 조회·답변 등록, 클레임(취소·반품·교환 요청) 조회**를 할 수 있다. 그래서 "수집 → LLM 분류 → 정책 근거 초안 → 사람 승인 → API로 등록" 파이프라인을 직접 만들 수 있고, 실제로 이렇게 만든 사례가 GitHub에 다수 있다([ANEC]). 시판 경로로는 채널톡(스마트스토어 연동과 ALF 주문조회·취소·반품), 브라우저 확장(REPLY AI 등), 크몽 외주가 있다. 공통 권장 원칙은 "**처음부터 자동 발송하지 말고 초안 → 운영자 확인**으로 시작하고, 금액·보상·정책 예외는 사람이 처리"하는 것이다. 플랫폼 자체의 판매자용 AI 답변 기능은 이번 조사에서 확인하지 못했다.

### Cited Findings
**A. 공식 API(오픈소스 코드에서 확인한 엔드포인트, [ANEC]이지만 공식 경로를 반영)**
- 네이버 커머스API
  - 고객문의 조회 `GET /v1/pay-user/inquiries`, 상품문의(Q&A) 조회 `GET /v1/contents/qnas`: [Peanut0711/easy-fulfill naver_commerce.py](https://github.com/Peanut0711/easy-fulfill/blob/7c97127563fcb7ebc8034c5b594f906781161790/naver_commerce.py)
  - 구매자 문의 답변 `POST /v1/pay-merchant/inquiries/{inquiryNo}/answer`: [naeil/dashboard-v2 ChannelSyncService.java](https://github.com/naeil/dashboard-v2/blob/679fd560d1bb081710beec3981a1a8e44e2833c8/src/main/java/naeil/dashboard/service/ChannelSyncService.java)
  - 상품 Q&A 답변 `PUT /v1/contents/qnas/{questionId}`: [snghnl/navercommerce tests](https://github.com/snghnl/navercommerce/blob/1fcb44ab52b9f410fbfcf1189fa1dff3c0aa7c70/tests/test_inquiries.py)
- 네이버 클레임 조회: `/v1/pay-order/seller/product-orders/last-changed-statuses`를 `CANCEL_REQUEST`·`RETURN_REQUEST`·`EXCHANGE_REQUEST`로 필터한다. **상품 Q&A는 별도 권한 그룹이 필요**하고 없으면 403이 난다: [Youn-hub-SM claims-poll.mjs](https://github.com/Youn-hub-SM/seamonster-meeting-notes/blob/f7aeacf5ddb91e7ce8fbcdeaa293623a3c13aad8/scripts/claims-poll.mjs)
- 네이버 API는 **서버 IP를 허용 목록에 등록**해야 한다. 미등록 시 `403 GW.IP_NOT_ALLOWED`: [Kohgane/proxy-commerce CLAUDE.md](https://github.com/Kohgane/proxy-commerce/blob/d05c1e7879bb4309bda423b62bbae4a60902c338/CLAUDE.md)
- 쿠팡 Wing Open API
  - 고객문의 조회 `GET /v2/providers/openapi/apis/api/v5/vendors/{vendorId}/onlineInquiries`(answeredType=NOANSWER 등): [halion125-co coupang_openapi_ko.json](https://github.com/halion125-co/populer125/blob/2495d891d57a912072eb47ffc1d9e5cb3203983d/docs/coupang_openapi_ko.json)
  - 답변 `POST …/v4/vendors/{vendorId}/onlineInquiries/{inquiryId}/replies`: [kyungdongseo/coupang cs.py](https://github.com/kyungdongseo/coupang/blob/f58b40a477f49734b5a6c3e4cd0398c86a931c68/cs.py), [tonykang22/hello-world-auto-store cs-manager](https://github.com/tonykang22/hello-world-auto-store/blob/246ab297d5097517657557b21144857c105132e6/cs-manager/src/main/java/com/github/kingwaggs/csmanager/sdk/coupang/service/CoupangMarketPlaceApi.java)
  - **쿠팡 고객센터 이관 문의**(`callCenterInquiries`): `NO_ANSWER`(답변 필요), `TRANSFER`(쿠팡 상담 완료 후 이관되어 판매자 확인이 필요한 건). 반품은 `status=RU/UC`, 교환은 `RECEIPT`: [claims-poll.mjs](https://github.com/Youn-hub-SM/seamonster-meeting-notes/blob/f7aeacf5ddb91e7ce8fbcdeaa293623a3c13aad8/scripts/claims-poll.mjs)
  - 제약(2026-04-23 공식 문서 확인 기록): 조회 기간은 **최대 7일 권장**(넘으면 타임아웃 위험). 답변은 `inquiryStatus=progress`이고 `partnerTransferStatus=requestAnswer`일 때만 가능: [modeumjeon-team-share coupang/inquiries.py](https://github.com/rnwhgowh2-commits/modeumjeon-team-share/blob/8efb326daf0cd5b11579d9b7df2ee3726a98f6b4/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8/_%EC%8B%9C%EC%8A%A4%ED%85%9C/shared/platforms/coupang/inquiries.py)
- 한 개발자의 운영 노트(공식 한도 아님) [ANEC]: 쿠팡은 vendorId당 초당 7건으로 운용(429를 피하려고 10에서 하향), 네이버는 초당 1.5건을 안전 마진으로 둔다. 429·5xx는 지수 백오프로 최대 3회 재시도: [Kohgane/proxy-commerce CLAUDE.md](https://github.com/Kohgane/proxy-commerce/blob/d05c1e7879bb4309bda423b62bbae4a60902c338/CLAUDE.md)

**B. 실제 DIY 클레임·문의 triage 사례 [ANEC]**
- **10분마다 cron**으로 네이버·쿠팡·카페24의 클레임(취소·반품·교환 요청)과 문의를 수집한다. 서버가 `(channel, claim_key)` 유니크 키로 중복을 거르고 **신규 건만 Teams 채널에 알림**을 보낸다. 조회 창은 40~48시간을 겹쳐서 되돌아본다. 함정: **카페24 토큰 `expires_at`에 시간대 표기가 없어** 9시간 오차가 생기고 인증이 조용히 실패한다. 카페24 클레임 코드는 C00/R00/E00. [claims-poll.mjs](https://github.com/Youn-hub-SM/seamonster-meeting-notes/blob/f7aeacf5ddb91e7ce8fbcdeaa293623a3c13aad8/scripts/claims-poll.mjs)
- **n8n + Gemini CS 워크플로 설계서**: 스마트스토어·쿠팡·11번가의 Q&A와 리뷰를 매일 크롤링한다. 매뉴얼에 없는 반복 질문이 임계치를 넘으면 Gemini가 보충 답변 초안을 만들고, 사람이 1클릭 승인하면 Notion 매뉴얼이 갱신되며 잔디(JANDI)로 알림이 간다. "수작업 90% 감소"를 주장하지만 설계 목표치일 뿐 실측이 아니다: [USEONGEE/n8n-example cs_워크.txt](https://github.com/USEONGEE/n8n-example/blob/8d817d796e277931d4ecd47aaad930bf3afcca9c/docs/specs/cs_%EC%9B%8C%ED%81%AC.txt)

**C. 시판·외주 도구**
- **채널톡**: 스마트스토어 문의를 채널톡에서 답변하고, ALF로 주문 조회·취소·반품 처리 [VENDOR]. [채널톡 도움말](https://docs.channel.io/help/ko/articles/%EB%84%A4%EC%9D%B4%EB%B2%84-%EC%8A%A4%EB%A7%88%ED%8A%B8%EC%8A%A4%ED%86%A0%EC%96%B4-6d4e4039)
- **REPLY AI 크롬 확장**("스마트스토어·ESM 리뷰 자동 답글"): 스마트스토어를 포함한 6개 플랫폼 지원. OpenAI·Claude·Gemini 중 하나의 **API 키를 직접 발급**받아야 한다(검색 요약 기반, 가격·사용자 수는 미확인). [Chrome Web Store](https://chromewebstore.google.com/detail/reply-ai-%E2%80%94-%EC%8A%A4%EB%A7%88%ED%8A%B8%EC%8A%A4%ED%86%A0%EC%96%B4%C2%B7esm-%EB%A6%AC%EB%B7%B0/ckpidhkombkcdkckaaehbphcgbbfejai)
- **개인이 만든 크롬 확장(스마트스토어 리뷰·상품문의 답글)** [ANEC]: Gemini 등으로 답글을 만들어 셀러센터에 자동으로 채워 넣고 제출한다. 공식 커머스API가 아니라 **브라우저 자동화** 방식이다. 베타 v1.3.31이고, 베타 사용자는 토스페이먼츠로 구독 결제한다(2026-06 생성, 2026-09 업데이트). [Dodam09/naver-smartstore-review-reply](https://github.com/Dodam09/naver-smartstore-review-reply)
- 외주·수요 신호 [ANEC]: 크몽 "2025 N사 AI 질문 자동 답변 프로그램": [크몽](https://kmong.com/gig/637515). 위시켓 "AI 답변으로 쇼핑몰(스마트스토어) 리뷰 및 답…" 프로젝트: [위시켓](https://www.wishket.com/project/similar-case-search/share/8S5EOegpo8oV3wE2/)

**D. 운영 원칙(국내 실무 가이드)**
- 현실적인 시작은 "문의를 읽고 **분류 → 답변 초안 → 운영자 확인**" 순서다. "처음부터 고객에게 답변을 보내는 방식으로 시작하면 위험"하다. 분류 예시는 배송·교환·환불·상품문의·제휴문의다. **정책·금액·배송일·보상**처럼 고객 피해가 생길 수 있는 답변은 운영자가 확인한다. **불만 표현, 주문번호가 필요한 상황, 정책 예외**는 상담원에게 넘기는 기준을 명확히 한다. [애드펄스 인사이트](https://www.addpulse.co.kr/insight/detail.php?slug=ai-inquiry-classification). 관련 개괄: [하우콘텐츠 "쇼핑몰 운영에 AI 자동화를 적용할 수 있는 업무 7가지"](https://howcontent.co.kr/blog/ecommerce-ai-automation-use-cases)

### Inferences
- **1인~중소 셀러용 권장 파이프라인**(위 출처 조합):
  1. 공식 API 키를 발급받는다. 네이버는 앱 등록, 서버 IP 허용, Q&A 권한 그룹 신청이 필요하고, 쿠팡은 vendorId와 Access/Secret 키가 필요하다.
  2. 10~15분 주기로 미답변 문의와 클레임을 수집하고 키 기준으로 중복을 제거한다.
  3. LLM으로 분류한다(배송/교환/반품/환불/상품/기타 + 긴급도·감정).
  4. 정책 문서(RAG)를 근거로 초안을 만들고 근거 문장을 첨부한다.
  5. 저위험 유형(배송 조회 안내, 재입고, 사이즈 정보)만 자동 발송한다. 금액·보상·예외 건은 Slack·Teams·잔디에서 사람이 승인한다.
  6. 승인된 답변을 API로 등록한다.
  7. 매주 오답을 리뷰하고 지식베이스를 갱신한다.
- 쿠팡 `TRANSFER`(쿠팡 상담 후 이관된 건)는 이미 한 번 응대를 거친 고객이다. 자동 답변에서 빼고 사람이 우선 처리하는 편이 안전하다.
- 브라우저 자동화형 확장과 크롤링 기반 수집은 셀러센터 UI가 바뀌면 깨지고, 계정 보안·약관 문제가 생길 수 있다. 공식 API가 있는 작업(문의·Q&A·클레임)은 **API 경로를 우선**하는 것이 합리적이다.
- 리뷰 답글 자동화는 기술 장벽이 가장 낮다(크롬 확장 + 개인 API 키). 다만 템플릿처럼 똑같은 답글이나, 보상·교환을 약속하는 환각 답글이 달리면 공개적으로 박제된다. 불만 리뷰(저평점)는 초안 모드로 운영하는 편이 좋다.
- 클레임 triage의 1차 가치는 LLM이 아니라 **누락 방지(알림)**에 있다. LLM은 사유 분류(단순변심·불량·오배송)와 회신 초안에 얹는 구조가 비용 대비 효과적이다.

### Gaps
- **네이버(스마트스토어센터·톡톡)·쿠팡 윙의 판매자용 네이티브 AI 기능**(AI 답변 추천, 리뷰 답글 AI 등): 존재 여부, 출시일, 상태 미확인.
- 11번가, G마켓/옥션(ESM), 카카오 톡스토어·선물하기, 무신사·29CM·에이블리·지그재그·오늘의집·컬리 파트너센터의 AI CS 기능과 문의 API 제공 여부 미확인.
- 문의 응답 속도가 판매자 등급·노출에 주는 공식 기준 미확인.
- AI 리뷰 답글의 매출·평점 영향, 문의 AI의 전환율에 대한 정량 데이터 없음.
- 사방넷·이지어드민 등 OMS의 CS 통합 기능과 AI 초안 기능 미확인(3장).

---

## 3. 백오피스 자동화: OMS·통합관리 AI 기능, 멀티마켓 대량등록과 AI 리라이팅·번역, 정산 대사, 노코드+LLM, 범용 AI 에이전트

### Takeaway
국내 통합관리(OMS) 5사(사방넷·플레이오토·셀러허브·이지어드민·샵링커)의 AI 기능과 가격은 **이번 세션에서 1차 확인하지 못했다**(검색 한도 소진, 도메인 차단). 확인한 것은 네 가지다. (a) 1인 셀러의 수작업 기준선은 하루 약 6시간이고 그중 주문 확인·송장 입력이 4시간이다([ANEC]). (b) 상용 OMS 비용 부담(사방넷 연 120만원 이상이라는 주장)과 이를 대체하려는 오픈소스·DIY 흐름이 있다. (c) 공식 API를 통합할 때 실무 함정이 있다(IP 허용, 레이트리밋, 키 승인, 부분 실패 검증). (d) AI 상세페이지·번역 SaaS는 월 9.9만~15만원대다. 2026년에 셀러가 **Claude·Gemini·n8n으로 자체 운영 도구를 만든 사례**가 GitHub에 여럿 올라와 있지만, 성과 수치는 모두 목표치이고 실측이 아니다.

### Cited Findings
- **상용 OMS 비용 인식**: "사방넷 같은 서비스는 **연 120만원 이상(약 $900)**"이라 1인 창업자에게 부담이라는 주장. 오픈소스 README의 주장이고 공식 가격이 아니다 [ANEC]. [hyojae04/FreeSeller](https://github.com/hyojae04/FreeSeller)
- **FreeSeller**(2026-06 생성, 오픈소스, 로컬 우선): 스마트스토어·쿠팡 WING·SSG.COM·롯데ON·카카오톡스토어에 상품을 동기화한다. 27개 필드짜리 표준 엑셀 템플릿을 쓰고 필수 필드 11개를 검증한다. (몰코드+상품코드) 복합키로 업데이트를 관리하고 공식 API를 쓴다. AI 기능은 없다 [ANEC]. [GitHub](https://github.com/hyojae04/FreeSeller)
- **1인 셀러 수작업 기준선**(제품 기획서 PRD, 2026-02-05) [ANEC]
  - 하루 **6시간**: 아침 2h(스마트스토어·쿠팡 등 3개 채널에 로그인해 주문 확인, 채널당 20분 + 엑셀 취합), 오후 2h(송장번호를 채널마다 수기 입력), 저녁 2h(네이버 트렌드·경쟁사 조사).
  - 페인포인트: 다채널 로그인, 재고 계산 오류로 인한 과재고·품절, 가격 대응 지연.
  - 타깃: **월매출 1천만~5천만원 1인 사업자**, 그다음 2~5인 팀.
  - 목표: 90% 단축(6h→30분), 재고회전 30일→20일, 품절률 5% 이하. 모두 목표치다.
  - [minjae-488/MARK-1 PRD](https://github.com/minjae-488/MARK-1/blob/675f9ecae296360efd003fbe908d84441925d31d/PRD.md)
- **멀티마켓 API 통합의 실무 함정**(Claude Code로 운영하는 저장소의 CLAUDE.md) [ANEC]
  - 네이버 IP 허용 목록(403 `GW.IP_NOT_ALLOWED`)
  - **11번가는 API 키 발급·승인이 필요**하고 며칠 걸릴 수 있다
  - `GNCP-GW-RateLimit-Remaining` 헤더로 남은 호출량을 로깅한다
  - 자격증명은 하드코딩하지 않고 암호화해 저장한다
  - 대량 업로드 후 재조회로 실제 반영을 검증하고, "성공/실패 분리 집계 + failedItems 반환"으로 실패 항목만 재시도한다. 가짜 성공 보고를 금지한다
  - AI로 코드를 쓸 때는 "API=문서 정밀 확인 후 코딩(추측 금지)"을 규칙으로 둔다
  - [Kohgane/proxy-commerce CLAUDE.md](https://github.com/Kohgane/proxy-commerce/blob/d05c1e7879bb4309bda423b62bbae4a60902c338/CLAUDE.md)
- **다채널·크로스보더 리스팅 운영 로그**(2026-09-06) [ANEC]
  - 채널별 상세를 정규화한다: 스마트스토어는 `originProduct.name`/`detailContent`와 ko-KR, 쿠팡은 **제목 100자**와 `items[].contents`.
  - '외부 승인'이 채널 게시, 법규 적합성, 실물 확인을 뜻하지 않는다고 명시한다.
  - 게시 전 게이트와 조정(reconciliation) 대기 건을 따로 관리한다. 대상 채널은 Qoo10·Lazada·Shopee·eBay·Temu·11번가 등이다.
  - [couplit-korean/sellerpilot-global](https://github.com/couplit-korean/sellerpilot-global) (docs/Aside-운영진행-20260906.md)
- **위탁·도매 소싱→등록 자동화 시도**: 도매꾹에서 스마트스토어 등록을 준비하는 MVP("safe browser-harness preview flow") [ANEC]. [aiebrain/domeggook-smartstore-mvp](https://github.com/aiebrain/domeggook-smartstore-mvp)
- 셀러가 직접 만든 '스킬' 모음 "various skills i made for naver smartstore"(2026-05). AI 에이전트 스킬로 보이지만 확인하지 못했다 [ANEC]: [cyoon84/smartstore-project](https://github.com/cyoon84/smartstore-project). 소싱·풀필먼트 에이전트를 'AI 직원'으로 구성해 테스트한 저장소도 있다 [ANEC]: [seiyeolo/ai-employee-memory](https://github.com/seiyeolo/ai-employee-memory)
- **노코드+LLM**: n8n이 스마트스토어·쿠팡·11번가 Q&A와 리뷰를 수집하고 Gemini가 분석·초안을 만들며, 사람 승인 후 Notion에 반영하고 잔디로 알린다. "매출 집계·Q&A 수집 수작업 90% 감소"는 목표 주장이다 [ANEC]. [USEONGEE/n8n-example](https://github.com/USEONGEE/n8n-example/blob/8d817d796e277931d4ecd47aaad930bf3afcca9c/docs/specs/cs_%EC%9B%8C%ED%81%AC.txt)
- **AI 상세페이지·광고소재·번역 SaaS 가격**(카탈로그 정가) [VENDOR]. 출처: [modoAI-Solution-Pack](https://github.com/aghoc/modoAI-Solution-Pack/blob/3d0c582ab6ddfb7fbc9c3e9df2a0bb8e96c80623/public/packs/goal-branding.md)
  - 크리에이지(Creazy) **월 99,000원**(프로): "상품 사진만 올리면 1분 만에 상세페이지"
  - 모스트(Moast) **월 150,000원**(Max): 메타·네이버·구글 광고 소재와 상세페이지 생성
  - 딜리버리아이오(Dealivery) **월 148,000원**(Pro): AI 다국어 번역을 지원하는 수출 특화 자사몰
  - TasteQ **월 100,000원**: AI 개인화 추천
  - AI 더빙·자막 각 **월 300,000원**

### Inferences
- 1인 셀러 시간 사용의 큰 덩어리(주문 수집·송장 입력 4h/일, [ANEC] 기준)는 **LLM이 아니라 OMS·API 연동**이 없애는 영역이다. 순서는 ① OMS(또는 API 동기화)로 주문·송장·재고를 먼저 자동화하고, ② 그 위에 LLM을 **예외 처리(클레임 사유 분류), 문의 초안, 상품명·상세 리라이팅·번역**에 얹는 것이 합리적이다.
- DIY 경로(Claude·코딩 에이전트, n8n)는 구독료가 낮다. 대신 IP 허용, 레이트리밋, 토큰 시간대, 부분 실패 검증 같은 **운영 부채**가 크다. 개발 역량이 있는 중소 브랜드에는 맞지만, 비개발 1인 셀러에게는 SaaS나 OMS가 안전하다.
- AI로 쓴 상세·번역은 '게시 전 사람 검수 게이트'(표시광고 법규, 실물 일치, 채널별 글자 수 제한)를 표준 절차로 두어야 한다. sellerpilot 운영 로그가 이 관행을 보여 준다.

### Gaps
아래는 모두 **미확인 사항이거나, 배경지식(2026-06 이전)에서 나온 단서라 반드시 재확인해야 하는** 항목이다.
- **사방넷·플레이오토·셀러허브·이지어드민·샵링커**: AI 기능(AI 상품명·상세 리라이팅, 번역, CS 초안, 수요예측), 출시일, 현재 요금.
- **정산·회계 대사 자동화**: 셀러봇캐시 등 정산예정금 조회 도구, 캐시노트류, 마켓별 정산 파일 대사와 LLM 활용.
- **Make·Zapier·n8n**: 2026 요금과 AI 에이전트 기능(n8n 셀프호스트 무료 여부 등).
- **범용 AI 에이전트의 스토어 운영 활용**
  - ChatGPT agent: 2025년 7월 출시로 기억한다. 브라우저를 조작하는 에이전트다.
  - Claude: 브라우저·스프레드시트 연동 기능과 Claude Code를 활용한 내부 도구 제작(위 GitHub 사례로 간접 확인).
  - Gemini in Google Sheets: AI 함수와 사이드패널.
  - Shopify Sidekick: 관리자용 AI 어시스턴트. 2025년 에디션에서 에이전트 기능이 확대된 것으로 기억한다. 한국어 지원은 미확인.
  - Amazon Project Amelia: 2024-09 Amazon Accelerate에서 미국 일부 셀러 대상 베타로 발표된 것으로 기억한다. 이후 'Seller Assistant'의 에이전트 기능으로 확장되었다는 보도를 기억하지만 미확인.
  - 위 항목들의 **상태, 가격, 한국(또는 Amazon Global Selling 셀러) 가용성**은 이번 세션에서 1차 확인하지 못했다.
- 셀러센터 로그인 정보를 범용 브라우저 에이전트에 맡길 때의 보안·약관 이슈에 대한 플랫폼 공식 입장 미확인.
- 카페24(예: AI 상세·배너 도구), 아임웹·식스샵·고도몰의 AI 운영 기능 미확인.

---

## 4. 셀러 분석 AI: 자연어 리포팅, 이상 탐지, 주간 KPI 요약

### Takeaway
확인된 1차 정보는 **국산 통합 대시보드 SaaS의 정가** 정도다. 예를 들어 AdSync는 광고(메타·구글·네이버·카카오)와 판매 채널(스마트스토어·쿠팡·자사몰)을 API로 모아 월 9.9만/24.9만/49만원을 받는다. 플랫폼 네이티브 기능(네이버 비즈어드바이저, 쿠팡, 카페24, Shopify Sidekick, Amazon)의 자연어 질의·이상 탐지·주간 요약은 이번 세션에서 확인하지 못했다. 소규모 셀러가 현실적으로 쓸 수 있는 방법은 "OMS·마켓 데이터 → 시트 → LLM 요약" 같은 DIY 조합이다(추론).

### Cited Findings
- **AdSync(애드싱크)** [VENDOR]: 온라인 광고 채널과 커머스 매출 채널 데이터를 **API로 자동 수집해 하나의 대시보드에서 통합 조회**하는 "AI 기반 마케팅 성과 분석 솔루션". **Basic 월 99,000원 / Pro 249,000원 / Enterprise 490,000원**. [modoAI-Solution-Pack 카탈로그](https://github.com/aghoc/modoAI-Solution-Pack/blob/3d0c582ab6ddfb7fbc9c3e9df2a0bb8e96c80623/public/packs/goal-branding.md)
- 같은 카탈로그의 성과·평판 분석 계열 [VENDOR]
  - MA-HA 월 39,000원: "365일 24시간 일하는 AI 퍼포먼스마케터"
  - 픽켓팅(Picketing) 월 490,000원: AI 광고 자동 최적화
  - Insight Page 월 95,000원: 뉴스·블로그·SNS·카페 평판 모니터링
  - LALA 월 250,000원: 댓글 모니터링과 위기 알림
  - [modoAI-Solution-Pack](https://github.com/aghoc/modoAI-Solution-Pack/blob/3d0c582ab6ddfb7fbc9c3e9df2a0bb8e96c80623/public/packs/goal-branding.md)
- DIY 집계 [ANEC]: n8n 설계서의 목표는 "매출 집계 수작업 90% 감소"다(실측 아님). [USEONGEE/n8n-example](https://github.com/USEONGEE/n8n-example/blob/8d817d796e277931d4ecd47aaad930bf3afcca9c/docs/specs/cs_%EC%9B%8C%ED%81%AC.txt). 'AI 직원'에게 "오늘 판매 실적"(예: 쿠팡 15건×19,900원, 스마트스토어 8건…)을 대화로 넣어 집계하게 하는 테스트 시나리오도 있다. [seiyeolo/ai-employee-memory](https://github.com/seiyeolo/ai-employee-memory)
- 멀티마켓 데이터를 모으는 관점에서 셀러용 무료 **수수료·마진 계산기**가 오픈소스로 나와 있다(13개 마켓 수수료 계산기, 실마진·손익분기 도구) [ANEC]. [hana108789-png/marketfee](https://github.com/hana108789-png/marketfee), [Kim-BanSeok/seller-margin-lab](https://github.com/Kim-BanSeok/seller-margin-lab)

### Inferences
- 1인~소형 셀러가 저비용으로 만드는 '주간 KPI 요약' 구성 예시(추론):
  1. OMS 또는 마켓 API·엑셀로 주문·클레임·광고비를 매일 스프레드시트에 적재한다.
  2. 전주 대비 매출·주문수·객단가·반품률·광고 ROAS 변화율을 수식으로 계산한다.
  3. LLM에 "±X% 이상 변화 항목과 원인 후보(상품·채널·광고)"만 요약하게 한다.
  4. 결과를 메신저로 보낸다.

  LLM에 원자료 계산을 맡기지 말고 **계산은 수식, 해석은 LLM**으로 나누는 편이 환각 위험이 적다.
- 광고와 매출을 통합하는 대시보드(월 10만~50만원)는 광고비 규모가 큰 중소 브랜드에 맞다. 광고비가 적은 1인 셀러에게는 과할 수 있다.

### Gaps
- **플랫폼 네이티브 AI 분석**(네이버 비즈어드바이저·스마트스토어 통계의 AI 기능, 쿠팡 윙 판매 분석, 카페24 애널리틱스 AI, Shopify Sidekick의 자연어 리포트, Amazon Seller Central AI 인사이트)의 기능, 출시일, 한국 가용성 미확인.
- 해외 커머스 분석 SaaS(Triple Whale·Polar 등)의 AI 기능과 가격 미수집.
- 이상 탐지·예측(품절·반품 급증) 도구가 내는 실측 성과 데이터 없음.

---

## 5. 주의 사례와 가드레일: Klarna 번복, Air Canada 판결, 정책 환각, 고객 정서 데이터

### Takeaway
AI 상담의 대표 성공 사례였던 **Klarna는 2025년 5월 "비용 중심 평가가 품질 저하를 불렀다"고 인정하고 사람 상담을 다시 늘렸다.** **Air Canada 판결(2024-02)**은 챗봇이 한 말에 기업이 책임진다는 원칙을 세웠다. **Cursor 'Sam' 사건(2025-04)**은 지원 봇이 존재하지 않는 정책을 지어내 실제 구독 해지로 이어진 사례다. Gartner의 2024~2026 연속 서베이도 같은 방향을 가리킨다. 고객의 64%는 기업이 AI를 쓰지 않기를 원했고(2024), 87%는 사람 연결 옵션이 필수라고 답했다(2026). 챗봇에서 나쁜 경험을 한 뒤 다시 쓰겠다는 고객은 27%에 그쳤다(2026). 가드레일의 핵심은 사람 연결, 범위 제한(금액·보상·정책 예외 금지), 지식베이스 위생, AI 응답 표시, 그리고 '해결률'이 아닌 품질 지표를 모니터링하는 것이다.

### Cited Findings
**A. Klarna(2024 주장 → 2025 부분 번복)**
- 2024-02 OpenAI 기반 어시스턴트를 글로벌 출시. 첫 달 **230만 건** 대화, "상담원 약 **700명분**", 해결 시간 **11분→2분 미만**, 반복 문의 **25%↓**, 2024년 **$40M 이익 개선** 전망 [VENDOR, Klarna 자체 발표를 2차 출처가 인용]. [Bigeye](https://www.bigeye.com/blog/klarnas-ai-customer-service-deployment), [CX Dive](https://www.customerexperiencedive.com/news/klarna-reinvests-human-talent-customer-service-AI-chatbot/747586/)
- 2025-05-08 CEO 세바스티안 시에미아트코프스키가 Bloomberg에 말했다: "As cost unfortunately seems to have been a too predominant evaluation factor when organizing this, what you end up having is **lower quality**." 고객이 **언제든 사람과 대화할 수 있게** 하겠다며 "Uber 방식"의 프리랜서형 상담원 채용을 추진했다 [PRESS]. [CX Dive](https://www.customerexperiencedive.com/news/klarna-reinvests-human-talent-customer-service-AI-chatbot/747586/), [Forbes 2025-05-18](https://www.forbes.com/sites/quickerbettertech/2025/05/18/business-tech-news-klarna-reverses-on-ai-says-customers-like-talking-to-people/), [eMarketer](https://www.emarketer.com/content/klarna-backtracks-ai-customer-service-plans)
- 이후 "공격적인 AI 인력 감축이 지나쳤다"며 미국 IPO 이후 채용을 재개했다고 보도되었다 [PRESS, 2차]. [MLQ News](https://mlq.ai/news/klarna-ceo-admits-aggressive-ai-job-cuts-went-too-far-starts-hiring-again-after-us-ipo/). "human customer service will almost be seen as a **VIP thing**"라는 CEO 발언이 인용되는데, 원 발언의 시점·매체는 미확인이다(2차 블로그는 2026-06 프레이밍으로 소개). [Perspective AI](https://getperspective.ai/blog/klarna-ai-customer-service-replacing-700-agents-conversational-ai-case-study)

**B. 법적 책임: Moffatt v. Air Canada(BC 민사분쟁조정심판소, 2024-02) [IND]**
- 챗봇이 "탑승 후 90일 안에 신청하면 유족 할인(bereavement fare)을 소급 적용받는다"고 잘못 안내했다. Air Canada는 챗봇이 "별개의 주체"라고 항변했지만 기각되었다. 심판소는 합리적 주의로 표시가 정확하도록 할 의무를 인정했고 **CA$812.02** 배상을 명령했다. [ABA Business Law Today 2024-02](https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-february/bc-tribunal-confirms-companies-remain-liable-information-provided-ai-chatbot/), [McCarthy Tétrault](https://www.mccarthy.ca/en/insights/blogs/techlex/moffatt-v-air-canada-misrepresentation-ai-chatbot), [CBC](https://www.cbc.ca/amp/1.7116416)

**C. 정책 환각·탈선 사례**
- **Cursor 'Sam'(2025-04)**: 로그아웃 버그(세션 경합 조건)를 설명하면서 AI 지원 봇이 "구독당 기기 1대"라는 **존재하지 않는 정책**을 지어냈다. Reddit·HN에서 확산되며 실제 구독 해지가 발생했다. 회사는 사과하고 환불했으며, **이메일 지원의 AI 응답에 AI라고 명시**하도록 절차를 바꿨다 [IND 사건DB/PRESS]. [WinBuzzer 2025-04-22](https://winbuzzer.com/2025/04/22/cursor-ais-support-bot-hallucinates-policy-sparking-user-backlash-and-company-apology-xcxwbn/), [AI Incident Database #1039](https://incidentdatabase.ai/cite/1039/)
- 기타 사례(사례 모음 저장소 기준) [ANEC 정리 + 언론 링크]:
  - **DPD 챗봇**(2024-01): 욕설을 하고 자사를 "최악의 배송 서비스"라고 비꼬는 시를 썼다. 조회 130만+ 확산.
  - **쉐보레 딜러 챗봇**: 프롬프트 인젝션에 넘어가 2024 Tahoe를 **$1**에 판다고 '합의'했다.
  - **NYC MyCity 챗봇**(2024): 불법적인 노무 조언.
  - **McDonald's–IBM 드라이브스루 AI**(2024-06 종료): 치킨너겟 260개 주문 등 오주문.
  - [vectara/awesome-agent-failures](https://github.com/vectara/awesome-agent-failures)

**D. 고객 정서·업계 전망(Gartner) [IND 서베이, 단 예측(prediction)은 전망치]**

| 발표일 | 내용 | 출처 |
|---|---|---|
| 2024-07-09 | 고객 5,728명(2023-12 조사) 중 **64%**가 기업이 CS에 AI를 쓰지 않기를 원함. **53%**는 AI를 쓰면 경쟁사 전환을 고려. 우려 사항: 사람 연결이 어려워짐 60%, AI 답변 불신 42%, 일자리 우려 46%. CS 리더 60%는 AI 도입 압박을 받음 | [Gartner](https://www.gartner.com/en/newsroom/press-releases/2024-07-09-gartner-survey-finds-64-percent-of-customers-would-prefer-that-companies-didnt-use-ai-for-customer-service) |
| 2024-12-09 | CS 리더 **85%**가 2025년 고객 대면 대화형 GenAI를 탐색하거나 파일럿 예정 | [Gartner](https://www.gartner.com/en/newsroom/press-releases/2024-12-09-gartner-survey-reveals-85-percent-of-customer-service-leaders-will-explore-or-pilot-customer-facing-conversational-genai-in-2025) |
| 2025-03-05 | (예측) 2029년까지 에이전틱 AI가 일반 CS 이슈의 **80%**를 사람 개입 없이 해결 | [Gartner](https://www.gartner.com/en/newsroom/press-releases/2025-03-05-gartner-predicts-agentic-ai-will-autonomously-resolve-80-percent-of-common-customer-service-issues-without-human-intervention-by-20290) |
| 2025-06-10 | (예측) 2027년까지 CS 인력을 크게 줄이려던 조직의 **50%**가 계획을 포기. 2025-03 리더 163명 폴에서 **95%**가 사람 상담원 유지 계획 | [Gartner](https://www.gartner.com/en/newsroom/press-releases/2025-06-10-gartner-predicts-50-percent-of-organizations-will-abandon-plans-to-reduce-customer-service-workforce-due-to-ai), [CMSWire](https://www.cmswire.com/the-wire/gartner-predicts-50-of-organizations-will-abandon-plans-to-reduce-customer-service-workforce-due-to-ai/) |
| 2025-09-10 | (예측) 2028년까지 Fortune 500 중 사람 CS를 완전히 없앤 기업은 **0곳** | [Gartner](https://www.gartner.com/en/newsroom/press-releases/2025-09-10-gartner-predicts-none-of-the-fortune-500-companies-will-have-fully-eliminated-human-customer-service-by-2028) |
| 2025-12-02 | AI 때문에 상담 인력을 실제로 줄인 CS 리더는 **20%**뿐 | [Gartner](https://www.gartner.com/en/newsroom/press-releases/2025-12-02-gartner-survey-finds-only-20-percent-of-customer-service-leaders-report-ai-driven-headcount-reduction) |
| 2026-02-03 | (예측) AI 때문에 CS 인력을 줄인 기업의 **절반이 2027년까지 재채용**(직함은 달라짐). 최근 감원은 AI보다 거시경제 영향이 컸다는 분석 | [Gartner](https://www.gartner.com/en/newsroom/press-releases/2026-02-03-gartner-predicts-half-of-companies-that-cut-customer-service-staff-due-to-ai-will-rehire-by-2027), [CX Dive](https://www.customerexperiencedive.com/news/ai-driven-customer-service-cuts-gartner-predicts-rehiring/830114/) |
| 2026-07-08 | 고객이 기업 제공 챗봇보다 **서드파티 GenAI(ChatGPT 등)**를 CS에 쓸 가능성이 약 **3배** | [Gartner](https://www.gartner.com/en/newsroom/press-releases/2026-07-08-gartner-survey-finds-customers-are-three-times-more-likely-to-use-third-party-genai-than-company-provided-chatbots-for-customer-service) |
| 2026-08-04 | 고객 3,566명(2026-02~03 조사) 중 **87%**가 GenAI로 CS를 하는 기업은 **사람 상담원 연결 옵션이 필수**라고 답함. GenAI 덕에 상호작용이 쉬워졌다는 응답은 **50%** | [Gartner](https://www.gartner.com/en/newsroom/press-releases/2026-08-04-gartner-survey-finds-87-percent-of-customers-say-companies-using-genai-for-customer-service-must-provide-access-to-a-human-agent0), [Insurance-Canada](https://insurance-canada.ca/2026/08/20/gartner-ai-customer-service-human-agents/) |
| 2026-09-02 | 챗봇에서 나쁜 경험을 한 뒤 다시 쓰겠다는 고객 **27%**. 기업이 챗봇을 제공했다면 썼을 것이라는 응답 49%인데, 최근 서비스 접점에서 실제로 챗봇을 쓴 고객은 **7%** | [Gartner](https://www.gartner.com/en/newsroom/press-releases/2026-09-02-gartner-finds-only-27-percent-of-customers-would-try-a-chatbot-again-after-a-negative-experience), [MacTech](https://www.mactech.com/2026/09/08/gartner-only-27-of-customers-would-try-a-chatbot-again-after-a-negative-experience/) |

**E. 벤더 해결률 vs 관측치(과장 경고)**
- Fin: 벤더 76% vs 제3자 관측 45~53%(경쟁사 블로그). [Salesforce](https://www.salesforce.com/news/press-releases/2026/09/10/salesforce-completes-acquisition-of-fin/), [CloneDesk](https://clonedesk.ai/blog/intercom-fin-limitations)
- Tidio Lyro: 벤더 67% vs "대부분 40~60%"(3P). Premium의 보장선은 50%. [Chatarmin](https://chatarmin.com/en/blog/tidio-pricing)

**F. 가드레일 실무(국내 가이드·사례에서 확인된 것)**
- 정책·금액·배송일·보상 답변은 운영자가 확인한다. 불만, 주문번호가 필요한 문의, 정책 예외는 사람에게 이관한다. 처음부터 자동 발송하지 않는다. [애드펄스](https://www.addpulse.co.kr/insight/detail.php?slug=ai-inquiry-classification)
- AI 응답임을 표시한다(Cursor의 사후 조치). [WinBuzzer](https://winbuzzer.com/2025/04/22/cursor-ais-support-bot-hallucinates-policy-sparking-user-backlash-and-company-apology-xcxwbn/)
- 사람 연결 옵션을 상시 제공한다(Klarna의 재설계, Gartner 87%). [CX Dive](https://www.customerexperiencedive.com/news/klarna-reinvests-human-talent-customer-service-AI-chatbot/747586/)
- 게시 전 검수 게이트를 두고 부분 실패를 정직하게 보고한다(가짜 성공 금지) [ANEC]. [Kohgane/proxy-commerce](https://github.com/Kohgane/proxy-commerce/blob/d05c1e7879bb4309bda423b62bbae4a60902c338/CLAUDE.md), [sellerpilot-global](https://github.com/couplit-korean/sellerpilot-global)

### Inferences
- **셀러용 가드레일 체크리스트**(위 사례를 종합):
  1. 봇의 범위를 명시적으로 제한한다. 배송 조회, 교환·반품 '절차' 안내, 상품 스펙은 허용하고, 환불 금액, 보상, 예외 승인, 법적 판단은 금지한다.
  2. 환불·교환 정책은 LLM이 자유롭게 생성하지 않고, **승인된 정책 문구를 인용**하게 한다(Air Canada·Cursor형 환각 방지).
  3. 모든 화면에 '상담원 연결' 버튼과 운영시간 외 접수 안내를 둔다(Gartner 87%).
  4. 대화 시작 시 AI라고 고지한다.
  5. 지식베이스를 위생적으로 관리한다. 시즌·프로모션·배송 마감일 변경을 즉시 반영하고, 오래된 문서는 폐기한다.
  6. KPI를 해결률 단독으로 보지 않는다. **재문의율, 사람 이관 후 CSAT, 클레임·분쟁 전환, 리뷰 평점**을 같이 본다.
  7. 가격 조작, '$1 판매' 같은 프롬프트 인젝션을 공개 전에 테스트한다.
- Gartner 27% 재시도율이 주는 함의: 나쁜 첫 경험은 채널 자체를 망가뜨린다. 좁은 범위로 높은 정확도를 먼저 확보한 뒤 범위를 넓히는 단계적 확장이 비용과 신뢰 양쪽에서 유리하다.
- Gartner 2026-07의 '서드파티 GenAI 3배'는 고객이 ChatGPT 등에 우리 가게 정책을 먼저 물어본다는 뜻이다. 반품·배송 정책을 **공개적이고 명확한 텍스트**(상세페이지·FAQ)로 두는 것이 봇 밖의 AI에서도 오답을 줄인다. 카카오톡 내 '챗GPT 챗봇' 출시(2026-06)도 이런 흐름에 맞닿아 있다.
- Air Canada 원칙을 한국에 그대로 적용할 수 있는지는 법률 검토가 필요하다. 다만 판매자가 운영하는 봇의 안내는 판매자 표시로 간주될 가능성이 높다고 보는 편이 보수적이다(추론, 법률 자문 아님).

### Gaps
- **한국 규제**(미검증 단서): 「인공지능 발전과 신뢰 기반 조성 등에 관한 기본법」(AI 기본법)이 2026-01-22 시행된 것으로 기억하며, 생성형 AI 이용 사실을 고지하는 투명성 의무와 계도기간이 있다. 이번 세션에서는 확인하지 못했다. 쇼핑몰 CS 챗봇에 적용되는 범위를 반드시 확인해야 한다.
- 전자상거래법상 청약철회 안내 등과 충돌하는 챗봇 오안내로 분쟁·제재가 생긴 **국내 사례**는 찾지 못했다.
- 한국 소비자의 AI 상담 선호·불만 조사(한국소비자원 등) 미수집.
- Klarna 2024 발표의 원문 세부(전체 채팅의 약 2/3 처리, 인간과 동등한 CSAT 주장 등)는 기억상의 단서일 뿐 이번 세션에서 미확인. MIT NANDA 'GenAI Divide'(2025-08, "기업 파일럿의 95%가 P&L 효과 없음")도 미확인.

---

## 6. 소규모 이커머스 팀의 정량 생산성 벤치마크: 시간 절감, 티켓당 비용, 인력 효과

### Takeaway
가장 신뢰도 높은 증거는 Brynjolfsson·Li·Raymond의 연구(QJE 2025)다. 상담원 5,179명에게 GenAI 보조 도구를 주자 시간당 해결 건수가 평균 **+14%**, 신입·저숙련은 **+34%** 늘었고 숙련자는 거의 변화가 없었다. 고객 감정과 상담원 유지율도 좋아졌다. 반면 덴마크 대규모 연구(Humlum & Vestergaard, NBER 2025)는 챗봇 사용자의 평균 시간 절감이 **근무시간의 2.8%**에 그치고 임금·근로시간 효과가 없다고 보고했다. 벤더가 내세우는 '해결률 80%' 같은 수치를 곧바로 인력 절감으로 환산하면 과대평가가 된다. 실제 인력 감축을 한 조직도 20%뿐이다(Gartner 2025-12). 소규모 셀러에게 AI의 주된 가치는 **야간·주말 커버리지, 첫 응답 속도, 신입·알바 교육 단축**에 있다고 보는 편이 증거에 맞다.

### Cited Findings
- **Brynjolfsson, Li, Raymond, "Generative AI at Work"**, *Quarterly Journal of Economics* 140(2): 889–942 (2025), NBER WP w31161 [IND]
  - 표본: 고객지원 상담원 **5,179명**에게 GenAI 대화 보조 도구를 단계적으로 도입했다.
  - 생산성: 평균 **+14%**, 신입·저숙련 **+34%**, 숙련·고숙련은 효과가 미미했다.
  - 메커니즘: 우수 상담원의 모범 관행을 전파하고, 신입의 학습곡선을 앞당긴다.
  - 부수 효과: 고객 감정(sentiment)과 직원 유지율이 개선되었다.
  - [NBER](https://www.nber.org/papers/w31161), [QJE](https://academic.oup.com/qje/article/140/2/889/7990658)
- **Humlum & Vestergaard, "Large Language Models, Small Labor Market Effects"**, NBER WP w33777 (2025) [IND]
  - 표본: 덴마크 노출 직종 11개, 근로자 **25,000명**, 사업장 **7,000곳**의 설문을 행정자료와 연결했다.
  - 시간 절감: 사용자 평균 **근무시간의 2.8%**. 사용자의 **64~90%**가 시간을 아꼈다고 응답했다.
  - 노동시장 효과: 임금·기록 근로시간에 유의한 효과가 없다(1%를 넘는 효과는 신뢰구간이 배제).
  - 대비: 같은 직종의 RCT들은 흔히 **15% 이상** 생산성 향상을 보고한다.
  - [NBER PDF](https://www.nber.org/system/files/working_papers/w33777/w33777.pdf), [BFI WP 2025-56](https://bfi.uchicago.edu/wp-content/uploads/2025/04/BFI_WP_2025-56-1.pdf)
- **인력 효과** [IND]: AI로 상담 인력을 줄인 CS 리더는 20%(2025-12). 줄인 기업의 절반은 2027년까지 재채용할 것이라는 예측(2026-02). [Gartner 2025-12-02](https://www.gartner.com/en/newsroom/press-releases/2025-12-02-gartner-survey-finds-only-20-percent-of-customer-service-leaders-report-ai-driven-headcount-reduction), [Gartner 2026-02-03](https://www.gartner.com/en/newsroom/press-releases/2026-02-03-gartner-predicts-half-of-companies-that-cut-customer-service-staff-due-to-ai-will-rehire-by-2027)
- **벤더·자사 보고 성과** [VENDOR]
  - Klarna(2024): 700명분 업무, 11분→2분 미만, 반복 문의 25%↓, 이익 개선 $40M 전망. 이후 품질 문제로 사람 상담을 재확대했다. [Bigeye](https://www.bigeye.com/blog/klarnas-ai-customer-service-deployment), [CX Dive](https://www.customerexperiencedive.com/news/klarna-reinvests-human-talent-customer-service-AI-chatbot/747586/)
  - 채널톡 ALF: 자사 CS 해결률 80%(추석 85%), 여행사 사례에서 문의 23%/19%↓(1개월), 44%↓(6개월). [채널톡 블로그](https://channel.io/ko/blog/articles/alfv2-cx-case-02942123), [머니투데이](https://www.mt.co.kr/future/2025/11/06/2025110611161567414)
- **소규모 셀러 기준선** [ANEC]: 1인 셀러의 수작업은 하루 약 6시간이다(주문 확인 채널당 20분 등). 도구 개발자가 제시한 '90% 절감'은 목표치이고 실측이 아니다. [MARK-1 PRD](https://github.com/minjae-488/MARK-1/blob/675f9ecae296360efd003fbe908d84441925d31d/PRD.md), [n8n-example](https://github.com/USEONGEE/n8n-example/blob/8d817d796e277931d4ecd47aaad930bf3afcca9c/docs/specs/cs_%EC%9B%8C%ED%81%AC.txt)

### Inferences
- **티켓당 비용 비교(가정에 따라 크게 달라지는 예시)**
  - 가정: 단순 문의 처리 3분/건, 인건비 시급 ₩10,000대(최저임금 수준, **미검증 가정**), 환율 ₩1,400/$.
  - 사람: 시간당 약 20건이므로 직접 인건비는 **건당 약 ₩500**.
  - AI(해결당 과금): Fin $0.99 ≈ ₩1,390, Gorgias $0.90 ≈ ₩1,260(+티켓비), Zendesk $1.5~2 ≈ ₩2,100~2,800.
  - 해석: 한국 인건비 수준에서는 **단순 문의 1건의 직접 비용은 USD 해결당 과금 AI가 오히려 비쌀 수 있다.** AI의 경제성은 비용 절감보다 **24시간 응대(야간·주말·연휴), 첫 응답 속도, 피크 흡수, 신규 인력 교육 단축**에서 나온다. 반대로 정액형 국산 챗봇(월 5만~40만원)은 월 볼륨이 클수록 건당 비용이 떨어진다.
- **시간 절감 추정(예시)**: 하루 문의 30건 × 3분 = 1.5시간/일. AI가 그중 50%를 끝까지 처리하면 약 45분/일, 월 약 20시간이 절감된다. 단, 초안 검수 시간이 새로 생기므로 순절감은 이보다 작다. Humlum의 2.8%와 RCT의 15% 이상 사이의 간극은 '업무 단위 자동화율'과 '직무 전체 절감'이 다르다는 점을 보여 준다.
- **인력 효과**: 연구 증거(신입 +34%, 숙련자 미미)에 따르면 1인 대표가 직접 응대할 때보다 **알바·신입 CS 인력을 쓰는 중소 브랜드**에서 AI 초안·보조의 효과가 크다. 인원 감축보다 추가 채용을 미루는 효과로 나타날 가능성이 높다. Gartner의 20%, 재채용 예측과도 맞는다.
- 벤더 해결률(67~80%)을 인력 계획에 반영할 때는 제3자 관측치(40~60%)와 자사 문의 구성(주문·배송·클레임 비중)을 반영해 **30~50% 선에서 보수적으로** 가정하는 편이 안전하다(추론).

### Gaps
- **한국 이커머스 CS의 티켓당 비용, 셀러 규모별 월 문의량, 평균 처리시간**에 대한 신뢰할 만한 공개 벤치마크를 찾지 못했다.
- 소규모 이커머스 팀을 대상으로 한 독립(학술·RCT) 연구 미수집. Brynjolfsson 연구는 대형 BPO 소프트웨어 지원 맥락이다.
- 챗 기반 AI 상담의 **매출 영향**(전환율, 객단가)에 대한 독립 연구 없음. 벤더 사례 수치도 이번 세션에서는 미수집.
- Humlum 연구의 11개 직종에 '고객지원 상담원'이 포함되는지 이번 세션에서 확인하지 못했다(포함된 것으로 기억하나 미검증).
