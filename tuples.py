# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 14:58:32 2019

@author: Administrator
"""
x=2
y=3
print (x,y)
x,y = y,x 
print (x,y)
# tuple is () read only array
tuple_a = (1,2,)
tuple_a = (1,3,)
x,y = tuple_a
print (x,y)

a="Hello World"
for x in enumerate(a):
    a,b = x
    print (a,b)
    
data = [["batman",26],["superman",36]]

for name,age in data:
    print (name,age)