from matplotlib import pyplot as plt

# この辺を高度化していったら，pytorch みたいになるのかね．
def f(x):
    return x * x

def df(x):
    return 2*x

x = 10
print(f(x), df(x))