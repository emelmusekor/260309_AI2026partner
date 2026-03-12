import glob

for f in glob.glob('chapter-*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        t = file.read()
    
    t = t.replace('theme: default', "theme: 'default'")
    t = t.replace('msg.style.display = block;', "msg.style.display = 'block';")
    t = t.replace('msg.style.display = none;', "msg.style.display = 'none';")
    t = t.replace('document.getElementById(`reflection-answer-${chap_num}`).value', 'document.getElementById(`reflection-answer-${chapterNum}`).value')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(t)
print('Fixed JS bugs in all chapters!')
