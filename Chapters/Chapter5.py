#Warp Perspective

import cv2
import numpy as np

img = cv2.imread('Resources/playing-cards-167049_640.jpg')
height,width=350,250
pts = np.float32([[385,106],[639,190],[264,425],[569,426]])
pts1 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts,pts1)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow('Image',img)
cv2.imshow('Output',imgOutput)
cv2.waitKey(0)