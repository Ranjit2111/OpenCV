import cv2
import numpy as np
img = cv2.imread('Resources/algorithms.jpg')

#Converting the image intro greyscale - cv2.cvtColor

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image",imgGray)
'''cv2.waitKey(0)'''

#Blur Function

imgBlur = cv2.GaussianBlur(imgGray,(9,9),0)
cv2.imshow("Blur Image",imgBlur)
'''cv2.waitKey(0)'''

#Edge Detector - to find the edges in our images

imgCanny = cv2.Canny(img,100,100) #Increase the threshold to increase/decrease the edges
cv2.imshow('Canny image',imgCanny)
'''cv2.waitKey(0)'''

#Dialation - increasing the thickness of the edge

kernal = np.ones((5,5),np.uint8)
imgDialation = cv2.dilate(imgCanny,kernal,iterations=5)
cv2.imshow('Dialation image',imgDialation)
'''cv2.waitKey(0)'''

#Erotion - Decreasing the thickness of the edge or making it thinner

imgEroded = cv2.erode(imgDialation,kernal,iterations=1)
cv2.imshow('Eroded image',imgEroded)
cv2.waitKey(0)

