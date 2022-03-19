# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 12:53:10 2019

@author: Administrator
"""

list_a=[1,2,3]
list_b=[1,2,3]
list_c=[8,2,5]
#list_a.append(list_b)
list_a.extend(list_b)
print (list_a)
list_d = list_c.copy()
print (list_d)
#print (list_a[-1][0])
#print (list_a[-1][1])
#print (list_a[-1][-1])

matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]

print(matrix)
print(matrix[0][0])
print(matrix[1][0])
print(matrix[0][1])
print(matrix[2][2])