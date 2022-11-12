import numpy as np
import time
import matplotlib.pyplot as plt
def genHamSpace(n):
    hamSpace = np.zeros((n,2**n))
    Z=np.arange(2**n)
    for i in range(n):
        hamSpace[i]=Z%2**(i+1)>=2**i
    return hamSpace
def minWeight(generators):
    shape=np.shape(generators)
    k=shape[1]
    hamSpace=genHamSpace(k)[:,1:]
    weightM=np.matmul(generators,hamSpace)%2
    res = np.sum(weightM,axis=0)
    return np.amin(res)
def genC1(rank,hamSpace):
    shape = np.shape(hamSpace)
    init = np.random.randint(1,high=shape[1])
    C=hamSpace[:,init,None]
    while np.shape(C)[1]<rank:
        init = np.random.randint(1,high=shape[1])
        tryC = np.hstack((C,hamSpace[:,init,None]))
        if minWeight(C):
            C=tryC
        else:
            pass
    return C

def genC2(d,hamSpace):
    shape = np.shape(hamSpace)
    C=np.zeros((shape[0],1))
    basis=np.zeros((shape[0],0))
    order = np.arange(1,shape[1])
    np.random.shuffle(order)
    for i in order:
        col = hamSpace[:,i,None]
        newM=(C+col)%2
        res = np.sum(newM, axis=0)
        if np.amin(res)>=d:
            C=np.hstack((C,newM))
            basis=np.hstack((basis,col))
    return basis
n=25
d=2
hamSpace=genHamSpace(n)
start = time.time()
print(minWeight(genC1(d,hamSpace)))
print(time.time()-start)
