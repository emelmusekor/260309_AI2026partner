import os
import glob
from bs4 import BeautifulSoup
import re

# We will extract the global CSS and JS from a sample file (e.g., chapter-1.html)
# and write them to external files, then remove them from all files.

def create_global_assets():
    sample_file = "d:/AIED2.0_docs/docs/chapter-1.html"
    with open(sample_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    style_tags = soup.find_all('style')
    script_tags = soup.find_all('script')

    css_content = ""
    for st in style_tags:
        # Avoid extracting generic mathjax styles if any, target widgets
        if "interactive-widget" in st.text or "mcq-option" in st.text:
            css_content += st.text + "\n"

    js_content = ""
    for sc in script_tags:
        # Ensure we only pick the interactive logic, not external cdn loaded scripts
        if not sc.has_attr('src'):
            if "saveReflection" in sc.text or "fireConfetti" in sc.text:
                js_content += sc.text + "\n"

    # Refactor the saveReflection inline logic to a class-based delegator in js_content
    # The original saveReflection requires `chapterNum` argument. We'll change the HTML
    # `<button onclick="saveReflection(1)">` -> `<button class="reflection-submit" data-chapter="1">`
    # and handle it in the JS gracefully.
    
    # We will build a unified, clean widgets.js:
    refined_js = """
// -------------------------------------------------------------
// Interactive Widget and Reflection Logic
// Extracted & Refactored during Phase 5 Frontend Optimization Loop
// -------------------------------------------------------------

// Confetti Effect
function fireConfetti(container) {
    for(let i = 0; i < 30; i++) {
        const confetti = document.createElement('div');
        confetti.className = 'confetti';
        confetti.style.left = Math.random() * 100 + '%';
        confetti.style.animationDelay = Math.random() * 0.2 + 's';
        confetti.style.backgroundColor = ['#ef4444', '#3b82f6', '#10b981', '#f59e0b', '#8b5cf6'][Math.floor(Math.random() * 5)];
        container.appendChild(confetti);
        setTimeout(() => confetti.remove(), 1000);
    }
}

document.addEventListener("DOMContentLoaded", () => {
    // MCQ Check
    document.querySelectorAll('.mcq-widget').forEach(widget => {
        const options = widget.querySelectorAll('.mcq-option');
        options.forEach(opt => {
            opt.addEventListener('click', () => {
                options.forEach(o => o.classList.remove('selected'));
                opt.classList.add('selected');
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
                feedback.innerHTML = feedback.dataset.successMsg || '🎯 <strong>정답입니다!</strong>';
                fireConfetti(widget);
            } else {
                feedback.className = 'feedback-msg error';
                feedback.innerHTML = feedback.dataset.errorMsg || '❌ <strong>아쉽습니다. 다시 시도해 보세요.</strong>';
            }
        });
    });

    // Drag & Drop Wait Check
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

    // Short Answer Check
    document.querySelectorAll('.sa-widget').forEach(widget => {
        const btn = widget.querySelector('.submit-btn');
        const input = widget.querySelector('input');
        const feedback = widget.querySelector('.feedback-msg');
        
        input.addEventListener('keypress', function (e) {
            if (e.key === 'Enter') btn.click();
        });

        btn.addEventListener('click', () => {
            const val = input.value.trim().replace(/\\s+/g, '');
            const target = input.dataset.target.split(',');
            if(val === '') {
                feedback.className = 'feedback-msg error';
                feedback.innerHTML = '⚠️ 정답을 입력해주세요.';
                return;
            }
            if(target.some(t => val.includes(t.replace(/\\s+/g, '')))) {
                feedback.className = 'feedback-msg success';
                feedback.innerHTML = '🎯 <strong>정확합니다!</strong> 핵심 개념을 훌륭하게 인지하셨습니다.';
                fireConfetti(widget);
            } else {
                feedback.className = 'feedback-msg error';
                feedback.innerHTML = '❌ 예상되는 핵심 개념어가 아닙니다. 본문의 흐름을 다시 학인해주세요.';
            }
        });
    });

    // Refactored Reflection Save Logic via Delegation
    document.querySelectorAll('.reflection-submit').forEach(btn => {
        const chapterNum = btn.dataset.chapter;
        const textarea = document.getElementById(`reflection-answer-${chapterNum}`);
        
        // Auto-load cookie if exists
        const match = document.cookie.match(new RegExp('(^| )reflection_' + chapterNum + '=([^;]+)'));
        if (match && textarea) {
            textarea.value = decodeURIComponent(match[2]);
        }

        btn.addEventListener('click', () => {
            if(!textarea) return;
            const answer = textarea.value;
            document.cookie = `reflection_${chapterNum}=${encodeURIComponent(answer)}; max-age=31536000; path=/`;
            const msg = document.getElementById(`save-msg-${chapterNum}`);
            if(msg) {
                msg.style.display = 'block';
                setTimeout(() => { msg.style.display = 'none'; }, 3000);
            }
        });
    });
});
"""

    refined_css = """
/* ------------------------------------------------------------- */
/* Interactive Widget & Reflection CSS                           */
/* Extracted & Refactored during Phase 5 Frontend Optimization   */
/* ------------------------------------------------------------- */

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
    padding: 1rem 1.5rem;
    margin-bottom: 0.8rem;
    border: 2px solid #e2e8f0;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.2s;
    font-size: 1.05rem;
    color: #334155;
}
.mcq-option:hover {
    border-color: #cbd5e1;
    background: #f8fafc;
}
.mcq-option.selected {
    border-color: #3b82f6;
    background: #eff6ff;
    font-weight: 500;
    color: #1e40af;
}
.submit-btn {
    display: inline-block;
    background: #0f172a;
    color: #fff;
    border: none;
    padding: 0.8rem 1.8rem;
    border-radius: 6px;
    font-size: 1.05rem;
    font-weight: 600;
    cursor: pointer;
    margin-top: 1rem;
    transition: background 0.2s;
}
.submit-btn:hover { background: #334155; }
.feedback-msg {
    margin-top: 1.2rem;
    padding: 1rem;
    border-radius: 6px;
    display: none;
    font-size: 1.05rem;
}
.feedback-msg.success {
    display: block;
    background: #ecfdf5;
    border: 1px solid #a7f3d0;
    color: #065f46;
}
.feedback-msg.error {
    display: block;
    background: #fef2f2;
    border: 1px solid #fecaca;
    color: #991b1b;
}

/* Base Confetti Logic */
.confetti {
    position: absolute;
    width: 10px;
    height: 10px;
    opacity: 0;
    pointer-events: none;
    animation: fall 1s ease-in forwards;
}
@keyframes fall {
    0% { transform: translateY(0) rotate(0deg); opacity: 1; }
    100% { transform: translateY(100px) rotate(360deg); opacity: 0; }
}
.interactive-widget { position: relative; overflow: hidden; }

/* Drag & Drop */
.dnd-container {
    display: flex; gap: 1rem; flex-wrap: wrap; margin-bottom: 1.5rem;
}
.draggable {
    padding: 0.6rem 1.2rem;
    background: #fff; border: 2px dashed #94a3b8; border-radius: 8px;
    cursor: grab; font-weight: 600; color: #334155;
}
.draggable:active { cursor: grabbing; }
.dropzone {
    display: inline-block;
    min-width: 80px; height: 32px;
    background: #f1f5f9; border: 2px dashed #cbd5e1; border-radius: 4px;
    vertical-align: bottom; margin: 0 0.4rem; padding: 0 0.8rem;
    line-height:30px; text-align: center; color: transparent;
    transition: all 0.2s;
}
.dropzone.dragover { background: #e2e8f0; border-color: #94a3b8; }
.dropzone.filled {
    background: #eff6ff; border: 2px solid #3b82f6; border-style: solid;
    color: #1e40af; font-weight: 600;
}

/* Short Answer */
.short-answer-input {
    width: 100%; padding: 1rem 1.2rem;
    font-size: 1.05rem; border: 2px solid #e2e8f0; border-radius: 8px;
    outline: none; transition: border-color 0.2s;
    font-family: inherit; margin-bottom: 0.5rem;
}
.short-answer-input:focus { border-color: #3b82f6; }
"""
    
    with open("d:/AIED2.0_docs/docs/widgets.css", "w", encoding="utf-8") as f:
        f.write(refined_css)
        
    with open("d:/AIED2.0_docs/docs/widgets.js", "w", encoding="utf-8") as f:
        f.write(refined_js)
    
    print("Exported global widgets.css and widgets.js")

def process_file(filepath):
    filename = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Purge inline <style> and <script> tags that relate to our exported logic
    soup = BeautifulSoup(html, 'html.parser')
    
    # Process html lang
    html_tag = soup.find('html')
    if html_tag and not html_tag.has_attr('lang'):
        html_tag['lang'] = 'ko'

    head = soup.find('head')
    if head:
        import_css = bool(head.find(lambda t: t.name == 'link' and getattr(t, 'href', '') == 'widgets.css'))
        import_js = bool(head.find(lambda t: t.name == 'script' and getattr(t, 'src', '') == 'widgets.js'))
        import_meta = bool(head.find(lambda t: t.name == 'meta' and t.get('name') == 'description'))
        
        if not import_css:
            new_css = soup.new_tag('link', rel='stylesheet', href='widgets.css')
            head.append(new_css)
        if not import_js:
            new_js = soup.new_tag('script', src='widgets.js', defer=True)
            head.append(new_js)
        if not import_meta:
            new_meta = soup.new_tag('meta', attrs={"name": "description", "content": "AI Education 2026 - 인공지능 시대의 시스템 재설계서"})
            head.insert(0, new_meta)

    for st in soup.find_all('style'):
        if "interactive-widget" in st.text or "mcq-option" in st.text or "Drag & Drop" in st.text:
            st.decompose()

    for sc in soup.find_all('script'):
        if not sc.has_attr('src'):
            if "saveReflection" in sc.text or "fireConfetti" in sc.text or "mcq-widget" in sc.text:
                sc.decompose()

    # Refactor inline onclick
    for btn in soup.find_all('button', onclick=re.compile(r'saveReflection\((\d+)\)')):
        match = re.search(r'saveReflection\((\d+)\)', btn['onclick'])
        if match:
            btn['class'] = btn.get('class', []) + ['reflection-submit']
            btn['data-chapter'] = match.group(1)
            del btn['onclick']

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    
    print(f"Purged inline assets, appended lang/meta, and refactored HTML events in {filename}")

if __name__ == "__main__":
    create_global_assets()
    for filepath in glob.glob("d:/AIED2.0_docs/docs/*.html"):
        process_file(filepath)
