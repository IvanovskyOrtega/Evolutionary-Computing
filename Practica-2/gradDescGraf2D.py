"""
DESCENSO DEL GRADIENTE EN DOS DIMENSIONES
Creditos: Ortega Victoriano Ivan
Email: ivanovskyortega@gmail.com
"""
import matplotlib.pyplot as plt
import numpy as np
import math

dx = 0.0001
dy = 0.0001
gamma = 0.1

def grad2D(x,y):
    return (f2D(x + dx,y) - f2D(x,y))/dx, (f2D(x,y + dy) - f2D(x,y))/dy

def f2D(x,y):
    return x*x + y*y

def gradDescent2D(x,y):
    x1 = []
    y1 = []
    for i in range(10):
        g = grad2D(x,y)
        x -= gamma*g[0]
        y -= gamma*g[1]
        x1.append(x)
        y1.append(y)
    xx = np.linspace(-1,1,100)
    yy = xx.copy()
    X,Y = np.meshgrid(xx,yy)
    Z = X**2 + Y**2
    f = plt.contourf(X, Y, Z, 25)
    cbar = plt.colorbar(f)
    f = plt.contour(X, Y, Z, f.levels, colors='k')
    cbar.add_lines(f)
    plt.plot(x1,y1,'ro')
    plt.xlabel("Descenso del Gradiente para 2 variables")
    plt.show()

if __name__ == "__main__":
    print (gradDescent2D(0.5,0.5))