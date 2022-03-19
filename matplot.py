# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 17:35:42 2019

@author: Administrator
"""

import numpy as np
from matplotlib import pyplot as plt

x=np.arange(1,11)
y=2*x+5
plt.title("Sample")
plt.xlabel("Time")
plt.ylabel("Money")
plt.plot(x,y,"*",color="yellow")
plt.show()