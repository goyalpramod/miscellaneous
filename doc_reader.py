from ast import Num
from operator import ge
import cv2
import cv2
import numpy as np

widthImg=540
heightImg =640

cap = cv2.VideoCapture(0)
cap.set(3,640) 
cap.set(4,480) 

def getContours(img):
    biggest = np.array([])
    maxArea = 0 
    contous, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contous:
        area = cv2.contourArea(cnt)
        if area > 5000:
            # cv2.drawContours(imgContour,cnt,-1,(255,0,0),1)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            if area > maxArea and len(approx) == 4:
                biggest = approx
                maxArea = area 
    cv2.drawContours(imgContour,biggest,-1,(255,0,0),2)
    return biggest


def preProcessing(img):
    
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5,5),1)
    imgCanny = cv2.Canny(imgBlur,200,200)
    kernel = np.ones((5,5))
    imgDial = cv2.dilate(imgCanny,kernel=kernel, iterations=2)
    imgThreshold = cv2.erode(imgDial,kernel=kernel,iterations=1)

    return imgThreshold

def reorder(myPoints):
    myPoints = myPoints.reshape((4,2))
    myPointsNew = np.zeros((4,1,2), np.int32)
    add= myPoints.sum(1)
    print("add",add)

    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]
    print("New points", myPointsNew)
    diff = np.diff(myPoints,axis=1)
    myPointsNew[1] = myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]

    return myPointsNew

def getWarp(img,biggest):
    biggest = reorder(biggest)
    pts1 = np.float32(biggest) 
    pts2 = np.float32([[0,0],[widthImg,0],[heightImg,0],[widthImg,heightImg]])
    matrix = cv2.getPerspectiveTransform(pts1,pts2)
    imgOutput = cv2.warpPerspective(img,matrix,(widthImg,heightImg))

    return imgOutput

while True:
    success, img = cap.read() 
    img = cv2.resize(img,(640,480))
    imgThres = preProcessing(img)
    imgContour = img.copy()
    
    biggest = getContours(imgThres)
    imgWarped = getWarp(img,biggest)

    cv2.imshow("Result",imgContour)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break