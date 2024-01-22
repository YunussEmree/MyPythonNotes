# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 14:59:43 2024

@author: Yunus Emre
"""
#1A
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


biryetmis = np.arange(1, 71, 1)


n = (2*10*biryetmis)**(1/2)
d = ((n**2)/4.2)


fig, ax = plt.subplots()  # Create a figure containing a single axes.
plt.xlabel('h değeri')
plt.ylabel('d değeri')

    

plt.plot(biryetmis, d, marker='o', linestyle='-', color='blue')
plt.grid(True)
plt.legend()
    

