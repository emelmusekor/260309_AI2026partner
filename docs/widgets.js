
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
            opt.setAttribute('role', 'button');
            opt.setAttribute('tabindex', '0');
            opt.setAttribute('aria-pressed', 'false');
            
            // Allow keyboard activation
            opt.addEventListener('keydown', (e) => {
                if(e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault();
                    opt.click();
                }
            });
            opt.addEventListener('click', () => {
                options.forEach(o => {
                    o.classList.remove('selected');
                    o.setAttribute('aria-pressed', 'false');
                });
                opt.classList.add('selected');
                opt.setAttribute('aria-pressed', 'true');
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
            d.setAttribute('tabindex', '0');
            d.setAttribute('aria-grabbed', 'false');
            d.addEventListener('dragstart', function() { 
                draggedItem = this; 
                this.setAttribute('aria-grabbed', 'true');
            });
            d.addEventListener('dragend', function() { 
                this.setAttribute('aria-grabbed', 'false');
            });
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
            const val = input.value.trim().replace(/\s+/g, '');
            const target = input.dataset.target.split(',');
            if(val === '') {
                feedback.className = 'feedback-msg error';
                feedback.innerHTML = '⚠️ 정답을 입력해주세요.';
                return;
            }
            if(target.some(t => val.includes(t.replace(/\s+/g, '')))) {
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
