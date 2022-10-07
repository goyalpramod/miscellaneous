import cv2
import numpy as np 

img = cv2.imread("resources/monet.jpg")
imgResize = cv2.resize(img,(300,300))
imgHor = np.hstack((imgResize,imgResize))
imgVer = np.vstack((imgResize,imgResize))


cv2.imshow("Horizontal image" ,imgHor)
cv2.imshow("Vertical image" ,imgVer)

cv2.waitKey(0)