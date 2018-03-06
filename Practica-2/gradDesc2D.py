dx = 0.0001
dy = 0.0001
gamma = 0.1

def grad2D(x,y):
    return (f2D(x + dx,y) - f2D(x,y))/dx, (f2D(x,y + dy) - f2D(x,y))/dy

def f2D(x,y):
    return x*x + y*y

def gradDescent2D(x,y):
    for i in range(10):
        g = grad2D(x,y)
        x -= gamma*g[0]
        y -= gamma*g[1]
        print(x,y,f2D(x,y),grad2D(x,y))

print(f2D(0.5,0.5))
print(grad2D(0.5,0.5))
print (gradDescent2D(0.5,0.5))