# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 14:59:43 2024

@author: Yunus Emre
"""
#1A
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import math


biryetmis = np.arange(1, 71, 1)


n = ((20*biryetmis)**(1/2))
print(n)
vb = (0 - (1-(0.21 * np.emath.power(np.tan(np.radians(n)), -1))))
print(vb)
a = np.emath.power(vb, 1/2)
print(a)
b = (n*a)
print(b)


fig, ax = plt.subplots()  # Create a figure containing a single axes.
plt.xlabel('h değeri')
plt.ylabel('b değeri')

    

plt.plot(biryetmis, b, marker='o', linestyle='-', color='blue')
plt.grid(True)
plt.legend()
    

