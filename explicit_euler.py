import math

h=1/10
yn=1
t=0

def f(t,y):
    return 4*t*y**(1/2)
def y(t):
    return (1+t**2)**2
for i in range(10):
    yn=yn+f(t,yn)*h
    u=y(t)
    t=t+h
    e=abs(yn-u)
    print(yn,e)

h=1/2
yn=1
t=0

for i in range(10):
    yn=yn+f(t,yn)*h
    u=y(t)
    t=t+h
    e=abs(yn-u)
    print(yn,e)
