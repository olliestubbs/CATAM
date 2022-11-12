import numpy as np
import matplotlib.pyplot as plt
def E(nu,C):
    term = 1
    sigma = 0
    for i in range(C):
        sigma += term
        term = term*(C-i)/nu
    sigma += term
    return 1/sigma
nu = 600
C= 600
xaxis = np.linspace(0,1,100)
yaxis = np.zeros(100)
for i in range(100):
    yaxis[i]=E(nu+2*nu*xaxis[i]*(1-xaxis[i]),C)
plt.plot(xaxis,xaxis,label='B',color = 'gray',linewidth = 1,linestyle = '--')
plt.plot(xaxis,yaxis,label=r'E($600+2\times600$B(1-B),600)',color = '#a80766')
plt.grid()
plt.legend()
plt.xlabel('B')
plt.show()
