import cv2
import numpy as np
import json
import matplotlib.pyplot as plt
from skimage import morphology

# 定义分割颜色的阈值
COLOR_THRESH = 50

# 加载图像
img = cv2.imread("/home/jerry/Documents/code/demand_analysis/3-3264x2488/20230413105133334.png")
img = img[770:1500, 320:3140]
# cv2.namedWindow('xxx', 0)
# cv2.imshow('xxx', img)
# cv2.waitKey()

# 进行中值滤波
img = cv2.medianBlur(img, 5)

# 分离通道并转换为浮点数类型
b, g, r = cv2.split(img)
b = b.astype(float)
g = g.astype(float)
r = r.astype(float)

# 计算 RGB 值的标准差，作为颜色鲜明度的指标
std_rgb = np.sqrt(np.square(r - g) + np.square(g - b))

# 根据颜色鲜明度进行分割
mask = np.zeros_like(std_rgb)
mask[std_rgb > COLOR_THRESH] = 1

# 对分割结果的 mask 图进行闭运算
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (10, 10))
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

mask[mask==255] = 1
mask = morphology.skeletonize(mask)

# 检测直线
lines = cv2.HoughLinesP(mask.astype(np.uint8)*255, rho=10, theta=np.pi/280, threshold=100, minLineLength=50, maxLineGap=10)  #函数将通过步长为1的半径和步长为π/180的角来搜索所有可能的直线

# 统计直线数量
num_lines = len(lines)

# 输出直线数量
print("直线数量:", num_lines)
print(lines)

# 打印所有直线的倾斜角度
for i in range(num_lines):
    x1, y1, x2, y2 = lines[i][0]
    theta = np.arctan2(y2 - y1, x2 - x1) * 180 / np.pi
    # print("直线 %d 的倾斜角度为 %.2f 度" % (i+1, theta))

# 将分割结果的 mask 图可视化
plt.imshow(mask, cmap="gray")

# 将检测到的直线可视化到 mask 图上
if lines is not None:
    for i in range(num_lines):
        x1, y1, x2, y2 = lines[i][0]
        theta = np.arctan2(y2 - y1, x2 - x1) * 180 / np.pi
        # if -45 < theta < 45:
        if -90 < theta < -85 or 85 < theta < 90 or -1 < theta < 5:
            plt.plot([x1, x2], [y1, y2], color="green", linewidth=2)
        else:
            plt.plot([x1, x2], [y1, y2], color="red", linewidth=2)
        print(int(theta))

# 设置坐标轴不可见，并显示图像
plt.axis("off")
plt.show()
