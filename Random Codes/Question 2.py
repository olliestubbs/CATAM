import numpy as np
import time
import matplotlib.pyplot as plt
n=12
d=4
def randBin(n):
    
    out = np.random.binomial(1,0.5,size=(n,1))
    if not np.all(out==0):
        return out
    else:
        return randBin(n)
start = time.time()
def genC(n, d):
    C=np.zeros((n,1))
    for i in range(2**n):
        col = randBin(n)
        M=(C+col)%2
        res=np.sum(M,axis=0)
        if np.amin(res)<d:
            return C
        else:
            C=np.hstack((C,col))
xaxis=np.arange(2,n+1)
yaxis=np.zeros((n-1))
for i in range(n-1):
    maxr=0
    for j in range(100):
        trymax=np.shape(genC(n,i+2))[1]
        if trymax>maxr:
            maxr=trymax
    yaxis[i]=maxr
plt.plot(xaxis,yaxis,label='largest value of r found by program')
plt.grid()
plt.legend()
plt.xlabel('min distance d')
plt.show()
