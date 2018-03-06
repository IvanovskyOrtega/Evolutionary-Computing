"""
0-1 KNAPSACK PROBLEM UTILIZANDO PROGRAMACION DINAMICA
Creditos: Ortega Victoriano Ivan
Email: ivanovskyortega@gmail.com
"""

# Definimos los valores de los pesos
w = [2,3,4,4,5]
v = [3,3,3,5,6]

def solveKnapsackDP(W):
    
    num_obj = len(w)
    
    # Creamos la tabla (matriz) de la DP
    M = [[0 for x in range(W+1)] for y in range(num_obj)] 
    
    # Llenamos los casos base
    for i in range(num_obj):
        M[i][0] = 0
    
    # Llenamos la tabla
    for i in range(num_obj):
        for j in range(1,W+1):
            if j - w[i] < 0:
                M[i][j] = M[i-1][j]
            else:
                M[i][j] = max(M[i-1][j],M[i-1][j-w[i]]+v[i])
                
    return M
                    
if __name__ == "__main__":
    M = solveKnapsackDP(10)
    for fila in M:
        print(fila)
    