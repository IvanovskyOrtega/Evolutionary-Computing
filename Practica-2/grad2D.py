dx = 0.00001
dy = 0.00001

def grad2D(x,y):
    return (f2D(x + dx,y) - f2D(x,y))/dx,(f2D(x,y + dy) - f2D(x,y))/dy

def f2D(x,y):
    return x*x + y*y

print(f2D(0.5,0.5))

print(grad2D(0.5,0.5))