from matplotlib import pyplot as plt
import math

# この辺を高度化していったら，pytorch みたいになるのかね．
# そもそも variables をちゃんとクラス指定にしたほうがだいぶとわかりやすいような
# pytorch ってモデル構築というより，数値計算ライブラリ的な側面の方が強いかも？
def dob(x):
    return x * x - 1

# そもそも，式のまま微分することはできないのか？
def ddob2(x):
    return 2

# これも微分の式を自分が知ってないと出来ないので，何かしら自動微分は欲しいな．
# 微分方程式を解くものもあれば便利だという話だよな
def ddob(x):
    return 2*x 

def dddob(x):
    return 2

def exp(x):
    return math.exp(x)

def multi(x):
    return x**4-3*x**2 - 2

def dmulti(x):
    return 4*x**3 - 6*x

def ddmulti(x):
    return 12*x**2 - 6

x = 10
eta = 0.1

def grad_decent_opt(f, df, x, eta=0.1):
    xk = x
    for i in range(100):
        xk -= eta * df(xk)
        #print(xk)
        if abs(df(xk)) < 0.00001:
            break
        # print(y)
        
    return xk

def grad_decent_root(f, df2, df, x, eta=0.1):
    xk = x
    for i in range(1000):
        xk -= eta * df2(x)*f(xk)*df(xk)
        
    return xk

def newton_method_root(f, df, x):
    xk = x
    for i in range(100):
        xkn = xk - f(xk)/df(xk)
        xk = xkn
        if abs(df(xk)) < 0.00001:
            break

    return xkn

def newton_method_opt(df, ddf, x):
    xk = x
    for i in range(100):
        xkn = xk - df(xk)/ddf(xk)
        xk = xkn
        if abs(df(xk)) < 0.00001:
            break

    return xkn
        

f = multi
df = dmulti
ddf = ddmulti
x = -4

y = grad_decent_opt(f, df, x, eta=0.001)
print(y, f(y), df(y))

y = newton_method_opt(df, ddf, x)
print(y, f(y), df(y))

#y = grad_decent_root(f, df, x, eta=0.001)
#print(y, f(y), df(y))

y = newton_method_root(f, df, x)
print(y, f(y), df(y))

# なんか難しいな，関数を受け取って勝手にグラフを書いてくれるメソッドとか作れんだろうか？
# まあ，そうやったほうが効率的だって状況まで自分を追い込む + 管理方法を身につけることにより，
# そういうことができるようになるのかもしれんが．

def show_graph(f, x_range, df=None, fig_name="default"):
    xs = [i*0.01*6 - x_range/2 for i in range(100)]
    ys = [f(x) for x in xs]
    plt.plot(xs, ys)
    plt.savefig(f"figs/{fig_name}")
    
#show_graph(f)
show_graph(multi, x_range=6)
#show_graph(exp)