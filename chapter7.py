import cv2
from cv2 import COLOR_BGR2HSV
import numpy as np

def empty(a):
    pass

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue min","TrackBars",0,179,empty)  #what will be the name, use which window,min value, max value, function that is invoked
cv2.createTrackbar("Hue max","TrackBars",19,179,empty) # hue ranges from 0 to 360 but here we have used till 180
cv2.createTrackbar("Sat min","TrackBars",110,255,empty)
cv2.createTrackbar("Sat max","TrackBars",240,255,empty)
cv2.createTrackbar("Val min","TrackBars",153,255,empty)
cv2.createTrackbar("Val max","TrackBars",255,255,empty)


while True:

    img = cv2.imread("resources/lambo.png")
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("Hue min","TrackBars")
    h_max = cv2.getTrackbarPos("Hue max","TrackBars")
    s_min = cv2.getTrackbarPos("Sat min","TrackBars")
    s_max = cv2.getTrackbarPos("Sat max","TrackBars")
    v_min = cv2.getTrackbarPos("Val min","TrackBars")
    v_max = cv2.getTrackbarPos("Val max","TrackBars")

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    imgResult = cv2.bitwise_and(img,img,mask=mask)

    # print(h_min,h_max,s_max,s_min,v_min,v_max)
    cv2.imshow("Image",img);
    # cv2.imshow("HSV Image",imgHSV);
    # cv2.imshow("Mask", mask);
    cv2.imshow("Result img", imgResult);


    cv2.waitKey(1)