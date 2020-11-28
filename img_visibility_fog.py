import cv2
import numpy as np
import math

img = cv2.imread('original_frame1.bmp')
img = cv2.resize(img, (128,72), interpolation = cv2.INTER_AREA)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

def zmMinFilterGray(src, r=7):
    '''最小值滤波，r是滤波器半径'''
    return cv2.erode(src, np.ones((2 * r + 1, 2 * r + 1)))

V1 = np.min(img, 2)                           # 得到暗通道图像
Dark_Channel = zmMinFilterGray(V1, 7)
# cv2.imshow('Dark',Dark_Channel)    # 查看暗通道
# cv2.waitKey(0)

print(Dark_Channel.shape)
def select_sort(Array, K):
    '''
        Time complexity: O(n^2)
    '''
    Array = Array.flatten()
    array = Array.copy().astype(float)
    l = []
    print('before sort:{}'.format(array))
    min_loc = 0
    for i in range(K):
        for j in range(0, len(array)):
            # print('1')
            if array[j] < array[min_loc]:
                min_loc = j
        l.append(array[min_loc] )
        array[min_loc] = float('inf')
    return min_loc
    # print('K:{}'.format(l))
    # print('position:{}'.format(min_loc))


# array = np.random.randint(low=1,high=20,size=(3,3))
b = select_sort(Dark_Channel,9)
x, y = divmod(b,128)
# print(x,y)

Ac = gray[x,y]

mincc = Dark_Channel/Ac

# print(mincc.shape)

t1 = 1-mincc[54][50]
t2 = 1-mincc[58][53]
t3 = 1-mincc[56][82]
t4 = 1-mincc[60][89]
print(t1,t2,t3,t4)


beta1 = abs(math.log(t1/t2,2.7))
beta2 = abs(math.log(t3/t4,2.7))
beta = (beta1+beta2)/2
print(beta)

V = 3/beta
print(V)


