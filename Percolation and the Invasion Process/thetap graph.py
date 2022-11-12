import numpy as np
import matplotlib.pyplot as plt
xaxis = np.linspace(0,1,1000)
yaxis = np.zeros((1000))
for i in range(1000):
    p = xaxis[i]
    if p<=0.5:
        phi=0
    else:
        phi=(2*p-1)/p**2
    yaxis[i]=3*p*phi-3*p**2*phi**2+p**3*phi**3
plt.plot(xaxis,yaxis)
plt.xlabel(r'$p$')
plt.ylabel(r'$\theta_p$')
plt.grid()
plt.show()
