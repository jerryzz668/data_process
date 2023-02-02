import numpy as np
from utils import read_txt
import numpy
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from sklearn.manifold import TSNE


txt_path = 'data_analysis/log/log/demo_d_current_pop-02-01.txt'
new_pop_txt_path = 'data_analysis/log/log/demo_d_new_population-02-01.txt'
# txt_path = 'log/demo_c_current_pop-01-30.txt'
# new_pop_txt_path = 'log/demo_c_new_population-01-30.txt'

curr_pop = read_txt(txt_path)
new_pop = read_txt(new_pop_txt_path)
# print(len(data))
# print(type(data))
def all_data2xydata(data):
    all_data = []  # list中每个元素都是42*8的二维数组
    for line in data:
        float_line = list(map(eval, line.split(',')))
        line_data = np.array(float_line).reshape(42,10)  # 二维矩阵(42*8), 每个种群8=7+1   ------------------------->这里参数需要封装
        all_data.append(line_data)

    xdata, ydata = [], []
    d1, d2 = 2,3  # 1,2,3,4,5,6,7
    tsne = False
    for i, content in enumerate(all_data):
        if tsne:
            tsne_input = content[::,:7:]
            # print(type(tsne_input))
            # print(tsne_input.shape)
            X_embedded = TSNE(n_components=2, learning_rate='auto', init='random', perplexity=3).fit_transform(tsne_input)
            d1_dimension = X_embedded[::,0:1:].ravel()
            d2_dimension = X_embedded[::,1:2:].ravel()
            # print(X_embedded)
            xdata.append(np.round(d1_dimension, 2))
            ydata.append(np.round(d2_dimension, 2))
        else:
            d1_dimension = content[::,d1-1:d1:].ravel()  # 切片--平铺
            d2_dimension = content[::,d2-1:d2:].ravel()  # 切片--平铺
            # xdata.append(np.round(d1_dimension, 2).tolist())
            # ydata.append(np.round(d2_dimension, 2).tolist())
            xdata.append(np.round(d1_dimension, 2))
            ydata.append(np.round(d2_dimension, 2))
    return xdata, ydata

curr_pop_xdata, curr_pop_ydata = all_data2xydata(curr_pop)
new_pop_xdata, new_pop_ydata = all_data2xydata(new_pop)

# set up figure
fig = plt.figure()
ax = fig.add_subplot(111)
ax.autoscale(True)
plt.subplots_adjust(left=0.25, bottom=0.25)

# plot first data set
frame = 0
ln, = ax.plot(curr_pop_xdata[frame],curr_pop_ydata[frame], 'ro')
# ln_1, = ax.plot(curr_pop_xdata[frame+1],curr_pop_ydata[frame+1], '^')
ln_1, = ax.plot(new_pop_xdata[frame],new_pop_ydata[frame], '^')

plt.axis([0, 1, 0, 1])  # 设置范围，四个数分别对应x的起点终点和y的起点终点
# make the slider
axframe = plt.axes([0.25, 0.1, 0.65, 0.03])
sframe = Slider(axframe, 'Frame', 0, len(curr_pop_xdata), valinit=0,valfmt='%d')  # ------------------------->这里参数需要封装

# call back function
def update(val):
    frame = int(numpy.floor(sframe.val))
    ln.set_xdata(curr_pop_xdata[frame])
    ln.set_ydata(curr_pop_ydata[frame])
    # ln_1.set_xdata(curr_pop_xdata[frame+1])
    # ln_1.set_ydata(curr_pop_ydata[frame+1])
    ln_1.set_xdata(new_pop_xdata[frame])
    ln_1.set_ydata(new_pop_ydata[frame])
    ax.set_title(frame)
    ax.relim()
    ax.autoscale_view()
    plt.draw()

# connect callback to slider   
sframe.on_changed(update)
plt.show()
















# file1 = open('demo_d_all_route_index.txt', 'r', encoding='utf-8')   # 打开要去掉空行的文件
# file2 = open('data.txt', 'w', encoding='utf-8')  # 生成没有空行的文件

# for line in file1.readlines():
#     if line == '\n':
#         line = line.strip('\n')
#     file2.write(line)

# file1.close()
# file2.close()
