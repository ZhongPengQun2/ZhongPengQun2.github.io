import os
# import redis

#docs_path = "/Users/vzhong/Documents/ZhongPengQun2.github.io/docs"
docs_path = os.path.abspath(os.path.join(os.getcwd(), "../docs"))

doc_postfixs = ['md', 'txt']


search_input = ""

import re
import glob
import time

RELATED_LINES_UP_COUNT = 5
RELATED_LINES_DOWN_COUNT = 10

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

def print_keyword_related_note(keyword):
    for _i, _line in enumerate(all_lines):
        if keyword in _line.lower():
            all_lines[_i] = all_lines[_i].replace(keyword, f'\033[92m{keyword}\033[0m')
            print('\n'.join(all_lines[_i - RELATED_LINES_UP_COUNT : _i + RELATED_LINES_DOWN_COUNT]))
            # print(_line)
            # print(_i)
            # print('\n\n')
            print('-'*50)

# all_lines_lower = [x.lower() for x in all_lines]

test_str = '扛'
test_str = read_from_clipboard()

current_keyword = ''

while True:
    clipboard_content = read_from_clipboard()
    if clipboard_content != current_keyword:
        print_keyword_related_note(clipboard_content)
        current_keyword = clipboard_content
    time.sleep(2)


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