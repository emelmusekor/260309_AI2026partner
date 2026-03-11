import os
import glob
import re
from bs4 import BeautifulSoup, NavigableString
import random

GLOSSARY_TERMS = {
    "panopticon": "판옵티콘(Panopticon): 영국의 철학자 제러미 벤담이 고안한 원형 감옥 구조. 감시자는 보이지 않으나 죄수는 항상 감시받는다고 느끼게 통제하는 시스템입니다.",
    "luddite": "러다이트(Luddite): 19세기 영국에서 일어난 기계 파괴 운동. 신기술의 도입을 맹목적으로 거부하고 두려워하는 태도를 비유합니다.",
    "tabula rasa": "타불라 라사(Tabula Rasa): 라틴어로 '백지 상태'를 의미하며, 인간의 마음은 비어 있고 경험에 의해 지식이 형성된다는 개념입니다.",
    "homo sapiens": "호모 사피엔스(Homo Sapiens): '지혜로운 인간'이라는 뜻으로, 현생 인류를 지칭합니다.",
    "levinas": "에마뉘엘 레비나스(Emmanuel Levinas): 타자의 얼굴과 윤리적 책임을 강조한 프랑스의 철학자입니다.",
    "foucault": "미셸 푸코(Michel Foucault): 권력과 지식의 관계, 감시 체계와 규율을 통찰한 프랑스의 사상가입니다.",
    "vygotsky": "레프 비고츠키(Lev Vygotsky): 사회발달이론을 주창한 구소련의 심리학자로, 교사의 스캐폴딩(비계 설정)을 강조했습니다.",
    "sandel": "마이클 샌델(Michael Sandel): 정의와 기회라는 주제를 깊이 연구한 정치철학자로, 공동체적 연대를 강조합니다.",
    "bentham": "제러미 벤담(Jeremy Bentham): 영국의 공리주의 철학자이자 판옵티콘 구조의 창시자입니다.",
    "grand narrative": "거대 서사(Grand Narrative): 역사의 발전을 설명하는 포괄적이고 거시적인 이데올로기나 철학적 틀을 의미합니다.",
    "symbiosis": "공진화(Symbiosis): 서로 다른 개체가 상호작용하며 함께 진화하고 발전하는 현상을 뜻합니다.",
    "resilience": "회복탄력성(Resilience): 역경이나 실패에 좌절하지 않고 밑바닥에서 다시 튀어 오르는 심리적 근력을 의미합니다.",
    "echo chamber": "에코체임버(Echo Chamber): 자신과 비슷한 성향의 정보만 반복적으로 수용하여 편향된 사고에 갇히는 현상을 의미합니다.",
    "hallucination": "환각(Hallucination): 인공지능이 사실이 아닌 내용을 마치 사실인 것처럼 그럴듯하게 생성해내는 오류 현상입니다."
}

def tone_unify(text):
    # Change plain verb endings to polite (~습니다, ~합니다, ~일까요?) forms.
    # We do regex matches for common patterns ending with a period.
    text = re.sub(r'([가-힣]+)한다\.', r'\1합니다.', text)
    text = re.sub(r'([가-힣]+)된다\.', r'\1됩니다.', text)
    text = re.sub(r'([가-힣]+)이다\.', r'\1입니다.', text)
    text = re.sub(r'([가-힣0-9a-zA-Z]+)이다\.', r'\1입니다.', text)
    text = re.sub(r'([가-힣]+)것이다\.', r'\1것입니다.', text)
    text = re.sub(r'([가-힣]+)있다\.', r'\1있습니다.', text)
    text = re.sub(r'([가-힣]+)없다\.', r'\1없습니다.', text)
    text = re.sub(r'([가-힣]+)않는다\.', r'\1않습니다.', text)
    text = re.sub(r'([가-힣]+)아니다\.', r'\1아닙니다.', text)
    text = re.sub(r'([가-힣]+)시킨다\.', r'\1시킵니다.', text)
    text = re.sub(r'([가-힣]+)받는다\.', r'\1받습니다.', text)
    text = re.sub(r'([가-힣]+)넘는다\.', r'\1넘습니다.', text)
    text = re.sub(r'([가-힣]+)모른다\.', r'\1모릅니다.', text)
    text = re.sub(r'([가-힣]+)맞는다\.', r'\1맞습니다.', text)
    text = re.sub(r'([가-힣]+)끝난다\.', r'\1끝납니다.', text)
    text = re.sub(r'([가-힣]+)나타난다\.', r'\1나타납니다.', text)
    text = re.sub(r'([가-힣]+)사라진다\.', r'\1사라집니다.', text)
    text = re.sub(r'([가-힣]+)가진다\.', r'\1가집니다.', text)
    text = re.sub(r'([가-힣]+)생긴다\.', r'\1생깁니다.', text)
    text = re.sub(r'([가-힣]+)바뀐다\.', r'\1바뀝니다.', text)
    text = re.sub(r'([가-힣]+)돌아간다\.', r'\1돌아갑니다.', text)
    
    # Question marks
    text = re.sub(r'([가-힣]+)일까\?', r'\1일까요?', text)
    text = re.sub(r'([가-힣]+)할까\?', r'\1할까요?', text)
    text = re.sub(r'([가-힣]+)있는가\?', r'\1있을까요?', text)
    text = re.sub(r'([가-힣]+)되는가\?', r'\1될까요?', text)
    text = re.sub(r'([가-힣]+)된단 말인가\?', r'\1된다는 말입니까?', text)

    return text

def generate_checkpoint_html(idx):
    # Variety of generic but highly relevant philosophical checkpoints
    checkpoints = [
        f"""
        <div class="checkpoint-widget" style="background:#f8fafc; padding:1.5rem; border-radius:8px; margin: 3rem 0; border: 1px solid #e2e8f0;">
          <h4 style="margin-top:0; color:#0f172a; display:flex; align-items:center; gap:0.5rem;">🎯 단원 점검 (Checkpoint)</h4>
          <p style="margin-bottom:1rem; color:#334155;">이 단원의 핵심 논조로 올바른 것을 하나 선택해주세요.</p>
          <div style="display:flex; flex-direction:column; gap:0.5rem;">
             <button onclick="showAlert(this, true, '정답입니다! 매끄러운 쾌락보다는 인간 고유의 의도적 마찰이 중요합니다.')" style="text-align:left; padding:1rem; border:1px solid #cbd5e1; background:white; cursor:pointer; border-radius:6px; transition:all 0.2s;">
                 A. 기계의 완벽함에 의존하기보다, 피 흘리는 연대와 의도적 마찰을 통한 비판적 사유가 필수적입니다.
             </button>
             <button onclick="showAlert(this, false, '오답입니다. 기계에 의존하는 것은 인간성의 상실을 초래합니다.')" style="text-align:left; padding:1rem; border:1px solid #cbd5e1; background:white; cursor:pointer; border-radius:6px; transition:all 0.2s;">
                 B. 초거대 인공지능이 제공하는 정답을 무조건적으로 신뢰하고 학습 속도를 높이는 것이 2026년 교육의 유일한 목표입니다.
             </button>
          </div>
          <p class="feedback-msg" style="display:none; margin-top:1rem; font-weight:600;"></p>
        </div>
        """,
        f"""
        <div class="checkpoint-widget" style="background:#fdf4ff; padding:1.5rem; border-radius:8px; margin: 3rem 0; border: 1px solid #fae8ff;">
          <h4 style="margin-top:0; color:#701a75; display:flex; align-items:center; gap:0.5rem;">💭 개념 연결 (Drag & Drop 체험)</h4>
          <p style="margin-bottom:1rem; color:#4a044e;">문맥에 맞는 올바른 단어를 마음속으로 배치해 보거나 버튼을 클릭해 확인해 보세요.</p>
          <div style="padding:1.5rem; background:white; border-radius:6px; border:1px dashed #e879f9;">
              "미래의 교육은 디지털 <strong>[ 빈칸 ]</strong>(을)를 넘어서, 가장 통제된 아날로그적 연대와 <strong>[ 빈칸 ]</strong>(을)를 복원해야만 합니다."
          </div>
          <div style="display:flex; gap:1rem; margin-top:1rem;">
              <button onclick="alert('정답 해설: 미래 교육은 맹목적인 디지털 [종속]을 넘어서 아날로그적 [비판]과 연대를 복원해야 합니다.')" style="background:#d946ef; color:white; border:none; padding:0.8rem 1.5rem; border-radius:4px; font-weight:600; cursor:pointer;">정답과 해설 보기</button>
          </div>
        </div>
        """,
        f"""
        <div class="checkpoint-widget" style="background:#ecfdf5; padding:1.5rem; border-radius:8px; margin: 3rem 0; border: 1px solid #d1fae5;">
          <h4 style="margin-top:0; color:#065f46; display:flex; align-items:center; gap:0.5rem;">⚖️ 가치 판단 (True or False)</h4>
          <p style="margin-bottom:1rem; color:#064e3b;">다음 명제가 이 단원의 철학적 방향과 일치하면 <strong>O</strong>, 아니면 <strong>X</strong>를 선택하세요.</p>
          <p style="font-size:1.1rem; font-style:italic; padding:1rem; background:white; border-radius:4px;">"훌륭한 교사란, 3초 만에 결과물을 뱉어내는 AI를 배척하고 오로지 종이책만 읽히는 러다이트(Luddite)적인 교사이다."</p>
          <div style="display:flex; gap:1rem; margin-top:1rem;">
             <button onclick="showAlert(this, false, '오답입니다. 무조건 배척하는 것이 아니라, AI를 압도적으로 다루되 인간의 마찰을 사수하는 교사여야 합니다.')" style="flex:1; padding:1rem; border:1px solid #34d399; background:white; cursor:pointer; border-radius:6px; font-size:1.2rem; font-weight:bold;">O (주장과 일치함)</button>
             <button onclick="showAlert(this, true, '정답입니다! 극단적 배척이 아닌 마찰적 공진화를 주도하는 것이 올바른 교사의 상입니다.')" style="flex:1; padding:1rem; border:1px solid #34d399; background:white; cursor:pointer; border-radius:6px; font-size:1.2rem; font-weight:bold;">X (주장과 다름)</button>
          </div>
          <p class="feedback-msg" style="display:none; margin-top:1rem; font-weight:600;"></p>
        </div>
        """
    ]
    return random.choice(checkpoints)

# Generic JS used by the checkpoints
js_script = """
<script>
function showAlert(btn, isCorrect, msg) {
    const parent = btn.parentElement.parentElement;
    const msgElement = parent.querySelector('.feedback-msg');
    
    // reset borders
    const btns = parent.querySelectorAll('button');
    btns.forEach(b => {
        b.style.borderColor = '#cbd5e1';
        b.style.backgroundColor = 'white';
        b.style.color = '#333';
    });
    
    if (isCorrect) {
        btn.style.borderColor = '#22c55e';
        btn.style.backgroundColor = '#f0fdf4';
        btn.style.color = '#166534';
        msgElement.style.color = '#166534';
    } else {
        btn.style.borderColor = '#ef4444';
        btn.style.backgroundColor = '#fef2f2';
        btn.style.color = '#991b1b';
        msgElement.style.color = '#991b1b';
    }
    
    msgElement.innerText = msg;
    msgElement.style.display = 'block';
}
</script>
"""

def refine_html(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, "html.parser")
    article = soup.find(class_="article-content")
    if not article: return

    found_glossary = set()

    for text_node in article.find_all(string=True):
        if text_node.parent.name in ['script', 'style', 'code', 'textarea', 'button']:
            continue
            
        original_text = text_node.string
        if not original_text.strip():
            continue

        new_text = str(original_text)

        # 1. Remove/Process English Parentheses
        matches = list(re.finditer(r'\(([A-Za-z][A-Za-z\s\-]+)\)', new_text))
        
        # Traverse backwards to preserve indices
        for match in reversed(matches):
            eng_word = match.group(1).strip()
            
            # Check glossary mapping
            for g_key in GLOSSARY_TERMS:
                if g_key.lower() in eng_word.lower():
                    found_glossary.add(g_key.lower())
                    break
            
            # Delete the parenthesis wrapping English words entirely
            start, end = match.span()
            new_text = new_text[:start] + new_text[end:]

        # 2. Replace Single Quotes with double quotes
        new_text = re.sub(r"'([^']+)'", r'"\1"', new_text)
        
        # 3. Apply Tone Unification (~습니다 / 합쇼체)
        new_text = tone_unify(new_text)

        if new_text != original_text:
            text_node.replace_with(new_text)

    # 4. Convert Highlight Box Bold Colons
    for highlight in article.find_all(class_='highlight-box'):
        strong_tag = highlight.find('strong')
        if strong_tag and strong_tag.text.strip().endswith(':'):
            title_text = strong_tag.text.strip()[:-1]  # remove colon
            
            # Collect everything after strong tag inside highlight
            content_nodes = list(strong_tag.next_siblings)
            
            content_text = ""
            for node in content_nodes:
                if isinstance(node, str):
                    content_text += node
                elif node.name == 'br':
                    content_text += " " # Replace BR with space
                else:
                    content_text += node.get_text()
                    
            content_text = content_text.strip()
            
            # Clear out the highlight box and append the new p
            p_tag = soup.new_tag("p")
            p_tag['style'] = "margin:0;"
            inner_strong = soup.new_tag("strong")
            inner_strong.string = title_text
            
            p_tag.append(inner_strong)
            p_tag.append("은(는) " + content_text)
            
            highlight.clear()
            highlight.append(p_tag)

    # Convert back to raw HTML to inject widgets easily using string manipulation
    # Because find_all('h2') manipulation in soup is tricky with sibling flows
    html_out = str(soup)
    
    # 5. Inject Checkpoint Widgets BEFORE each next <h2> or Glossary/Reflection
    # We can split the text by <h2> and inject the widget before it.
    parts = html_out.split('<h2>')
    if len(parts) > 1:
        new_parts = [parts[0]] # Everything before the first <h2>
        for i in range(1, len(parts)):
            if i < len(parts) - 1:
                # This is a block that ends completely before the next <h2>
                # We inject the widget at the very bottom of this block
                block = parts[i]
                widget = generate_checkpoint_html(i)
                block = block + "\n" + widget + "\n"
                new_parts.append(block)
            else:
                # The very last <h2> block. It ends either before <div class="reflection-section" or before </article>
                last_block = parts[i]
                widget = generate_checkpoint_html(i)
                
                if '<div class="reflection-section"' in last_block:
                    last_block = last_block.replace('<div class="reflection-section"', "\n" + widget + '\n<div class="reflection-section"')
                else:
                    last_block = last_block + "\n" + widget + "\n"
                new_parts.append(last_block)
                
        html_out = '<h2>'.join(new_parts)

    
    # Append Glossary
    if found_glossary:
        glossary_html = '<div class="glossary-section" style="margin-top: 3rem; padding: 2.5rem; background: #fafafa; border-radius:8px; border: 1px solid #eaeaea; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">'
        glossary_html += '<h3 style="margin-top:0; font-size:1.4rem; color:#333; margin-bottom:1.5rem;">📖 용어 해설</h3><ul style="line-height:2.0; color:#555; font-size: 1.1rem; padding-left:1.5rem;">'
        for term in found_glossary:
            glossary_html += f'<li><strong>{GLOSSARY_TERMS[term].split(":")[0]}</strong>: {GLOSSARY_TERMS[term].split(":")[1]}</li>'
        glossary_html += '</ul></div>'
        
        # Inject before reflection section if it exists
        if '<div class="reflection-section"' in html_out:
            html_out = html_out.replace('<div class="reflection-section"', glossary_html + '\n\n<div class="reflection-section"')
        elif '</div>\n        </article>' in html_out:
            html_out = html_out.replace('</div>\n        </article>', glossary_html + '\n</div>\n        </article>')
            
    # Inject JS scripts for interactivity if not present
    if '<script>function showAlert' not in html_out:
        html_out = html_out.replace('</body>', js_script + '\n</body>')

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_out)

for file in glob.glob("d:/AIED2.0_docs/docs/chapter-*.html"):
    refine_html(file)
    print(f"Phase 2 Refinements applied to: {os.path.basename(file)}")
