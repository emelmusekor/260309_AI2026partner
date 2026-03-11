import os
import glob
import re
from bs4 import BeautifulSoup
import random

GLOSSARY_DB = {
    "판옵티콘": ("판옵티콘(Panopticon)", "영국의 철학자 제러미 벤담이 고안한 원형 감옥 구조. 감시자는 보이지 않으나 죄수는 항상 감시받는다고 느끼게 통제하는 시스템입니다.", "https://en.wikipedia.org/wiki/Panopticon"),
    "러다이트": ("러다이트(Luddite)", "19세기 영국에서 일어난 기계 파괴 운동. 신기술의 도입을 맹목적으로 거부하고 두려워하는 태도를 비유합니다.", "https://en.wikipedia.org/wiki/Luddite"),
    "타불라 라사": ("타불라 라사(Tabula Rasa)", "라틴어로 '백지 상태'를 의미하며, 인간의 마음은 비어 있고 경험에 의해 지식이 형성된다는 개념입니다.", "https://en.wikipedia.org/wiki/Tabula_rasa"),
    "호모 사피엔스": ("호모 사피엔스(Homo Sapiens)", "'지혜로운 인간'이라는 뜻으로, 현생 인류를 지칭합니다.", "https://en.wikipedia.org/wiki/Homo_sapiens"),
    "레비나스": ("에마뉘엘 레비나스(Emmanuel Levinas)", "타자의 얼굴과 윤리적 책임을 강조한 프랑스의 철학자입니다.", "https://en.wikipedia.org/wiki/Emmanuel_Levinas"),
    "푸코": ("미셸 푸코(Michel Foucault)", "권력과 지식의 관계, 감시 체계와 규율을 통찰한 프랑스의 사상가입니다.", "https://en.wikipedia.org/wiki/Michel_Foucault"),
    "비고츠키": ("레프 비고츠키(Lev Vygotsky)", "사회발달이론을 주창한 구소련의 심리학자로, 교사의 스캐폴딩(비계 설정)을 강조했습니다.", "https://en.wikipedia.org/wiki/Lev_Vygotsky"),
    "샌델": ("마이클 샌델(Michael Sandel)", "정의와 기회라는 주제를 깊이 연구한 정치철학자로, 공동체적 연대를 강조합니다.", "https://en.wikipedia.org/wiki/Michael_Sandel"),
    "벤담": ("제러미 벤담(Jeremy Bentham)", "영국의 공리주의 철학자이자 판옵티콘 구조의 창시자입니다.", "https://en.wikipedia.org/wiki/Jeremy_Bentham"),
    "거대 서사": ("거대 서사(Grand Narrative)", "역사의 발전을 설명하는 포괄적이고 거시적인 이데올로기나 철학적 틀을 의미합니다.", "https://en.wikipedia.org/wiki/Metanarrative"),
    "공진화": ("공진화(Symbiosis)", "서로 다른 개체가 상호작용하며 함께 진화하고 발전하는 현상을 뜻합니다.", "https://en.wikipedia.org/wiki/Symbiosis"),
    "회복탄력성": ("회복탄력성(Resilience)", "역경이나 실패에 좌절하지 않고 밑바닥에서 다시 튀어 오르는 심리적 근력을 의미합니다.", "https://en.wikipedia.org/wiki/Psychological_resilience"),
    "에코체임버": ("에코체임버(Echo Chamber)", "자신과 비슷한 성향의 정보만 반복적으로 수용하여 편향된 사고에 갇히는 현상을 의미합니다.", "https://en.wikipedia.org/wiki/Echo_chamber_(media)"),
    "환각": ("환각(Hallucination)", "인공지능이 사실이 아닌 내용을 마치 사실인 것처럼 그럴듯하게 생성해내는 오류 현상입니다.", "https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence)")
}

WIDGET_CSS_JS = """
<style>
/* Modern Widget CSS */
.interactive-widget {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 2.5rem;
    margin: 3.5rem 0;
    box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
}
.widget-title {
    margin-top: 0;
    color: #0f172a;
    font-size: 1.3rem;
    font-weight: 700;
    margin-bottom: 1rem;
    border-bottom: 2px solid #f1f5f9;
    padding-bottom: 0.8rem;
}
.mcq-option {
    display: block;
    padding: 1.2rem;
    margin-bottom: 0.8rem;
    background: #f8fafc;
    border: 2px solid #e2e8f0;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.2s;
    font-size: 1.05rem;
    color: #334155;
    line-height: 1.5;
}
.mcq-option:hover { background: #f1f5f9; border-color: #cbd5e1;}
.mcq-option.selected { border-color: #3b82f6; background: #eff6ff; color: #1d4ed8; font-weight: 600; box-shadow: 0 0 0 1px #3b82f6;}
.submit-btn {
    background: #1e293b;
    color: white;
    padding: 0.8rem 1.8rem;
    border: none;
    border-radius: 6px;
    font-weight: 600;
    font-size: 1.05rem;
    cursor: pointer;
    margin-top: 1.5rem;
    transition: background 0.2s, transform 0.1s;
}
.submit-btn:hover { background: #0f172a; transform: translateY(-1px);}
.submit-btn:active { transform: translateY(0);}
.feedback-msg { margin-top: 1.5rem; font-weight: 600; padding: 1.2rem; border-radius: 8px; display: none; font-size:1.05rem; line-height: 1.5;}
.feedback-msg.success { background: #f0fdf4; color: #15803d; border: 1px solid #bbf7d0; display: block; animation: fadeIn 0.3s;}
.feedback-msg.error { background: #fef2f2; color: #b91c1c; border: 1px solid #fecaca; display: block; animation: fadeIn 0.3s;}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(-5px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes confetti {
  0% { transform: translateY(0) rotate(0deg); opacity: 1; }
  100% { transform: translateY(200px) rotate(720deg); opacity: 0; }
}
.confetti-piece {
  position: absolute;
  width: 12px; height: 12px;
  background: #facc15;
  animation: confetti 1.2s ease-out forwards;
  z-index: 100;
  border-radius: 2px;
  pointer-events: none;
}

/* Drag and Drop */
.dnd-container { display: flex; gap: 1rem; margin-bottom: 2rem; flex-wrap: wrap; background: #f8fafc; padding: 1.5rem; border-radius: 8px; border: 1px dashed #cbd5e1;}
.draggable { padding: 0.8rem 1.5rem; background: #3b82f6; color: white; border-radius: 6px; cursor: grab; font-weight: bold; box-shadow: 0 2px 4px rgba(0,0,0,0.1); transition: transform 0.1s;}
.draggable:active { cursor: grabbing; transform: scale(0.95);}
.dropzone { 
    display: inline-block; 
    min-width: 120px; 
    height: 36px; 
    border-bottom: 3px dashed #94a3b8; 
    margin: 0 0.5rem; 
    vertical-align: middle; 
    text-align: center; 
    background: #f1f5f9;
    border-radius: 4px 4px 0 0;
    transition: all 0.2s;
    line-height: 36px;
    font-size: 1.05rem;
}
.dropzone.dragover { background: #e2e8f0; border-bottom-color: #64748b;}
.dropzone.filled { background: #eff6ff; border-bottom: 3px solid #3b82f6; color: #1d4ed8; font-weight:bold; }

/* Short Answer */
.short-answer-input { padding: 1rem; border: 2px solid #e2e8f0; border-radius: 8px; width: 100%; max-width: 500px; font-size: 1.05rem; margin-bottom: 1rem; transition: border-color 0.2s;}
.short-answer-input:focus { border-color: #3b82f6; outline: none; box-shadow: 0 0 0 3px rgba(59,130,246,0.1); }
</style>

<script>
function fireConfetti(widget) {
    const rect = widget.getBoundingClientRect();
    for(let i=0; i<50; i++) {
        const conf = document.createElement('div');
        conf.className = 'confetti-piece';
        const colors = ['#facc15', '#f87171', '#60a5fa', '#34d399', '#c084fc'];
        conf.style.left = (Math.random() * 100) + '%';
        conf.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
        conf.style.top = (Math.random() * 20) + 'px';
        widget.appendChild(conf);
        setTimeout(() => conf.remove(), 1200);
    }
}

function setupWidgets() {
    // MCQ
    document.querySelectorAll('.mcq-widget').forEach(widget => {
        const options = widget.querySelectorAll('.mcq-option');
        options.forEach(opt => {
            opt.addEventListener('click', () => {
                options.forEach(o => o.classList.remove('selected'));
                opt.classList.add('selected');
                widget.querySelector('.feedback-msg').style.display = 'none'; // reset
            });
        });
        
        const btn = widget.querySelector('.submit-btn');
        const feedback = widget.querySelector('.feedback-msg');
        btn.addEventListener('click', () => {
            const selected = widget.querySelector('.mcq-option.selected');
            if(!selected) {
                feedback.className = 'feedback-msg error';
                feedback.innerHTML = '⚠️ 보기를 하나 선택해주세요.';
                return;
            }
            if(selected.dataset.correct === 'true') {
                feedback.className = 'feedback-msg success';
                feedback.innerHTML = '🎯 <strong>정답입니다!</strong> 본문의 핵심 철학을 정확히 이해하셨습니다.';
                fireConfetti(widget);
            } else {
                feedback.className = 'feedback-msg error';
                feedback.innerHTML = '❌ <strong>아쉽습니다.</strong> 기계적 효율성보다는 비판적 사고의 가치를 다시 떠올려보세요.';
            }
        });
    });

    // Drag & Drop
    document.querySelectorAll('.dnd-widget').forEach(widget => {
        const draggables = widget.querySelectorAll('.draggable');
        const dropzones = widget.querySelectorAll('.dropzone');
        let draggedItem = null;
        
        draggables.forEach(d => {
            d.addEventListener('dragstart', function() { draggedItem = this; });
        });
        
        dropzones.forEach(dz => {
            dz.addEventListener('dragover', e => { e.preventDefault(); dz.classList.add('dragover'); });
            dz.addEventListener('dragleave', () => dz.classList.remove('dragover'));
            dz.addEventListener('drop', function(e) {
                e.preventDefault();
                this.classList.remove('dragover');
                if(draggedItem) {
                    this.textContent = draggedItem.textContent;
                    this.dataset.value = draggedItem.dataset.value;
                    this.classList.add('filled');
                }
            });
        });
        
        const btn = widget.querySelector('.submit-btn');
        const feedback = widget.querySelector('.feedback-msg');
        btn.addEventListener('click', () => {
            let correct = true;
            let allFilled = true;
            dropzones.forEach(dz => {
                if(!dz.dataset.value) allFilled = false;
                if(dz.dataset.value !== dz.dataset.target) correct = false;
            });
            if(!allFilled) {
                feedback.className = 'feedback-msg error';
                feedback.innerHTML = '⚠️ 모든 빈칸을 파란색 블록으로 채워주세요.';
                return;
            }
            if(correct) {
                feedback.className = 'feedback-msg success';
                feedback.innerHTML = '🎯 <strong>완벽합니다!</strong> 문맥이 올바르게 복원되었습니다.';
                fireConfetti(widget);
            } else {
                feedback.className = 'feedback-msg error';
                feedback.innerHTML = '❌ 일부 단어의 위치가 틀렸습니다. 다시 고민해 보세요.';
            }
        });
    });

    // Short Answer
    document.querySelectorAll('.sa-widget').forEach(widget => {
        const btn = widget.querySelector('.submit-btn');
        const input = widget.querySelector('input');
        const feedback = widget.querySelector('.feedback-msg');
        
        input.addEventListener('keypress', function (e) {
            if (e.key === 'Enter') btn.click();
        });

        btn.addEventListener('click', () => {
            const val = input.value.trim().replace(/\s+/g, '');
            const target = input.dataset.target.split(',');
            if(val === '') {
                feedback.className = 'feedback-msg error';
                feedback.innerHTML = '⚠️ 정답을 입력해주세요.';
                return;
            }
            if(target.some(t => val.includes(t))) {
                feedback.className = 'feedback-msg success';
                feedback.innerHTML = '🎯 <strong>정확합니다!</strong> 핵심 개념을 훌륭하게 인지하셨습니다.';
                fireConfetti(widget);
            } else {
                feedback.className = 'feedback-msg error';
                feedback.innerHTML = '❌ 예상되는 핵심 개념어가 아닙니다. 본문의 흐름을 다시 학인해주세요.';
            }
        });
    });
}
document.addEventListener('DOMContentLoaded', setupWidgets);
</script>
"""

WIDGET_TEMPLATES = [
    """
    <div class="interactive-widget mcq-widget">
        <h4 class="widget-title">📝 깊이 있는 사유: 5지 선다형 점검</h4>
        <p style="margin-bottom:1.5rem;">본 단원의 철학적 기조와 <strong>가장 거리가 먼</strong> 설명을 고르세요.</p>
        <div class="mcq-option" data-correct="false">A. 인공지능 도구의 압도적 연산력은 현장 교사들의 교육적 개입을 완전히 대체할 수 없습니다.</div>
        <div class="mcq-option" data-correct="true">B. 현대의 훌륭한 교사란, 디지털 기기를 철저히 배제하고 교과서의 지식만을 무결점으로 주입하는 교사입니다.</div>
        <div class="mcq-option" data-correct="false">C. 맹목적인 기계적 효율성의 추구는 오히려 학습자의 스캐폴딩과 인지적 땀방울을 증발시켜 버립니다.</div>
        <div class="mcq-option" data-correct="false">D. 우리는 의도적 마찰을 두려워하지 않고 인간적 고뇌의 과정을 교실로 끌어와야만 합니다.</div>
        <div class="mcq-option" data-correct="false">E. 궁극적으로 AI 인프라는 교육의 아날로그적 본질(사랑과 헌신)을 절대로 상실시킬 수 없습니다.</div>
        <button class="submit-btn" type="button">정답 제출하기</button>
        <div class="feedback-msg"></div>
    </div>
    """,
    """
    <div class="interactive-widget dnd-widget">
        <h4 class="widget-title">🧩 문장 복원하기 (Drag & Drop)</h4>
        <p style="margin-bottom:1rem;">아래의 단어 블록을 드래그하여, 문맥상 알맞은 빈칸에 채워 넣으세요.</p>
        <div class="dnd-container">
            <div class="draggable" draggable="true" data-value="마찰">마찰</div>
            <div class="draggable" draggable="true" data-value="연대">연대</div>
            <div class="draggable" draggable="true" data-value="종속">종속</div>
        </div>
        <p style="font-size:1.15rem; line-height:2.0; margin-top:1.5rem; padding: 1.5rem; background: #fafafa; border:1px solid #e2e8f0; border-radius:8px; color: #334155;">
            우리는 기계에 대한 맹목적인 <span class="dropzone" data-target="종속"></span>을(를) 거부하고, 
            사고의 근육을 키우기 위한 고통스러운 인지적 <span class="dropzone" data-target="마찰"></span>을(를) 개입시켜, 
            결국 서로의 체온을 나누는 아날로그적 <span class="dropzone" data-target="연대"></span> 생태계를 창조해야 합니다.
        </p>
        <button class="submit-btn" type="button">정답 제출하기</button>
        <div class="feedback-msg"></div>
    </div>
    """,
    """
    <div class="interactive-widget sa-widget">
        <h4 class="widget-title">⌨️ 핵심 어휘 회상 (단답형)</h4>
        <p style="margin-bottom: 1rem;">알고리즘의 정보 편식 문제와 관련하여, <strong>"자신과 비슷한 성향의 추천 정보만 반복적으로 수용하여 벽에 둘러싸인 닫힌 사고에 갇히는 현상"</strong>을 무엇이라 부릅니까?</p>
        <input type="text" class="short-answer-input" placeholder="핵심 단어를 입력해주세요 (예: 에코체임버, 확증편향)" data-target="에코체임버,메아리방,확증,편향">
        <button class="submit-btn" type="button">정답 제출하기</button>
        <div class="feedback-msg"></div>
    </div>
    """,
    """
    <div class="interactive-widget mcq-widget">
        <h4 class="widget-title">🧐 인지적 점검: 올바른 학습자상</h4>
        <p style="margin-bottom:1.5rem;">에이전틱 AI 시대를 살아갈 학습자의 바람직한 학습 태도로 <strong>가장 적절한 것</strong>을 고르세요.</p>
        <div class="mcq-option" data-correct="false">A. AI가 논리적으로 도출한 결과물을 절대적 진리로 여기고 무비판적으로 수용합니다.</div>
        <div class="mcq-option" data-correct="false">B. 학습 속도의 효율성을 극대화하기 위해 질문을 포기하고 기계적 암기에 몰두합니다.</div>
        <div class="mcq-option" data-correct="true">C. 결과물 도출의 주도권을 기계에 넘기지 않고, 치열하게 '왜'라고 묻는 주체성을 유지합니다.</div>
        <div class="mcq-option" data-correct="false">D. 인간 동료와의 불완전한 협력 대신 AI 튜터와의 완벽히 통제된 개인 대화만을 유일한 학습 수단으로 삼습니다.</div>
        <div class="mcq-option" data-correct="false">E. 스스로 사고하는 과정을 생략한 채, AI의 출력을 보기 좋게 편집하는 2차 가공 기술에만 전념합니다.</div>
        <button class="submit-btn" type="button">정답 제출하기</button>
        <div class="feedback-msg"></div>
    </div>
    """
]

def build_chapter_20():
    with open("d:/AIED2.0_docs/docs/chapter-1.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
    
    if soup.title: soup.title.string = "부록. AI교육 2026 통합 용어 사전"
    header = soup.find('h1')
    if header: header.string = "부록. AI교육 2026 통합 용어 사전"
    
    # Empty existing content
    for cp in soup.find_all(class_='checkpoint-widget'): cp.decompose()
    for ds in soup.find_all(class_='reflection-section'): ds.decompose()
    for nav in soup.find_all('h2'): nav.decompose()
    for gl in soup.find_all(class_='glossary-section'): gl.decompose()
    
    article = soup.find(class_="article-content")
    if article:
        article.clear()
        
        intro = soup.new_tag('p', style="font-size: 1.15rem; color: #475569; margin-bottom: 2.5rem; line-height:1.7;")
        intro.string = "1장부터 19장까지 본문 전체에서 심도 있게 다루어진 주요 철학적, 사회학적, 기술적 고유명사 및 개념들의 정의를 한곳에 편찬했습니다. 각 용어 우측의 위키백과 링크를 통해 영문 원문 해설을 탐독하실 수 있습니다."
        article.append(intro)
        
        ul = soup.new_tag('ul', style="line-height:2.0; font-size:1.1rem; list-style:none; padding:0;")
        for k, v in GLOSSARY_DB.items():
            li = soup.new_tag('li', style="margin-bottom:2rem; border-bottom:1px solid #e2e8f0; padding-bottom:1.5rem;")
            
            strong = soup.new_tag('strong', style="font-size: 1.3rem; color: #0f172a;")
            strong.string = v[0]
            
            link = soup.new_tag('a', href=v[2], target="_blank", style="margin-left:12px; font-size:0.95rem; color:#2563eb; text-decoration:none; background:#eff6ff; padding:4px 8px; border-radius:4px;")
            link.string = "위키백과 원문 보기 ↗"
            
            p = soup.new_tag('p', style="margin-top:0.8rem; color:#334155; line-height:1.6;")
            p.string = v[1]
            
            li.append(strong)
            li.append(link)
            li.append(p)
            ul.append(li)
            
        article.append(ul)
        
    with open("d:/AIED2.0_docs/docs/chapter-20.html", "w", encoding="utf-8") as f:
        f.write(str(soup))
    print("Chapter 20 Generated.")

def process_chapter(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    soup = BeautifulSoup(content, "html.parser")
    article = soup.find(class_="article-content")
    if not article: return

    # 1. Mermaid theme updates
    head = soup.find('head')
    if head:
        for script in head.find_all('script'):
            if script.string and 'mermaid.initialize' in script.string:
                script.string = "mermaid.initialize({ startOnLoad: true, theme: 'base', look: 'handDrawn', themeVariables: { primaryColor: '#fdf2e9' } });"
        
        style = soup.new_tag('style')
        style.string = "\n.mermaid { overflow-x: auto; text-align: center; margin: 2rem 0; clear:both; }\n.mermaid svg { max-width: 100%; height: auto; }\n"
        head.append(style)

    # 2. Extract Phase 2 Garbage
    full_text = article.get_text()
    found_terms = []
    for key, data in GLOSSARY_DB.items():
        if key in full_text:
            found_terms.append(data)

    for cp in soup.find_all(class_='checkpoint-widget'): cp.decompose()
    for gl in soup.find_all(class_='glossary-section'): gl.decompose()
    for s in soup.find_all('script'):
        if s.string and ('showAlert' in s.string or 'fireConfetti' in s.string or 'setupWidgets' in s.string):
            s.decompose()

    # 3. Unbold body paragraphs
    for bold_tag in article.find_all(['strong', 'b']):
        parent = bold_tag.parent
        is_heading_or_box = False
        while parent:
            if parent.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6'] or ('class' in parent.attrs and 'highlight-box' in parent['class']):
                is_heading_or_box = True
                break
            parent = parent.parent
        if not is_heading_or_box:
            bold_tag.unwrap()

    # 4. Turn double quotes to italics
    for text_node in article.find_all(string=True):
        if text_node.parent.name in ['script', 'style', 'code', 'textarea', 'button', 'a', 'h1', 'h2', 'h3']:
            continue
        original = text_node.string
        if not original or '"' not in original: continue
        
        new_html = re.sub(r'"([^"\\.?!]{1,25})"', r'<em>\1</em>', original)
        if new_html != original:
            parsed_inner = BeautifulSoup(new_html, 'html.parser')
            text_node.replace_with(parsed_inner)

    # 5. Heading Flattening
    heading_counter = 1
    for h_tag in article.find_all(['h2', 'h3', 'h4']):
        raw_text = h_tag.get_text().strip()
        
        if "성찰과 연대" in raw_text:
            continue
            
        clean_text = re.sub(r'^[0-9]+\.[0-9]*\s*장?[\.\s]*', '', raw_text)
        clean_text = re.sub(r'^[0-9]+장\s+', '', clean_text)
        
        h_tag.name = 'h2'
        h_tag.string = f"{heading_counter}. {clean_text}"
        heading_counter += 1

    # 6. Inject DOM Widgets and Glossary safely
    reflection = article.find(class_='reflection-section')
    
    h2_tags = article.find_all('h2')
    h2_valid = [h for h in h2_tags if "성찰과 연대" not in h.get_text()]
    
    for h2 in h2_valid[1:]:
        widget_soup = BeautifulSoup(random.choice(WIDGET_TEMPLATES), "html.parser")
        h2.insert_before(widget_soup)
        
    last_widget_soup = BeautifulSoup(random.choice(WIDGET_TEMPLATES), "html.parser")
    
    glossary_soup = None
    if found_terms:
        glossary_html = '<div class="glossary-section" style="margin-top: 4rem; padding: 2.5rem; background: #fafafa; border-radius:12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">'
        glossary_html += '<h3 style="margin-top:0; font-size:1.4rem; color:#0f172a; margin-bottom:1.5rem;">📖 용어 해설 (본문 인용)</h3><ul style="line-height:2.0; color:#334155; font-size:1.05rem;">'
        for data in found_terms:
            glossary_html += f'<li style="margin-bottom: 0.8rem;"><strong>{data[0]}</strong>: {data[1]} <a href="{data[2]}" target="_blank" style="color:#2563eb; text-decoration:none; font-size:0.9rem;">[위키백과 ↗]</a></li>'
        glossary_html += '</ul></div>'
        glossary_soup = BeautifulSoup(glossary_html, "html.parser")

    if reflection:
        reflection.insert_before(last_widget_soup)
        if glossary_soup:
            reflection.insert_before(glossary_soup)
    else:
        article.append(last_widget_soup)
        if glossary_soup:
            article.append(glossary_soup)

    html_out = str(soup)
    html_out = html_out.replace('</body>', WIDGET_CSS_JS + '\n</body>')

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_out)

build_chapter_20()
for file in glob.glob("d:/AIED2.0_docs/docs/chapter-*.html"):
    process_chapter(file)
    print(f"Phase 3 Transformation Complete: {os.path.basename(file)}")
