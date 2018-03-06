dx = 0.0001

def grad1D(x):
    return (f1D(x+dx)-f1D(x))/dx

def f1D(x):
    return x*x

print(f1D(0.5))

print(grad1D(0.5))