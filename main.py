import cv2 as cv
import numpy as np
import sys
import noise
import filting


img=cv.imread('1.jpg')
cv.imshow("1",img)

noise.whitenoise(img,5000)
cv.imshow("2",img)
img=filting.yang_gaussfliting(img,3,30,30)
cv.imshow("3", img)
cv.waitKey()