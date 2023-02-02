import cv2
import numpy as np
import math

img = cv2.imread('original_frame1.bmp')
# img = cv2.resize(img, (128,72), interpolation = cv2.INTER_AREA)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

def zmMinFilterGray(src, r=7):
    '''最小值滤波，r是滤波器半径'''
    return cv2.erode(src, np.ones((2 * r + 1, 2 * r + 1)))

V1 = np.min(img, 2)                           # 得到暗通道图像
Dark_Channel = zmMinFilterGray(V1, 7)
# cv2.imwrite('Dark_channel.jpg', Dark_Channel)

cv2.imshow('Dark',Dark_Channel)    # 查看暗通道
cv2.waitKey(0)