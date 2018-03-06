"""
DESCENSO DEL GRADIENTE EN UNA DIMENSION
Creditos: Ortega Victoriano Ivan
Email: ivanovskyortega@gmail.com
"""

from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
import math

X = np.linspace(-1, 1)  
Y = X**2

dx = 0.0001
gamma = 0.1

def grad1D(x):
    return (f1D(x+dx)-f1D(x))/dx

def f1D(x):
    return x*x

def gradDescent1D(x):
    x1 = []
    y1 = []
    for i in range(10):
        x -= gamma*grad1D(x)
        x1.append(x)
        y1.append(f1D(x))
    plt.plot(X,Y)
    plt.plot(x1,y1,'or')
    plt.xlabel("Descenso del Gradiente para 1 variable")
    plt.show()

if __name__ == "__main__":
    print(gradDescent1D(0.5))