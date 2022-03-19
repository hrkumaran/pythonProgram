# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 10:34:08 2019

@author: Administrator
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
dataset=pd.read_csv("Data.csv")
X=dataset.iloc[:,:3].values;
y=dataset.iloc[:,3].values;
#print (dataset)

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values=np.nan,strategy="mean")
imputer = imputer.fit(X[:,1:])
X[:,1:]=imputer.transform(X[:,1:])
#print (X)

from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder_X=LabelEncoder()
X[:,0] = labelencoder_X.fit_transform(X[:,0])
#print (X)
onehotencoder_X=OneHotEncoder(categorical_features=[0])
X=onehotencoder_X.fit_transform(X).toarray()
print (X)

labelencoder_y=LabelEncoder()
y = labelencoder_y.fit_transform(y)
print (y)

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,y,test_size=0.2,random_state=0)
print (X)

from sklearn.preprocessing import StandardScaler
sc_X= StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)


#x=np.arange(1,11)
#y=2*x+5
#plt.title("Sample")
#plt.xlabel("Time")
#plt.ylabel("Money")
#plt.plot(x,y,"*",color="yellow")
#plt.show()