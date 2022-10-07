import cv2
# print("hello World!")

# to Import images

# img = cv2.imread("resources/monet.jpg")

# cv2.imshow("Output",img)
# cv2.waitKey(0) #how long to display the image for, in ms. 0 means infinity

# cap = cv2.VideoCapture("resources/faded.mp4") #to import video
cap = cv2.VideoCapture(0) #for webcam
cap.set(3,480) #length
cap.set(4,480) #height
# cap.set(10,100) #brightness (each num like 3,4,10 is an id for something related to the webcam)




while True:
    success, img = cap.read() # as a video is a series of many images we are using a while loop. each image is stored in img and success shows wheter it worked or not 
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'): # quit if q is pressed
        break