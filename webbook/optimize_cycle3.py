import os
import glob
from bs4 import BeautifulSoup
import re

def optimize_accessibilityCSSJS():
    # 1. Update widgets.css for keyboard navigation focus
    css_path = "d:/AIED2.0_docs/webbook/widgets.css"
    if os.path.exists(css_path):
        with open(css_path, "r", encoding="utf-8") as f:
            css = f.read()
        
        if ":focus-visible" not in css:
            focus_css = """

/* --- Phase 5 Cycle 3 Accessibility (a11y) --- */
.mcq-option:focus-visible, .submit-btn:focus-visible, .short-answer-input:focus-visible, .draggable:focus-visible, .reflection-submit:focus-visible {
    outline: 3px solid #ef4444;
    outline-offset: 2px;
}
.mcq-option[role="button"]:focus {
    /* For standard focus fallbacks */
    border-color: #3b82f6;
    background: #f8fafc;
}
"""
            with open(css_path, "w", encoding="utf-8") as f:
                f.write(css + focus_css)

    # 2. Update widgets.js to dynamically inject ARIA properties and Keydown handlers
    js_path = "d:/AIED2.0_docs/webbook/widgets.js"
    if os.path.exists(js_path):
        with open(js_path, "r", encoding="utf-8") as f:
            js = f.read()
            
        if "role='button'" not in js and 'role="button"' not in js:
            js = js.replace("options.forEach(opt => {", """options.forEach(opt => {
            opt.setAttribute('role', 'button');
            opt.setAttribute('tabindex', '0');
            opt.setAttribute('aria-pressed', 'false');
            
            // Allow keyboard activation
            opt.addEventListener('keydown', (e) => {
                if(e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault();
                    opt.click();
                }
            });""")
            
            js = js.replace("opt.classList.add('selected');", """opt.classList.add('selected');
                opt.setAttribute('aria-pressed', 'true');""")
            
            js = js.replace("options.forEach(o => o.classList.remove('selected'));", """options.forEach(o => {
                    o.classList.remove('selected');
                    o.setAttribute('aria-pressed', 'false');
                });""")
            
            js = js.replace("draggables.forEach(d => {", """draggables.forEach(d => {
            d.setAttribute('tabindex', '0');
            d.setAttribute('aria-grabbed', 'false');""")
            
            js = js.replace("d.addEventListener('dragstart', function() { draggedItem = this; });", """d.addEventListener('dragstart', function() { 
                draggedItem = this; 
                this.setAttribute('aria-grabbed', 'true');
            });
            d.addEventListener('dragend', function() { 
                this.setAttribute('aria-grabbed', 'false');
            });""")
            
            
            with open(js_path, "w", encoding="utf-8") as f:
                f.write(js)
            print("Injected ARIA logic into widgets.js")

def optimize_html(filepath):
    filename = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    
    modified = False
    # 1. Header banner
    header = soup.find('header', class_='site-header')
    if header and not header.has_attr('role'):
        header['role'] = 'banner'
        modified = True
        
    # 2. Main
    main = soup.find('main')
    if main and not main.has_attr('role'):
        main['role'] = 'main'
        modified = True
        
    # 3. Footer
    footer = soup.find('footer', class_='site-footer')
    if footer and not footer.has_attr('role'):
        footer['role'] = 'contentinfo'
        modified = True
        
    # 4. Breadcrumb
    back_link = soup.find('a', class_='back-link')
    if back_link and back_link.parent.name != 'nav':
        nav = soup.new_tag('nav', attrs={'aria-label': 'Breadcrumb'})
        back_link.wrap(nav)
        modified = True

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"Applied semantic ARIA landmarks to {filename}")

if __name__ == "__main__":
    optimize_accessibilityCSSJS()
    for filepath in glob.glob("d:/AIED2.0_docs/webbook/*.html"):
        optimize_html(filepath)
