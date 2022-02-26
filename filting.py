import cv2 as cv
import numpy as np
import sys


#我的高斯滤波
def yang_gaussfliting(img,size,ave,stand):   #输入（原始图像，滤波核半径（奇数），方差，标准差）
    corepoint=((size+1)/2)-1#卷积核中心坐标
    kernal=np.zeros((size,size),dtype='float32')
    for i in range(size):
        for j in range(size):
            r2=pow(corepoint-i,2)+pow(corepoint-j,2)
            kernal[i,j]=stand*np.exp((-r2)/(2*pow(ave,2)))

    kernal=kernal/sum((sum(kernal)))
    img= cv.filter2D(img, -1, kernel=kernal)

    cv.imshow("高斯滤波图像",img)

    return img


