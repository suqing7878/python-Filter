import cv2 as cv
import numpy as np
import sys

def whitenoise(img,n):#输入图像，噪声数量
    #为图像增加椒盐噪声
    row=img.shape[0]
    col=img.shape[1]
    for i in range(n):
        x=np.random.randint(0,row)  #（x，y）坐标
        y=np.random.randint(0,col)
        noise=np.random.randint(0,2)*255 #黑白噪声
        img[x,y]=noise


def whitenoise_color(img,n):#输入图像，噪声数量
    #为图像增加彩色椒盐噪声
    row=img.shape[0]
    col=img.shape[1]
    channel=img.shape[2]

    for j in range(0,channel):
        for i in range(n):
            x=np.random.randint(0,row)  #（x，y）坐标
            y=np.random.randint(0,col)
            noise=np.random.randint(0,2)*255 #黑白噪声
            img[x,y,j]=noise
