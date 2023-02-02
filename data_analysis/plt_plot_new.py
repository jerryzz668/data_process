import numpy as np
from utils import read_txt
import numpy
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from sklearn.manifold import TSNE

# 1.数据格式初始化
# txt_path = 'demo_d_current_pop-01-10_copy.txt'
# txt_path = 'demo_d_new_population-01-10_copy.txt'
txt_path = 'log/demo_d_current_pop-01-14.txt'
data = read_txt(txt_path)
# print(len(data))
# print(type(data))
all_data = []  # list中每个元素都是42*8的二维数组
for line in data:
    float_line = list(map(eval, line.split(',')))
    line_data = np.array(float_line).reshape(42,10)  # 二维矩阵(42*8), 每个种群8=7+1     ------------------------->这里参数需要封装
    all_data.append(line_data)

# 2.获取所有的ylabel  42*150的二维矩阵
ylabel_all = [[]*1]*42
for i, content in enumerate(all_data):
    ylabel_line = content[::,9:10:]     #   ------------------------->这里参数需要封装
    ylabel_all = np.concatenate((ylabel_all, np.round(ylabel_line, 4)), axis=1)

# 3.开始画折线图
fig = plt.figure()
ax = fig.add_subplot(111)
x = list(range(0, 139))
for line in ylabel_all:
    ax.plot(x, line)
plt.show()