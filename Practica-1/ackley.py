"""
GRAFICANDO LA FUNCION DE ACKLEY CON MATPLOTLIB
Creditos: Ortega Victoriano Ivan
Email: ivanovskyortega@gmail.com
"""

from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
import sys

# Esta funcion corresponde a la función de Ackley para n variables.
def ackley(*X):
    sum1 = np.sqrt(0.5*(sum([x**2 for x in X])))
    cosine_term = sum([np.cos(2*np.pi*x) for x in X])
    return -20*np.exp(-0.2*sum1)-np.exp(0.5*cosine_term)+np.e+20

if __name__ == '__main__':
    # Creamos una figura
    fig = plt.figure()

    # Establecemos los ejes asociados a la figura
    ax = fig.gca(projection='3d')
    
    # Colocamos el titulo de la grafica
    ax.text2D(0.05, 0.95, "Ackley Function", transform=ax.transAxes)

    # La funcion es evaluada normalmente en un rango de 
    # x_i ∈[-32.768, 32.768], para toda i=1, 2, 3, ..., n
    # Para este ejemplo lo haremos el intervalo [-4, 4]
    X = np.linspace(-4, 4, 100)
    Y = np.linspace(-4, 4, 100)

    # Creamos la rejilla
    X, Y = np.meshgrid(X, Y)

    # Evaluamos los puntos (x,y) en la funcion
    Z = ackley(X,Y)

    # Graficamos la superficie generada
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.plasma,linewidth=0, antialiased=False)
    
     # Establecemos las etiquetas de los ejes
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_zlabel('$z$')

    # Mostramos la barra de color para los valores de Z
    fig.colorbar(surf, shrink=0.5, aspect=5)

    # Guardamos la grafica a un archivo
    plt.savefig("ackley.png")