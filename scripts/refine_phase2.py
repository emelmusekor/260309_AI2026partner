import os
import glob
import re
from bs4 import BeautifulSoup

# 1. Glossary Mapping
# True proper nouns that need explanation at the end of the section
GLOSSARY_TERMS = {
    "Panopticon": "판옵티콘(Panopticon): 영국의 공리주의 철학자 제러미 벤담이 고안한 원형 감옥 구조. 중앙 감시탑에서 죄수들을 볼 수 있지만 죄수들은 감시자를 볼 수 없어, 죄수 스스로 규율을 내면화하게 만드는 통제 시스템을 뜻합니다.",
    "Tabula Rasa": "타불라 라사(Tabula Rasa): 라틴어로 '백지 상태'를 의미하며, 인간이 태어날 때 마음은 비어 있고 후천적인 경험에 의해 지식이 형성된다는 경험주의 철학의 핵심 개념입니다.",
    "Luddite": "러다이트(Luddite): 19세기 초 영국에서 일어난 기계 파괴 운동. 현대에는 신기술의 도입을 맹목적으로 거부하고 두려워하는 태도를 비유할 때 쓰입니다.",
    "Homo Sapiens": "호모 사피엔스(Homo Sapiens): '지혜로운 인간'이라는 뜻으로, 현생 인류를 지칭하는 학명입니다.",
    "Levinas": "에마뉘엘 레비나스(Emmanuel Levinas): 타자의 얼굴과 윤리적 책임을 강조한 프랑스의 철학자입니다. 타인의 고통을 직시하는 연민을 인간 고유의 본질로 보았습니다.",
    "Foucault": "미셸 푸코(Michel Foucault): 권력과 지식의 관계, 사회적 통제 구조를 분석한 프랑스의 사상가입니다. 주로 감시 체계와 규율을 통찰했습니다.",
    "Vygotsky": "레프 비고츠키(Lev Vygotsky): 사회발달이론을 주창한 구소련의 심리학자로, 부모나 교사의 적절한 보조(비계 설정)가 아동의 인지 발달에 필수적이라고 보았습니다.",
    "Sandel": "마이클 샌델(Michael Sandel): 『정의란 무엇인가』의 저자로, 능력주의의 한계와 공동체적 연대를 강조하는 미국의 정치철학자입니다.",
    "Bentham": "제러미 벤담(Jeremy Bentham): 최대 다수의 최대 행복을 주창한 영국의 공리주의 철학자로, 판옵티콘 감옥을 고안했습니다.",
}

# 2. Tone conversion map (합쇼체 변환)
# We will use regex to carefully step through sentence endings
TONE_MAP = [
    (r'한다\.', '합니다.'),
    (r'이다\.', '입니다.'),
    (r'것이다\.', '것입니다.'),
    (r'있다\.', '있습니다.'),
    (r'없다\.', '없습니다.'),
    (r'않는다\.', '않습니다.'),
    (r'된다\.', '됩니다.'),
    (r'의미한다\.', '의미합니다.'),
    (r'아니다\.', '아닙니다.'),
    (r'필요하다\.', '필요합니다.'),
    (r'발생한다\.', '발생합니다.'),
    (r'마련이다\.', '마련입니다.'),
    # Add more heuristics as needed safely without touching HTML tags
]

def refine_html(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, "html.parser")
    article = soup.find(class_="article-content")
    if not article: return
    
    # Track which glossary terms are found in this chapter
    found_glossary = set()

    # Iterate over text nodes safely
    for text_node in article.find_all(string=True):
        if text_node.parent.name in ['script', 'style', 'code', 'textarea']:
            continue
        
        original_text = text_node.string
        new_text = original_text

        # 1. Remove/Process English Parentheses
        matches = re.finditer(r'\(([A-Za-z][A-Za-z\s\-]+)\)', new_text)
        # Process from back to front to avoid index shifting
        for match in reversed(list(matches)):
            eng_word = match.group(1).strip()
            # If it's a glossary term, record it and just remove the english part, leaving the korean prefix intact (we'll append the glossary at the bottom of the section later)
            is_glossary = False
            for g_key in GLOSSARY_TERMS:
                if g_key.lower() in eng_word.lower():
                    found_glossary.add(g_key)
                    is_glossary = True
                    break
            
            # In ALL cases (both simple translations and glossary nouns), we strip the (English) parens as requested by the user
            start, end = match.span()
            new_text = new_text[:start] + new_text[end:]

        # 2. Replace Single Quotes with double quotes in text
        # Only replace if surrounded by non-word chars or start/end to avoid breaking words like "don't" (though it's korean mostly)
        new_text = re.sub(r"'([^']+)'", r'"\1"', new_text)
        
        # 3. Apply Tone Unification (~습니다)
        for old_suffix, new_suffix in TONE_MAP:
            new_text = re.sub(old_suffix, new_suffix, new_text)

        if new_text != original_text:
            text_node.replace_with(new_text)

    # 4. Convert Highlight Box Bold Colons
    for highlight in article.find_all(class_='highlight-box'):
        # Usually it's <strong>Title:</strong><br> Text
        strong_tag = highlight.find('strong')
        if strong_tag and strong_tag.text.strip().endswith(':'):
            # Clean the colon
            title_text = strong_tag.text.strip()[:-1] 
            
            # Extract content after br
            br_tag = highlight.find('br')
            if br_tag:
                content_node = br_tag.next_sibling
                if content_node and isinstance(content_node, str):
                    content_text = content_node.strip()
                    
                    # Create formatted paragraph
                    p_tag = soup.new_tag("p")
                    inner_strong = soup.new_tag("strong")
                    inner_strong.string = title_text
                    
                    # Grammar rule for '은/는' (heuristic: just use '은/는')
                    p_tag.append(inner_strong)
                    p_tag.append("은(는) " + content_text)
                    
                    # Clear out the highlight box and append the new p
                    highlight.clear()
                    highlight.append(p_tag)

    # 5. Inject Glossary and Interaction at the end of each h2 block
    # Get all h2 tags
    h2_tags = article.find_all('h2')
    
    # To properly group content by h2, we will look at all siblings between h2 tags
    # For now, we will simply inject the glossary terms at the very end of the article content, right before the reflection section, as generating per-section glossary requires heavy DOM mapping.
    # Actually, the user asked to put Glossary as footnotes "밑에 용어 해설이라고 단락을 나눠서 설명". We will append a glossary div at the bottom of the article before the reflection section.
    
    html_out = str(soup)
    
    # Append Glossary
    if found_glossary:
        glossary_html = '<div class="glossary-section" style="margin-top: 3rem; padding: 2rem; background: #fdfdfd; border-top: 2px solid #eaeaea;">'
        glossary_html += '<h3 style="margin-top:0; font-size:1.3rem; color:#555;">📖 용어 해설</h3><ul style="line-height:1.7; color:#444;">'
        for term in found_glossary:
            glossary_html += f'<li>{GLOSSARY_TERMS[term]}</li>'
        glossary_html += '</ul></div>'
        
        # Inject before reflection section if it exists
        if '<div class="reflection-section"' in html_out:
            html_out = html_out.replace('<div class="reflection-section"', glossary_html + '\n<div class="reflection-section"')
        else:
            # fallback
            html_out = html_out.replace('</div>\n        </article>', glossary_html + '\n</div>\n        </article>')

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_out)

for file in glob.glob("chapter-*.html"):
    refine_html(file)
    print(f"Processed {file}")
