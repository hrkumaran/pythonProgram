# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 16:22:56 2019

@author: Administrator
"""

import numpy as np
import pandas as pd

a=np.arange(9)
print(a)
result = pd.Series(a)  # inmutable
print(result)


a=np.arange(3)
print(a)
result = pd.Series(a,index=["room1","room2","room3"])
print(result)
print(result[0])
print(result["room1"])
result = pd.Series(a,index=[10,20,30])
print(result)
print(result[10])
print(result*2)
print(result[20]*2)

source={
        "server1":23,
        "server2":45,
        "server3":50
        }
results=pd.Series(source,index=["server1","server3","server2"],dtype=np.int16)
print(results[1:])
print(results[["server2","server1"]])

#DataFrame # two dimendsionals

df=pd.DataFrame([1,2,3,4],columns=["SerialNo"],index=[100,101,102,103])
print (df)
print (df.values)
print (df.values)

source=[
        {
                "name":"batman",
                 "age": 25
                 },
                {
                 "name":"batman",
                 "age": 25
                }
        ]

df=pd.DataFrame(source)
print (df)
print (df.values)
print (df.values)

source2=[["batman",25],["superman",35]]

df=pd.DataFrame(source2)
print (df)
#print (df.values)
#print (df.values)

source5=["batman","superman"]
source6=[24,35]
source7=[2,4]

source8={
        "name":source5,
        "age":source6,
        "points":source7}

df=pd.DataFrame(source8)
print (df)
print (df["age"])
print (df["age"][1])
print (df[["age","points"]])

df["source"]=df["age"]+df["points"]
print(df)
#del df["age"]
#del df["points"]
print(df.loc[0])
print(type(df.loc[0]))
print(df.loc[1]["age"])
print(df.iloc[1]["age"])
print(df.iloc[1])

df=pd.DataFrame(source8,index=['A','B'])
print (df)
#print (df["age"])
#print (df["age"][1])
#print (df[["age","points"]])

df["source"]=df["age"]+df["points"]
print(df)
#del df["age"]
#del df["points"]
#print(df.loc[0])
#print(type(df.loc[0]))
#print(df.loc[1]["age"])
#print(df.iloc[1]["age"])
#print(df.iloc[1])

df=df.drop('A');
