import os
import glob
from bs4 import BeautifulSoup
import re

def audit_html_files():
    print("--- Starting Deep Error Audit ---")
    errors_found = []
    
    for filepath in glob.glob("d:/AIED2.0_docs/docs/*.html"):
        filename = os.path.basename(filepath)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 1. Unclosed tags or malformed HTML check using a simple regex heuristic 
        # (BeautifulSoup auto-fixes, so we test raw string for common mistakes)
        if "<<" in content or ">>" in content:
            errors_found.append(f"{filename}: Found malformed brackets '<<' or '>>'")
            
        if "단답형" in content and "sa-widget" not in content:
            errors_found.append(f"{filename}: Missing Short Answer widget structure but text present.")
            
        # 2. Check for missing quotes in attributes
        attrs_no_quotes = re.compile(r'=\s*([^"\'>\s]+)[>\s]')
        # This is very noisy for valid HTML5 (like width=100) but good for catching malformed injected data.
        
        # 3. BeautifulSoup structural checks
        soup = BeautifulSoup(content, 'html.parser')
        
        # Check for empty links
        for a in soup.find_all('a'):
            href = a.get('href', '')
            if not href or href == '#':
                errors_found.append(f"{filename}: Empty or placeholder link found '{a.text}'")
                
        # Check for missing alt tags on images
        for img in soup.find_all('img'):
            if not img.has_attr('alt') or img['alt'].strip() == "":
                errors_found.append(f"{filename}: Image missing alt tag.")
                
        # Check for broken Mermaid syntax blocks (e.g., hanging arrows)
        for mermaid in soup.find_all('div', class_='mermaid'):
            text = mermaid.get_text()
            if "-->|" in text and "| " not in text.replace("-->|", ""): # rudimentary check
                pass
                
        # Check for duplicate IDs
        ids = [tag.get('id') for tag in soup.find_all(id=True)]
        if len(ids) != len(set(ids)):
            import collections
            duplicates = [item for item, count in collections.Counter(ids).items() if count > 1]
            errors_found.append(f"{filename}: Duplicate IDs found: {duplicates}")

    # 4. Check JS syntax errors or console warnings manually
    js_path = "d:/AIED2.0_docs/docs/widgets.js"
    if os.path.exists(js_path):
        with open(js_path, 'r', encoding='utf-8') as f:
            js = f.read()
            if "console.log" in js:
                errors_found.append("widgets.js: Contains console.log statements that should be removed.")
            if "let " in js and "var " in js:
                pass # just looking for bad practices
            if "replace(/\\\\s+/g, '')" in js:
                pass # Check regex escaping

    CSS_path = "d:/AIED2.0_docs/docs/widgets.css"
    if os.path.exists(CSS_path):
        with open(CSS_path, 'r', encoding='utf-8') as f:
            css = f.read()
            if "px" in css and "pt" in css:
                pass 

    if errors_found:
        print("Errors Detected:")
        for e in errors_found:
            print(" -", e)
    else:
        print("No obvious structural errors found by the basic auditor.")

if __name__ == "__main__":
    audit_html_files()
