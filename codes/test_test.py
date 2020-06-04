import numpy as np
from PIL import ImageGrab
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Listener, Controller as KeyboardController
import cv2
import time
# just so this doesn't go on forever:
mouse = Controller()
key_board = KeyboardController()
a = 4
c = -100
d = -100
x1 = 0
y1 = 0
z = 6
i = 0
round = 1
def screen_record():
    last_time = time.time()

    global c,d,a,i,z,x1,y1

    while (True):


        print(a)
        print(z)
        # 800x600 windowed mode
        printscreen = np.array(ImageGrab.grab(bbox=(413, 576, 877, 773)))
        #print('loop took {} seconds'.format(time.time() - last_time))
        #last_time = time.time()
        cv2.imshow('window',cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
        hsv = cv2.cvtColor(printscreen, cv2.COLOR_BGR2HSV)

        # define range of blue color in HSV
        low_blue = np.array([0,  50, 0])
        high_blue = np.array([255, 255, 50])

        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, low_blue, high_blue)

        # Bitwise-AND mask and original image

        cv2.imshow('mask',mask)
        coord = cv2.findNonZero(mask)
        if mouse.position == (0, 0):
            print('wait')
            a += 4
            z += 2
            time.sleep(3)
        if np.any(coord) == True:
            print('yeet')
            print(x1)
            print(y1)
            x = coord[x1, 0, 0] + 416
            y = coord[x1, 0, 1] + 576

            x += a

            if (x in range(c - 43, c + 43)) and (y in range(d - 30, d + 30)) :
                print('onno')
                continue

            else:
                time.sleep(0.006)
                mouse.position = (x, y)
                mouse.click(Button.left, 2)
                i += 2
                print(i)
                c = x
                d = y
                x1 = 0
                y1 = 0
                if i == z:
                    key_board.press(Key.space)
                    time.sleep(1)
                    key_board.release(Key.space)
                    i = 0
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break





time.sleep(3)
screen_record()
