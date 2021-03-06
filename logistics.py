# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 11:47:40 2019

@author: Administrator
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
dataset=pd.read_csv("Social_Network_Ads.csv")
X=dataset.iloc[:,[2,3]].values;
y=dataset.iloc[:,4].values;
#print (dataset)



from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=0)

print (X)
print (y)

from sklearn.preprocessing import StandardScaler
sc_X= StandardScaler()
X_train= sc_X.fit_transform(X_train)
X_test= sc_X.transform(X_test)

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state=0)
classifier.fit(X_train,y_train)

y_pred = classifier.predict(X_test)