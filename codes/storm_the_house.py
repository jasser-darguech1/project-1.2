import numpy as np
from PIL import ImageGrab
from pynput.mouse import Button, Controller
import cv2
import time
# just so this doesn't go on forever:
mouse = Controller()
def screen_record():
    last_time = time.time()
    while(True):
        # 800x600 windowed mode
        printscreen =  np.array(ImageGrab.grab(bbox=(468,322,736,562)))
        print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        cv2.imshow('window',cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
        hsv = cv2.cvtColor(printscreen, cv2.COLOR_BGR2HSV)

        # define range of blue color in HSV
        low_blue = np.array([0, 50, 0])
        high_blue = np.array([255, 255, 50])


        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, low_blue, high_blue)


        # Bitwise-AND mask and original image

        cv2.imshow('mask',mask)
        coord = cv2.findNonZero(mask)
        if np.any(coord) == True  :
            print('yeet')
            x = coord[0, 0, 0]
            y = coord[0, 0, 1]
            mouse.position = (x + 473, y + 316)
            mouse.click(Button.left)

        if cv2.waitKey(1) & 0xFF == ord('q'):

            cv2.destroyAllWindows()
            break
time.sleep(1)
screen_record()
