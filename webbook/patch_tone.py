import glob
import re

for file_path in glob.glob("d:/AIED2.0_docs/webbook/chapter-*.html"):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Aggressive replace
    replacements = {
        "한다.": "합니다.",
        "된다.": "됩니다.",
        "이다.": "입니다.",
        "것이다.": "것입니다.",
        "있다.": "있습니다.",
        "없다.": "없습니다.",
        "않는다.": "않습니다.",
        "아니다.": "아닙니다.",
        "시킨다.": "시킵니다.",
        "받는다.": "받습니다.",
        "비판한다.": "비판합니다.",
        "마련이다.": "마련입니다.",
        "발생한다.": "발생합니다.",
        "필요하다.": "필요합니다.",
        "만든다.": "만듭니다.",
        "넘는다.": "넘습니다.",
        "모른다.": "모릅니다.",
        "가진다.": "가집니다.",
        "시작한다.": "시작합니다.",
        "증명한다.": "증명합니다."
    }

    for old, new in replacements.items():
        content = content.replace(" " + old, " " + new)
        content = content.replace(">" + old, ">" + new)
        content = content.replace("." + old, "." + new)

    # For endings right before a closing tag (e.g. </p>, </strong>)
    content = re.sub(r' 한다(</)', r' 합니다\1', content)
    content = re.sub(r' 된다(</)', r' 됩니다\1', content)
    content = re.sub(r' 이다(</)', r' 입니다\1', content)
    content = re.sub(r' 것이다(</)', r' 것입니다\1', content)
    content = re.sub(r' 있다(</)', r' 있습니다\1', content)
    content = re.sub(r' 없다(</)', r' 없습니다\1', content)
    content = re.sub(r' 아니다(</)', r' 아닙니다\1', content)
    content = re.sub(r' 않는다(</)', r' 않습니다\1', content)
    
    # Catch any remaining non-space ones
    content = re.sub(r'([가-힣])한다(</)', r'\1합니다\1', content)
    content = re.sub(r'([가-힣])된다(</)', r'\1됩니다\1', content)
    content = re.sub(r'([가-힣])이다(</)', r'\1입니다\1', content)
    content = re.sub(r'([가-힣])것이다(</)', r'\1것입니다\1', content)
    content = re.sub(r'([가-힣])있다(</)', r'\1있습니다\1', content)
    content = re.sub(r'([가-힣])없다(</)', r'\1없습니다\1', content)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Aggressive Tone Patch Applied.")
