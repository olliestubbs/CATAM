import numpy as np
import matplotlib.pyplot as plt

def E(nu,C,mu,s):
    term = 1
    sigma = 0
    for i in range(s):
        sigma += term
        term = term*(C-i)/nu
    for i in range(C-s):
        sigma+=term
        term = term*(C-i-s)/(nu+mu)
    sigma += term
    return 1/sigma
def T(nu,C,mu,s):
    sigma = 0
    term = E(nu,C,mu,s)
    for i in range(s):
        sigma+=term
        term=term*(C-i)/nu
    sigma+=term
    return sigma
def estBR(initB,initR,nu,C,s,n):
    B=initB
    R=initR
    for i in range(n):
        newB=E(nu,C,2*nu*B*(1-R),s)
        newR=T(nu,C,2*nu*B*(1-R),s)
        B=newB
        R=newR
    return B*(2*R-R**2)
for i in range(11):
    print(estBR(0,0,560,600,i,20))
"""
xaxis = np.arange(1,100)
yaxis = np.zeros(99)
for i in range(99):
    print(i)
    yaxis[i]=estBR(0,0,560,600,xaxis[i],20)
plt.plot(xaxis,yaxis,label='blocking probability')
plt.xlabel('value of s')
plt.grid()
plt.legend()
plt.show()"""
