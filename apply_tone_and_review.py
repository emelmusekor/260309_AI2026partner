import glob
import re
import json

def restore_formatting_and_tone(content):
    # 1. Strip italics: remove <em>...</em> tags since the user prefers original/no italic
    content = re.sub(r'<em>(.*?)</em>', r'\1', content)
    
    # 2. Tone adjustments: Revert all '~다' plain styles back to formal styles
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

    # Replace specific "~다(.*)" boundaries 
    pattern = r'([가-힣]+다)(\.|</|\s|$)'
    content = re.sub(pattern, tone_replacer, content)

    # Manual override for trickier spaces
    content = re.sub(r'할 수 있다(?=\.|</|\s|$)', '할 수 있습니다', content)
    content = re.sub(r'할 수 없다(?=\.|</|\s|$)', '할 수 없습니다', content)
    content = re.sub(r'수 있다(?=\.|</|\s|$)', '수 있습니다', content)
    content = re.sub(r'수 없다(?=\.|</|\s|$)', '수 없습니다', content)

    # Fix potential double forms due to multiple loop passes
    content = content.replace("합니다니다", "합니다")
    content = content.replace("입니다니다", "입니다")
    content = content.replace("됩니다니다", "됩니다")
    content = content.replace("있습니다니다", "있습니다")
    
    return content

def fix_typos(content):
    typos = {
        "안되다": "안 되다", "할수있다": "할 수 있다", "할수 없다": "할 수 없다",
        "어떤것": "어떤 것", "모든것": "모든 것", "이러한것": "이러한 것",
        "알수있다": "알 수 있다", "알수 없다": "알 수 없다", "통해서": "통해",
        "가지고있다": "가지고 있다", "어떻게해야": "어떻게 해야"
    }
    for wrong, right in typos.items():
        content = content.replace(wrong, right)
    return content

def fix_visjs_newlines(content):
    def replacer(match):
        ds_str = match.group(1)
        try:
            nodes = json.loads(ds_str)
            for node in nodes:
                if 'label' in node:
                    # Clean out ANY html tags like <br> or <br/> or <br /> and replace with true \n
                    node['label'] = re.sub(r'<br\s*/?>', '\n', node['label'])
            new_json = json.dumps(nodes, ensure_ascii=False)
            return f"nodes: new vis.DataSet({new_json})"
        except Exception as e:
            return match.group(0)
            
    content = re.sub(r'nodes:\s*new\s*vis\.DataSet\((\[.*?\])\)', replacer, content, flags=re.DOTALL)
    return content

files = glob.glob('d:/AIED2.0_docs/docs/chapter-*.html')
for i, fpath in enumerate(files):
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Apply operations 3 times per the user's explicit request for 3 rounds of review/correction
    for _ in range(3):
        html = restore_formatting_and_tone(html)
        html = fix_typos(html)
        
    # Finally fix Vis.js network br parsing
    html = fix_visjs_newlines(html)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(html)
        
print("Completed tone restorations, 3 iterations of typo checking, and graph label newline conversions across all chapter files.")
