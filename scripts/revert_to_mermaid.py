import subprocess
import glob
import re

files = glob.glob('d:/AIED2.0_docs/docs/chapter-*.html')

for fpath in files:
    chap_num = re.search(r'chapter-(\d+)', fpath).group(1)
    
    try:
        old_html = subprocess.check_output(['git', 'show', f'9a39b10:webbook/chapter-{chap_num}.html'], encoding='utf-8')
    except Exception as e:
        print(f"Skipping chapter {chap_num}: {e}")
        continue
        
    old_mermaids = re.findall(r'<(div|pre)[^>]*class="mermaid"[^>]*>(.*?)</\1>', old_html, re.DOTALL)
    
    with open(fpath, 'r', encoding='utf-8') as f:
        curr_html = f.read()
        
    # Remove Vis.js 
    curr_html = re.sub(r'<script[^>]*vis-network[^>]*></script>', '', curr_html)
    curr_html = re.sub(r'<script>\s*document\.addEventListener\("DOMContentLoaded".*?</script>', '', curr_html, flags=re.DOTALL)
    
    # Replace Vis.js divs
    vis_div_pattern = re.compile(r'<div id="vis-net-[^"]+" class="vis-network-container"[^>]*></div>')
    
    def replacer(match, idx=[0]):
        if idx[0] < len(old_mermaids):
            m_code = old_mermaids[idx[0]][1].strip()
            # Quote unquoted nodes to fix syntax errors
            m_code = re.sub(r'([A-Za-z0-9_]+)\[([^"\]]+)\]', r'\1["\2"]', m_code)
            
            replacement = f'''<div class="mermaid-wrapper" style="width: 100%; overflow-x: auto; background: #fdf8f5; padding: 2rem; border-radius: 12px; margin: 2rem 0; border: 1px solid #e2e8f0; text-align: center;">
<pre class="mermaid" style="font-size: 1.25rem; font-family: Pretendard, sans-serif;">
{m_code}
</pre>
</div>'''
            idx[0] += 1
            return replacement
        return match.group(0)
        
    curr_html = vis_div_pattern.sub(replacer, curr_html)
    
    mermaid_loader = '''
<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
  mermaid.initialize({ 
    startOnLoad: true, 
    theme: 'default',
    securityLevel: 'loose',
    flowchart: { htmlLabels: true, curve: 'basis' }
  });
</script>
</body>'''
    
    if "mermaid@10" not in curr_html:
        curr_html = curr_html.replace('</body>', mermaid_loader)
        
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(curr_html)
        
print("Reverted to scalable Mermaid SVG graphics with responsive wrappers.")
