#Resizing and Cropping

import cv2
import numpy as np

img = cv2.imread('Resources/images.jpeg')
print(img.shape)

imgResize = cv2.resize(img,(640,480))   #(width,height)
print(imgResize.shape)

cv2.imshow('Image',img)
cv2.imshow('ImageResize',imgResize)

'''cv2.waitKey(0)'''

#Cropping - no cv function. using matrix

imgCropped = img[0:200,0:100]
cv2.imshow('ImageCropped',imgCropped)
print(imgCropped.shape)
cv2.waitKey(0)