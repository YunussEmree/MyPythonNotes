# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 14:46:40 2023

@author: Yunus Emre
"""

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


m2 = 10000
m1 = np.arange(1, 101, 1)


fig, ax = plt.subplots()  # Create a figure containing a single axes.
plt.xlabel('m1 değeri')
plt.ylabel('v2s değeri')

    
sonuc1 = ((m1 - m2) * 14) / (m1 + m2)
sonuc2 = (2 * m1 * 14) / (m1 + m2) 




plt.plot(m1, sonuc1, marker='o', linestyle='-', color='blue', label='v2')
plt.plot(m1, sonuc2, marker='o', linestyle='-', color='red', label='v1')
plt.grid(True)
plt.legend()
    

