from pynput.keyboard import Key, Listener, Controller as KeyboardController
import time


key_board = KeyboardController()
i = 0

break_program = False
time.sleep(3)
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
        key_board.press(Key.space)
        time.sleep(0.006)
        key_board.release(Key.space)
        time.sleep(0.006)
        key_board.press(Key.right)
        i += 1
        print(i)
        if i in range (100,151):
            key_board.release(Key.up)

            print('yeet')
        else:
            key_board.press(Key.up)
        if i == 150 :
            i = 0

    listener.join()



