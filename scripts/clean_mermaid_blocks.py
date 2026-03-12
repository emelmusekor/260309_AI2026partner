import glob
import re

def restore_formatting_and_tone(content):
    content = re.sub(r'<em>(.*?)</em>', r'\1', content)
    content = re.sub(r'<br\s*/?>', ' ', content) # Replace <br> with space
    
    revert_dict = {
        "한다": "합니다", "된다": "됩니다", "이다": "입니다", "것이다": "것입니다",
        "있다": "있습니다", "없다": "없습니다", "않는다": "않습니다", "아니다": "아닙니다",
        "시킨다": "시킵니다", "받는다": "받습니다", "비판한다": "비판합니다", "발생한다": "발생합니다",
        "필요하다": "필요합니다", "만든다": "만듭니다", "넘는다": "넘습니다", "모른다": "모릅니다",
        "가진다": "가집니다", "살펴보겠다": "살펴보겠습니다", "알아보겠다": "알아보겠습니다",
        "배워보겠다": "배워보겠습니다", "진행된다": "진행됩니다", "시작한다": "시작합니다",
        "증명한다": "증명합니다", "제공한다": "제공합니다", "보여준다": "보여줍니다",
        "나타난다": "나타납니다", "의미한다": "의미합니다", "말한다": "말합니다",
        "맞다": "맞습니다", "좋다": "좋습니다", "많다": "많습니다", "적다": "적습니다",
        "같다": "같습니다", "그렇다": "그렇습니다", "어떻다": "어떻습니다", "생긴다": "생깁니다",
        "어렵다": "어렵습니다", "쉽다": "쉽습니다", "온다": "옵니다", "간다": "갑니다",
        "본다": "봅니다", "마련이다": "마련입니다", "수행한다": "수행합니다",
        "분석한다": "분석합니다", "적용한다": "적용합니다", "제안한다": "제안합니다", 
        "설명한다": "설명합니다", "다룬다": "다룹니다", "나온다": "나옵니다",
        "나간다": "나갑니다", "들어간다": "들어갑니다", "생각한다": "생각합니다",
        "가져온다": "가져옵니다", "기대된다": "기대됩니다"
    }

    def tone_replacer(match):
        word = match.group(1)
        suffix = match.group(2)
        return revert_dict.get(word, word) + suffix

    # This regex looks for dictionary matches that end with quote ", space, dot, or end of line.
    # In Mermaid, text is usually inside quotes like ["...다"]
    pattern = r'([가-힣]+다)(\.|"|\s|$)'
    content = re.sub(pattern, tone_replacer, content)

    content = re.sub(r'할 수 있다(?=\.|"|\s|$)', '할 수 있습니다', content)
    content = re.sub(r'할 수 없다(?=\.|"|\s|$)', '할 수 없습니다', content)
    content = re.sub(r'수 있다(?=\.|"|\s|$)', '수 있습니다', content)
    content = re.sub(r'수 없다(?=\.|"|\s|$)', '수 없습니다', content)
    
    return content

files = glob.glob('d:/AIED2.0_docs/docs/chapter-*.html')

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()

    def replacer(match):
        original_mermaid = match.group(1)
        cleaned_mermaid = restore_formatting_and_tone(original_mermaid)
        # remove internal literal html tags which may break rendering or look ugly
        cleaned_mermaid = cleaned_mermaid.replace('&lt;br&gt;', ' ')
        cleaned_mermaid = cleaned_mermaid.replace('&lt;em&gt;', '')
        cleaned_mermaid = cleaned_mermaid.replace('&lt;/em&gt;', '')
        return f'<pre class="mermaid" style="font-size: 1.25rem; font-family: Pretendard, sans-serif;">\n{cleaned_mermaid}\n</pre>'

    curr_html = re.sub(r'<pre class="mermaid"[^>]*>(.*?)</pre>', replacer, html, flags=re.DOTALL)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(curr_html)

print("Successfully cleaned up Mermaid blocks.")
