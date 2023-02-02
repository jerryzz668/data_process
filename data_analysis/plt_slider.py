import numpy
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from utils import read_txt
# fake data
# xdata = numpy.random.rand(100,100) 
# ydata = numpy.random.rand(100,100) 
# xdata = [[7, 7, 0, 0, 3, 4, 2], [2, 2, 5, 7, 1, 6, 9]]
# ydata = [[4, 8, 9, 3, 5, 5, 2], [4, 9, 7, 0, 8, 6, 1]]
xdata, ydata = [], []

d1, d2 = 1,4  # 1,4,7,10,13,16,19

txt_path = 'data.txt'

data = read_txt(txt_path)
x, y = [], []
for i, line in enumerate(data):
    x.append(int(line[d1]))
    y.append(int(line[d2]))
    if i%42 == 0:
        xdata.append(x)
        ydata.append(y)
        x, y = [], []
print(xdata)

# set up figure
fig = plt.figure()
ax = fig.add_subplot(111)
ax.autoscale(True)
plt.subplots_adjust(left=0.25, bottom=0.25)

# plot first data set
frame = 0
ln, = ax.plot(xdata[frame],ydata[frame], 'ro')
ln_1, = ax.plot(xdata[frame+1],ydata[frame+1], '^')

# make the slider
axframe = plt.axes([0.25, 0.1, 0.65, 0.03])
sframe = Slider(axframe, 'Frame', 0, 134, valinit=0,valfmt='%d')

# call back function
def update(val):
    frame = int(numpy.floor(sframe.val))
    ln.set_xdata(xdata[frame])
    ln.set_ydata(ydata[frame])
    ln_1.set_xdata(xdata[frame+1])
    ln_1.set_ydata(ydata[frame+1])
    ax.set_title(frame)
    ax.relim()
    ax.autoscale_view()
    plt.draw()

# connect callback to slider   
sframe.on_changed(update)
plt.show()
