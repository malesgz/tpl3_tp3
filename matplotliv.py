import matplotlib.pyplot as plt
import pandas as pd
# import numpy as np

# x = np.linspace(0,5,11)
# y = x ** 2

df = pd.DataFrame({ "x": [1,2,3,4,5], "y": [6,7,8,9,0]})

plt.plot(df["x"], df["y"])
# plt.plot(x, y) No hace falta volver a declarar x e y ya que arriba ya se esta llamando a las mismas variables que se van a utilizar para la gráfica.

plt.xlabel("Nombre del eje X")
plt.ylabel("Nombre del eje Y")
plt.title("Matplotlib con pandas")
plt.show()


# Método básico para graficar X vs Y.
# plt.plot(x,y)
# Define un título de la gráfica.
# plt.title("Práctica de Matplotlib")
# Mostrar la gráfica luego de que ya se definió todos los elementos.
# plt.show()