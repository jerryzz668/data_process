import cv2
import pytesseract
import re

# 加载图像
img = cv2.imread('/home/jerry/Documents/code/demand_analysis/3-3264x2488/20230413103237484.png')
img= img[760:1750,750:2410]
# cv2.namedWindow('xxx', 0)
# cv2.imshow('xxx', img)
# cv2.waitKey()

# 文本识别
text = pytesseract.image_to_string(img)
# text = pytesseract.image_to_string(img, lang='chi_sim')

# 处理识别结果
text = re.sub(r'\D', '', text)
print(text)
