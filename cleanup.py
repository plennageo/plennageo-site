path = "index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Cleaning up the exact typo from string replacements:
# Example: src="assets/images/allen1.webp" style="object-position: center 20%;" " alt="Serviços no campo"
content = content.replace('%;" "', '%;"')
content = content.replace('%;"  alt=', '%;" alt=')

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Cleanup successful!")
