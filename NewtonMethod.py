r = 6150.0
x = 8888.0#initial x

def f(x):
    return 3.0*r*x**2.0 - x**3.0 - 0.4*r**3.0
def fd(x):
    return 6.0*r*x - 3.0*x**2.0
while True:
    a = f(x)
    b = fd(x)
    x = x - a/b
    print x,a
    if a == 0.0:
        break

