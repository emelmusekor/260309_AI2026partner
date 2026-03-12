import glob
import re
import json

files = sorted(glob.glob('d:/AIED2.0_docs/docs/chapter-*.html'), key=lambda x: int(re.search(r'chapter-(\d+)', x).group(1)))

summary = "# 📚 챕터별 도표 변환 요약 (Vis.js)\n\n"

for fpath in files:
    chapter_num = re.search(r'chapter-(\d+)', fpath).group(1)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find vis.DataSet({nodes_json})
    # We can extract the nodes_json array strings.
    datasets = re.findall(r'nodes:\s*new\s*vis\.DataSet\((\[.*?\])\),', content, re.DOTALL)
    
    if datasets:
        summary += f"## 📖 챕터 {chapter_num}\n"
        for i, ds_str in enumerate(datasets):
            try:
                nodes = json.loads(ds_str)
                labels = [n.get('label', '').replace('\n', ' ') for n in nodes]
                if labels:
                    summary += f"- **도표 {i+1} 핵심 키워드**: {', '.join(labels[:5])}"
                    if len(labels) > 5:
                        summary += f" 등 (총 {len(labels)}개 노드)\n"
                    else:
                        summary += "\n"
            except Exception as e:
                summary += f"- 도표 {i+1}: 내부 파싱 오류\n"
        summary += "\n"

with open('d:/AIED2.0_docs/diagram_summary.md', 'w', encoding='utf-8') as f:
    f.write(summary)

print("Summary generated at d:/AIED2.0_docs/diagram_summary.md")
