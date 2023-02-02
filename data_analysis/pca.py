from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

X = np.array([[12, 350, 1.825, 0.102, 315, 0, 2, 4], 
[25, 300, 5.57, 0.45, 220, 25, 3, 2.5],  
[25, 300, 5.25, 1.1, 220, 20, 4, 3]])

Y = np.array([22, 300, 4.25, 1.86, 210, 18, 3, 2])
# n_components指定降维后的维数
pca = PCA(n_components=2)
pca.fit(X)  # 应用于训练集数据进行PCA降维

pca_new = pca.transform(X)
print('降维结果', pca_new)
print('具有最大方差的成分', pca.components_)
print('各主成分的方差', pca.explained_variance_)
print('各主成分的方差占比', pca.explained_variance_ratio_)


# plt.title("Test Plot")  # 显示图的标题
# plt.xlabel("Factors")  # xy轴的名字
# plt.ylabel("Eigenvalue")  # xy轴的名字
# plt.grid()  # 显示网格
# plt.show()  # 显示图形

