import glob
import re
import json
import uuid

def patch_tone(content):
    replacements = {
        "합니다.": "한다.", "됩니다.": "된다.", "입니다.": "이다.", "것입니다.": "것이다.",
        "있습니다.": "있다.", "없습니다.": "없다.", "않습니다.": "않는다.", "아닙니다.": "아니다.",
        "시킵니다.": "시킨다.", "받습니다.": "받는다.", "비판합니다.": "비판한다.", "발생합니다.": "발생한다.",
        "필요합니다.": "필요하다.", "만듭니다.": "만든다.", "넘습니다.": "넘는다.", "모릅니다.": "모른다.",
        "가집니다.": "가진다.", "살펴보겠습니다.": "살펴보겠다.", "알아보겠습니다.": "알아보겠다.",
        "배워보겠습니다.": "배워보겠다.", "진행됩니다.": "진행된다.", "시작합니다.": "시작한다.",
        "증명합니다.": "증명한다.", "제공합니다.": "제공한다.", "할 수 있습니다.": "할 수 있다.",
        "보여줍니다.": "보여준다.", "나타납니다.": "나타난다.", "의미합니다.": "의미한다.",
        "말합니다.": "말한다.", "맞습니다.": "맞다.", "좋습니다.": "좋다.", "많습니다.": "많다.",
        "적습니다.": "적다.", "같습니다.": "같다.", "그렇습니다.": "그렇다.", "어떻습니다.": "어떻다.",
        "생깁니다.": "생긴다.", "어렵습니다.": "어렵다.", "쉽습니다.": "쉽다.", "옵니다.": "온다.",
        "갑니다.": "간다.", "봅니다.": "본다.", "마련입니다.": "마련이다.", "수행합니다.": "수행한다."
    }
    
    for old, new in replacements.items():
        content = content.replace(" " + old, " " + new)
        content = content.replace(">" + old, ">" + new)
        
        old_nd = old[:-1]; new_nd = new[:-1]
        content = content.replace(" " + old_nd + "</", " " + new_nd + "</")
        content = content.replace(">" + old_nd + "</", ">" + new_nd + "</")
        content = content.replace(" " + old + "</", " " + new + "</")
        content = content.replace(">" + old + "</", ">" + new + "</")

    roots = {
        "합니다": "한다", "됩니다": "된다", "입니다": "이다", "것입니다": "것이다",
        "있습니다": "있다", "없습니다": "없다", "않습니다": "않는다", "아닙니다": "아니다",
        "시킵니다": "시킨다", "받습니다": "받는다", "옵니다": "온다", "갑니다": "간다",
        "줍니다": "준다", "봅니다": "본다", "모릅니다": "모른다", "만듭니다": "만든다",
        "넘습니다": "넘는다", "가집니다": "가진다", "생깁니다": "생긴다", "필요합니다": "필요하다",
        "발생합니다": "발생한다", "수행합니다": "수행한다"
    }
    for old, new in roots.items():
        content = re.sub(r'([가-힣])' + old + r'(</|\. )', r'\1' + new + r'\2', content)
        content = re.sub(r'([가-힣])' + old + r'(?=\s|$)', r'\1' + new, content)
        
    return content

def parse_mermaid(text):
    nodes = {}
    edges = []
    
    node_pattern = re.compile(r'([A-Za-z0-9_]+)(?:\["([^"]+)"\]|\[([^\]]+)\]|\("([^"]+)"\)|\(([^)]+)\)|\{"([^"]+)"\}|\{([^}]+)\})')
    
    direction = 'UD'
    if 'flowchart LR' in text or 'graph LR' in text:
        direction = 'LR'
        
    for line in text.replace('&amp;', '&').split('\n'):
        line = line.strip()
        if not line: continue
        
        m_part = re.match(r'^participant\s+([A-Za-z0-9_]+)\s+as\s+(.+)', line)
        if m_part:
            nodes[m_part.group(1)] = m_part.group(2).strip()
            continue
            
        for m in node_pattern.finditer(line):
            nid = m.group(1)
            label = next((g for g in m.groups()[1:] if g is not None), nid)
            nodes[nid] = label.strip()
            
        # bracket skipping logic to correctly parse edges in the graph
        bracket_skip = r'(?:\["[^"]*"\]|\[[^\]]*\]|\([^)]*\)|\{[^}]*\})?'
        
        m3 = re.search(r'([A-Za-z0-9_]+)\s*(?:->>|-->>|->|-->)\s*([A-Za-z0-9_]+)\s*:\s*(.+)', line)
        m1 = re.search(r'([A-Za-z0-9_]+)\s*' + bracket_skip + r'\s*-->\|([^|]+)\|\s*([A-Za-z0-9_]+)', line)
        m2 = re.search(r'([A-Za-z0-9_]+)\s*' + bracket_skip + r'\s*--\s*([^>\-\s][^-]*)\s*-->\s*([A-Za-z0-9_]+)', line)
        
        if m3:
            u, v, l = m3.groups()
            edges.append({'from': u, 'to': v, 'label': l.strip(), 'arrows': 'to', 'font': {'size': 14, 'color': '#1d4ed8', 'background': '#eff6ff', 'strokeWidth': 0}})
            if u not in nodes: nodes[u] = u
            if v not in nodes: nodes[v] = v
        elif m1:
            u, l, v = m1.groups()
            edges.append({'from': u, 'to': v, 'label': l.strip(), 'arrows': 'to', 'font': {'align': 'middle', 'size': 14, 'color': '#1d4ed8', 'background': '#eff6ff', 'strokeWidth': 0}})
            if u not in nodes: nodes[u] = u
            if v not in nodes: nodes[v] = v
        elif m2:
            u, l, v = m2.groups()
            edges.append({'from': u, 'to': v, 'label': l.strip(), 'arrows': 'to', 'font': {'align': 'middle', 'size': 14, 'color': '#1d4ed8', 'background': '#eff6ff', 'strokeWidth': 0}})
            if u not in nodes: nodes[u] = u
            if v not in nodes: nodes[v] = v
        else:
            m4_all = re.findall(r'(?:\A|\s)([A-Za-z0-9_]+)\s*' + bracket_skip + r'\s*(-->|->|---|==>|<-->)\s*([A-Za-z0-9_]+)', line)
            for u, arr, v in m4_all:
                arrows = 'to' if '->' in arr or '=>' in arr else ''
                if '<-->' in arr: arrows = 'to, from'
                edges.append({'from': u, 'to': v, 'arrows': arrows})
                if u not in nodes: nodes[u] = u
                if v not in nodes: nodes[v] = v
                
    vis_nodes = [{"id": k, "label": v, "shape": "box", "font": {"size": 16, "face": "Pretendard, sans-serif", "color": "#1e293b"}, "color": {"background": "#fdf2e9", "border": "#e67e22"}} for k, v in nodes.items()]
    return vis_nodes, edges, direction

def replace_mermaid_with_vis(content):
    pattern = re.compile(r'<(div|pre) class="mermaid">(.*?)</\1>', re.DOTALL)
    
    script_injections = []
    
    def replacer(match):
        mermaid_code = match.group(2)
        net_id = "vis-net-" + str(uuid.uuid4())[:8]
        try:
            nodes, edges, direction = parse_mermaid(mermaid_code)
            
            nodes_json = json.dumps(nodes, ensure_ascii=False)
            edges_json = json.dumps(edges, ensure_ascii=False)
            
            js_code = f"""
            document.addEventListener("DOMContentLoaded", function() {{
                if(typeof vis === 'undefined') return;
                var container = document.getElementById('{net_id}');
                var data = {{
                    nodes: new vis.DataSet({nodes_json}),
                    edges: new vis.DataSet({edges_json})
                }};
                var options = {{
                    layout: {{
                        hierarchical: {{
                            enabled: true,
                            direction: '{direction}',
                            sortMethod: 'directed',
                            nodeSpacing: 250,
                            levelSeparation: 150
                        }}
                    }},
                    physics: {{
                        enabled: true,
                        hierarchicalRepulsion: {{ nodeDistance: 200, springLength: 100, damping: 0.09 }}
                    }},
                    edges: {{ smooth: {{ type: 'cubicBezier', forceDirection: '{'vertical' if direction=='UD' else 'horizontal'}' }}, color: '#94a3b8', width: 2 }},
                    interaction: {{ hover: true, dragNodes: true }}
                }};
                new vis.Network(container, data, options);
            }});
            """
            script_injections.append(js_code)
            
            return f'<div id="{net_id}" class="vis-network-container" style="width: 100%; height: 400px; border: 1px solid #e2e8f0; border-radius: 12px; background: #fafafa; margin: 2rem 0; cursor: grab; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);"></div>'
        except Exception as e:
            print("Failed to parse", e)
            return match.group(0)
            
    content = pattern.sub(replacer, content)
    
    if script_injections:
        all_scripts = "\n<script>\n" + "\n".join(script_injections) + "\n</script>\n"
        if "</body>" in content:
            content = content.replace("</body>", all_scripts + "</body>")
        else:
            content += all_scripts
            
    return content

files = glob.glob('d:/AIED2.0_docs/webbook/chapter-*.html')
for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()

    html = patch_tone(html)
    
    # Remove Mermaid CDN and initialization
    html = re.sub(r'<script src="https://(?:cdn\.jsdelivr\.net|unpkg\.com)[^"]*mermaid[^"]*"></script>\s*', '', html)
    html = re.sub(r'<script>mermaid\.initialize[^<]+</script>\s*', '', html)
    
    # Add Vis.js CDN
    if ('<div class="mermaid">' in html or '<pre class="mermaid">' in html) and 'vis-network.min.js' not in html:
        html = html.replace('</head>', '\n<script type="text/javascript" src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>\n</head>')
        
    html = replace_mermaid_with_vis(html)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(html)
        
print("Successfully applied tone patch and vis.js conversion.")
