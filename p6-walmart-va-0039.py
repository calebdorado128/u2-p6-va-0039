import matplotlib.pyplot as plt
import numpy as np

# Caleb Dorado NC = 0039

cant_productos=[100,150,200,300,500]
precio = [4000, 7000, 9000, 12000, 18000]

# plt.plot(cant_productos,precio)
# plt.show()

# Personalizar grafica
plt.plot(cant_productos, precio, color="purple", marker='o', linestyle='dashed', linewidth=2, markersize=12)
plt.title("Ventas de Walmart")
plt.xlabel("Cant_productos")
plt.ylabel("Precios")
plt.show()