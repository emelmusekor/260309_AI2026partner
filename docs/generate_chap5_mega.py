import os

html_start = """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>5장. 넥서스와 진실의 위기: 정보 권력 시대의 새로운 디지털 시민성 | AI교육 2026</title>
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
                <h1 class="article-title">5장. 넥서스와 진실의 위기: 정보 권력 시대의 새로운 디지털 시민성</h1>
            </div>
        </div>
        <article class="container">
            <div class="article-content">
"""

part1 = """
<h2>1. 인류 최초의 '비인간 편집자(Non-human Editor)' 강림</h2>
<p>유발 하라리의 최근 저작 <strong>『넥서스(Nexus)』</strong>는 정보 네트워크의 역사를 통찰하며, 인공지능이 과거의 기술 사파리와 질적으로 다른 이유를 명쾌하게 짚어냅니다. 하라리에 따르면 인류는 언제나 이야기를 발명하고 이를 대규모 네트워크(종교, 법치 등)로 엮어내어 협력해 온 '스토리텔러' 종(種)이었습니다. 그리고 그 역사 속에서 등장한 모든 정보 기술 매체는 철저히 파편적이고 수동적이었습니다.</p>
<p>구텐베르크의 인쇄기는 자신이 찍어내는 책이 마녀사냥을 부추기는 글인지 셰익스피어의 희곡인지 이해하지 못했습니다. 라디오 스피커는 독재자의 선동에 혐오감을 느끼지 못한 채 그저 주파수를 증폭시킬 뿐이었습니다. 인간만이 의미를 이해하고, 인간만이 정보를 편집하여 권력을 행사했습니다.</p>

<div class="highlight-box">
    <strong>기술적 특이점을 넘어선 '편집의 특이점':</strong><br>
    그러나 지금 우리가 마주한 AI 기반의 알고리즘(추천, 생성 알고리즘) 네트워크는 역사상 최초의 '비인간 편집자'입니다. 유튜브의 추천 알고리즘과 틱톡의 피드는 청소년의 도파민을 자극하는 법을 우리 자신보다 더 잘 알며, 사용자 맞춤형으로 텍스트를 조합하는 LLM은 우리가 무의식적으로 소비할 '가장 그럴싸한(Plausible) 진실'을 대량으로 주조해내고 있습니다.
</div>

<p>이 지점에서 교육의 렌즈는 치명적으로 심각한 방향 전환을 요구받습니다. <strong>교실에서 딥페이크(Deepfake)나 가짜 뉴스를 팩트테크하는 기술 몇 가지를 가르치는 것만으로는 부족합니다.</strong> 우리는 아이들을, 거대 자본이 독점한 '스스로 학습하고 판단하는 렉서스(Network)'의 먹잇감이 되지 않도록 무장시켜야 합니다.</p>

<div class="mermaid">
flowchart LR
    subgraph 과거의 매체: 도구적 전송망
    P1("인간 발신자") -->|의도와 편집| M1("수동적 미디어 (인쇄/TV)")
    M1 -->|일방향 전달| R1("인간 수신자")
    end
    
    subgraph 현재의 매체: 인지적 매개망
    P2("다수의 인간 데이터") -->|알고리즘 학습| AI("비인간 편집자 (AI 추천 및 자동 생성)")
    AI -->|초개인화된 편향 피드| R2("인간 수신자")
    R2 -->|반응 데이터 재학습| AI
    end

    style M1 fill:#f1f5f9,stroke:#94a3b8
    style AI fill:#fee2e2,stroke:#ef4444,stroke-width:2px
    style R2 fill:#e8f4f8,stroke:#5d98c4
</div>

<h2>2. 딥페이크와 진공 창출: 진실의 종언(End of Truth)</h2>
<p>2024년, 전 세계를 휩쓴 선거판과 심지어 학교 교실 내부에서도 가장 파괴적인 위력으로 등장한 것이 바로 딥페이크와 가짜 생성 이미지들입니다. 교사나 동급생의 얼굴을 합성하여 조작된 폭력적, 혐오적 이미지를 만들어내는 범죄적 행태는 이미 학교 폭력의 새로운 뇌관이 되었습니다.</p>
<p>그러나 이보다 더 무서운 철학적 파국은 <strong>'진실의 부재(Liar's Dividend)'</strong> 현상입니다. 거짓된 영상과 정보가 홍수처럼 범람하는 세상에서는 대중이 무엇이 참인지 검증하기를 아예 포기해 버리는 상태, 즉 <strong>모든 텍스트와 사진에 대해 냉소적으로 돌변하는 허무주의</strong>가 만연하게 됩니다. 정치인은 명백히 자신이 저지른 부정부패의 증거 영상 앞에서도 "저것은 AI가 조작한 딥페이크"라고 우겨대며 빠져나가는 극단적인 후기-진실(Post-Truth) 사회로 진입했습니다.</p>

<h3>2.1. 회의주의(Skepticism)와 허무주의(Nihilism) 구분하기</h3>
<p>학교의 민주시민 교육은 바로 이 허무주의와 정면으로 맞서 싸워야 합니다. 모든 데이터가 AI에 의해 조작될 수 있으니 "세상에 믿을 것은 아무것도 없다"라고 아이들이 조소하게 내버려 두어서는 안 됩니다.</p>
<p>대신, 우리는 학생들에게 건강한 <strong>'합리적 회의주의(Rational Skepticism)'</strong>를 교육해야 합니다. 이는 의심에서 멈추는 것이 아니라, 출처(Source)를 다각도로 교차 검증하고, 원본 데이터와 인공적 변형을 추적하는 디지털 포렌식적 태도를 지니며, 신뢰할 수 있는 언론과 전문가 집단을 판별해 내는 지적 투지(Grit)를 일컫습니다.</p>
"""

part2 = """
<h2>3. 렌즈를 바꾸다: 정보 권력 시대의 새로운 교육 목표</h2>
<p>1부 전체를 관통하며 우리가 도달한 결론은 자명합니다. AI 교육은 단발성 IT 연수가 아니라 전 지구적인 인지 전쟁에서 살아남기 위한 **'생존 무기'**이자 **'진실을 감별하는 렌즈'**여야 합니다. 이를 위해 교실은 다음과 같은 3대 방어 기제를 커리큘럼의 심장부에 심어야 합니다.</p>

<div class="mermaid">
flowchart TD
    Core["정보 권력 시대의 디지털 시민성 핵심 기제"]
    Core --> Pillar1["1. 알고리즘 리터러시"]
    Core --> Pillar2["2. 팩트체크 시스템 내재화"]
    Core --> Pillar3["3. 인간 주체성의 수호"]
    
    Pillar1 -.-> Detail1("추천 알고리즘의 수익 구조(도파민 경제) 파악")
    Pillar2 -.-> Detail2("AI 환각 식별, 교차 검증, 원본 출처 확인")
    Pillar3 -.-> Detail3("맹신 거부, 의도적 디지털 마찰, 접속 단절 능력")

    style Core fill:#dbeafe,stroke:#2563eb,stroke-width:2px
    style Pillar1 fill:#fdf2e9,stroke:#e67e22
    style Pillar2 fill:#fdf2e9,stroke:#e67e22
    style Pillar3 fill:#fdf2e9,stroke:#e67e22
</div>

<h3>3.1. 제1기제: '보이지 않는 손' 해부하기 (알고리즘 리터러시)</h3>
<p>아이들이 틱톡과 쇼츠를 무한히 스크롤할 때, 그 뒤에는 스탠퍼드 출신의 심리학자들과 딥러닝 개발자들이 구축한 정교한 '인지 해킹(Cognitive Hacking)' 알고리즘이 작동하고 있음을 폭로해야 합니다. 내가 화가 나고, 슬프고, 무언가 사고 싶게 만드는 그 '욕망'이 나의 내부에서 자연스럽게 발원한 것인지, 아니면 거대 자본이 코딩한 AI의 매끄러운 추천 경로에 의해 '설계당한' 것인지 객관화하는 메타인지 훈련입니다.</p>

<h3>3.2. 제2기제: 팩트체크를 숨 쉬듯 (오염된 데이터 정화법)</h3>
<p>AI가 아무리 그럴싸한 에세이를 3초 만에 쏟아내더라도, "이 정보의 출처는 어디인가?", "이 데이터셋에서 의도적으로 배제된 소수자의 입장은 없는가?"를 따져 묻는 고단하고 느릿느릿한 훈련 과정입니다. 신뢰의 앵커(Anchor)를 도서관, 검증된 학술 기관, 그리고 교실 내의 동료 시민(친구)들과의 직접적인 대화에서 찾게 하는 것이 핵심입니다.</p>

<h3>3.3. 제3기제: 로그아웃 할 수 있는 용기</h3>
<p>역설적이지만, 최고의 디지털 시민성 교육은 **'기기에 종속되지 않고 스스로 스위치를 끄는 법'**을 가르치는 일입니다. 백지 위에서 연필만으로 자신의 생각을 구축해 낼 수 있는 아이만이, 다시 모니터를 켰을 때 AI의 추천을 노예처럼 따르지 않고 주체적으로 조율할 수 있습니다. 접속하지 않을 권리, 끊임없이 연결되지 않을 자유를 옹호하는 철학적 기조가 요구됩니다.</p>

<h2>4. 1부 마무리: 새로운 렌즈를 장착하며 (생태계로의 진입)</h2>
<p>지금까지 우리는 1부(1~5장)의 여정을 통해, 교실에 불어닥친 AI 혁명을 어떤 렌즈로 바라볼 것인지 치열하게 성찰했습니다.</p>
<p>우리는 단순히 교사가 하던 일을 AI 튜터로 교체하여 인건비를 절감하고 성적을 올리는 낡은 기술적 환상(2장)을 강도 높게 비판했습니다. 또한 기계가 신체를 입고 현실 세계로 등판하는 딥테크 혁명의 거대함(3장) 속에서, AGI의 특이점이 몰고 올 지능의 양극화(4장)와 거대 네트워크가 주조해 내는 가짜 진실의 해일(5장)이 아이들의 지성을 어떻게 위협하고 있는지 목도했습니다.</p>
<p>자, 이제 불안과 맹신의 렌즈는 깨졌으며 우리는 정확한 위기감이라는 처절하고도 명징한 '새로운 렌즈'를 장착했습니다. 진단은 충분합니다. 다가오는 2부에서는 본격적으로 이 철학적 전제를 바탕으로, 우리 학교의 **학생-교사-AI의 낡은 역할 삼각형**을 어떻게 뜯어고쳐야 할지, 그리고 그 교실 안의 평가 체제는 어떤 방식으로 혁명적으로 재구조화되어야 할지, 그 구체적인 생태계 설계도를 펼쳐 보겠습니다.</p>
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

with open("d:/AIED2.0_docs/docs/chapter-5.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print("5장(chapter-5.html) 대규모 확장 및 Mermaid 도표 적용 완벽 완료.")
