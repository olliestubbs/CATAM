import numpy as np
from decimal import Decimal
n=10000000
nu=3
C=6

def E(nu,C):
    term = 1
    sigma = 0
    for i in range(C):
        sigma += term
        term = term*(C-i)/nu
    sigma += term
    return 1/sigma
def empiricalE(nu,C,n):
    uniform = np.random.rand(n)
    arrivals = 0
    cArrivals=0
    y = np.zeros(n)
    y[0]=0
    for i in range(1,n):
        prev = y[i-1]
        if prev == C:
            if uniform[i]<nu/(nu+C):
                y[i]=C
                arrivals+=1
                cArrivals+=1
            else:
                y[i]=C-1
        else:
            if uniform[i]<= nu/(nu+prev):
                y[i]=prev+1
                arrivals+=1
            else:
                y[i]=prev-1
    return(cArrivals/arrivals)
for nu in [1,5,20,80,300,1200]:
    print(f"C&\\hat{{E}}({nu},C)&E({nu},C)\\\\")
    for C in [5,10,20,50,100,200,600]:
        print(f"{C}&{Decimal(empiricalE(nu,C,1000000)):.3E}&{Decimal(E(nu,C)):.3E}\\\\")
    print('')
    
        
