from PIL import Image
import os

files_to_optimize = {
    "assets/images/allen1.webp": "assets/images/allen1.webp",
    "assets/images/gnss.webp": "assets/images/gnss.webp",
    "assets/images/estacao-total.webp": "assets/images/estacao-total.webp",
    "assets/images/drone-freepik.webp": "assets/images/drone-freepik.webp",
    "assets/images/car-freepik2.webp": "assets/images/car-freepik2.webp",
    "assets/images/sigef-freepik.png": "assets/images/sigef-freepik.webp", # converte png p webp
    "assets/images/reurb-freepik.webp": "assets/images/reurb-freepik.webp",
    "assets/images/proj-loteamento.webp": "assets/images/proj-loteamento.webp"
}

target_height = 720

for in_path, out_path in files_to_optimize.items():
    if not os.path.exists(in_path):
        print(f"File not found: {in_path}")
        continue
    
    try:
        orig_size = os.path.getsize(in_path)
        with Image.open(in_path) as img:
            print(f"Original {in_path}: {img.size}, {orig_size/1024:.1f} KB")
            
            if img.mode not in ("RGB", "RGBA"):
                img = img.convert("RGBA")
                
            w, h = img.size
            if h > target_height:
                ratio = target_height / h
                new_w = int(w * ratio)
                img = img.resize((new_w, target_height), Image.Resampling.LANCZOS)
                
            img.save(out_path, "WEBP", quality=82, method=6)
            
        new_size = os.path.getsize(out_path)
        print(f"Otimizado {out_path}: {new_size/1024:.1f} KB. Reducao: {(1 - new_size/orig_size)*100:.1f}%")
        
    except Exception as e:
        print(f"Error on {in_path}: {e}")
