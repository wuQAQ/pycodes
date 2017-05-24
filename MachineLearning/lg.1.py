#!/usr/bin/env python
# -*- coding:UTF-8 -*-

'''
Created on 20**-**-**

@author: fangmeng
'''

import numpy

#=====================================
# 输入：
#        空
# 输出:
#        dataMat: 测试数据集
#        labelMat: 测试分类标签集
#=====================================
def loadDataSet():
    '创建测试数据集，分类标签集并返回。'
    
    # 测试数据集
    dataMat = []; 
    # 测试分类标签集
    labelMat = []
    # 文本数据源
    fr = open('/home/wuqaq/project/pycodes/MachineLearning/testSet.txt')
    
    # 载入数据
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
        
    return dataMat,labelMat


#=====================================
# 输入：
#        inX: 目标转换向量
# 输出:
#       1.0/(1+numpy.exp(-inX)): 转换结果
#=====================================
def sigmoid(inX):
    'sigmoid转换函数'
    
    return 1.0/(1+numpy.exp(-inX))

#=====================================
# 输入：
#        dataMatIn: 数据集
#        classLabels: 分类标签集
# 输出:
#        weights: 最佳拟合参数向量
#=====================================
def gradAscent(dataMatIn, classLabels):
    '基于梯度上升法的logistic回归分类器'
   
    # 将数据集，分类标签集存入矩阵类型。 
    dataMatrix = numpy.mat(dataMatIn)
    labelMat = numpy.mat(classLabels).transpose()
   
    # 上升步长度
    alpha = 0.001
    # 迭代次数
    maxCycles = 500
    # 初始化回归参数向量
    m,n = numpy.shape(dataMatrix)
    weights = numpy.ones((n,1))
    
    # 对回归系数进行maxCycles次梯度上升
    for k in range(maxCycles):
        h = sigmoid(dataMatrix*weights)
        error = (labelMat - h) 
        weights = weights + alpha * dataMatrix.transpose()* error
        
    return weights

def test():
    '测试'
    
    dataArr, labelMat = loadDataSet()
    print gradAscent(dataArr, labelMat)

if __name__ == '__main__':
    test()

#======================================
#    输入:
#            weights: 回归系数向量
#    输出:
#            图形化的决策边界演示
#======================================
def plotBestFit(weights):
    '决策边界演示'
    
    import matplotlib.pyplot as plt
    # 获取数据集 分类标签集
    dataMat,labelMat=loadDataSet()
    dataArr = numpy.array(dataMat)
    
    # 两种分类下的两种特征列表
    xcord1 = []; ycord1 = []
    xcord2 = []; ycord2 = []
    for i in range(numpy.shape(dataArr)[0]):
        if int(labelMat[i])== 1:
            xcord1.append(dataArr[i,1]); ycord1.append(dataArr[i,2])
        else:
            xcord2.append(dataArr[i,1]); ycord2.append(dataArr[i,2])
            
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c='green')
    
    # 绘制决策边界
    x = numpy.arange(-3.0, 3.0, 0.1)
    y = (-weights[0]-weights[1]*x)/weights[2]
    ax.plot(x, y)
    
    plt.xlabel('X1'); plt.ylabel('X2');
    plt.show()
    
def test():
    '测试'
    
    dataArr, labelMat = loadDataSet()
    weights = gradAscent(dataArr, labelMat)
    plotBestFit(weights.getA())