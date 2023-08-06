import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import matplotlib.pyplot as plt
from utils import read_txt
import numpy as np

def get_data(log_path):
    data = read_txt(log_path)
    print(len(data))
    y = []
    for line in data:
        score = line.split('is')[-1]
        score = np.round(float(score), 4)
        y.append(score)
    return y

# lambda1 = [0.05, 0.1, 0.2, 0.5, 0.6]
# y1 = [93.99, 93.34, 93.09, 92.97, 91.77]
# y2 = [56.63, 62.27, 75.76, 78.78, 85.82]
# y3 = [58.96, 61.27, 73.99, 76.88, 84.97]
lambda1 = list(range(1, 101))

# y3 = get_data('/home/jerry/Desktop/log_curve/demo_a/demo_a_chain_p_log.out')[0:100]
# y2 = get_data('/home/jerry/Desktop/log_curve/demo_a/demo_a_chain_p_log_01-12.out')[0:100]
# y1 = get_data('/home/jerry/Desktop/log_curve/demo_a/demo_a_chain_p_log_01-25.out')[0:100]

# y3 = get_data('/home/jerry/Desktop/log_curve/demo_b/demo_b_chain_p_log.out')[0:100]
# y2 = get_data('/home/jerry/Desktop/log_curve/demo_b/demo_b_chain_p_log_02-27.out')[0:100]
# y1 = get_data('/home/jerry/Desktop/log_curve/demo_b/demo_b_chain_p_log_01-26.out')[0:100]

y3 = get_data('/home/jerry/Desktop/log_curve/demo_c/demo_c_chain_p_log.out')[0:100]
y2 = get_data('/home/jerry/Desktop/log_curve/demo_c/demo_c_chain_p_log_01-28.out')[0:100]
y1 = get_data('/home/jerry/Desktop/log_curve/demo_c/demo_c_chain_p_log_01-27.out')[0:100]

# y3 = get_data('/home/jerry/Desktop/log_curve/demo_d/demo_d_chain_p_log-01-10.out')[0:100]
# y2 = get_data('/home/jerry/Desktop/log_curve/demo_d/demo_d_chain_p_log-01-11.out')[0:100]
# y1 = get_data('/home/jerry/Desktop/log_curve/demo_d/demo_d_chain_p_log-01-12.out')[0:100]
print(len(y1))
print(len(y2))
print(len(y3))

# plt.plot(lambda1, y1, c='red', marker='o', linestyle='-', label='y1')
# plt.plot(lambda1, y2, c='blue', marker='*', linestyle='-', label='y2')
# plt.plot(lambda1, y3, c='green', marker='+', linestyle='-', label='y3')

plt.plot(lambda1, y1, c='red', label='f1(x)')
plt.plot(lambda1, y2, c='blue', label='f2(x)')
plt.plot(lambda1, y3, c='green', label='f3(x)')

#设置图例并且设置图例的字体及大小
font1 = {'family': 'Times New Roman', 'weight': 'normal', 'size': 10}
plt.xticks(fontproperties = 'Times New Roman',fontsize=10)
plt.yticks(fontproperties = 'Times New Roman',fontsize=10)

plt.title('Demo_C', fontsize=10)
plt.xlabel(u'Number of generations', font1)
plt.ylabel(u'Score', font1)

# 图例展示位置，数字代表第几象限
plt.legend(loc=1, prop=font1)   

# Axes(ax)对象，主要操作两个坐标轴间距
# x_major_locator = MultipleLocator(0.05)
# ax = plt.gca()              
# ax.xaxis.set_major_locator(x_major_locator)
# plt.show()
plt.savefig("/home/jerry/Desktop/log_curve/demo_c.png",dpi=500,bbox_inches = 'tight')#解决图片不清晰，不完整的问题