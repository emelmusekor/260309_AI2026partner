import glob
import re

files = glob.glob('d:/AIED2.0_docs/docs/chapter-*.html')

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()

    def fix_mermaid(match):
        mermaid_code = match.group(1)
        lines = mermaid_code.split('\n')
        fixed_lines = []
        for line in lines:
            if not line.strip():
                fixed_lines.append(line)
                continue
            
            # Replace double double-quotes which are usually mistakes from my previous regexes
            line = line.replace('""', '"')
            
            # Fix broken ["Text] -> ["Text"]
            line = re.sub(r'\["([^"]*?)\]', r'["\1"]', line)
            # Fix broken [Text"] -> ["Text"]
            line = re.sub(r'\[([^"\]]*?)"\]', r'["\1"]', line)
            
            # Fix broken |"Text| -> |"Text"|
            line = re.sub(r'\|"([^"|]*?)\|', r'|"\1"|', line)
            # Fix broken |Text"| -> |"Text"|
            line = re.sub(r'\|([^"|]*?)"\|', r'|"\1"|', line)
            
            # Clean up stray single quotes in ()
            # Find everything inside ( ), if it has exactly ONE quote, remove it.
            def fix_parens(m):
                inner = m.group(1)
                if inner.count('"') == 1:
                    inner = inner.replace('"', '')
                return f'({inner})'
            line = re.sub(r'\(([^)]+)\)', fix_parens, line)
            
            fixed_lines.append(line)
        
        return '<pre class="mermaid" style="font-size: 1.25rem; font-family: Pretendard, sans-serif;">\n' + '\n'.join(fixed_lines) + '\n</pre>'

    curr_html = re.sub(r'<pre class="mermaid"[^>]*>(.*?)</pre>', fix_mermaid, html, flags=re.DOTALL)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(curr_html)

print("Mermaid syntax errors fixed intelligently across all files.")
