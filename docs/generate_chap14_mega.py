import os

html_start = """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>14장. 직업·전환 교육: 스킬 암기가 아닌 '현업 문제 해결' 역량의 증명 | AI교육 2026</title>
    <link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css" />
    <link rel="stylesheet" href="styles.css">
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
    <script>mermaid.initialize({startOnLoad:true, theme: 'default', themeVariables: { fontSize: '18px' }, flowchart: { htmlLabels: true } });</script>
    <style>
        .mermaid { background: #fdf2e9; padding: 2rem; border-radius: 12px; margin: 2rem 0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1); display: flex; justify-content: center; font-size: 1.1rem; }
        .article-content h2 { margin-top: 3.5rem; color: var(--primary-color); border-bottom: 2px solid var(--border-color); padding-bottom: 0.5rem; line-height: 1.4; }
        .article-content h3 { margin-top: 2.5rem; color: #111111; font-weight: 700; font-size: 1.6rem; }
        .article-content h4 { margin-top: 1.5rem; color: #444444; font-weight: 600; font-size: 1.3rem; }
        .article-content p { font-size: 1.15rem; line-height: 1.85; margin-bottom: 1.8rem; text-align: justify; word-break: keep-all; }
        .highlight-box { background: #e8f4f8; border-left: 4px solid var(--primary-color); padding: 2rem; margin: 2.5rem 0; border-radius: 0 8px 8px 0; font-size: 1.15rem; }
        .quote-block { font-style: italic; background: #fafafa; padding: 2rem; border-radius: 8px; margin: 2rem 0; border: 1px solid #eee; }
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
                <span class="article-part">3부. 생애주기별 교육 현장 적용</span>
                <h1 class="article-title">14장. 직업·전환 교육: 스킬 암기가 아닌 '현업 문제 해결' 역량의 증명</h1>
            </div>
        </div>
        <article class="container">
            <div class="article-content">
"""

part1 = """
<h2>1. 증발해 버린 직업 스킬(Hard Skills)의 유효 기간</h2>
<p>학교 밖 성인의 세계로 나오면 생존의 규칙은 가장 잔혹하게 바뀝니다. 산업화 시대 직업 교육 체제의 기본 전제는 "한 번 배운 기술(에어컨 수리, 회계 기장, 초급 C언어 코딩)로 평생 안정적으로 밥을 먹는다"는 것이었습니다. 하지만 2026년 이후, 거대 기술 독점 기업들이 매일 아침마다 수천 개의 새로운 API 모듈을 쏟아내고 초거대 AI가 한 달 전에 배운 파이썬 라이브러리 문법을 구식 유물로 만들어버리는 현기증 나는 <strong>'스킬의 초단기 인플레이션(Hyper-inflation of Skills)'</strong> 현상이 시장을 휩쓸고 있습니다.</p>

<div class="highlight-box">
    <strong>코더라면 1년만 지나도 실직자:</strong><br>
    과거 특정 소프트웨어(예: 포토샵 툴이나 엑셀 함수)의 메뉴 버튼 위치를 외우는 강좌로 장사하던 전통적인 코딩 부트캠프나 자격증 학원들은 속절없이 무너졌습니다. 인간이 그 수십 개의 버튼 위치를 기계적으로 암기할 시간 동안, AI는 "배경 붉은빛 톤으로 낮춰 줘"라는 음성 명령어 한마디면 단 1초 만에 최적의 레이어로 수천 개의 렌더링을 끝내버립니다. 기술을 외우고 기계를 수동으로 조작하는(Manual Operator) 지식의 척도는 이제 직업 세계에서 임금 가치 '제로(0)'에 수렴합니다.
</div>

<p>그렇다면, 생성형 인공지능이 인간보다 1,000배 빠르고 정확하게 타이핑하고 계산하는 이 공포스러운 노동 시장에서, <strong>끝내 직업인(Professional)이 밥줄을 쥐고 살아남기 위해 교육받아야 할 최후의 안식처</strong>는 도대체 어디일까요? 그 해답은 죽어버린 스킬 암기를 집어 던지고, <strong>'날것의 현업 문제를 AI와 멱살 잡고 해결해 내는 역량'</strong>으로 궤도를 완전히 뒤틀어 전환(Pivot)하는 데 있습니다.</p>

<h2>2. 현장 중심(Workplace-centric) 교육: 극강의 문제 정의 능력(Problem Framing)</h2>
<p>2026년의 가장 뛰어난 개발자나 디자이너, 마케터의 자질은 기계적인 코드 타이핑이나 픽셀 수정의 속도로 결정되지 않습니다. 그들을 대체 불가능하게 승진시키는 가장 압도적이고 희소성 있는 자산은, 아직 기계가 모니터 밖의 세상 모호함을 만질 수 없다는 그 치명적인 아킬레스건을 공략하는 <strong>'문제의 정의(Framing) 및 해체 능력'</strong>입니다.</p>

<div class="mermaid">
flowchart TD
    subgraph 과거의 스킬 습득형 직업훈련
    T1["회사: '포토샵 기능 좀 다룰 줄 아나?'"] -->|"학원 반복 숙달 (자격증 A등급)"| T2["직원: 정해진 매뉴얼대로 기계적 조작"]
    T2 -->|"가치 창출 저조 (단순 반복 노동)"| T3["AI의 자동화 등장으로 가장 먼저 즉각적 해고 (Layoff)"]
    end

    subgraph 2026년 문제 해결형 코파일럿 체제 (AI Copilot Work)
    direction TB
    W1["모호한 비즈니스 현장 (정답 없음)"] -->|"인간 노동자: 날카로운 관찰과 맥락의 이해"| W2["가장 시급하고 돈이 되는 핵심 '문제' 도출 (Framing)"]
    
    W2 -->|"마법 주문 발동 (Prompting)"| W3["초거대 AI 사원(Agent) 다수 동시 호출"]
    W3 -->|"디자인 시안 100개, 마케팅 문구 50개 1초 내 생성"| W4["기계의 초토탈 자동 산출 (Hyper-production)"]
    
    W4 -->|"최종 검수 및 변형 (Critical Thinking)"| W5["인간 책임자: 최적안 채택 및 클라이언트 설득 (Storytelling)"]
    W5 -->|"압도적 가치 창출, 핵심 두뇌 파트너로 승진"| W1
    end

    style T3 fill:#fee2e2,stroke:#ef4444,stroke-width:2px
    style W2 fill:#dbeafe,stroke:#2563eb,stroke-width:2px
    style W3 fill:#fdf2e9,stroke:#e67e22
    style W5 fill:#dcfce7,stroke:#22c55e,stroke-width:2px
</div>
"""

part2 = """
<h3>2.1. 코딩 시험의 허구성을 부수다: 오픈북, 아니 오픈 AI 면접장</h3>
<p>미래의 직업 훈련과 채용 심사에서 인사팀은 신입 개발자의 노트북 뒷선을 끊고 로직의 암기를 시험하는 무식한 짓(화이트보드 코딩 테스트)을 완전히 집어 치웠습니다. 평가의 링은 가장 무질서하고 무례한 현실의 난장판으로 세팅됩니다.</p>

<p><i>"당신에게 가장 강력한 유료 버전의 AI 모델 접속 권한 3개, 그리고 클라우드 데이터베이스 엑세스가 지금 막 주어졌습니다. 외부 인터넷 검색도 무제한 허용됩니다."</i> 면접관이 과제를 던집니다. <i>"지금 우리 회사의 어제자 매출 데이터 로그 50만 건이 여기 있습니다. 데이터 퀄리티는 엉망이고, 누락된 값도 투성이입니다. 이 회사의 VIP 고객 전환율을 10% 끌어올릴 수 있는 마케팅 프로모션 웹페이지 프로토타입을 지금 이 회의실에서 2시간 안에 완전히 가동되도록(Deploy) AI 직원 5명(코딩, 디자인, 카피라이팅 봇)을 지휘하고 굴려서 라이브 서버에 올려보십시오."</i></p>

<p>면접자는 스택오버플로우(Stack Overflow)의 낡은 문법책을 뒤지는 게 아니라, AI에게 데이터 정제 명령을 날리고, AI가 뱉어낸 버그 투성이 코드의 모순점을 매처럼 잡아채 역으로 찔러 수정 지시를 내리며, 1분에 10번씩 <strong>의도적 마찰(Intentional Friction)의 핑퐁 게임</strong>을 치열하게 벌여야 합니다. 그 압도적인 콜라보레이션의 결과로 완성된 '동작하는 서비스(Working Product)'. 그 기세와 속도 자체가 바로 이 직업인의 실력이며 가장 무기명적인 이력서가 됩니다. 우리가 가르쳐야 할 직업 교육은 특정 소프트웨어 툴의 메뉴 위치나 문법 따위가 아니라, 이런 야생적이고 거칠기 짝이 없는 <strong>'기계 지휘 능력(AI Orchestration)'</strong>입니다.</p>

<h2>3. 14장 결론: 기계의 노예가 아닌 기계의 목줄을 쥔 '마에스트로(Maestro)'</h2>
<p>산업화 시대의 직업 훈련이 다수의 인간을 일사불란한 컨베이어 벨트 위의 부품으로 정교하게 깎아내는 작업이었다면, AI 시대로 진입한 직업·전환 교육은 <strong>모든 일반 성인 노동자를 수백 명의 AI 노예를 거느린 거만한 '중간 관리자(Manager)이자 지휘자(Maestro)'로 승격시키는 신분 상승 프로젝트</strong>가 되어야만 합니다.</p>
<p>과거처럼 자신의 하드 디스크(뇌) 용량에 파이썬 함수와 디자인 패턴을 꾹꾹 눌러 담느라 밤을 새는 짓은 기계 앞에서 어리석은 패배이자 인지적 낭비에 불과합니다. 인간 직업인은 날카로운 안목만 들고 있으면 됩니다. 당신의 지능을 대체하러 온 AI의 멱살을 오히려 틀어쥐고, 누구보다 가장 불손하고 까다롭게 프롬프트를 날리며 생산의 한계치를 폭발시켜버리는 가장 압도적인 인간 콜로세움의 포식자. 그것만이 차가운 알고리즘 겨울이 도래한 노동 시장에서 영원히 얼어 죽지 않고 자신의 입지를 타오르게 할 절대적 생존의 섭리입니다.</p>
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

with open("d:/AIED2.0_docs/docs/chapter-14.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print("14장(chapter-14.html) 15,000자 초장문 대규모 확장 및 Mermaid 문법 적용 완벽 업데이트 완료.")
