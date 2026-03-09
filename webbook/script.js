const bookData = {
    title: "AI교육 2026",
    subtitle: "교육 협력 파트너로서의 AI: 시스템 재설계서",
    description: "불안과 맹신을 넘어, K-12부터 평생학습까지 AI 시대의 교육 시스템을 어떻게 재설계할 것인가에 대한 거시적이고 실천적인 로드맵",
    parts: [
        {
            id: "part-1",
            title: "1부. 시대를 읽는 렌즈",
            desc: "불안과 맹신을 넘어선 교육적 성찰",
            chapters: [
                {
                    id: "chapter-1",
                    title: "1장. AI교육 2026",
                    subtitle: "기술의 작동법을 넘어 '공진(Symbiosis)'의 교실로",
                    summary: "AI를 배우는 교육이 아닌 AI와 함께 살아가는 교육으로의 패러다임 전환 선언",
                    tags: ["패러다임 전환", "공진주의", "시스템 재설계"]
                },
                {
                    id: "chapter-2",
                    title: "2장. IT 교육의 역사와 교훈",
                    subtitle: "과대포장, 환멸, 그리고 남은 것들",
                    summary: "과거 ICT 교육 도입의 실패와 성공 사례를 통한 기술 유행의 무비판적 추종 경계",
                    tags: ["IT역사", "기술결정론 비판", "교훈"]
                },
                {
                    id: "chapter-3",
                    title: "3장. 챗봇을 넘어서",
                    subtitle: "피지컬 AI와 자율 에이전트, 무대를 넓히다",
                    summary: "화면 속 텍스트 생성을 넘어 물리 세계와 상호작용하는 에이전트와 로봇으로의 확장",
                    tags: ["피지컬AI", "AI에이전트", "메이커교육"]
                },
                {
                    id: "chapter-4",
                    title: "4장. AGI와 특이점 담론의 타격점",
                    subtitle: "교육은 무엇을 믿고, 무엇을 의심할 것인가",
                    summary: "종말론적 AGI 담론을 비판하며 인내, 경험, 관계 등 인간 학습의 불변하는 본질 조명",
                    tags: ["AGI", "특이점", "인간의 본질"]
                },
                {
                    id: "chapter-5",
                    title: "5장. 넥서스와 진실의 위기",
                    subtitle: "정보 권력 시대의 새로운 디지털 시민성",
                    summary: "알고리즘 권력, 딥페이크 등 공론장의 위협에 맞서는 능동적 디지털 시민성 교육",
                    tags: ["디지털시민성", "알고리즘", "정보권력"]
                }
            ]
        },
        {
            id: "part-2",
            title: "2부. 교육 시스템의 재구조화",
            desc: "파트너십과 스캐폴딩의 설계",
            chapters: [
                {
                    id: "chapter-6",
                    title: "6장. 교육 삼각형의 균열과 복원",
                    subtitle: "AI-교사-학습자의 새로운 관계망",
                    summary: "AI(지식/루틴), 교사(동기/윤리), 학습자(주도권)의 역할 재배치와 삼각형 구조 설계",
                    tags: ["역할구조", "협력망", "메타협력주의"]
                },
                {
                    id: "chapter-7",
                    title: "7장. AI와 함께 배우기",
                    subtitle: "유창한 대답보다 위대한 '질문'의 설계",
                    summary: "인지 부채를 벗어나 메타인지를 발동시키는 학습자 주도적 질문과 사고 확장 원칙",
                    tags: ["메타인지", "질문설계", "학습역량"]
                },
                {
                    id: "chapter-8",
                    title: "8장. AI와 함께 가르치기",
                    subtitle: "교사의 '인간적 연결'을 위한 시간 벌기",
                    summary: "업무 자동화로 절약된 시간을 학생 관찰과 정서 지원으로 치환하는 교사의 역할 전환",
                    tags: ["교수역량", "행정자동화", "정서지원"]
                },
                {
                    id: "chapter-9",
                    title: "9장. 평가 패러다임의 혁신",
                    subtitle: "결과(Product)에서 '사고의 궤적(Process)'으로",
                    summary: "완성된 결과물이 아닌 프롬프트 이력, 수정 과정 등 사고의 흔적을 평가하는 새로운 프레임워크",
                    tags: ["과정중심평가", "사고의궤적", "평가혁신"]
                },
                {
                    id: "chapter-10",
                    title: "10장. 책임 있는 AI 교육 거버넌스",
                    subtitle: "데이터 주권, 편향성, 그리고 안전의 울타리",
                    summary: "학생 데이터 파이프라인, 알고리즘 이의 제기, 저작권 등 안전한 교육 환경 구축 지침",
                    tags: ["AI거버넌스", "데이터주권", "AI윤리"]
                }
            ]
        },
        {
            id: "part-3",
            title: "3부. 생애주기별 교육 현장 적용",
            desc: "K-12부터 평생학습까지",
            chapters: [
                {
                    id: "chapter-11",
                    title: "11장. K-12 (1) 포용적 교육의 실현",
                    subtitle: "기초학력 보정과 느린 학습자를 위한 사다리",
                    summary: "모두가 스크린만 보는 교육을 넘어, 특수 교육 및 느린 학습자를 보조하는 인간 중심 접근",
                    tags: ["K-12", "포용교육", "기초학력"]
                },
                {
                    id: "chapter-12",
                    title: "12장. K-12 (2) 지식의 융합과 창조",
                    subtitle: "탐구형·메이커형 AI 프로젝트 수업",
                    summary: "전 교과로 해방된 AI를 지역사회 문제 해결과 센서/데이터 분석에 결합하는 프로젝트",
                    tags: ["프로젝트수업", "메이커교육", "교과융합"]
                },
                {
                    id: "chapter-13",
                    title: "13장. 고등교육의 전환",
                    subtitle: "전공 지식의 융합, 연구 성실성, 차세대 학사 운영",
                    summary: "AI in 도메인 특화, 연구 윤리 재제정, AI 캠퍼스로의 진화를 대학의 과제로 조명",
                    tags: ["고등교육", "연구윤리", "AI캠퍼스"]
                },
                {
                    id: "chapter-14",
                    title: "14장. 직업·전환 교육",
                    subtitle: "스킬 암기가 아닌 '현업 문제 해결' 역량의 증명",
                    summary: "취업을 위한 자소서 첨삭이 아닌 실제 산업 현장의 비즈니스 문제를 AI와 협력하여 해결하는 훈련",
                    tags: ["직업교육", "포트폴리오", "실무역량"]
                },
                {
                    id: "chapter-15",
                    title: "15장. 평생교육과 시민 문해력",
                    subtitle: "고령층, 소상공인, 디지털 소외계층 포용",
                    summary: "기업 재직자를 넘어 중장년층, 지역주민을 아우르는 전 생애 AI 리터러시 안전망 구축",
                    tags: ["평생교육", "소외계층포용", "시민문해력"]
                }
            ]
        },
        {
            id: "part-4",
            title: "4부. 국가 정책과 거시적 생태계",
            desc: "국가 핵심 경쟁력으로서의 AI 교육",
            chapters: [
                {
                    id: "chapter-16",
                    title: "16장. 정책자에게 묻다",
                    subtitle: "AI 교육은 복지이자 국가 노동·산업 전략이다",
                    summary: "AI 활용 능력의 양극화, 지역/학교 간 인프라 불균형을 타파하기 위한 공공 영역의 개입과 복지 관점",
                    tags: ["교육정책", "양극화해소", "공공성"]
                },
                {
                    id: "chapter-17",
                    title: "17장. 에듀테크 생태계와 민관학 거버넌스",
                    subtitle: "플랫폼 종속을 넘어선 상생 모델",
                    summary: "빅테크 플랫폼에 공교육이 종속될 위험 방어 및 공공 데이터 플랫폼과 민간 혁신의 파트너십",
                    tags: ["에듀테크", "민관학협력", "플랫폼독점"]
                },
                {
                    id: "chapter-18",
                    title: "18장. 교원 양성 체계의 대수술",
                    subtitle: "AI 시대, '가르치는 사람'은 어떻게 길러지는가",
                    summary: "사범대, 교대의 커리큘럼 개편과 기존 방식에 갇힌 예비 교사 양성 구조의 시급한 혁신 제언",
                    tags: ["교원양성", "사범대개혁", "교사연수"]
                },
                {
                    id: "chapter-19",
                    title: "19장. [결론] 2030 이후 새로운 교육 계약",
                    subtitle: "기술의 진보 속에서 지켜낼 인간다움과 민주주의",
                    summary: "AI 일상화 시대에도 교육이 존재하는 이유, 철학적 사유와 대체 불가능한 '인간다움'의 선언",
                    tags: ["인간다움", "새로운계약", "민주주의"]
                }
            ]
        }
    ]
};

// DOM이 로드되면 목차 생성
document.addEventListener('DOMContentLoaded', () => {
    // 만약 index.html 메인 페이지라면
    const container = document.getElementById('parts-container');
    if (container) {
        renderIndexPage(container);
    }
});

function renderIndexPage(container) {
    let html = '';
    
    bookData.parts.forEach(part => {
        html += `
            <div class="part-section" id="${part.id}">
                <div class="part-header">
                    <h2 class="part-title">${part.title}</h2>
                    <p class="part-desc">${part.desc}</p>
                </div>
                <div class="chapters-grid">
        `;
        
        part.chapters.forEach(chapter => {
            const tagsHtml = chapter.tags.map(tag => `<span class="tag">#${tag}</span>`).join('');
            
            html += `
                <a href="${chapter.id}.html" class="chapter-card">
                    <div class="chapter-number">${chapter.title.split('.')[0]}</div>
                    <h3 class="chapter-title">${chapter.title.substring(chapter.title.indexOf('.') + 1).trim()}:<br>${chapter.subtitle}</h3>
                    <p class="chapter-summary">${chapter.summary}</p>
                    <div class="chapter-tags">
                        ${tagsHtml}
                    </div>
                    <div class="card-footer">
                        <span>본문 읽기</span>
                        <span class="read-more-icon">→</span>
                    </div>
                </a>
            `;
        });
        
        html += `
                </div>
            </div>
        `;
    });
    
    container.innerHTML = html;
}
