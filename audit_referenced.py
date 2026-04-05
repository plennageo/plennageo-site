import os
import re
from PIL import Image

image_dir = "assets/images"
html_file = "index.html"
css_file = "assets/css/style.css"

with open(html_file, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Try to capture both 'assets/images/X.ext' and "assets/images/X.ext"
# Using a simpler regex
img_tags = re.findall(r'assets/images/[a-zA-Z0-9_.-]+', html_content)

with open(css_file, 'r', encoding='utf-8') as f:
    css_content = f.read()
css_imgs = re.findall(r'assets/images/[a-zA-Z0-9_.-]+', css_content)

all_referenced_images = set(img_tags + css_imgs)

print("=== REFERENCED IMAGES ===")
total_size = 0
for ref in sorted(list(all_referenced_images)):
    path = ref
    if os.path.isfile(path):
        size_kb = os.path.getsize(path) / 1024
        total_size += size_kb
        try:
            with Image.open(path) as img:
                print(f"{os.path.basename(path):<25} | {img.size} | {size_kb:.1f} KB")
        except Exception:
            print(f"{os.path.basename(path):<25} | ?x? | {size_kb:.1f} KB")

print(f"Total size of referenced images: {total_size/1024:.1f} MB")
