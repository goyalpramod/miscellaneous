import cv2
import numpy as np

def getContours(img):
    contous, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contous:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 500:
            cv2.drawContours(imgContour,cnt,-1,(255,0,0),1)
            peri = cv2.arcLength(cnt,True)
            # print(peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            cv2.rectangle(imgContour,(x,y),(x+w, y + h),(0,255,0),2)

            if objCor == 3: objectType = "Tri"
            elif objCor == 4: objectType = "quadrilateral"
            else: objectType == "Circle"

            cv2.putText(imgContour,objectType,(x + (w//2) - 10, y + (h//2) - 10),cv2.FONT_HERSHEY_COMPLEX,0.3,(0,0,0),1)



img = cv2.imread("resources/shapes.jpg")
imgContour = img.copy()
imgGray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
imgBlur = cv2.GaussianBlur(img,(7,7),1)
# imgBlur = cv2.resize(imgBlur,(300,300))
imgCanny = cv2.Canny(imgBlur,50,50)
# imgCanny = cv2.resize(imgCanny,(250,250))
imgBlank = np.zeros_like(img)

getContours(imgCanny) 
cv2.imshow("Contour image", imgContour)


# cv2.imshow("image", img)
# cv2.imshow("Blur image", imgBlur)
# cv2.imshow("Gray image", imgGray)
# cv2.imshow("Canny image", imgCanny)
# cv2.imshow("Blank image", imgBlank)

# h_stack = np.hstack((img,imgBlur,imgGray))

# cv2.imshow("Stack image", h_stack)

cv2.waitKey(0)

# print("Hello World!")