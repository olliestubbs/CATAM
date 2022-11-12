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
def genC1(hamSpace,r):
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
def randBin(n):
    
    out = np.random.binomial(1,0.5,size=(n,1))
    if not np.all(out==0):
        return out
    else:
        return randBin(n)
start = time.time()
def genC2(n, d):
    C=np.zeros((n,1))
    for i in range(2**n):
        col = randBin(n)
        M=(C+col)%2
        res=np.sum(M,axis=0)
        if np.amin(res)<d:
            return C
        else:
            C=np.hstack((C,col))
datapoints1=[]
datapoints2=[]
for n in range(10,21):
    roundtime=1
    hamSpace=genHamSpace(n)
    for j in range(25):
        r=int(np.ceil(2**(n*np.random.uniform())))
        start=time.time()
        maxd=0
        while time.time()-start<=roundtime:
            newmax=minDist(genC1(hamSpace,r))
            if newmax>maxd:
                maxd=newmax
        datapoints1.append((n,r,maxd))
        print((n,r,maxd))
        d=np.random.choice(np.arange(1,n+1))
        start = time.time()
        maxr=0
        while time.time()-start<=roundtime:
            newmax=np.shape(genC2(n,d))[1]
            if newmax>maxr:
                maxr=newmax
        datapoints2.append((n,maxr,d))
        print(n,maxr,d)
with open('data1.p','wb') as out1:
    pickle.dump(datapoints1,out1)
with open('data2.p','wb') as out2:
    pickle.dump(datapoints2,out2)
    
    
