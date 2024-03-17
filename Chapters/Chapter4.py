# Shapes and Texts

import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)            #zeros - black
#cv2.line(img,(0,0),(300,300),(0,254,0),3)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
#img[:] = 255,0,0
#cv2.imshow('Image',img)
#cv2.waitKey(0)

#Rectangle
'''cv2.rectangle(img,(0,0),(250,350),(255,0,0),cv2.FILLED)
cv2.imshow('Image',img)
cv2.waitKey(0)'''

#circle
cv2.circle(img,(400,50),30,(255,255,255),5)

#how to add text on images
cv2.putText(img,'OpenCV',(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1)

cv2.imshow('Image',img)
cv2.waitKey(0)

