import cv2
import numpy as np

img = cv2.imread("resources/monet.jpg")
kernel = np.ones((5,5), np.int8)
# cv2.imshow("output",img)
# cv2.waitKey(0)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)  #kernel size has to be an odd number 
imgCanny = cv2.Canny(img,150,200) #edge detector 
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1) #iterations is responsible for the boldness of the edges, kernel is responsible for the thickness
imgEroded =  cv2.erode(imgDialation, kernel,iterations=1)

# cv2.imshow("Gray Image",imgGray)
# cv2.imshow("Blur Image",imgBlur)
# cv2.imshow("Canny Image",imgCanny)    
# cv2.imshow("Dialation Image",imgDialation)
cv2.imshow("Eroded Image",imgEroded)
cv2.waitKey(0) 