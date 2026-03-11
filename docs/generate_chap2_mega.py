import os

html_start = """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>2장. IT 교육의 역사와 교훈: 과대포장, 환멸, 그리고 남은 것들 | AI교육 2026</title>
    <link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css" />
    <link rel="stylesheet" href="styles.css">
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
    <script>mermaid.initialize({startOnLoad:true, theme: 'default', themeVariables: { fontSize: '18px' }, flowchart: { htmlLabels: true } });</script>
    <style>
        .mermaid { background: #fdf2e9; padding: 2rem; border-radius: 12px; margin: 2rem 0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1); display: flex; justify-content: center; font-size: 1.1rem; }
        .article-content h2 { margin-top: 3rem; color: var(--primary-color); border-bottom: 2px solid var(--border-color); padding-bottom: 0.5rem; }
        .article-content h3 { margin-top: 2rem; color: #111111; font-weight: 700; }
        .highlight-box { background: #e8f4f8; border-left: 4px solid var(--primary-color); padding: 1.5rem; margin: 2rem 0; border-radius: 0 8px 8px 0; }
    </style>
</head>
<body>
    <header class="site-header">
        <div class="container header-content">
            <a href="index.html" class="site-title">AI교육 <span>2026</span></a>
            <div class="header-description">시스템 재설계서</div>
        </div>
    </header>
    <main>
        <div class="article-header">
            <div class="container">
                <a href="index.html" class="back-link">← 목차로 돌아가기</a>
                <span class="article-part">1부. 시대를 읽는 렌즈</span>
                <h1 class="article-title">2장. IT 교육의 역사와 교훈: 과대포장, 환멸, 그리고 남은 것들</h1>
            </div>
        </div>
        <article class="container">
            <div class="article-content">
"""

part1 = """
<h2>1. 교육 기술 도입의 역사: 반복되는 기시감(Déjà vu)</h2>
<p>2026년 현재, 모든 미디어와 정책 입안자들은 "AI가 교육의 지형을 송두리째 바꿀 것"이라며 열변을 토하고 있습니다. 수백억 원의 예산이 'AI 수학 튜터'와 '디지털 교과서' 서버 증설에 쏟아지고 있으며, 학교 현장은 또다시 새로운 기기와 플랫폼 사용 연수에 내몰리고 있습니다. 그런데 이러한 풍경, 어딘가 매우 낯익지 않으십니까? 우리는 이미 지난 수십 년간 이와 완벽하게 동일한 <strong>'기술적 메시아주의(Technological Messianism)'</strong>의 사이클을 여러 번 목격해 왔습니다.</p>
<p>1990년대의 '열린 교육과 멀티미디어 PC 보급', 2000년대의 '전자 칠판(IWB) 및 ICT 활용 교육', 2010년대의 '스마트 스쿨과 1인 1태블릿 PC 배급', 그리고 불과 몇 년 전 코로나19 직후 불어닥쳤던 거품 낀 '에듀테크 메타버스' 열풍까지. 새로운 IT 기술이 등장할 때마다 사회는 그것이 학교의 낡은 주입식 교육을 끝장내고 진정한 맞춤형 교육을 실현할 '마법의 지팡이'인 양 추앙했습니다.</p>

<div class="highlight-box">
    <strong>기술 컨설팅 기업 가트너(Gartner)의 하이프 사이클(Hype Cycle):</strong><br>
    새로운 기술이 등장할 때 대중의 기대 심리가 겪는 5단계를 묘사한 모델입니다. 교육계의 기술 도입 역사는 이 곡선의 무자비함을 정확히 증명해왔습니다. 우리는 매번 '부풀려진 기대의 정점'에서 흥분하고 예산을 쏟아부었으나, 결국 '환멸의 계곡'으로 처박혀 먼지 쌓인 하드웨어만을 남기곤 했습니다.
</div>

<p>그러나 수조 원의 예산이 투입된 그 수많은 '에듀테크 혁명' 이후, 과연 우리 아이들의 비판적 사고력은 기술 투입량에 비례하여 비약적으로 성장했습니까? 대답은 안타깝게도 '아니오'입니다. 칠판이 분필에서 스마트 터치스크린으로 형태만 바뀌었을 뿐, 교사가 앞에서 지식을 일방향적으로 전송하고 학생이 그것을 받아 적는 교실의 본력(Gravity)은 꿈쩍도 하지 않았습니다. 태블릿 PC는 창의적 도구가 되기보다 문제 풀이 앱을 띄우거나 영상을 시청하는 수동적 단말기로 전락하기 일쑤였습니다.</p>

<div class="mermaid">
flowchart LR
    A[기술 촉발<br>Innovation] -->|황홀경| B[기대의 정점<br>Peak of Inflated Expectations]
    B -->|한계 노출| C[환멸의 계곡<br>Trough of Disillusionment]
    C -->|재평가/교정| D[계몽의 비탈<br>Slope of Enlightenment]
    D -->|실질적 교육 안착| E[생산성의 안정기<br>Plateau of Productivity]
    
    style A fill:#ffffff,stroke:#8ab6d6
    style B fill:#fdf2e9,stroke:#e67e22,stroke-width:2px
    style C fill:#f1f5f9,stroke:#94a3b8
    style D fill:#ffffff,stroke:#8ab6d6
    style E fill:#e8f4f8,stroke:#5d98c4,stroke-width:2px
</div>

<h3>1.1. 환멸의 계곡은 왜 필연적인가?</h3>
<p>교육계의 하이프 사이클이 유독 가파르고 그 추락이 뼈아픈 이유는, 학교라는 공간이 지닌 특유의 <strong>생체적 복잡성(Biological & Social Complexity)</strong>을 기술자들과 관료들이 번번이 무시하기 때문입니다. 기업의 소프트웨어 시연회장에서 매끄럽게 돌아가는 AI 튜터 프로그램은 빛과 소음이 절제된 이상적 환경의 결과물입니다.</p>
<p>하지만 현실의 교실은 매 순간 돌발 변수(쉬는 시간의 다툼, 와이파이 혼선, 집중력이 흩어진 30명의 각기 다른 감정 상태 등)가 난무하는 일종의 유기체입니다. 하드웨어의 미세한 버그나 로그인 지연 사태 3초만으로도 수업 흐름 전체가 깨지며, 학생들은 신기술의 인터페이스에 곧 매력을 잃습니다. 화려한 시연(Demo)에 속아 섣불리 막대한 예산으로 인프라를 깔아버리는 정부의 하향식(Top-down) 정책은 필연적으로 현장 교사들의 피로감과 냉소를 부르고, 이는 곧 '환멸의 계곡'이라는 거대한 무덤으로 직행하게 만듭니다.</p>

<h2>2. 기술 결정론(Technological Determinism)의 오류</h2>
<p>왜 우리는 이 지독한 실패의 사이클을 20년째 반복하는 것일까요? 그 근저에는 <strong>'기술 결정론(Technological Determinism)'</strong>이라는 맹목적인 종교가 똬리를 틀고 있습니다. 기술 결정론이란 "새롭고 효율적인 기술(원인)을 투입하기만 하면, 사회나 교육 현장(결과)이 자동적으로 긍정적인 방향으로 개선될 것"이라고 믿는 극도의 단순 순결주의입니다.</p>

<p>과거의 정책 입안자들은 "스마트 패드를 보급하면 종이 없는 친환경적이고 자기주도적인 학습이 일어날 것"이라 굳게 믿었습니다. 하지만 디바이스라는 '기계(Hardware)'에만 몰두한 나머지, 그것을 운용할 <strong>소프트웨어(Contents)</strong>의 빈곤함, 그리고 무엇보다 학생들이 온라인 상에서 헤매지 않도록 곁에서 멱살을 잡고 끌어줄 <strong>교사의 철학과 정서적 밀착(Human Connection)</strong>이라는 가장 결정적인 변수를 간과했습니다.</p>

<h3>2.1. 목적 잃은 수단의 비극</h3>
<p>다가오는 AI 교육 시대 역시 이 '수단과 목적의 전도 현상'에서 자유롭지 못합니다. 현재 많은 학교의 AI 도입 추진단은 "어떻게 하면 최신 거대 언어 모델(LLM)을 학교 서버에 무사히 연동시킬 것인가", "내년에 몇 대의 AI 단말기를 추가 예산으로 확보할 것인가"와 같은 <strong>수단적(Instrumental) 과제</strong>에만 혈안이 되어 있습니다.</p>

<div class="mermaid">
graph TD
    subgraph 과거의 실패: 기술 중심 접근
    T1[기술 인프라 보급] -->|강제 투입| T2[교사 및 학생의 혼란]
    T2 -->|사용률 저조| T3[환멸과 예산 낭비]
    end
    subgraph 미래의 성공: 목적 중심 접근
    P1[교육적 '목적' 정의<br>비판적 사고, 창의성, 연대] -->|목적 달성을 위한 도구 탐색| P2[AI 기술 선별 도입]
    P2 -->|교사의 재구조화 개입| P3[메타 인지적 학습 및 공진 창출]
    end
    
    style T1 fill:#f1f5f9,stroke:#94a3b8
    style T3 fill:#fee2e2,stroke:#ef4444
    style P1 fill:#dcfce7,stroke:#22c55e,stroke-width:2px
    style P3 fill:#dbeafe,stroke:#2563eb
</div>

<p>우리는 다시 원점의 질문으로 돌아가야 합니다. <strong>"무엇을 위한 AI인가?"</strong></p>
<p>학생의 수학 점수 백분위를 올리기 위한 도구인가요? 아니면 교사의 채점 시간을 덜어주어 행정 편의를 높이기 위함인가요? 만약 목표가 그것뿐이라면, 굳이 막대한 전력 소모와 거버넌스 위험을 초래하는 생성형 AI를 투입할 필요조차 없습니다. 구시대의 Rule-based(규칙 기반) 알고리즘이나 OMR 카드로도 충분히 가능한 일입니다.<br>
기초학력이 무너지고 소셜 미디어 알고리즘에 아이들의 정신 건강이 잠식당하는 이 시대에 진정 학교가 AI를 통해 이루어야 할 '목적(Purpose)'은, 모든 아이가 정보의 파편에 이리저리 휘둘리지 않고 거대 데이터 속에 숨은 인간적 가치와 진실의 맥락을 길어 올리는 <strong>'강인한 지적 근육'</strong>을 만들어주는 것입니다. 목적의식 없는 기계의 도입은, 엔진 없이 바퀴만 달린 화려한 마차를 절벽으로 밀어버리는 것과 같습니다.</p>

<h2>3. 유행을 절대화하지 않는 '의심의 눈(Skeptical Eye)' 무장하기</h2>
<p>과거의 뼈아픈 교훈이 말해주는 바는 명확합니다. 새로운 에듀테크나 AI 서비스가 등장했을 때, 우리는 그것에 곧바로 열광하고 굴복하는 대신, 두 발을 딛고 서서 그것을 까칠하게 검열해 내는 <strong>'의심의 눈(Skeptical Eye)'</strong>을 가져야 합니다. 빅테크 기업이나 교육 당국의 브리핑 자료를 무비판적으로 절대화하지 않는 태도야말로 AI 교육 2026이 요구하는 가장 최우선의 리터러시입니다.</p>

<h3>3.1. 에듀테크 마케팅의 환상 해체하기</h3>
<ul>
    <li><strong>"1:1 완벽한 초개인화 학습 경험을 제공합니다":</strong> 이 매혹적인 마케팅 문구를 들을 때 우리는 의심해야 합니다. 학습자가 오직 자신의 수준에 맞춰 통제된 인터페이스 안에서만 머물 때, 타인과 마찰하고 갈등하며 더 넓은 시야를 획득하는 '사회화(Socialization)' 과정이 거세될 위험은 없는가? 효율성이라는 미명 하에 아이들을 파편화된 화면 감방에 영원히 가두어버리는 것은 아닌가?</li>
    <li><strong>"편향 없는 가장 최신의 지식 데이터베이스":</strong> 세상에 가치 중립적인 AI는 존재하지 않습니다. 우리가 도입하려는 이 챗봇의 뼈대 모델은 어느 국가 혹은 기업의 이념이 집중된 텍스트 뭉치로 사전 훈련(Pre-trained)되었습니까? 소외된 지역, 소외된 언어의 데이터를 무시하지는 않았습니까? 이 보이지 않는 이데올로기의 편향성을 어떻게 방어해 낼 것인지 교사는 끊임없이 집요하게 질문해야 합니다.</li>
</ul>

<h3>3.2. 도입이 혁신을 증명하지 않는다</h3>
<p>"우리 시/도 교육청은 전 학교에 AI 튜터 라이선스를 100% 보급했습니다."라는 선언은 정치적 슬로건으로서는 훌륭할지 몰라도 교육 혁신의 지표로는 완전한 낙제점입니다. 진정한 혁신의 증명은 <strong>교실 내 '상호작용의 질적 변화'</strong>에 있습니다.</p>
<p>기계를 들여놓은 뒤 학생의 표정은 얼마나 달라졌는가? AI가 내린 오답 분석을 놓고 교사와 학생이 눈을 맞추며 대화하는 시간이 늘어났는가? 과거라면 불가능했을 다국적, 다문화 학생 간의 협업 프로젝트가 번역봇을 통해 기적처럼 타통(打通)되었는가? 만약 이러한 '인간적 연결의 복원'이 이루어지지 않았다면, 그 어떤 수백만 원짜리 AI 서버도 고철 덩어리에 불과합니다.</p>

<h2>4. 2장 결론: 폐허 위에서 다시 세우는 교육 철학</h2>
<p>IT 정보 기술은 태생적으로 속도를 숭배합니다. '더 빨리, 더 매끄럽게, 더 편리하게'가 실리콘밸리의 미덕입니다. 그러나 수십 년의 교육 기술 도입 역사가 부르짖는 교훈은 이와 정반대입니다. <strong>교육은 태생적으로 느리고, 불편하며, 마찰을 수반해야만 하는 고도화된 인간 발달의 과정입니다.</strong></p>

<p>우리는 지나간 '스마트 교육 광풍'의 폐허 위에서 다시 출발선에 섭니다. 다급하게 외국의 앞선 AI 서비스를 벤치마킹하여 수입하기 전에, 우리 내부의 교육 철학을 반문해야 합니다. 환멸의 계곡에 또다시 처박히지 않으려면, 기술을 맹신하는 유토피아주의와 기술을 철저히 배격하는 러다이트(Luddite)적인 공포 사이에서 차갑고도 역동적인 균형점에 올라서야 합니다. 기술의 도입을 서두르지 말고 인간의 역량이 먼저 기술을 통제할 윤리적 영점을 세우는 것. 과거의 실패가 우리에게 외치고 있는, 단 하나 남은 진실이자 유일한 생존의 길입니다.</p>
"""

html_end = """
            </div>
        </article>
    </main>
    <footer class="site-footer">
        <div class="container"><p>&copy; 2026 AI교육 2026. All rights reserved.</p></div>
    </footer>
</body>
</html>
"""

final_html = html_start + part1 + html_end

with open("d:/AIED2.0_docs/docs/chapter-2.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print("2장(chapter-2.html) 대규모 확장 및 Mermaid 도표 적용 완벽 완료.")
