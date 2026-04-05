import os
import re
from PIL import Image

image_dir = "assets/images"
html_file = "index.html"
css_file = "assets/css/style.css"

with open(html_file, 'r', encoding='utf-8') as f:
    html_content = f.read()
with open(css_file, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Find all image paths in HTML
img_tags = re.findall(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>', html_content)
css_imgs = re.findall(r'url\([\'"]?(assets/images/[^\'")]+)[\'"]?\)', css_content)

all_referenced_images = set(img_tags + css_imgs)

# Gather file info
print("=== IMAGE AUDIT ===")
total_size = 0
for file in os.listdir(image_dir):
    path = os.path.join(image_dir, file)
    if os.path.isfile(path):
        size_kb = os.path.getsize(path) / 1024
        total_size += size_kb
        ref = path.replace("\\", "/")
        is_ref = "YES" if ref in all_referenced_images else "NO"
        try:
            with Image.open(path) as img:
                w, h = img.size
                fmt = img.format
                print(f"{file:<30} | {fmt:<4} | {w}x{h:<4} | {size_kb:.1f} KB | Ref: {is_ref}")
        except Exception as e:
            print(f"{file:<30} | ??? | ?x? | {size_kb:.1f} KB | Ref: {is_ref}")

print(f"\nTotal size: {total_size/1024:.1f} MB")
