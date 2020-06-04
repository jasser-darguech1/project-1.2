from pynput.mouse import Button, Controller as MouseController


import time

time.sleep(3)

mouse = MouseController()
while True :
    mouse.press(Button.left)
    time.sleep(1)
    if mouse.position == (0,0):
        print('ooof')
        break