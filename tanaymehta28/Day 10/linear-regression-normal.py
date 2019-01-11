import numpy as np
import pandas as pd

data = pd.DataFrame(pd.read_csv("Admission_Predict.csv"))

norm_data = (data-data.mean())/(data.max()-data.min())

data.head()
norm_data.head()

serial = data.iloc[:,0:1]
X = norm_data.iloc[:,1:8]
Y = norm_data.iloc[:,8:9]

theta = np.dot((1/(np.dot(X.T,X))),np.dot(X.T,Y))

print(theta)
