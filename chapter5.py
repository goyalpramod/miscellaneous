import cv2
import numpy as np 
# Did not work tr again later sometime 
img = cv2.imread("resources/cards.jpg")

width,height = 250,350

pts1 = np.float32([[929,335],[1255,370],[874,791],[1215,835]]) 
pts2 = np.float32([[0,0],[width,0],[height,0],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))


# cv2.imshow("image",img)
cv2.imshow("Warped image",imgOutput)

cv2.waitKey(0)
