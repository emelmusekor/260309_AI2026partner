import os

data = [
    {'id': 'chapter-1', 'title': '1장. AI교육 2026', 'part': '1부. 시대를 읽는 렌즈'},
    {'id': 'chapter-2', 'title': '2장. IT 교육의 역사와 교훈', 'part': '1부. 시대를 읽는 렌즈'},
    {'id': 'chapter-3', 'title': '3장. 챗봇을 넘어서', 'part': '1부. 시대를 읽는 렌즈'},
    {'id': 'chapter-4', 'title': '4장. AGI와 특이점 담론의 타격점', 'part': '1부. 시대를 읽는 렌즈'},
    {'id': 'chapter-5', 'title': '5장. 넥서스와 진실의 위기', 'part': '1부. 시대를 읽는 렌즈'},
    {'id': 'chapter-6', 'title': '6장. 교육 삼각형의 균열과 복원', 'part': '2부. 교육 시스템의 재구조화'},
    {'id': 'chapter-7', 'title': '7장. AI와 함께 배우기', 'part': '2부. 교육 시스템의 재구조화'},
    {'id': 'chapter-8', 'title': '8장. AI와 함께 가르치기', 'part': '2부. 교육 시스템의 재구조화'},
    {'id': 'chapter-9', 'title': '9장. 평가 패러다임의 혁신', 'part': '2부. 교육 시스템의 재구조화'},
    {'id': 'chapter-10', 'title': '10장. 책임 있는 AI 교육 거버넌스', 'part': '2부. 교육 시스템의 재구조화'},
    {'id': 'chapter-11', 'title': '11장. K-12 (1) 포용적 교육의 실현', 'part': '3부. 생애주기별 교육 현장 적용'},
    {'id': 'chapter-12', 'title': '12장. K-12 (2) 지식의 융합과 창조', 'part': '3부. 생애주기별 교육 현장 적용'},
    {'id': 'chapter-13', 'title': '13장. 고등교육의 전환', 'part': '3부. 생애주기별 교육 현장 적용'},
    {'id': 'chapter-14', 'title': '14장. 직업·전환 교육', 'part': '3부. 생애주기별 교육 현장 적용'},
    {'id': 'chapter-15', 'title': '15장. 평생교육과 시민 문해력', 'part': '3부. 생애주기별 교육 현장 적용'},
    {'id': 'chapter-16', 'title': '16장. 정책자에게 묻다', 'part': '4부. 국가 정책과 거시적 생태계'},
    {'id': 'chapter-17', 'title': '17장. 에듀테크 생태계와 민관학 거버넌스', 'part': '4부. 국가 정책과 거시적 생태계'},
    {'id': 'chapter-18', 'title': '18장. 교원 양성 체계의 대수술', 'part': '4부. 국가 정책과 거시적 생태계'},
    {'id': 'chapter-19', 'title': '19장. [결론] 2030 이후 새로운 교육 계약', 'part': '4부. 국가 정책과 거시적 생태계'}
]

template = """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | AI교육 2026</title>
    <!-- Pretendard Font -->
    <link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css" />
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header class="site-header">
        <div class="container header-content">
            <a href="index.html" class="site-title">
                AI교육 <span>2026</span>
            </a>
            <div class="header-description">
                시스템 재설계서
            </div>
        </div>
    </header>

    <main>
        <div class="article-header">
            <div class="container">
                <a href="index.html" class="back-link">← 목차로 돌아가기</a>
                <span class="article-part">{part}</span>
                <h1 class="article-title">{title}</h1>
            </div>
        </div>

        <article class="container">
            <div class="article-content">
                <p><strong>(이곳에 {title}의 상세 본문이 들어갑니다. 이전 단계에서 작성한 보고서 기획안을 바탕으로 내용을 전개할 수 있습니다.)</strong></p>
                
                <h2>본문 핵심 키워드</h2>
                <p>이 장에서는 현재 AI 패러다임의 변화와 교육적 수용 방안, 정책 및 시스템 재설계 방향에 대해 다룹니다.</p>

                <blockquote>
                    <p>“AI 교육은 단순한 기술 습득이 아니라, 기술이 던지는 질문에 답할 수 있는 주체적 인간을 길러내는 과정이다.”</p>
                </blockquote>

                <h3>주요 논의점</h3>
                <ul>
                    <li>AI와 인간의 협업 파트너십 구축</li>
                    <li>기술 결정론에 의존하지 않는 비판론적 교육 철학</li>
                    <li>단순 활용(Utilizing)을 넘어선 조화(Symbiosis)</li>
                </ul>
            </div>
        </article>
    </main>

    <footer class="site-footer">
        <div class="container">
            <p>&copy; 2026 AI교육 2026. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>"""

for chapter in data:
    content = template.replace('{title}', chapter['title']).replace('{part}', chapter['part'])
    with open(f"d:/AIED2.0_docs/docs/{chapter['id']}.html", 'w', encoding='utf-8') as f:
        f.write(content)
print('모든 HTML 파일이 성공적으로 생성되었습니다.')
