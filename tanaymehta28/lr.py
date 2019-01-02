import pandas as pd
import numpy as np

train = pd.DataFrame(pd.read_csv("train.csv"))


train.head()
train = (train-train.mean())/(train.std())

X = train.iloc[:, 1:14]

Y = train.iloc[:, 14:15].values

id = train.iloc[:, 0:1].values

theta = (np.zeros([1,len(X)]))

ones = np.ones([X.shape[0],1])

X = np.concatenate((ones,X),axis=1)

alpha = 0.001
epochs = 10000

def computeCost(X,y,theta):
    summ = (np.matmul(theta,X)-y)**2
    return np.sum(summ)/(2*len(X))

computeCost(X,Y,theta)

def GradientDescentOptimizer(X,y,theta,alpha,epochs):
    cost = np.zeros(epochs)
    for i in range(epochs):
        theta = theta-(alpha/len(X))*np.sum(np.matmul(X,(np.matmul(X,theta)-y))
        cost[i] = computeCost(X,y,theta)
    return theta,cost

g,Cost = GradientDescentOptimizer(X,Y,theta,alpha,epochs)
