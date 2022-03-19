# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 15:24:16 2019

@author: Administrator
"""

#numpy needs data type
import numpy as np
a=np.array([1,2,3],dtype=np.int16)
print (a)
print (a.shape)

import numpy as np
a=np.array([1,2,3],dtype=np.int16,ndmin=2)
print (a)
print (a.shape)


import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9])
a.shape=(3,3,)
print (a)
print (a.itemsize)

import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9],dtype=np.int8)
a.shape=(3,3,)
print (a)
print (a.itemsize)

a=np.empty((3,3))
print(a)

a=np.zeros((3,3))
print(a)

a=np.ones((3,3))
print(a)

for x in range(0,100,1):
    print ("output={}".format(x))
    
a=np.arange(10,20,1)
print(a)

b=np.arange(10,12,0.20)
print(b)

print ( b[:5:2])

c=np.arange(16)
c.shape=(4,4,)
print (c)
print ( c[:5:2])


a=np.ones((3,),dtype=np.int32)
b=np.arange(3)

c = a*b

print (c)

a=np.ones((3,),dtype=np.int32)*2
b=np.arange(3)

c = a*b

print (c)
