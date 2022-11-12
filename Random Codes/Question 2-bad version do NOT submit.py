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
    for i in range(2**n):
        shape = np.shape(hamSpace)
        toDelete = []
        for j in range(shape[1]):
            test = np.tile(hamSpace[:,j,None],(1,np.shape(C)[1]))
            newM=np.logical_xor(C,test)
            res = np.sum(newM,axis=0)
            if np.amin(res)<d:
                toDelete.append(j)
        toDelete=np.array(toDelete)
        hamSpace=np.delete(hamSpace,toDelete,axis=1)
        if hamSpace.size==0:
            return C
        else:
            length=np.shape(hamSpace)[1]
            randint=np.random.randint(length)
            newCol=hamSpace[:,randint,None]
            C=np.hstack((C,newCol))
hamSpace = genHamSpace(n)
start = time.time()
for i in range(10):
    genC(hamSpace,d)
end=time.time()
print(end-start)
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
plt.show()
"""
