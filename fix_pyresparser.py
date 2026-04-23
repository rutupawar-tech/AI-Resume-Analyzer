import os
import re

# Path to utils.py
utils_path = os.path.join('venvapp', 'Lib', 'site-packages', 'pyresparser', 'utils.py')

# Read the file
with open(utils_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix all matcher.add() calls
# Old syntax: matcher.add('NAME', None, *pattern)
# New syntax: matcher.add('NAME', pattern)
content = re.sub(r"matcher\.add\('([^']+)',\s*None,\s*\*pattern\)", r"matcher.add('\1', pattern)", content)

# Write back
with open(utils_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed pyresparser utils.py!")
