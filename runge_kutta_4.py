# 初始参数
h=1/10
y0=1
t=0
step=10
# 定义初值问题的右端函数f
def f(t,y):
    return 4*t*y**(1/2)
# 定义初值问题的真解
def y(t):
    return (1+t**2)**2
# 定义使用runge-kutta方法求解初值问题的函数
def runge_kutta_4(y0,t,h,f,y,step):
    un=[y0]
    u=[y0]
    e=[0]
    c=[0,1/2*h,1/2*h,h]
    for i in range(step):
        k1=f(t,y0)
        k2=f(t+c[1],y0+c[1]*k1)
        k3=f(t+c[2],y0+c[2]*k2)
        k4=f(t+c[3],y0+c[3]*k3)
        y0=y0+1/6*h*(k1+2*k2+2*k3+k4)
        un.append(y0)
        t+=h
        u.append(y(t))
        e.append(abs(un[-1]-u[-1]))
    print(un,e)
ue=runge_kutta_4(y0,t,h,f,y,step)


