import cv2
import os
import numpy as np
"""
纵向拼图
"""


img_path = '/home/jerry/Desktop/xxx'

output_path = '/home/jerry/Desktop/xxx/total.png'

filelist = os.listdir(img_path)
filelist.sort()
print(filelist)
mask = np.zeros((4500, 815, 3), np.uint8)  # h*w
for i,file in enumerate(filelist):
    img = cv2.imread(os.path.join(img_path, file))
    img = cv2.resize(img,(815,900))  # w*h
    mask[i*900:(i+1)*900,0:815] = img  # y1:y2,x1:x2

# cv2.namedWindow('xxx',0)
# cv2.imshow('xxx',mask)
# cv2.waitKey(0)



cv2.imencode('.png', mask)[1].tofile(output_path)