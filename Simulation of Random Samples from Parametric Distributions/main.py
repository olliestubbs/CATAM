import numpy as np
import matplotlib.pyplot as plt
def expo(uniform,theta0,start,end,points):
    expos = (-1/theta0)*np.log(1-uniform)
    print(expos)
    print(np.sum(expos)*np.log(2)/len(uniform))
    ms = np.linspace(start,end,num=points)
    loglik = np.zeros((points))
    for i in range(points):
        gs = (np.log(2)/ms[i])*np.exp((-np.log(2)/ms[i])*expos)
        loglik[i]=np.sum(np.log(gs))
    return [ms,loglik]

def bisector(func,start,end,error):
    lower = func(start)
    upper = func(end)
    for i in range(100):
        if abs(lower)<error:
            return start
        elif abs(upper)<error:
            return end
        else:
            mid = (start+end)/2
            midval = func(mid)
            if midval*lower<=0:
                end=mid
                upper=midval
            else:
                start = mid
                lower = midval
    return 'couldnt find in 1000 iterations'
def gamma(theta0,uniform,xspace):
    gammas = np.zeros(uniform.shape)
    for i in range(uniform.shape[0]):
        found = False
        for j in range(14):
            cgamma = lambda y: 1-(theta0*y+1)*np.exp(-theta0*y)-uniform[i]
            if cgamma(2**j)>0:
                gammas[i]=bisector(cgamma,0,2**j,10**(-6))
                found = True
                break
            else:
                pass
        if not found:
            gammas[i]=2**14
    loglik = np.zeros(xspace.shape[0])
    for i in range(xspace.shape[0]):
        loglik[i]=np.sum(np.log(np.multiply(xspace[i]**2*gammas,np.exp(-xspace[i]*gammas))))
    return [gammas,loglik]
def normal(uniform1,uniform2,mu):
    Phi = np.pi*2*uniform1
    V = -2*np.log(1-uniform2)
    X= mu + np.multiply(np.sqrt(V),np.cos(Phi))
    return X
def chi2(p,n):
    sample = np.zeros((n))
    for i in range(n):
        uniform1 = np.random.rand(p)
        uniform2 = np.random.rand(p)
        X=normal(uniform1,uniform2,0)
        sample[i]=np.sum(np.square(X))
    return sample
#q12

sample=chi2(40,500)
plt.hist(sample,bins='auto')
plt.show()

#question 11 
"""
for i in range(25):
    uniform1= np.random.rand(100)
    uniform2 = np.random.rand(100)
    X = normal(uniform1,uniform2,0)
    mean = np.sum(X)/100
    lower = mean-0.1282
    upper = mean+0.1282
    inside = lower<=0 and upper>=0
    print(str(i)+' mean: '+str(mean)+' lower bound: '+str(lower)+' upper bound '+str(upper)+' inside? '+str(inside))
"""
#question 8
"""
n=10
N=200
estimates=[]
for i in range(N):
    uniform = np.random.rand(n)
    gammas = gamma(2.2,uniform,np.array([1]))[0]
    estimates.append(2*n/np.sum(gammas))
estimates = np.array(estimates)
plt.hist(estimates,bins='auto',range = (1,4))
plt.show()
"""
#question 6-7
"""
n=10
xspace=np.linspace(1,4,100)
uniform = np.random.rand(n)
results = gamma(2.2,uniform,xspace)
gammas = results[0]
loglik = results[1]
print(2*n/np.sum(gammas))
plt.plot(xspace,loglik)
plt.xlabel('m')
plt.ylabel('log likelihood')
plt.show()
"""
#question 1-3
"""
uniform = np.random.rand(100)
results = expo(uniform,1.2,0.25,2,1000)
plt.plot(results[0],results[1])
plt.xlabel('m')
plt.ylabel('log likelihood')
plt.show()"""
