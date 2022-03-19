# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 12:24:42 2019

@author: Administrator
"""

#list
a=1
list_a=[a,3.6,"yellow",False]
print (list_a)
print (list_a[3])
a=10
list_b = list_a #=[a,3.6,"yellow",False]
for x in list_a:
    print (x)
else:
    print ("Done")
    
for index,value in enumerate(list_b): # index are integers
   # print ("index = {} and value = {}".format(index,value))
   # if(index==4):
    #    break
    print ("index = {} and value = {}".format(index,value))
else:
    print ("index = {} and value = {}".format(index,value))
    print ("Done")
    del index
    del value
# list_a= list()
    
#name address value   count
#        100   4       1
#list_a  101  [#102,#103,#100] 1
#        102   1       1
#        103   2       1
#a       104   5        1
del list_a

#name address value   count
#a       104   5        1

