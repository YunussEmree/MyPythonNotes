# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 14:46:40 2023

@author: Yunus Emre
"""

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np



m = 0.1
v = 1.5

fig, ax = plt.subplots()  # Create a figure containing a single axes.
plt.xlabel('k değeri')
plt.ylabel('x değeri')


    
k = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
x = (m/k)**(1/2) * v
plt.plot(k, x, marker='o', linestyle='-', color='blue')
plt.grid(True)
plt.legend()
    

