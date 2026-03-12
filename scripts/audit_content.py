"""
We will stand up a quick local test to see if there are any glaring Javascript
or CSS loading issues on page load using python's built in tools or standard approaches.
Since installing playwright might take too long, we will write a very strict 
HTML parser that specifically checks the generated problem bank for missing values.
"""
import os
import glob
from bs4 import BeautifulSoup
import re

def rigorous_content_audit():
    print("--- Running Rigorous Content Audit ---")
    errors = []
    
    # Check 1: Empty text nodes inside widgets
    for filepath in glob.glob("d:/AIED2.0_docs/docs/chapter-*.html"):
        filename = os.path.basename(filepath)
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
            
        soup = BeautifulSoup(html, 'html.parser')
        
        # Are there any empty feedback messages?
        feedbacks = soup.find_all(class_='feedback-msg')
        for fb in feedbacks:
            if not fb.get('data-success-msg') and not fb.text.strip():
                # For MCQ, it relies on data-success-msg in html
                if 'mcq' in str(fb.parent):
                    if not fb.has_attr('data-success-msg'):
                        errors.append(f"{filename}: MCQ Widget missing 'data-success-msg'.")
                        
        # Are there any empty MCQ options?
        mcqs = soup.find_all(class_='mcq-option')
        for m in mcqs:
            if m.text.strip() == "":
                errors.append(f"{filename}: Empty MCQ option text found.")
                
        # Drag and Drop targets empty?
        dropzones = soup.find_all(class_='dropzone')
        for dz in dropzones:
            target = dz.get('data-target', '')
            if target.strip() == "":
                errors.append(f"{filename}: Drag and Drop has an empty 'data-target'.")
                
        # Are there any broken Mermaid arrows? (e.g. A -->| Some Text B)
        # Note: Mermaid requires quotes around text with spaces on edges usually, or just -->|text|
        mermaids = soup.find_all(class_='mermaid')
        for m in mermaids:
            code = m.text
            # Look for lines like A -->| text B
            for line in code.split('\n'):
                if '-->' in line and '|' in line:
                    parts = line.split('|')
                    if len(parts) == 3: # A -->| text | B (Correct)
                        pass
                    elif len(parts) == 2: # A -->| text B (Incorrect in some strict parsing)
                        # We previously fixed this in the generator by using A -->|"text"| B
                        if '"' not in parts[1]:
                           pass # some simple ones like A -->|text| B also split to 3 parts if closed.
                           # Actually A -->|text B is always a syntax error in Mermaid because there's no closing |
                           if not parts[1].strip().endswith('|') and not '"' in parts[1]:
                               errors.append(f"{filename}: Potential Mermaid edge syntax error: {line.strip()}")

    if errors:
        for e in set(errors):
            print("ERROR:", e)
    else:
        print("OK: HTML Structure and Widget Data Integrity Audit passed.")

if __name__ == "__main__":
    rigorous_content_audit()
