import numpy as np
import matplotlib.pyplot as plt

# Verilen değerler
v0 = 10
y_target = 10
theta_values = np.arange(1, 51)  # θ'nin 1'den 50'ye kadar olan değerleri

# İlişkiyi bulma fonksiyonu
def find_x(theta):
    equation = lambda x: np.tan(np.radians(theta)) * x - (9.8 / (2 * (v0 * np.cos(np.radians(theta))**2))) * x**2
    # Denklemin kökünü (x'in değerini) bulma
    result = np.roots([-(9.8 / (2 * (v0 * np.cos(np.radians(theta))**2))), np.tan(np.radians(theta)), 0])
    real_roots = result[np.isreal(result)].real  # Karmaşık kökleri hariç tut
    return real_roots[0] if len(real_roots) > 0 else None

# θ ile x arasındaki ilişkiyi grafik olarak çizme
x_values = [find_x(theta) for theta in theta_values]

# Grafik ayarları
plt.plot(theta_values, x_values, marker='o', linestyle='-', color='blue')
plt.xlabel('θ değeri')
plt.ylabel('x değeri')
plt.grid(True)
plt.show()
