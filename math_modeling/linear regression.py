from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
import numpy as np
import pandas as pd

df=pd.read_excel('/Users/zhangyan/Desktop/q1.xlsx',sheet_name='Sheet3')  # 可以通过sheet_name来指定读取的表单
# data = np.array(df)

data = df.iloc[:,:]

print(type(data))

#Max-Min标准化
#建立MinMaxScaler对象
minmax = preprocessing.MinMaxScaler()
# 标准化处理
data = minmax.fit_transform(data)
data = pd.DataFrame(data)
print(data)
print('Shape:',data.shape)


# 数据描述
print(data.describe())

# data.boxplot()
# plt.savefig("boxplot.jpg",dpi=500,bbox_inches = 'tight')#解决图片不清晰，不完整的问题
# plt.show()
#相关系数矩阵 r(相关系数) = x和y的协方差/(x的标准差*y的标准差) == cov（x,y）/σx*σy
# 相关系数0~0.3弱相关0.3~0.6中等程度相关0.6~1强相关
print(data.corr())


# c.to_excel('index3.xlsx')


X_train, X_test, Y_train, Y_test = train_test_split(data.iloc[:, :3], data.iloc[:,3], train_size=.80)

print("原始数据特征:", data.iloc[:, :3].shape,
      ",训练数据特征:", X_train.shape,
      ",测试数据特征:", X_test.shape)

print("原始数据标签:", data.iloc[:,3].shape,
      ",训练数据标签:", Y_train.shape,
      ",测试数据标签:", Y_test.shape)

model = LinearRegression()

model.fit(X_train, Y_train)

a = model.intercept_  # 截距

b = model.coef_  # 回归系数

print("最佳拟合线:截距", a, ",回归系数：", b)





