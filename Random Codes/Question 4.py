import numpy as np
import time
import matplotlib.pyplot as plt
import pickle
def genHamSpace(n):
    hamSpace = np.zeros((n,2**n))
    Z=np.arange(2**n)
    for i in range(n):
        hamSpace[i]=Z%2**(i+1)>=2**i
    return hamSpace
def isLinInd(C):
    C=np.copy(C)
    n=C.shape[0]
    k=C.shape[1]
    for i in range(k):
        col=np.copy(C[:,i])
        if np.all(col==0):
            return False
        else:
            sect = C[:,i:k]
            for j in range(n):
                if not np.all(sect[j]==0):
                    nextR=j
                    break
            for j in range(i,k):
                if C[nextR,j]==1:
                    nextC=j
                    break
            C[:,i]=C[:,nextC]
            C[:,nextC]=col
            for j in range(i+1,k):
                if C[nextR,j]:
                    C[:,j]=(1*C[:,j]+C[:,i])%2
                    
    return True
def minWeight(generators):
    shape=np.shape(generators)
    k=shape[1]
    hamSpace=genHamSpace(shape[1])[:,1:]
    weightM=np.matmul(generators,hamSpace)%2
    res = np.sum(weightM,axis=0)
    return np.amin(res)
def randBin(n):
    
    out = np.random.binomial(1,0.5,size=(n,1))
    if not np.all(out==0):
        return out
    else:
        col=randBin(n)
        return col
def genC1(rank,n):
    C=randBin(n)
    while np.shape(C)[1]<rank:
        tryC = np.hstack((C,randBin(n)))
        if isLinInd(tryC):
            C=tryC
        else:
            pass
            
    return C
def genC2(d,n):
    C=np.zeros((n,0))
    for i in range(n):
        col = randBin(n)
        test=np.hstack((C,col))
        if minWeight(test)<d:
            return C
        else:
            C=test
    return C
    

datapoints1=[]
datapoints2=[]
for n in range(10,21):
    roundtime=1
    for j in range(25):
        k=np.random.choice(np.arange(1,n+1))
        start=time.time()
        maxd=0
        while time.time()-start<=roundtime:
            newmax=int(minWeight(genC1(k,n)))
            if newmax>maxd:
                maxd=newmax
        datapoints1.append((n,k,maxd))
        print((n,k,maxd))
        d=np.random.choice(np.arange(1,n+1))
        start = time.time()
        maxr=0
        while time.time()-start<=roundtime:
            newC=genC2(d,n)
            newmax=newC.shape[1]
            if newmax>maxr:
                maxr=newmax
        datapoints2.append((n,maxr,d))
        print(n,maxr,d)
with open('data3.p','wb') as out1:
    pickle.dump(datapoints1,out1)
with open('data4.p','wb') as out2:
    pickle.dump(datapoints2,out2)
