import os
all_ = ''
for file in os.listdir():
    if file.startswith("_"):
        try:
            with open(f'./{file}/README.md', 'r', encoding='utf-8') as readme:
                all_ += file + '\n\n'
                all_ += readme.read() + '\n\n'
        except:
            pass
with open('README.md', 'w', encoding='utf-8') as readme:
    readme.write(all_)