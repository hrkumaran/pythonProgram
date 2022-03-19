# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 15:06:37 2019

@author: Administrator
"""

def add():
    print ("line1")
    print ("tlines")
    return 0
def add1(a,b):
    return a,b  # tuple 
print(add)
f=add
print(f())
print(add())
print(add1(2,5))