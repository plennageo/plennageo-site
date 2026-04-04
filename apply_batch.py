import re

path = "index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

start = content.find('<div class="hero-slider"')
end = content.find('</section>', start)

if start != -1 and end != -1:
    hero_html = content[start:end]

    replacements = {
        "hero-slide-01.webp": "allen1.webp\" style=\"object-position: center 20%;\" ",
        "hero-slide-02.webp": "gnss.webp\" style=\"object-position: center 25%;\" ",
        "hero-slide-03.webp": "estacao-total.webp",
        "hero-slide-04.webp": "drone-freepik.webp\" style=\"object-position: center 25%;\" ",
        "hero-slide-05.webp": "car-freepik2.webp",
        "hero-slide-06.webp": "sigef-freepik.webp",
        "hero-slide-07.webp": "reurb-freepik.webp",
        "hero-slide-08.webp": "proj-loteamento.webp"
    }

    # Step 1: Substituir as imagens
    for old, new in replacements.items():
        hero_html = hero_html.replace(old, new)
        
    # Step 2: Inject fetchpriority for high visibility images (no aria-hidden)
    # Using regex to find <img> elements without aria-hidden
    
    def add_perf(match):
        img_tag = match.group(0)
        if 'aria-hidden' not in img_tag and 'service-area' not in img_tag:
            return img_tag.replace('/>', 'fetchpriority="high" decoding="sync" />').replace('/></figure>', 'fetchpriority="high" decoding="sync" /></figure>')
        else:
            if 'loading="lazy"' not in img_tag:
                return img_tag.replace('/>', 'loading="lazy" decoding="async" />').replace('/></figure>', 'loading="lazy" decoding="async" /></figure>')
            return img_tag
            
    hero_html = re.sub(r'<img[^>]+>', add_perf, hero_html)

    content = content[:start] + hero_html + content[end:]
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
        
    print("Sucesso!")
