# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 14:25:37 2019

@author: Administrator
"""

# dict # key value pair

dict_a = {"name":"batman","age":25}
print ( dict_a)
print (dict_a["age"])
print (dict_a.get("address","No address"))
print ( dict_a)

dict_a["address"] = "BLR"
print ( dict_a)
print (dict_a["address"])

dict_b={"homework":[1,2.0,3,"Trythese"]}
dict_a.update(dict_b)
print ( dict_a)
del dict_a["name"]
print ( dict_a)

for key,value in dict_a.items():
    print (key,value)