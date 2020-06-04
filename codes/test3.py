import cv2
import numpy as np
from pynput.mouse import Button, Controller

cap = cv2.VideoCapture(0)
mouse = Controller()
while True:

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    low_blue = np.array([94, 80, 2])
    high_blue = np.array([126, 255, 255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, low_blue, high_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask=mask)

    coord = cv2.findNonZero(mask)
    x = coord[0,0,0]
    y = coord[0,0,1]
    print(x,y)


    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    k = cv2.waitKey(25) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()