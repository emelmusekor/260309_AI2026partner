import glob
import re
from bs4 import BeautifulSoup
import json

results = set()

for file_path in glob.glob("chapter-*.html"):
    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        
        # Search only inside article content
        article = soup.find(class_="article-content")
        if not article: continue
        
        # Regex to find (English words)
        for text_node in article.find_all(string=True):
            if text_node.parent.name in ['script', 'style', 'code']:
                continue
            
            matches = re.findall(r'\(([A-Za-z][A-Za-z\s\-]+)\)', text_node)
            for match in matches:
                results.add(match.strip())

# Save to a text file for review
with open("extracted_english.txt", "w", encoding="utf-8") as f:
    for word in sorted(list(results)):
        f.write(f"{word}\n")

print(f"Extracted {len(results)} unique English phrases.")
