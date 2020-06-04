from pynput.keyboard import Key, Listener, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController


import time

time.sleep(2)

mouse = MouseController()
key_board = KeyboardController()

break_program = False
def on_press(key):
    global break_program
    print (key)
    if key == Key.enter:
        print ('end pressed')
        break_program = True
        return False

listener = Listener(on_press=on_press)
with  listener :
    while break_program == False:
        print('program running')
        mouse.click(Button.left)
        time.sleep(0.006)
    listener.join()








