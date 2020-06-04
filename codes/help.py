import cv2
import numpy as np


import numpy as np
import cv2

frame = cv2.imread('ColorChecker.png',-1)


hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

lower_blue = np.array([10,50,50])
upper_blue = np.array([170,255,255])

mask1 = cv2.inRange(hsv, (0,100,20), (10,255,255))
mask2 = cv2.inRange(hsv, (160,100,20), (255,255,255))

mask = cv2.bitwise_or(mask1, mask2 )

res = cv2.bitwise_and(frame,frame, mask= mask)

cv2.imshow('frame',frame)
cv2.imshow('mask',mask)
cv2.imshow('res',res)
k = cv2.waitKey(5) & 0xFF
cv2.waitKey(0)
cv2.destroyAllWindows()