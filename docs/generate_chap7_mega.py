import os

html_start = """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>7장. AI와 함께 배우기: 유창한 대답보다 위대한 '질문'의 설계 | AI교육 2026</title>
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
                <span class="article-part">2부. 교육 시스템의 재구조화</span>
                <h1 class="article-title">7장. AI와 함께 배우기: 유창한 대답보다 위대한 '질문'의 설계</h1>
            </div>
        </div>
        <article class="container">
            <div class="article-content">
"""

part1 = """
<h2>1. 인지 부채(Cognitive Debt)의 늪</h2>
<p>교실에 도입된 AI 기반의 학습 코칭 프로그램들이 공통적으로 내세우는 핵심 가치는 '개인화된 편리함'과 '속도'입니다. 학생이 수학 문제의 해설을 요구하거나 한국사 개념의 요약을 지시하면, AI는 1초도 안 되어 군더더기 없이 완벽하게 정제된 정답의 흐름을 화면에 띄워줍니다. 학생들은 과거처럼 두꺼운 백과사전을 뒤적이거나 교무실 앞을 서성거리며 선생님의 여유 시간을 기다릴 필요가 없어졌습니다.</p>
<p>그러나 이 극단적인 '무마찰(Frictionless)'과 '편의성'의 이면에는, 학생들의 두뇌 깊숙한 곳에서 서서히 쌓여가는 치명적인 부작용이 존재합니다. 그것은 바로 <strong>'인지 부채(Cognitive Debt)'</strong>입니다.</p>

<div class="highlight-box">
    <strong>인지 부채(Cognitive Debt)란 무엇인가?</strong><br>
    학생 스스로 모호함을 견디고, 기억을 더듬으며, 흩어진 단서들을 논리적으로 조립해 내는 '두뇌의 고단한 연산 과정'을 기계에게 외주화(Outsourcing)함으로써 발생하는 지적 결손 현상입니다. 기계가 뱉어낸 유창한 대답을 읽으면서 학생의 뇌는 스스로 그 지식을 완벽하게 이해하고 통제하고 있다는 매혹적인 '착각'에 빠지지만, 실제로는 타인의 지식을 임대(Rent)하여 당장의 과제만 땜질해 낸 빚더미에 불과합니다.
</div>

<p>독서와 암기, 그리고 스스로 며칠 밤을 새워가며 논리를 증명해 내는 과정은 뇌의 신경망(시냅스)을 굵고 질기게 연결하는 유일한 생물학적 메커니즘입니다. 이 과정을 AI에게 전부 위임해 버릴 때, 우리 아이들의 지능은 역설적으로 가장 나태해지고 취약해집니다. 정보의 바다 한가운데서 뗏목을 지어본 적이 없는 아이는, 스마트폰의 배터리가 방전되는 순간 아무리 얕은 물살에도 익사하게 될 것입니다.</p>

<h2>2. 패러다임의 역전: '정답 획득'에서 '질문 육성'으로</h2>
<p>이 지독한 인지 부채의 늪에서 학생들을 구출해 '공진(Symbiosis)'의 궤도로 끌어올리기 위해서는 "어떻게 하면 AI에게 정답을 빠르고 정확하게 얻어낼 것인가?"라는 프롬프트 엔지니어링 류의 얄팍한 처방전을 과감히 쓰레기통에 던져버려야 합니다.</p>
<p>우리의 교육 도메인은 이제 철저하게 <strong>'위대한 질문(The Great Question)의 설계'</strong>로 방향을 틀어야 합니다. AI가 아무리 똑똑하다 한들, 좋은 텍스트와 통찰을 끌어내는 방아쇠(Trigger)는 결국 인간의 입력, 즉 <strong>'프롬프트의 질(Quality)'</strong>에 철저하게 종속되어 있습니다.</p>

<div class="mermaid">
flowchart TD
    subgraph 과거의 학습 구조 (선형적)
    L1("수동적 질문<br>(지식 확인용)") --> L2("교사/교재의 일방적 답변") --> L3("맹목적 암기")
    end

    subgraph 미래의 메타인지 학습 루프 (나선형)
    M1("맥락적/탐구적 프롬프트 입력") --> M2("AI의 1차 답변 생성")
    M2 --> M3{"학습자의 '인지적 의심' 발동"}
    M3 -->|논리적 비약 발견| M4("꼬리 질문 (Reflective Questioning) 재입력")
    M3 -->|패러다임 전환 모색| M5("반대 입장(Devil's Advocate) 시뮬레이션 요구")
    M4 --> M6("새로운 지식의 융합 및 사고망 확장")
    M5 --> M6
    M6 -.->|더 깊은 호기심| M1
    end

    style L1 fill:#f1f5f9,stroke:#94a3b8
    style M1 fill:#dcfce7,stroke:#22c55e,stroke-width:2px
    style M3 fill:#fee2e2,stroke:#ef4444
    style M6 fill:#dbeafe,stroke:#2563eb,stroke-width:2px
</div>

<h3>2.1. 프롬프트는 코딩이 아니라 철학이다</h3>
<p>AI에게 던지는 질문은 더 이상 '명령어 타이핑'이나 '검색 키워드 입력'이 아닙니다. 학생이 AI와 대화하며 입력창에 적어 내려가는 한 줄 한 줄의 문장은, 곧 <strong>나의 세계관과 논리적 구조를 객관적으로 끄집어내는 행위</strong>입니다.</p>
<p>수준 낮은 질문("지구 온난화에 대해 알려줘")은 위키백과 수준의 파편화된 정보를 앵무새처럼 되풀이하게 만들 뿐입니다. 하지만 고도로 맥락화된 철학적 질문("지구 온난화를 막기 위한 탄소세 도입이, 개발도상국의 경제 성장 및 생존권과 충돌할 때 어떤 윤리적 우선순위를 두어야 하는지 존 롤스의 정의론 관점에서 비판적으로 논증해 줘")은 기계의 대뇌를 풀가동시켜 학자 수준의 통찰을 뱉어내게 만듭니다. 기계는 인간이 던진 질문의 크기 딱 그만큼만 작동합니다.</p>
"""

part2 = """
<h2>3. AI와의 핑퐁 게임: 메타인지(Metacognition)의 극대화</h2>
<p>그렇다면 구체적으로 수업 현장에서 학생들은 AI 튜터를 어떻게 다루어야 할까요? 2026년 교실의 방점은 AI의 결과물(Out-put)을 제출하는 데 있지 않습니다. 오히려 학생이 AI와 어떠한 논리적 티키타카(핑퐁 게임)를 거쳤는지, 즉 <strong>명령과 피드백의 투쟁 과정 체인(Chain of Thought)</strong> 자체가 학습의 본질이 됩니다.</p>

<h3>3.1. 의도적 제약과 '소크라테스식 문답'의 적용</h3>
<p>가장 강력한 학습법은 교사가 AI 시스템(튜터)에게 <strong>'의도적 제약(Intentional Constraint)'</strong>을 걸어두는 것입니다.</p>
<ul>
    <li><strong>지시어 세팅:</strong> "너는 정답을 곧바로 알려주지 마라. 학생이 오답을 제시하면, 그 논리의 모순점을 학생 스스로 깨달을 수 있도록 반드시 역질문(소크라테스식 문답법)으로만 대응하라."</li>
    <li><strong>작동 예시:</strong> 학생이 수학 공식의 부호를 틀렸을 때, AI는 정답을 띄워주는 대신 <i>"네가 방금 왼쪽 항으로 넘긴 숫자의 부호가 유지되는 것이 등식의 성질에 위배되지 않을까? 수직선을 떠올려 보렴."</i>이라고 힌트를 던집니다.</li>
</ul>

<p>이러한 의도된 마찰의 구간에서 학생은 자신의 뇌 회로를 다시 점검할 수밖에 없습니다. <strong>'내가 지금 무엇을 알고, 무엇을 모르고 있는가?'</strong>를 객관적으로 조망하는 능력, 즉 상위 인지 능력인 <strong>메타인지(Metacognition)</strong>가 집중적으로 타격당하고 뻗어 나가는 순간입니다.</p>

<h3>3.2. 반대파 시뮬레이션 (Devil's Advocate)</h3>
<p>인문/사회 교과에서 AI는 완벽한 <strong>'도전적 토론 파트너'</strong>로 활용되어야 합니다. 학생이 특정한 정치, 사회적 견해(예: "모든 촉법소년의 연령을 낮춰야 한다")로 에세이를 작성한 뒤, AI에게 이렇게 지시합니다. <br>
<i>"내 글의 가장 취약한 논리적 헛점을 공격하고 반대 입장에서 가장 날카로운 반박문 3가지를 제시해 봐."</i><br>
학생은 AI가 던진 비판의 화살을 방어하기 위해 다시 자료를 찾고 논리를 촘촘하게 메워 나갑니다. 이 치열한 공방(攻防)을 통해 학생의 사고는 편협한 확증 편향(Confirmation Bias)에서 벗어나, 입체적이고 균형 잡힌 '근육질의 지성'으로 단련됩니다.</p>

<h2>4. 7장 결론: 의심하고 끈질기게 매달리는 아이들</h2>
<p>미래의 교실에서 유창한 텍스트를 순식간에 뽑아내는 기술적 쇼크는 더 이상 중요하지 않습니다. 인지 부채의 함정을 피해 가기 위해, 교사는 끊임없이 학생들의 지적 고통(마찰력)을 의도적으로 설계해 주어야 합니다.</p>
<p>우리가 길러내야 할 아이들은 AI가 내놓은 매끄러운 보고서를 보고 감탄하며 박수 치는 구경꾼이 아닙니다. AI의 첫 번째 답변을 향해 불만족스러운 듯 미간을 찌푸리며, "이건 표면적인 답변이잖아. 다시, 경제적 변수까지 합쳐서 더 깊게 추론해 봐"라고 집요하게 키보드를 두드리는 깐깐한 아이들, 그리고 마침내 기계가 내놓은 최상의 통찰마저도 한 번 더 의심의 눈으로 교차 검증하는 <strong>건방지고도 위대한 '질문자'</strong>들입니다. 인간 고유의 호기심과 성찰적 지성만이 기계의 파도 위를 무사히 활강하는 유일한 서핑 보드가 될 것입니다.</p>
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

final_html = html_start + part1 + part2 + html_end

with open("d:/AIED2.0_docs/docs/chapter-7.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print("7장(chapter-7.html) 대규모 확장 및 Mermaid 도표 적용 완벽 완료.")
