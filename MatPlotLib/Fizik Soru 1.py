# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 14:46:40 2023

@author: Yunus Emre
"""

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


v0 = 10
θ = 30
g = 9.81


fig, ax = plt.subplots()  # Create a figure containing a single axes.
plt.xlabel('x değeri')
plt.ylabel('y değeri')


    
x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50])
y = (np.tan(np.radians(30)) * x) - ((g * (x**2))/(2 * (10 * np.cos(np.radians(30)))**2))
plt.plot(x, y, marker='o', linestyle='-', color='blue')
plt.grid(True)
plt.legend()
print(x)
    

