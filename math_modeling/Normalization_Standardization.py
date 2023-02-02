import pandas as pd
import matplotlib.pyplot as plt
from sklearn import  preprocessing
df=pd.read_excel('/Users/zhangyan/Desktop/q1.xlsx',sheet_name='Sheet2')  # 可以通过sheet_name来指定读取的表单
data = df.iloc[:,:]

print(type(data))
print(data)

minmax = preprocessing.MinMaxScaler()
# 标准化处理
data = minmax.fit_transform(data)
data = pd.DataFrame(data)
print(data)

# x = data.iloc[:,0]
# y1 = data.iloc[:,2]
#
# print(x)
# print(y1)
#
# # 开始画图
#
# plt.title('y与log(x3)的散点图', fontsize=9)
# plt.scatter(x, y1, marker = 'x',color = 'purple', s = 40 ,label = '风速')
#
# plt.legend()  # 显示图例
#
# plt.xlabel('WSINS', fontsize=9)
# plt.ylabel('MOR_RAW', fontsize=9)
# # plt.savefig("20-x3.jpg",dpi=500,bbox_inches = 'tight')#解决图片不清晰，不完整的问题
# plt.show()
