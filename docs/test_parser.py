import re

text = """
graph TD
    A["과거: AI as a Tool"] -->|발전| B["현재: AI as an Assistant"]
    B -->|패러다임 전환| C["미래: AI as a Symbiotic Partner"]
    C --> D["인지적 역할 분담"]
    C --> E["메타 협력적 지식 창출"]
    C --> F["윤리적/비판적 견제"]
"""
edges = []
bracket_skip = r'(?:\["[^"]*"\]|\[[^\]]*\]|\([^)]*\)|\{[^}]*\})?'

for line in text.split('\n'):
    m1 = re.search(r'([A-Za-z0-9_]+)\s*' + bracket_skip + r'\s*-->\|([^|]+)\|\s*([A-Za-z0-9_]+)', line)
    m2 = re.search(r'([A-Za-z0-9_]+)\s*' + bracket_skip + r'\s*--\s*([^>\-\s][^-]*)\s*-->\s*([A-Za-z0-9_]+)', line)
    m4_all = re.findall(r'(?:\A|\s)([A-Za-z0-9_]+)\s*' + bracket_skip + r'\s*(-->|->|---|==>|<-->)\s*([A-Za-z0-9_]+)', line)
    print("Line:", repr(line))
    if m1: print("m1:", m1.groups())
    if m2: print("m2:", m2.groups())
    if m4_all: print("m4_all:", m4_all)
