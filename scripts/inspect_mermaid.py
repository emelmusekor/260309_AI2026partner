import glob
import re

files = glob.glob('d:/AIED2.0_docs/docs/chapter-*.html')

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()

    blocks = re.findall(r'<pre class="mermaid"[^>]*>(.*?)</pre>', html, re.DOTALL)
    for i, b in enumerate(blocks):
        print(f"--- {fpath} Block {i+1} ---")
        print(b.strip())
