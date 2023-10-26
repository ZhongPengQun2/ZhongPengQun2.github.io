# python3.8 -m pip install --upgrade pip
# pip3 install pynput
import os
from pynput import keyboard


OPEN_OSM_NOTE_KEYS = ['']


# Current be pressed keys



def on_press(key):
    keys_are_pressed.append(key)
    keys_are_pressed = list(set(keys_are_pressed))

    print('-----')
    print(key.name)
    print(key.value)
    print('====')


def on_release(key):
    keys_are_pressed.remove(key)

if __name__=="__main__":
    keys_are_pressed = []
    
    with keyboard.Listener(on_press=on_press, on_release=on_release) as lsn:
        lsn.join()





-----------模拟键盘输入----
from pynput.keyboard import Key, Controller
import time

time.sleep(5)

keyboard = Controller()

# keyboard.press(Key.ctrl.value) #this would be for your key combination
keyboard.press(Key.cmd.value)
keyboard.press('c')
keyboard.release('c')
# keyboard.release(Key.ctrl.value) #this would be for your key combination
keyboard.release(Key.cmd.value)
