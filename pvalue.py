# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 16:27:56 2019

@author: Administrator
"""

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
#plt.show()


import statsmodels.api as sm
X=np.append(arr=np.ones((50,1)).astype(int),values=X,axis=1)
X_opt=X[:,[0,1,2,3,4,5]]
regressor_OLS = sm.OLS(endog=y,exog=X_opt)
regressor_OLS = regressor_OLS.fit()
regressor_OLS.summary()

def backwardElimination(X, s1):
    numVars = len(X[0])
    for i in range(0,numVars):
        regressor_OLS = sm.OLS(y,X).fit()
        maxVar = max(regressor_OLS.pvalues).astype(float)
        if maxVar > s1:
            for j in range(0,numVars - i):
                if( regressor_OLS.pvalues[j].astype(float) == maxVar):
                 X = np.delete(X,j,1)
                
    regressor_OLS.summary()
    return X

SL=0.05
X_opt=X[:,[0,1,2,3,4,5]]
X_Modelled = backwardElimination(X_opt,SL)