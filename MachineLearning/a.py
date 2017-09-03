#!/usr/bin/env python2
#-*- coding:utf-8 -*-
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import sys

reload(sys)
sys.setdefaultencoding('utf8')

#Input data
train_x = np.asarray([1,2,3,4,5,6,7,8,9,10,11,12,13,14])
train_y = np.asarray([3,5,7,9,11,13,15,17,19,21,23,25,27,29])

X = tf.placeholder("float")
Y = tf.placeholder("float")

#W,b分别代表θ1,θ0
#np.random.rann()用于初始化W和b
W = tf.Variable(np.random.randn(),name="theta1")
b = tf.Variable(np.random.randn(),name="theta0")

#1 假设函数的确定
pred = tf.add(tf.multiply(W,X),b)

#2 代价函数的确定
m = train_x.shape[0]  #
cost = tf.reduce_sum(tf.pow(pred-Y, 2))/(2*m)

#3 梯度下降
learning_rate = 0.01
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)
#至此模型构建完成

#Initialize the variables
init = tf.initialize_all_variables()

#Lauch the graph
with tf.Session() as sess:
    sess.run(init)
    for epoch in range(1000):   #进行100次的迭代训练
        for (x,y) in zip(train_x,train_y):
            sess.run(optimizer,feed_dict={X:x,Y:y})          
        #display
        if(epoch+1)%50==0:
            c=sess.run(cost,feed_dict={X:train_x,Y:train_y})
            print "step:%04d, cost=%.9f, θ1=%s, θ0=%s"%((epoch+1),c,sess.run(W),sess.run(b))
    print "Optimzer finished!"
    #training_cost = sess.run(cost,feed_dict={X:train_x,Y:train_y})

    print "The final is y=%sx+%s"%(sess.run(W),sess.run(b))
    plt.plot(train_x,train_y,'ro',label="Original data")
    plt.grid(True)
    plt.plot(range(1,))
    plt.plot(train_x,sess.run(W)*train_x+sess.run(b),label="Fitted line")
    plt.legend()
    plt.show()
