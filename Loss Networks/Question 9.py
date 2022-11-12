import numpy as np

def E(nu,C):
    term = 1
    sigma = 0
    for i in range(C):
        sigma += term
        term = term*(C-i)/nu
    sigma += term
    return 1/sigma
def binarySearch(func,low,high,n):
    flow = func(low)
    fhigh = func(high)
    if flow*fhigh>=0:
        return 'bad starting region'
    for i in range(n):
        mid = (low+high)/2

        fmid=func(mid)
        if flow*fmid<=0:
            high=mid
            fhigh=fmid
        else:
            low=mid
            flow=fmid
    return mid
def f(B):
    return E(560+2*560*B*(1-B),600)-B
B=binarySearch(f,0.15,0.2,100)
print(2*B**2-B**3)
