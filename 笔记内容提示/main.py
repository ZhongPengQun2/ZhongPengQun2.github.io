import os
# import redis

#docs_path = "/Users/vzhong/Documents/ZhongPengQun2.github.io/docs"
docs_path = os.path.abspath(os.path.join(os.getcwd(), "../docs"))

doc_postfixs = ['md', 'txt']


search_input = ""

import re
import glob
import time

all_lines = []
# all_lines_lower = []

current_clipboard_content = ""

def read_from_clipboard():
    import subprocess
    return subprocess.check_output(
        'pbpaste', env={'LANG': 'en_US.UTF-8'}).decode('utf-8')

def get_all_lines():
    for path, subdirs, files in os.walk(docs_path):
        for name in files:
            if not name.endswith(tuple(doc_postfixs)):
                continue
            with open(f'{path}/{name}') as f:
                for _line in f.readlines():
                    all_lines.append(_line)

get_all_lines()

# all_lines_lower = [x.lower() for x in all_lines]

test_str = 'python'

for _line in all_lines:
    if test_str in _line.lower():
        print(_line)
# if __name__ == "__main__":
#     while 1:
#         clipboard_text = read_from_clipboard()

#         # Escape keywords of re, ?=
#         clipboard_text = clipboard_text.replace('?', '\?')

#         if clipboard_text != current_clipboard_content:
#             matcheds = re.findall('.{100}' + clipboard_text + '.{100}', all_docs_text, re.DOTALL)
#             for matched in matcheds:
#                 print('-----------------%s'%clipboard_text)
#                 print(matched)

#             time.sleep(1)
#             current_clipboard_content = clipboard_text