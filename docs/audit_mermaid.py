"""
Since we cannot easily run node modules without installation, we will use Python's 
built-in 'tkinter' or a simple AST regex analyzer to find the precise Mermaid bugs 
that might be breaking rendering (e.g. unquoted spaces in Node declarations).
"""
import glob
import os
import re

def audit_mermaid_syntax():
    print("--- Auditing Mermaid JS Syntax ---")
    errors = []
    
    # Common mermaid errors:
    # 1. Spaces in Node IDs (e.g., A B[Text])
    # 2. Spaces in Node Labels without quotes if they contain certain special chars.
    # 3. Multiline syntax issues.
    
    for filepath in glob.glob("d:/AIED2.0_docs/docs/chapter-*.html"):
        filename = os.path.basename(filepath)
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
            
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')
        mermaids = soup.find_all(class_='mermaid')
        
        for idx, m in enumerate(mermaids):
            code = m.text
            lines = code.strip().split('\n')
            
            for line_no, line in enumerate(lines):
                original_line = line
                line = line.strip()
                if not line or line.startswith('%'): 
                    continue
                    
                # Check for Node declaration errors: NodeID[Label]
                # If Label has spaces or special characters, it is safer to be quoted.
                # E.g. A[인공지능 발전]  -> Safe usually in modern mermaid.
                # E.g. A["인공지능 발전, 그리고 인간"] -> Safe
                # E.g. A[인공지능 발전, 그리고 인간] -> Might break if commas are used depending on version.
                
                # Let's specifically look for broken quotes (e.g., Node["Test Text] missing closing quote)
                if '"' in line:
                    quote_count = line.count('"')
                    if quote_count % 2 != 0:
                        errors.append(f"{filename} (Diagram {idx+1}, Line {line_no+1}): Uneven quotes -> {original_line}")
                        
                # Check for Edge syntax errors
                if '-->' in line:
                    # Arrow with text but missing pipes: A --> text B (Error)
                    # Correct: A -->|text| B
                    parts = line.split('-->')
                    if len(parts) == 2:
                        right_side = parts[1].strip()
                        if right_side.startswith('|') and right_side.count('|') < 2:
                            # Starts with pipe but no closing pipe
                            errors.append(f"{filename} (Diagram {idx+1}, Line {line_no+1}): Missing closing pipe on edge -> {original_line}")

                # Check for subgraph syntax
                if line.startswith('subgraph '):
                    subgraph_title = line[9:].strip()
                    # if title has spaces it MUST be quoted, or it's just an ID
                    # Actually recently mermaid allows spaces but it's risky
                    pass
                    
    if errors:
        for e in set(errors):
            print("ERROR", e)
    else:
        print("OK: Mermaid Syntax Audit passed: No unbalanced quotes or missing edge pipes found.")

if __name__ == "__main__":
    audit_mermaid_syntax()
