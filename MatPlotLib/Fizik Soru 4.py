# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 16:12:08 2023

@author: Yunus Emre
"""

import matplotlib.pyplot as plt
import numpy as np

# Verilen sabitler
d = 10
g = 9.81

# θ değerlerini oluştur
theta_values = np.arange(1, 91, 1)

# t hesapla
t_values = ((2 * d) / (g * np.sin(np.radians(theta_values))))**(1/2)

# Grafik çizimi
plt.plot(theta_values, t_values, marker='o', linestyle='-', color='blue')
plt.xlabel('θ değeri')
plt.ylabel('t değer')
plt.legend()
plt.show()