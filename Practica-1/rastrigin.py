"""
GRAFICANDO LA FUNCION DE RASTRIGIN CON MATPLOTLIB
Creditos: Ortega Victoriano Ivan
Email: ivanovskyortega@gmail.com
"""

from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import sys
import math
# Descomentar esta linea si se usará Jupyter Notebook
# %matplotlib inline

# Esta funcion corresponde a la  funcion de Rastigin para n variables
def rastrigin(*X):
    dim = len(X)
    return 10*dim + sum([(x**2 - 10 * np.cos(2 * math.pi * x)) for x in X])

if __name__ == '__main__':

    # Creamos una figura
    fig = plt.figure()
    
    
    
    # Establecemos los ejes asociados a la figura
    ax = fig.gca(projection='3d')
    
    # Colocamos el titulo de la grafica
    ax.text2D(0.05, 0.95, "Rastrigin Function", transform=ax.transAxes)
    
    # La funcion es evaluada normalmente en un rango de 
    # x_i ∈[-5.12, 5.12], para toda i=1, 2, 3, ..., n
    # Para este ejemplo lo haremos en dicho intervalo
    X = np.linspace(-5.12, 5.12, 200)    
    Y = np.linspace(-5.12, 5.12, 200)    

    # Creamos la rejilla
    X, Y = np.meshgrid(X, Y)

    # Evaluamos los puntos (x,y) en la funcion 
    Z = rastrigin(X, Y)

    # Graficamos la superficie generada
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.plasma, linewidth=0, antialiased=False)
    
    # Establecemos las etiquetas de los ejes
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_zlabel('$z$')
    
    # Mostramos la barra de color para los valores de Z
    fig.colorbar(surf)
    
    plt.savefig('rastrigin.png')
