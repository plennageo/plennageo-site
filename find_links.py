import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.finditer(r'<a[^>]+href=["\']#(.*?)["\'][^>]*>(.*?)</a>', text, re.DOTALL)
for match in matches:
    href = match.group(1)
    content = re.sub(r'<[^>]+>', '', match.group(2)).strip()
    print(f'#{href} -> {content}')
