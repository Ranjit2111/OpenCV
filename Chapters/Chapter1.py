'''cv2 stands for computer vision'''
import cv2
print("Package Imported")

#how to read images, videos and webcam:

#importing image
img = cv2.imread('Resources/algorithms.jpg')
cv2.imshow('Output',img)
cv2.waitKey(0) #0 - Infinity milliseconds it will display the image.

#importing video
cap = cv2.VideoCapture('Resources/IMG_1642.MOV')
while True:
    success, img = cap.read()
    cv2.imshow('Video',img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

#using webcam
import cv2

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)
while True:
    success, img = cap.read()
    cv2.imshow('Video',img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
