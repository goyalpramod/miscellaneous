import cv2
import numpy as np 

faceCascade = cv2.CascadeClassifier("resources/") #put the pretrained weights here. just search cascade opencv

img = cv2.imread("resources/lena.png")
imgGray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

faces = faceCascade.detectMultiScale(imgGray,1.1,4)

for(x,y,w,h) in face:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    

cv2.imshow("Image",img)
cv2.waitKey(0)