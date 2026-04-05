import os
import re
from PIL import Image

image_dir = "assets/images"

# 1. Optimize specific heavy images
heavy_files = [
    ("allen-campo-freepik.png", "allen-campo-freepik.webp", 960),
    ("service-area-01.webp", "service-area-01.webp", 960),
    ("service-area-02.webp", "service-area-02.webp", 960),
    ("service-area-03.webp", "service-area-03.webp", 960),
    ("mapeamento-freepik.webp", "mapeamento-freepik.webp", 960),
    ("juridico-freepik.webp", "juridico-freepik.webp", 960)
]

print("Optimizing images...")
for in_name, out_name, target_h in heavy_files:
    in_path = os.path.join(image_dir, in_name)
    out_path = os.path.join(image_dir, out_name)
    if os.path.exists(in_path):
        with Image.open(in_path) as img:
            if img.mode not in ("RGB", "RGBA"):
                img = img.convert("RGBA")
            w, h = img.size
            if h > target_h:
                new_w = int(w * (target_h / h))
                img = img.resize((new_w, target_h), Image.Resampling.LANCZOS)
            img.save(out_path, "WEBP", quality=80, method=6)
        # If we converted PNG to WEBP, we can optionally delete the original PNG
        if in_path != out_path:
            os.remove(in_path)

# 2. Rewrite HTML
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace png with webp
html = html.replace('allen-campo-freepik.png', 'allen-campo-freepik.webp')

# Validate loading="lazy" for all images except the first few in hero
# Actually, the user already has them mostly correct, EXCEPT maybe line 553 which might be missing it due to multiline split?
# Let's cleanly inject loading="lazy" decoding="async" into any <img> that doesn't have loading= OR fetchpriority=
def add_lazy(match):
    tag = match.group(0)
    if 'loading=' not in tag and 'fetchpriority=' not in tag:
        return tag.replace('<img ', '<img loading="lazy" decoding="async" ')
    return tag

html = re.sub(r'<img[^>]+>', add_lazy, html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
    
print("Global optimization complete!")
