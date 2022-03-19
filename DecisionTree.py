# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 10:48:22 2019

@author: Administrator
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

dataset=pd.read_csv("Position_Salaries.csv")
X=dataset.iloc[:,1:2].values # two dimensional array
y=dataset.iloc[:,2].values

#from sklearn.tree import DecisionTreeRegressor
#regressor = DecisionTreeRegressor(random_state=0)
#regressor.fit(X,y)
#
#y_pred = regressor.predict([[6.5]])
#
#X_grid = np.arange(min(X),max(X),0.01)
#X_grid = X_grid.reshape(len(X_grid),1)
#plt.scatter(X,y,color="red")
#plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
#plt.title('Truth or Bluff')
#plt.xlabel('Position level')
#plt.ylabel('Salary')
#plt.show()

from sklearn.ensemble import RandomForestRegressor

regressor1 = RandomForestRegressor(n_estimators=1000,random_state=0)
regressor1.fit(X,y)

y_pred = regressor1.predict([[6.5]])

X_grid = np.arange(min(X),max(X),0.01)
X_grid = X_grid.reshape(len(X_grid),1)
plt.scatter(X,y,color="red")
plt.plot(X_grid, regressor1.predict(X_grid), color = 'blue')
plt.title('Truth or Bluff')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()