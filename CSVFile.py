# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 17:26:48 2019

@author: Administrator
"""

import pandas as pd
df=pd.read_csv("FL_insurance_sample.csv")
print (df)
df=df[["policyID"]]
print (df)
df.to_csv("file1.csv")
df.to_json("filew.json")
df.to_excel("file2.xlsx")