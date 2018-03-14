"ALGORITMOS DE PROGRAMACION DINAMICA"
"Creditos: Ortega Victoriano Ivan"
"Email: ivanovskyortega@gmail.com"

import sys
        
# Esta funcion construye la tabla de la solucion
# del KP 0/1 utilizando programacion dinamica
def solveKnapsackDP(W,w,v):
    
    num_obj = len(w)
    # Creamos la tabla (matriz) de la DP
    
    M = [[0 for _ in range(W+1)] for _ in range(num_obj+1)] 
    
    # Llenamos los casos base
    
    for i in range(num_obj+1):
        M[i][0] = 0
    
    # Llenamos la tabla
    
    for i in range(1,num_obj+1):
        for j in range(1,W+1):
            if j - w[i-1] < 0:
                M[i][j] = M[i-1][j]
            else:
                M[i][j] = max(M[i-1][j],M[i-1][j-w[i-1]]+v[i-1])
                
    return M
    
# Esta funcion obtiene los elementos utilizados para la
# solucion del KP 0/1 para un W especifico basandose en
# la tabla construida previamente. 
def getSolutionKP(M,W):
    
    solution = []
    j = W
    i = len(M)-1
    
    while i > 0 and j > 0 :
        if M[i][j] != M[i-1][j]:
            solution.append(i)
            j = j - w[i-1]
            i = i - 1
        else:
            i = i -1
        
    return solution

# Esta funcion construye la tabla de la solucion
# del Coin Change Problem utilizando programacion 
# dinamica
def solveCoinChange(d,N):
    
    coins = len(d)
    inf = sys.maxint
    M = [[0 for _ in range(N+1)] for _ in range(coins+1)]
    
    # Llenamos la primer fila con valores muy grandes

    for j in range(N+1):
        M[0][j] = inf

    for i in range(1,coins+1):
        for j in range(1,N+1):
            if d[i-1] == j:
                M[i][j] = 1
            elif d[i-1] > j:
                M[i][j] = M[i-1][j]
            else:
                M[i][j] = min(M[i-1][j],M[i][j-d[i-1]]+1)

    return M

# Esta funcion obtiene los elementos utilizados para la
# solucion del Coin Change Problem para un N especifico 
# basandose en la tabla construida previamente. 
def getSolutionCC(M,d,N):
    
    solution = {}

    # Inicializamos los valores para la solucion en ceros
    
    coins = len(d)
    for i in range(0,coins):
        coin = d[i]
        solution[coin] = 0
    
    # Ahora buscamos cuantas monedas se utilizaron de cada denominacion
    
    i = len(M)-1
    j = N
    
    while i > 0 and j > 0:
        if M[i][j] < M[i-1][j]:
            j = j - d[i-1]
            solution[d[i-1]] += 1
        else:
            i -= 1

    return solution
            

if __name__ == "__main__":
    
    # Ejemplo resolviendo el KP-0/1
    w = [2,3,4,4,5]
    v = [3,3,3,5,6]
    W = 10
    print('Knapsack Problem 0/1')
    M = solveKnapsackDP(W,w,v)
    print('Solucion:')

    for row in M:
        print(row)

    print('Se utilizaron los siguientes elementos:')
    print(getSolutionKP(M,W))

    # Ejemplo resolviendo el MCP
    d = [1, 2, 3] # Denominacion de las monedas
    N = 10
    print('Coin Change Problem')
    T = solveCoinChange(d,N)
    print('Solucion:')

    for row in T:
        print(row)

    print('Monedas utilizadas (moneda , # de monedas usadas):')
    solution = getSolutionCC(T,d,N)

    for s in solution:
        print(s,solution[s])
        
    # Solve the 0-1 knapsack problem and the change making using dp
        