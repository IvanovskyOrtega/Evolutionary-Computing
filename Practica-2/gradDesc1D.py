dx = 0.0001
gamma = 0.1

def grad1D(x):
    return (f1D(x+dx)-f1D(x))/dx

def f1D(x):
    return x*x

def gradDescent1D(x):
    for i in range(10):
        x -= gamma*grad1D(x)
        print(x,f1D(x),grad1D(x))

print(f1D(0.5))
print(grad1D(0.5))
print(gradDescent1D(0.5))