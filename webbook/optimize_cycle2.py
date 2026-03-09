import os
import glob
from bs4 import BeautifulSoup
import re

def optimize_css():
    css_path = "d:/AIED2.0_docs/webbook/styles.css"
    if not os.path.exists(css_path):
        return
        
    with open(css_path, "r", encoding="utf-8") as f:
        css = f.read()
        
    # Append mobile breakpoints if they aren't there
    if "@media (max-width: 768px)" not in css:
        mobile_css = """

/* --- Phase 5 Cycle 2 Mobile Optimization --- */
@media (max-width: 768px) {
    .container {
        width: 100%;
        padding: 0 1rem;
        max-width: 100%;
    }
    .article-content {
        padding: 1.5rem 1rem;
    }
    .interactive-widget {
        padding: 1.5rem;
    }
    h1.article-title {
        font-size: 1.5rem;
    }
    h2 {
        font-size: 1.3rem;
    }
    .glossary-section, .reflection-section {
        padding: 1.5rem !important;
    }
    .site-title {
        font-size: 1.2rem;
    }
    .header-description {
        display: none; /* Hide subtitle on tiny screens to save space */
    }
}
"""
        css += mobile_css
        with open(css_path, "w", encoding="utf-8") as f:
            f.write(css)
        print("Updated styles.css with mobile @media queries.")

def optimize_html(filepath):
    filename = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    
    # 1. Preconnect for fast Font loading
    head = soup.find('head')
    if head:
        import_preconnect = bool(head.find(lambda t: t.name == 'link' and t.get('rel') and 'preconnect' in t.get('rel')))
        if not import_preconnect:
            pre1 = soup.new_tag('link', rel='preconnect', href='https://cdn.jsdelivr.net')
            pre2 = soup.new_tag('link', rel='preconnect', href='https://cdn.jsdelivr.net', crossorigin="")
            # insert before the actual stylesheet
            first_css = head.find('link', rel='stylesheet')
            if first_css:
                first_css.insert_before(pre1)
                first_css.insert_before(pre2)
            else:
                head.append(pre1)
                head.append(pre2)

    # 2. Lazy loading for images and iframes
    for tag in soup.find_all(['img', 'iframe']):
        if not tag.has_attr('loading'):
            tag['loading'] = 'lazy'

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    
    print(f"Injected Preconnect and Lazy Loading in {filename}")

if __name__ == "__main__":
    optimize_css()
    for filepath in glob.glob("d:/AIED2.0_docs/webbook/*.html"):
        optimize_html(filepath)
