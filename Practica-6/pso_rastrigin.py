# File: pso_rastrigin.py
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import sys
import math

# N-Dimensional Rastrigin function
def rastrigin(*X):
    dim = len(X)
    return 10*dim + sum([(x**2 - 10 * np.cos(2 * np.pi * x)) for x in X])

# Usual limits for evaluate the Rastrigin function
lower_limit=-5.12
upper_limit=5.12

# We'll use 10 particles in a 2D space
n_particles=10
n_dimensions=2


# Initialize the particle positions and their velocities
P = lower_limit + (upper_limit - lower_limit) * np.random.rand(n_particles, n_dimensions)
assert P.shape == (n_particles, n_dimensions)
V = np.zeros(P.shape)
 
# Initialize the global and local fitness to the worst possible
fitness_gbest = np.inf
fitness_lbest = fitness_gbest * np.ones(n_particles)

# Initialize the best local and global points
P_lbest=1*P
P_gbest= 1*P_lbest[0]

fitness_P = np.zeros(P.shape)

for I in range(0, n_particles):
    if rastrigin(P_lbest[I][0],P_lbest[I][1]) < rastrigin(P_gbest[0],P_gbest[1]):
        P_gbest=1*P_lbest[I]

def iteration():
    
    global P,P_lbest,P_gbest,V
    weight=0.9
    C1=0.3
    C2=0.2
    g_best = rastrigin(P_gbest[0],P_gbest[1])
    print("Best particle in:",P_gbest," gbest: ",g_best)
    
    # Update the particle velocity and position
    for I in range(0, n_particles):
        for J in range(0, n_dimensions):
          R1 = np.random.rand() # Uniform random number
          R2 = np.random.rand() # Uniform random number 
          V[I][J] = (weight*V[I][J]
                    + C1*R1*(P_lbest[I][J] - P[I][J]) 
                    + C2*R2*(P_gbest[J] - P[I][J]))
          P[I][J] = P[I][J] + V[I][J]
        if  rastrigin(P[I][0],P[I][1]) < rastrigin(P_lbest[I][0],P_lbest[I][1]):
            P_lbest[I]=1*P[I]

            if rastrigin(P_lbest[I][0],P_lbest[I][1]) < rastrigin(P_gbest[0],P_gbest[1]):
                P_gbest=1*P_lbest[I]
 
if __name__ == '__main__':
    
    it_max = 1
    while it_max <= 1000:
        print("Iteration: ",it_max)
        iteration()
        it_max += 1

    # Plot the results
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    plt.title("Rastrigin Function")
    X = np.linspace(-5.12, 5.12, 200)    
    Y = np.linspace(-5.12, 5.12, 200)    
    X, Y = np.meshgrid(X, Y)
    Z = rastrigin(X, Y)

    surf = ax.plot_surface(X, Y, Z, 
        rstride=1, cstride=1, cmap=cm.plasma, 
        linewidth=0, antialiased=False)

    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_zlabel('$z$')
    fig.colorbar(surf)
    best = rastrigin(P_gbest[0], P_gbest[1])
    ax.plot([0,P_gbest[0]],[0,P_gbest[1]],[100,best],color='black')
    ax.scatter(0., 0., 100., c='green', marker='o')
    ax.scatter(P_gbest[0], P_gbest[1], best, c='black', marker='^')
    text = '\nBest particle at: ('+str(P_gbest[0])+','+str(P_gbest[0])+')'
    ax.text2D(0.5,0,text,ha='center',va='top',transform=ax.transAxes)
    plt.show()