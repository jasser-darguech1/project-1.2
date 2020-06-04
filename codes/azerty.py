import cv2
import numpy as np
## Read and merge
img = cv2.imread("ColorChecker.png")
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(img_hsv[0,1])