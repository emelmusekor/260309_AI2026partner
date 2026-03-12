import glob
import re

for f in glob.glob('chapter-*.html'):
    m = re.search(r'chapter-(\d+)\.html', f)
    if not m: continue
    cnum = m.group(1)
    
    with open(f, 'r', encoding='utf-8') as file:
        t = file.read()
    
    t = t.replace('document.getElementById(`reflection-answer-${chapterNum}`).value', f'document.getElementById("reflection-answer-{cnum}").value')
    t = t.replace('document.getElementById(`reflection-answer-${chap_num}`).value', f'document.getElementById("reflection-answer-{cnum}").value')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(t)
print('Fixed scope bug in JS in all chapters!')
