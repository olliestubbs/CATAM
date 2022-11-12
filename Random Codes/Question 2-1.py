import numpy as np
import time
import matplotlib.pyplot as plt
n=10
d=2
def genHamSpace(n):
    hamSpace = np.zeros((n,2**n))
    Z=np.arange(2**n)
    for i in range(n):
        hamSpace[i]=Z%2**(i+1)>=2**i
    return hamSpace
hamSpace = genHamSpace(n)
start = time.time()
def genC(hamSpace, d):
    shape = np.shape(hamSpace)
    C=np.zeros((shape[0],1))
    order = np.arange(1,shape[1])
    np.random.shuffle(order)
    for i in order:
        col = hamSpace[:,i,None]
        test = np.tile(col,(1,np.shape(C)[1]))
        newM=(C+test)%2
        res = np.sum(newM, axis=0)
        if np.amin(res)>=d:
            C=np.hstack((C,col))
    return C
hamSpace = genHamSpace(n)
start=time.time()
for i in range(10):
    genC(hamSpace,d)
print(time.time()-start)
"""
xaxis=np.arange(2,n+1)
yaxis=np.zeros((n-1))
for i in range(n-1):
    maxr=0
    for j in range(5):
        trymax=np.shape(genC(hamSpace,i+2))[1]
        if trymax>maxr:
            maxr=trymax
    yaxis[i]=maxr
plt.plot(xaxis,yaxis,label='largest value of r found by program')
plt.grid()
plt.legend()
plt.xlabel('min distance d')
plt.show()"""

