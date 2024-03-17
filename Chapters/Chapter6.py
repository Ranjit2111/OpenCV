#Joining Images

import cv2
import numpy as np

img = cv2.imread('Resources/images.jpeg')
Imghor = np.hstack((img,img))
Imgver = np.vstack((img,img))
cv2.imshow('Vertical',Imgver)
cv2.imshow('Horizontal',Imghor)
cv2.waitKey(0)

#issues
#1. cannot resize the image
#2. images should have same no of channels.

