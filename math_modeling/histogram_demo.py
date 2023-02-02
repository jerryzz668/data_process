import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def histogram_demo(image):
    plt.hist(image.ravel(), 256, [0, 256])#ravel函数功能是将多维数组降为一维数组
    plt.show()
    # plt.savefig("zhifantu.jpg",dpi=500,bbox_inches = 'tight')#解决图片不清晰，不完整的问题

image = cv.imread('5.jpg', 1)
# cv.imshow('souce image', image)
histogram_demo(image)
# cv.waitKey(0)
# cv.destroyAllWindows()

