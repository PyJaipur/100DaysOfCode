import numpy as np
import pandas as pd

data = pd.DataFrame(pd.read_csv("Desktop/Datasets/Admission_Predict.csv"))

norm_data = (data-data.mean())/(data.max()-data.min())

serial = data.iloc[:,0:1]
X = norm_data.iloc[:,1:8].values
Y = norm_data.iloc[:,8:9].values

class LinearRegression:
'''
----------------------------------------------------------------------------------------------------------------------------------------
Parameters Required:

X,y,leanring_rate, num_iters
----------------------------------------------------------------------------------------------------------------------------------------
Function Information:

__generate_theta(self,X) => Generates Theta Vector from given X-Matrix
__loss(self,hypothesis,y) => Calculates Loss (Predicted Value - Real value)
__cost(self,hypothesis,y,m) => Calculates the Cost (J(theta)) 
fit(self,X,y) => Provided X & Y matrices; It Performs the Gradient Descent Optimisation to find the Optimal Value of Weight-Vector Theta
----------------------------------------------------------------------------------------------------------------------------------------
'''

    
    def __init__(self,learning_rate,num_iters):
        self.learning_rate = learning_rate
        self.num_iters = num_iters
    
    def __generate_theta(self,X):
        return np.ones((X.shape[1]))
    
    def __loss(self,hypothesis,y):
        return np.sum(hypothesis-y)
    
    def __cost(self,hypothesis,y,m):
        temp01 = np.sum(hypothesis-y)**2
        return temp01/(2*m)
    
    def fit(self,X,y):
        m = y.size
        theta = self.__generate_theta(X)
        
        for i in range(self.num_iters):
            hypothesis = np.dot(X,theta)
            loss = self.__loss(hypothesis,y)
            cost = self.__cost(hypothesis,y,m)
            
            gradient = (np.sum(np.dot(X.T,(hypothesis-Y))))/m
            theta = theta - self.learning_rate * gradient
            
            hypothesis = np.dot(X,theta)
            loss = self.__loss(hypothesis,y)
            
            print("loss is: ",loss)
        return theta



