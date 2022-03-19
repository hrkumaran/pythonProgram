# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 14:17:09 2019

@author: Administrator
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
dataset=pd.read_csv("Salary_Data.csv")
X=dataset.iloc[:,0].values;
y=dataset.iloc[:,1].values;

print (X)
print (y)

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,y,test_size=0.2,random_state=4)
print (X)


from sklearn.linear_model import LinearRegression
regressor= LinearRegression()

X_train.shape=(-1,1)
Y_train.shape=(-1,1)
regressor.fit(X_train,Y_train)
X_test.shape=(-1,1)
Y_pred = regressor.predict(X_test)

Y_pred_NewPerson = regressor.predict([[6.5]])

plt.scatter(X_train,Y_train,color="yellow")
plt.title("Train Output")
plt.xlabel("Expereience")
plt.ylabel("Salary")
plt.plot(X_train,regressor.predict(X_train))
plt.show()

plt.scatter(X_test,Y_test,color="blue")
plt.title("Test Output")
plt.xlabel("Expereience")
plt.ylabel("Salary")
plt.plot(X_train,regressor.predict(X_train))
plt.show()