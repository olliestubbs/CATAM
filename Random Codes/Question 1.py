import numpy as np
import time
import matplotlib.pyplot as plt
n=15
m=128

def genHamSpace(n):
    hamSpace = np.zeros((n,2**n))
    Z=np.arange(2**n)
    for i in range(n):
        hamSpace[i]=Z%2**(i+1)>=2**i
    return hamSpace
def genC(hamSpace,r):
    n=np.shape(hamSpace)[0]
    cols = np.random.choice(np.arange(2**n),size=(r),replace=False)
    return hamSpace[:,cols]
def minDist(C):
    shape = np.shape(C)
    r=shape[1]
    minim=shape[0]
    for i in range(int(np.ceil(r/2))):
        rolled = np.roll(C,i+1,axis=1)
        newM=np.logical_xor(C,rolled)
        res = np.sum(newM,axis=0)
        newmin=np.amin(res)
        if newmin<minim:
            minim=newmin
        if minim==1:
            return minim
    return minim
hamSpace = genHamSpace(n)

xaxis=np.arange(2,m+1)
yaxis=np.zeros((m-1))
for i in range(m-1):
    maxd=0
    for j in range(100):
        C=genC(hamSpace,xaxis[i])
        minD=minDist(C)
        if minD>maxd:
            maxd=minD
    yaxis[i]=maxd
plt.plot(xaxis,yaxis,label='largest value of d found by program')
plt.xlabel('size r')
plt.grid()
plt.legend()
plt.show()

