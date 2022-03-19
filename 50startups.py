# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 16:08:59 2019

@author: Administrator
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
dataset=pd.read_csv("50_Startups.csv")
X=dataset.iloc[:,:4].values
y=dataset.iloc[:,4].values

#print (y)

from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder_X=LabelEncoder()
X[:,3] = labelencoder_X.fit_transform(X[:,3])
#print (X)
onehotencoder_X=OneHotEncoder(categorical_features=[3])
X=onehotencoder_X.fit_transform(X).toarray()
#print (X)

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,y,test_size=0.2,random_state=0)


from sklearn.linear_model import LinearRegression
regressor= LinearRegression()

regressor.fit(X_train,Y_train)

Y_pred = regressor.predict(X_test)
print (Y_pred)


plt.title("Train Output")
plt.xlabel("Expereience")
plt.ylabel("Salary")
plt.plot(np.arange(10),Y_test,color="red");
plt.plot(np.arange(10),regressor.predict(X_test),color="blue");
plt.show()

