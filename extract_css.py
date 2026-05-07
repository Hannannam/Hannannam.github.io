import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find <style>...</style> block
match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
if match:
    css_content = match.group(1).strip()
    with open('styles.css', 'w', encoding='utf-8') as f:
        f.write(css_content)
    
    new_content = content[:match.start()] + '<link rel="stylesheet" href="styles.css" />' + content[match.end():]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully extracted CSS")
else:
    print("Could not find style block")
