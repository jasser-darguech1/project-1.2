import numpy as np
import cv2

#BGR TO RGB

#BLUE
blue = np.uint8([[[255,0,0 ]]])
hsv_blue = cv2.cvtColor(blue,cv2.COLOR_BGR2HSV)
print (hsv_blue)

low_blue = np.array([94,80,2])
high_blue = np.array([126,255,255])


#GREEN
green = np.uint8([[[0,255,0 ]]])
hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print (hsv_green)

low_green = np.array([25,52,72])
high_green = np.array([102,255,255])



#RED
red = np.uint8([[[0,0,255 ]]])
hsv_red = cv2.cvtColor(red,cv2.COLOR_BGR2HSV)
print (hsv_red)

low_red = np.array([161,155,84])
high_red = np.array([179,255,255])



mask1 = cv2.inRange(hsv, (0,100,20), (10,255,255))
mask2 = cv2.inRange(hsv, (160,100,20), (255,255,255))

#@#############
# 2 MASKS red
mask1 = cv2.inRange(hsv, (0, 100, 20), (8, 255, 255))
mask2 = cv2.inRange(hsv, (160, 100, 20), (255, 255, 255))

mask = cv2.bitwise_or(mask1, mask2)

res = cv2.bitwise_and(frame, frame, mask=mask)
############
#1 MASK
lower_blue = np.array([94,80,2])
upper_blue = np.array([126,255,255])

# Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# Bitwise-AND mask and original image
res = cv2.bitwise_and(frame,frame, mask= mask)
