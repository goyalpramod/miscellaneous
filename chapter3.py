import cv2
from cv2 import imread
import numpy as np

img = cv2.imread("resources/monet.jpg")
print(img.shape)

imgResize = cv2.resize(img,(300,300)) #width first then the height
print(imgResize.shape)


imgCropped = img[0:200,200:500] #height first then width

# cv2.imshow("image", img)
# cv2.imshow("image resized", imgResize)
cv2.imshow("image cropped", imgCropped)
cv2.waitKey(0)

