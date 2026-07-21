import sys

try:
    from deep_translator import GoogleTranslator
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "deep-translator", "--break-system-packages"])
    from deep_translator import GoogleTranslator

# Original README content (without flags yet)
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Make sure we don't duplicate flags if they are already there
flags_block = """
🌐 **Read this in:** **🇬🇧 English** | [🇪🇸 Español](README_es.md) | [🇩🇪 Deutsch](README_de.md) | [🇷🇺 Русский](README_ru.md) | [🇯🇵 日本語](README_ja.md) | [🇺🇦 Українська](README_uk.md) | [🇨🇳 中文](README_zh.md)

---
"""

if "🌐 **Read this in:**" not in content:
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if line.startswith('**Alien Box** is a state-of-the-art'):
            lines.insert(i - 1, flags_block)
            break
    else:
        lines.insert(2, flags_block)
    content = '\n'.join(lines)
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

languages = {
    'es': 'Spanish',
    'de': 'German',
    'ru': 'Russian',
    'ja': 'Japanese',
    'uk': 'Ukrainian',
    'zh-CN': 'Chinese (Simplified)'
}

# The translations for the flags block
flags_translations = {
    'es': "🌐 **Léelo en:** [🇬🇧 English](README.md) | **🇪🇸 Español** | [🇩🇪 Deutsch](README_de.md) | [🇷🇺 Русский](README_ru.md) | [🇯🇵 日本語](README_ja.md) | [🇺🇦 Українська](README_uk.md) | [🇨🇳 中文](README_zh.md)",
    'de': "🌐 **Lies das auf:** [🇬🇧 English](README.md) | [🇪🇸 Español](README_es.md) | **🇩🇪 Deutsch** | [🇷🇺 Русский](README_ru.md) | [🇯🇵 日本語](README_ja.md) | [🇺🇦 Українська](README_uk.md) | [🇨🇳 中文](README_zh.md)",
    'ru': "🌐 **Читать на:** [🇬🇧 English](README.md) | [🇪🇸 Español](README_es.md) | [🇩🇪 Deutsch](README_de.md) | **🇷🇺 Русский** | [🇯🇵 日本語](README_ja.md) | [🇺🇦 Українська](README_uk.md) | [🇨🇳 中文](README_zh.md)",
    'ja': "🌐 **他の言語で読む:** [🇬🇧 English](README.md) | [🇪🇸 Español](README_es.md) | [🇩🇪 Deutsch](README_de.md) | [🇷🇺 Русский](README_ru.md) | **🇯🇵 日本語** | [🇺🇦 Українська](README_uk.md) | [🇨🇳 中文](README_zh.md)",
    'uk': "🌐 **Читати на:** [🇬🇧 English](README.md) | [🇪🇸 Español](README_es.md) | [🇩🇪 Deutsch](README_de.md) | [🇷🇺 Русский](README_ru.md) | [🇯🇵 日本語](README_ja.md) | **🇺🇦 Українська** | [🇨🇳 中文](README_zh.md)",
    'zh-CN': "🌐 **其他语言版本:** [🇬🇧 English](README.md) | [🇪🇸 Español](README_es.md) | [🇩🇪 Deutsch](README_de.md) | [🇷🇺 Русский](README_ru.md) | [🇯🇵 日本語](README_ja.md) | [🇺🇦 Українська](README_uk.md) | **🇨🇳 中文**"
}

# Parts to translate (split by blocks to avoid breaking markdown formatting)
blocks = content.split('\n\n')

for code, name in languages.items():
    filename = f"README_{code.replace('-CN', '')}.md"
    print(f"Translating to {name}...")
    translator = GoogleTranslator(source='en', target=code)
    
    translated_blocks = []
    for block in blocks:
        if "🌐 **Read this in:**" in block:
            translated_blocks.append(flags_translations[code] + "\n\n---")
            continue
        if block.startswith("![") or block.startswith("```"):
            translated_blocks.append(block)
            continue
            
        try:
            translated = translator.translate(block)
            translated_blocks.append(translated if translated else block)
        except Exception as e:
            print(f"Failed to translate block: {e}")
            translated_blocks.append(block)
            
    with open(filename, "w", encoding="utf-8") as f:
        f.write('\n\n'.join(translated_blocks).replace(' \n', '\n'))
        
print("All translations completed!")
