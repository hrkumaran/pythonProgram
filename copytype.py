# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 14:08:07 2019

@author: Administrator
"""

# shallow Copy if less Changes

source=[1,2]
backup_lists=[]
#backup_lists.append(source[:])
#backup_lists.append(list(source))
backup_lists.append(source.copy())
print (backup_lists)
source[-1]=99
print (source)
print (backup_lists)


# Deep Copy if more changes
from copy import deepcopy
list_a=[1,2,3]
list_b=[9,2,3]
list_c=[1,9,3]
list_b.append(list_c)
list_a.append(deepcopy(list_b))
#list_a.append(list_b)
list_b[-1]=99
list_c[-1]=99
print (list_a)