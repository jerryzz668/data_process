import numpy as np
import random

np.random.seed(22)

class CyrusSOM(object):
    # def __init__(self,net=[[1,1],[1,1]],epochs = 50,r_t = [None,None],eps=1e-6):
    def __init__(self,net=[1,1],epochs = 50,r_t = [None,None],eps=1e-6):
        """
        :param net: 竞争层的拓扑结构，支持一维及二维，1表示该输出节点存在，0表示不存在该输出节点
        :param epochs: 最大迭代次数
        :param r_t:   [C,B]    领域半径参数，r = C*e**(-B*t/eoochs),其中t表示当前迭代次数
        :param eps: learning rate的阈值
        """

        self.epochs = epochs
        self.C = r_t[0]
        self.B = r_t[1]
        self.eps = eps
        self.output_net = np.array(net)
        if len(self.output_net.shape) == 1:
            self.output_net = self.output_net.reshape([-1,1])
        self.coord = np.zeros([self.output_net.shape[0],self.output_net.shape[1],2])
        for i in range(self.output_net.shape[0]):
            for j in range(self.output_net.shape[1]):
                self.coord[i,j] = [i,j]
        print(self.coord)


    def __r_t(self,t):
        if not self.C:
            return 0.5
        else:
            return self.C*np.exp(-self.B*t/self.epochs)

    def __lr(self,t,distance):
        return (self.epochs-t)/self.epochs*np.exp(-distance)
    def standard_x(self,x):
        x = np.array(x)
        for i in range(x.shape[0]):
            x[i,:] = [value/(((x[i,:])**2).sum()**0.5) for value in x[i,:]]
        return x
    def standard_w(self,w):
        for i in range(w.shape[0]):
            for j in range(w.shape[1]):
                w[i,j,:] = [value/(((w[i,j,:])**2).sum()**0.5) for value in w[i,j,:]]
        return w
    def cal_similar(self,x,w):
        similar = (x*w).sum(axis=2)
        coord = np.where(similar==similar.max())
        return [coord[0][0],coord[1][0]]

    def update_w(self,center_coord,x,step):
        for i in range(self.coord.shape[0]):
            for j in range(self.coord.shape[1]):
                distance = (((center_coord-self.coord[i,j])**2).sum())**0.5
                if distance <= self.__r_t(step):
                    self.W[i,j] = self.W[i,j] + self.__lr(step,distance)*(x-self.W[i,j])

    def transform_fit(self,x):
        self.train_x = self.standard_x(x)
        self.W = np.zeros([self.output_net.shape[0],self.output_net.shape[1],self.train_x.shape[1]])
        for i in range(self.W.shape[0]):
            for j in range(self.W.shape[1]):
                self.W[i,j,:] = self.train_x[random.choice(range(self.train_x.shape[0])),:]
        self.W = self.standard_w(self.W)
        for step in range(int(self.epochs)):
            j = 0
            if self.__lr(step,0) <= self.eps:
                break
            for index in range(self.train_x.shape[0]):
                print("*"*8,"({},{})/{} W:\n".format(step,j,self.epochs),self.W)
                center_coord = self.cal_similar(self.train_x[index,:],self.W)
                self.update_w(center_coord,self.train_x[index,:],step)
                self.W = self.standard_w(self.W)
                j += 1
        label = []
        for index in range(self.train_x.shape[0]):
            center_coord = self.cal_similar(self.train_x[index, :], self.W)
            label.append(center_coord[1]*self.coord.shape[1] + center_coord[0])
        class_dict = {}
        for index in range(self.train_x.shape[0]):
            if label[index] in class_dict.keys():
                class_dict[label[index]].append(index)
            else:
                class_dict[label[index]] = [index]
        cluster_center = {}
        for key,value in class_dict.items():
            cluster_center[key] = np.array([x[i, :] for i in value]).mean(axis=0)
        self.cluster_center = cluster_center

        return label


    def fit(self,x):
        self.train_x = self.standard_x(x)
        self.W = np.random.rand(self.output_net.shape[0], self.output_net.shape[1], self.train_x.shape[1])
        self.W = self.standard_w(self.W)
        for step in range(int(self.epochs)):
            j = 0
            if self.__lr(step,0) <= self.eps:
                break
            for index in range(self.train_x.shape[0]):
                print("*"*8,"({},{})/{} W:\n".format(step, j, self.epochs), self.W)
                center_coord = self.cal_similar(self.train_x[index, :], self.W)
                self.update_w(center_coord, self.train_x[index, :], step)
                self.W = self.standard_w(self.W)
                j += 1
        label = []
        for index in range(self.train_x.shape[0]):
            center_coord = self.cal_similar(self.train_x[index, :], self.W)
            label.append(center_coord[1] * self.coord.shape[1] + center_coord[1])
        class_dict = {}
        for index in range(self.train_x.shape[0]):
            if label[index] in class_dict.keys():
                class_dict[label[index]].append(index)
            else:
                class_dict[label[index]] = [index]
        cluster_center = {}
        for key, value in class_dict.items():
            cluster_center[key] = np.array([x[i, :] for i in value]).mean(axis=0)
        self.cluster_center = cluster_center

    def predict(self,x):
        self.pre_x = self.standard_x(x)
        label = []
        for index in range(self.pre_x.shape[0]):
            center_coord = self.cal_similar(self.pre_x[index, :], self.W)
            label.append(center_coord[1] * self.coord.shape[1] + center_coord[1])
        return label

from sklearn.datasets import load_iris,make_blobs
import matplotlib.pyplot as plt
from  sklearn.metrics import classification_report
if __name__ == '__main__':
    SOM = CyrusSOM(epochs=50)
    # x,y = make_blobs(n_samples=100,n_features=4,centers=3,cluster_std=0.3)
    # x,y = make_blobs(n_samples=42,n_features=6,centers=3,cluster_std=1)

    x = [[7, 7, 0, 0, 3, 4, 2],
[4, 8, 9, 3, 5, 5, 2],
[2, 2, 5, 7, 1, 6, 9],
[4, 9, 7, 0, 8, 6, 1],
[5, 4, 9, 4, 8, 0, 2],
[0, 5, 1, 5, 4, 7, 3],
[6, 3, 8, 5, 0, 9, 3],
[2, 7, 3, 9, 6, 0, 9],
[3, 5, 3, 7, 4, 5, 4],
[2, 3, 0, 0, 7, 7, 6],
[5, 7, 1, 1, 0, 4, 5],
[9, 4, 8, 2, 2, 1, 6],
[1, 8, 7, 3, 8, 5, 6],
[7, 4, 4, 7, 2, 1, 1],
[7, 1, 4, 6, 3, 3, 1],
[2, 7, 9, 0, 5, 9, 0],
[4, 5, 4, 1, 5, 4, 4],
[9, 6, 6, 1, 0, 2, 0],
[3, 0, 2, 7, 0, 3, 7],
[8, 8, 1, 5, 4, 6, 7],
[6, 2, 0, 2, 8, 6, 8],
[0, 0, 2, 8, 1, 1, 2],
[1, 0, 6, 2, 9, 2, 9],
[9, 1, 8, 6, 3, 8, 2],
[8, 9, 6, 4, 7, 2, 7],
[7, 1, 0, 4, 9, 8, 7],
[2, 5, 2, 7, 1, 7, 1],
[0, 9, 2, 8, 2, 8, 9],
[0, 2, 7, 3, 7, 9, 4],
[6, 8, 3, 1, 6, 4, 5],
[9, 1, 4, 5, 7, 3, 8],
[8, 3, 8, 9, 6, 5, 8],
[1, 2, 5, 9, 6, 9, 5],
[6, 6, 7, 6, 2, 0, 3],
[4, 4, 2, 2, 7, 1, 6],
[1, 3, 9, 4, 5, 0, 0],
[5, 2, 1, 6, 1, 2, 4],
[8, 9, 6, 8, 9, 7, 5],
[3, 6, 5, 8, 3, 2, 0],
[3, 7, 5, 9, 4, 8, 8],
[5, 0, 7, 2, 9, 3, 7],
[7, 6, 3, 3, 2, 7, 3]]

    y_pre = SOM.transform_fit(x)
    print(y_pre)
    # print(type(y_pre))
    # print(len(y_pre))
    # colors = "rgby"
    colors = "rg"
    figure = plt.figure(figsize=[20,12])
    plt.scatter(x[:,0],x[:,1],c=[colors[i] for i in y_pre])
    # plt.scatter(x[:,0],x[:,1])
    plt.show()  




