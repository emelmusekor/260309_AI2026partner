import glob
import re

files = glob.glob('d:/AIED2.0_docs/docs/chapter-*.html')

# We need to target the entire options block and the nodes font settings inside the DataSet arrays
for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Magnify all nodes' font sizes from size: 16 to size: 28, bold
    # The existing json has things like "font": {"size": 16, "face": "Pretendard, sans-serif", "color": "#1e293b"}
    # We will expand it using regex replace on the JSON string representation
    html = re.sub(
        r'"font":\s*\{"size":\s*\d+,\s*"face":\s*"Pretendard,\s*sans-serif",\s*"color":\s*"#1e293b"(\,\s*"bold":\s*(true|True|false|False))?\}',
        r'"font": {"size": 32, "face": "Pretendard, sans-serif", "color": "#1e293b", "bold": true}, "margin": 16',
        html
    )

    # 2. Overwrite the `var options = { ... };` block with our maximized static legibility settings
    # We find everything between `var options = {` and `new vis.Network(container, data, options);`
    
    new_options = """var options = {
                    layout: {
                        hierarchical: {
                            enabled: true,
                            direction: 'UD', // fallback, will fix below to maintain LR if it was LR
                            sortMethod: 'directed',
                            nodeSpacing: 400,
                            levelSeparation: 300
                        }
                    },
                    physics: {
                        enabled: false // STRICTLY STATIC
                    },
                    edges: { 
                        smooth: { type: 'cubicBezier' }, 
                        color: { color: '#0f172a', highlight: '#000000' }, 
                        width: 6,
                        font: { size: 22, color: '#0f172a', strokeWidth: 4, strokeColor: '#ffffff', bold: true },
                        arrows: { to: { scaleFactor: 2.5 } }
                    },
                    interaction: { 
                        dragNodes: false,
                        dragView: false,
                        zoomView: false,
                        hover: false
                    }
                };
                var network = new vis.Network(container, data, options);
                
                // Force maximum visibility fit
                network.once("beforeDrawing", function() {
                    network.fit({
                        animation: false
                    });
                });"""

    # We need to preserve the `direction` (LR vs UD)
    def options_replacer(match):
        original_block = match.group(0)
        direction = 'LR' if "'LR'" in original_block else 'UD'
        customized_options = new_options.replace("direction: 'UD'", f"direction: '{direction}'")
        customized_options = customized_options.replace("type: 'cubicBezier' }", f"type: 'cubicBezier', forceDirection: '{'horizontal' if direction == 'LR' else 'vertical'}' }}")
        return customized_options

    html = re.sub(r'var options = \{.*?new vis\.Network\(container, data, options\);', options_replacer, html, flags=re.DOTALL)
    
    # 3. Increase container height significantly so that large graphs don't feel squished vertically
    html = re.sub(r'height:\s*\d+px;', 'height: 700px;', html)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(html)
        
print("Successfully magnified Vis.js graph legibility metrics (fonts, edges, spacing, static pinning).")
