import os
import glob
import re

questions = {
    1: "인공지능을 단순한 도구가 아닌 '인지적 파트너'로 받아들이기 위해, 당신의 일상이나 교실에서 가장 먼저 버려야 할 낡은 습관은 무엇입니까?",
    2: "기술의 도입이 오히려 인간의 고유한 권위(사랑, 연대, 철학적 사유)를 부각시킨 역사적 사례들을 떠올려 볼 때, 2026년 교사의 진정한 권위는 어디에서 비롯될 것이라 생각하십니까?",
    3: "물리적 칸막이를 허무는 일(무경계 교실)이 필연적으로 수반할 혼란과 마찰은, 역설적으로 아이들에게 어떤 민주적 합의의 기술을 가르쳐 줄 수 있을까요?",
    4: "AI가 초개인화된 학습 경로를 제공할 때, 고립된 학습자가 아닌 '연대하는 학습자'를 길러내기 위해 우리에게 필요한 공통의 경험은 무엇입니까?",
    5: "기계가 학생의 감정과 학습 상태를 데이터로 읽어내는 시대에, 오직 인간 교사만이 포착할 수 있는 '데이터 밖의 신호(예: 침묵의 질감)'는 무엇이 있을까요?",
    6: "생성 에이전트(Agentic AI)가 모든 초안을 3초 만에 작성해주는 환경에서, 우리는 학생들에게 '글을 쓴다는 것'의 의미를 어떻게 다시 정의하고 가르쳐야 할까요?",
    7: "평가가 더 이상 줄 세우기가 아닌 '성장 궤적의 추적'이 될 때, 학생과 학부모의 '성적에 대한 불안'을 어떻게 긍정적인 기대감으로 바꿀 수 있을까요?",
    8: "모든 지식이 AI를 통해 실시간으로 연결될 때, 각 교과목의 경계는 정말 사라져야 할까요, 아니면 새로운 형태로 재편되어야 할까요?",
    9: "지식의 생산 비용이 '0'에 수렴하는 이 상황을 15세기 활자 혁명과 비교한다면, 지금 우리에게 가장 시급하게 필요한 새로운 '문해력'은 무엇입니까?",
    10: "학생 개개인의 인지 모델을 AI가 완벽히 파악한다면, 이는 완벽한 맞춤형 교육일까요, 아니면 알고리즘에 의한 또 다른 의미의 '통제'일까요?",
    11: "AI 에이전트가 교사의 행정 업무를 전부 처리하는 여백의 시간에, 교사는 학생들에게 그 시간을 온전히 어떤 방식으로 돌려주어야 합니까?",
    12: "앰비언트 컴퓨팅 기반의 학습 공간에서 일어나는 상호작용은 기존 아날로그 교실의 상호작용과 어떤 한계와 철학적 가능성을 지닙니까?",
    13: "AI가 교육 행정과 정책 결정을 데이터 기반으로 주도할 때, 소수자를 위한 '데이터화 되지 않는 배려'는 시스템 내에 어떻게 설계되어야 할까요?",
    14: "지역적 불평등을 AI 클라우드가 기술적으로 해소한다고 가정할 때, 여전히 남을 수밖에 없는 '지역 사회의 문화적 자본' 격차는 어떻게 극복해야 할까요?",
    15: "교사 양성 과정(사범대, 교육대)이 AI 시대에 맞게 재편된다면, 예비 교사들이 가장 먼저 배워야 할 '기술 외적인' 학문은 무엇이 되어야 할까요?",
    16: "AI 에듀테크 상업 자본의 팽창 속에서, 공교육이 영리 기업의 논리에 휘둘리지 않기 위한 최후의 방어선(거버넌스)은 무엇입니까?",
    17: "교육의 3주체(교사, 학생, 학부모)에 'AI'라는 제4의 주체가 편입되는 인지적 혁명기에서, 기계의 제안에 오류가 났을 때 우리는 누구에게 윤리적 책임을 물어야 할까요?",
    18: "K-에듀가 글로벌 스탠다드로 도약해 유네스코 발전에 기여하려면, 한국 교육 특유의 어떤 '인문학적 연대 정서'를 세계와 공유해야 할까요?",
    19: "모든 것이 완벽하게 통제되고 수치화되는 알고리즘 사회 속에서, 공교육은 어떻게 학생들에게 '방황할 자유'와 '실패할 특권'을 보장할 수 있을까요?"
}

def refine_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract chapter number
    chapter_match = re.search(r'chapter-(\d+)\.html', os.path.basename(file_path))
    if not chapter_match: return False
    chap_num = int(chapter_match.group(1))

    # 1. Structural Regex Replacements
    # Remove all ** from text, excluding CSS contexts if any (unlikely in HTML text but just in case)
    content = content.replace("**", "")
    content = content.replace("``", "")
    
    # Remove single quotes enclosing Korean words or spaces, e.g. '공동체' -> 공동체
    # Negative lookbehind to avoid destroying HTML attributes like class='foo'
    # HTML attributes normally use double quotes, but just to be safe
    content = re.sub(r"(?<!=)'([가-힣\s]+)'", r"\1", content)
    content = re.sub(r"(?<!=)'([A-Za-z\s\-]+)'", r"\1", content)

    # 2. Add Reflection Section if not exists
    if "reflection-section" not in content:
        q = questions.get(chap_num, "2026년의 변화 속에서 당신의 역할을 어떻게 재정의하시겠습니까?")
        reflection_html = f"""
    <div class="reflection-section" style="margin-top: 4rem; padding: 2.5rem; background: #fafafa; border-radius: 12px; border: 1px solid #eaeaea; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
        <h3 style="margin-top: 0; color: #111; font-size: 1.5rem; margin-bottom: 0.5rem; display: flex; align-items: center; gap: 0.5rem;">
            성찰과 연대: 2026년을 향한 당신의 생각
        </h3>
        <p style="font-size: 1.15rem; color: #444; margin-bottom: 2rem; line-height: 1.6;">{q}</p>
        <textarea id="reflection-answer-{chap_num}" placeholder="자신의 생각을 편안하고 솔직하게 기록해보세요..." style="width: 100%; height: 140px; padding: 1.2rem; border-radius: 8px; border: 1px solid #ccc; font-family: inherit; font-size: 1.05rem; margin-bottom: 1.5rem; resize: vertical; box-sizing: border-box; background: #fff;"></textarea>
        <button onclick="saveReflection({chap_num})" style="background: #1a1a1a; color: white; border: none; padding: 1rem 2rem; border-radius: 8px; font-size: 1.05rem; font-weight: 600; cursor: pointer; transition: background 0.2s;">내 생각 제출하기 (로컬 저장)</button>
        <p id="save-msg-{chap_num}" style="display: none; color: #22c55e; margin-top: 1rem; font-weight: 500; font-size: 1.05rem;">✓ 기기에 안전하게 저장되었습니다. 향후 서버 연동 시 익명으로 공유될 수 있습니다.</p>
    </div>
    <script>
        function saveReflection(chapterNum) {{
            const answer = document.getElementById(`reflection-answer-${{chapterNum}}`).value;
            document.cookie = `reflection_${{chapterNum}}=${{encodeURIComponent(answer)}}; max-age=31536000; path=/`;
            const msg = document.getElementById(`save-msg-${{chapterNum}}`);
            msg.style.display = 'block';
            setTimeout(() => {{ msg.style.display = 'none'; }}, 3000);
        }}
        
        document.addEventListener("DOMContentLoaded", () => {{
            const match = document.cookie.match(new RegExp('(^| )reflection_' + {chap_num} + '=([^;]+)'));
            if (match) {{
                document.getElementById(`reflection-answer-${{chap_num}}`).value = decodeURIComponent(match[2]);
            }}
        }});
    </script>
"""
        target = "</div>\n        </article>"
        if target in content:
            content = content.replace(target, reflection_html + "\n        " + target)

    # 3. Mermaid error fixes
    # Find labels that have `(`, `)`, `,` but aren't quoted.
    # Exclude subgraph declarations and edge labels. Node IDs are alphanumeric/underscore.
    # A[Label containing (issue)] -> A["Label containing (issue)"]
    # We'll regex search for unquoted content between [ and ] that might break.
    def quote_mermaid(m):
        prefix = m.group(1)
        inner = m.group(2)
        if '"' in inner: # already contains quotes
            return m.group(0)
        # Quote if there's a parenthesis or comma
        if '(' in inner or ')' in inner or ',' in inner:
            return f'{prefix}["{inner}"]'
        return m.group(0)
    
    # We only want to apply this inside mermaid blocks.
    def process_mermaid_block(m_block):
        block_text = m_block.group(0)
        # Match A[...], B[...] inside block
        # Group 1 = node id, Group 2 = content
        block_text = re.sub(r'([A-Za-z0-9_]+)\[([^\]\n]+)\]', quote_mermaid, block_text)
        return block_text

    content = re.sub(r'<div class="mermaid">.*?</div>', process_mermaid_block, content, flags=re.DOTALL)

    # 4. Humanize tone by replacing typical AI phrases
    # Let's make it sound more like an essay or philosophical treatise.
    replacements = {
        "우리는 ~해야 합니다": "우리의 발걸음은 이미 그곳을 향해야 한다",
        "필수적입니다.": "이제 생존과 직결된 기본 전제가 되었다.",
        "결론적으로,": "결국 가장 밑바닥에 남는 질문은 이것이다.",
        "요약하자면,": "이 모든 현상을 관통하는 단 하나의 맥락은,",
        "생성형 인공지능": "생성 에이전트(Agentic AI)",
        "프롬프트 엔지니어링": "질문 설계(Prompt Architecting)",
        "해야 합니다.": "할 시대적 요구령에 직면했다.",
        "입니다.": "이다.",  # This could break formatting if overused, wait, let's avoid broad verbs
    }
    
    # We will only do safe phrase replacements so it doesn't break everything.
    safe_replacements = {
        "우리는 이제 ": "이제 우리는 ",
        "결론적으로, ": "결국 이 거대한 흐름이 가리키는 종착지는, ",
        "요약하자면, ": "앞선 논의들을 관통하는 하나의 거대한 줄기는, ",
    }
    for k, v in safe_replacements.items():
        content = content.replace(k, v)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    return True

processed = []
for file_path in glob.glob(r"d:\AIED2.0_docs\docs\chapter-*.html"):
    if refine_html(file_path):
        processed.append(os.path.basename(file_path))

print(f"Processed {len(processed)} chapters: {', '.join(processed)}")
