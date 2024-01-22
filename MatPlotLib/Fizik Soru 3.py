import matplotlib.pyplot as plt
import numpy as np

# Verilen sabitler
theta = 43
g = 9.81

# d değerlerini oluştur
d_values = np.arange(1, 51, 1)

# t hesapla
t_values = ((2 * d_values) / (g * np.sin(np.radians(theta))))**(1/2)

# Grafik çizimi
plt.plot(d_values, t_values, marker='o', linestyle='-', color='blue')
plt.xlabel('d değeri')
plt.ylabel('t değeri')
plt.legend()
plt.grid(True)
plt.show()
