import cv2
import numpy as np

# 读取图像并将其转换为灰度图像
img = cv2.imread('/home/jerry/Documents/code/demand_analysis/3-3264x2488/20230413105133334.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, binary = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.namedWindow('xxx', 0)
cv2.imshow('xxx', binary)
cv2.waitKey()

# 对图像进行边缘检测
edges = cv2.Canny(binary, 50, 150, apertureSize=3)

cv2.namedWindow('xxx', 0)
cv2.imshow('xxx', edges)
cv2.waitKey()

# 进行Hough线性变换检测直线
lines = cv2.HoughLines(edges, 1, np.pi/180, 180)

# 分类水平和垂直线
horizontal_lines = []
vertical_lines = []
for line in lines:
    rho, theta = line[0]
    # 计算斜率
    slope = np.tan(theta)
    if abs(slope) < 0.1: # 小于0.1度认为是水平线
        horizontal_lines.append(line)
    elif abs(slope) > 10: # 大于10度认为是竖直线
        vertical_lines.append(line)

# 在图像上绘制水平和垂直线
for line in horizontal_lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

for line in vertical_lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.namedWindow('xxx', 0)
cv2.imshow('xxx', img)
cv2.waitKey()