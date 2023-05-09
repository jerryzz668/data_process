import cv2
import numpy as np

# 读取原始图像和模板图像
img = cv2.imread('/home/jerry/Documents/code/demand_analysis/3-3264x2488/20230413105506295.png')
template = cv2.imread('/home/jerry/Desktop/screenshot.png')

h, w = template.shape[:2]
# 获取模板图像的宽度和高度
# w, h = template.shape[::-1]

# template = cv2.cvtColor(template, cv2.COLOR_BGR2RGB)
# 应用模板匹配
res = cv2.matchTemplate(img,template,cv2.TM_CCORR_NORMED)  # cv2.TM_CCORR_NORMED  cv2.TM_CCOEFF_NORMED

# 找到匹配得分最高的位置
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

# 绘制矩形框
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
cv2.rectangle(img, top_left, bottom_right, (0, 0, 255), 2)

# 显示结果
cv2.namedWindow('img', 0)
cv2.imshow('img', img)
cv2.waitKey(0)
# cv2.destroyAllWindows()
