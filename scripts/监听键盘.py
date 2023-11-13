# python3.8 -m pip install --upgrade pip
# pip3 install pynput
import os
import pynput
from pynput import keyboard

from enum import Enum


OPEN_OSM_NOTE_KEYS = ['']


keys_are_being_pressed = []


def get_key_char(key):
    if isinstance(key, pynput.keyboard._darwin.KeyCode):
        return key.char
    elif isinstance(key, Enum):
        return key.name

def on_press(key):
    global keys_are_being_pressed
    keys_are_being_pressed.append(get_key_char(key))
    keys_are_being_pressed = list(set(keys_are_being_pressed))

    print(keys_are_being_pressed)

    if 'c' in keys_are_being_pressed and 'enter' in keys_are_being_pressed:
        import os, sys
        os.system("vim /tmp/vvvv.txt")
        sys.exit()

def on_release(key):
    keys_are_being_pressed.remove(get_key_char(key))


if __name__=="__main__":
    with keyboard.Listener(on_press=on_press, on_release=on_release) as lsn:
        lsn.join()





# -----------模拟键盘输入----
# from pynput.keyboard import Key, Controller
# import time

# time.sleep(5)

# keyboard = Controller()

# # keyboard.press(Key.ctrl.value) #this would be for your key combination
# keyboard.press(Key.cmd.value)
# keyboard.press('c')
# keyboard.release('c')
# # keyboard.release(Key.ctrl.value) #this would be for your key combination
# keyboard.release(Key.cmd.value)
