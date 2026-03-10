import os
import glob
from bs4 import BeautifulSoup
import re

def fix_mermaid_in_file(filepath):
    filename = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    mermaids = soup.find_all(class_='mermaid')
    modified = False

    for m in mermaids:
        code = m.text
        lines = code.split('\n')
        new_lines = []
        
        for line in lines:
            original_line = line
            
            # 1. Fix uneven quotes in Node definitions like: A["Some Text] or B[Text"]
            if '"' in line:
                quote_count = line.count('"')
                if quote_count % 2 != 0: # Uneven quotes detected
                    # Let's extract everything inside the brackets [ ... ]
                    # e.g., A["Some text] --> we need to ensure the text inside brackets is properly quoted
                    # match A[something] or A["something"]
                    match = re.search(r'\[(.*?)\]', line)
                    if match:
                        inner_text = match.group(1).replace('"', '') # strip existing broken quotes
                        # rebuild with proper quotes
                        new_line = line[:match.start()] + f'["{inner_text}"]' + line[match.end():]
                        line = new_line
                        modified = True
                        print(f"Fixed Node in {filename}: {original_line} -> {line}")
                        
            # 2. Fix edges without closing | like -->|Some Text
            # We want -->|"Some Text"|
            if '-->' in line and '|' in line:
                parts = line.split('-->')
                if len(parts) == 2:
                    right_side = parts[1]
                    if right_side.strip().startswith('|'):
                        # Check if it has a closing pipe
                        if right_side.count('|') < 2:
                            # e.g., |Some Text NodeB
                            # find the text after pipe up to the space before NodeB
                            # A -->| text B -> we need A -->|"text"| B
                            match = re.match(r'\s*\|([^|]+)\s+(\w+.*)', right_side)
                            if match:
                                text_inside = match.group(1).strip().replace('"', '')
                                node_target = match.group(2)
                                line = f"{parts[0]}-->|\"{text_inside}\"| {node_target}"
                                modified = True
                                print(f"Fixed Edge in {filename}: {original_line} -> {line}")

            new_lines.append(line)
            
        if modified:
            m.string = '\n'.join(new_lines)
            
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
            
if __name__ == "__main__":
    for filepath in glob.glob("d:/AIED2.0_docs/webbook/*.html"):
        fix_mermaid_in_file(filepath)
