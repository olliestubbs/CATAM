import numpy as np
import matplotlib.pyplot as plt
import random
n=5000000
network = {}
K=5
nu=560
C=600
for i in range(K):
    for j in range(K):
        if i<j:
            network[frozenset([i,j])]=[0,[]]
cumulative=np.zeros(n)
times = np.zeros(n)
load = 0
rands = np.random.rand(n,2)
for i in range(1,n):
    if rands[i][0]<load/(load+nu*K*(K-1)/2):
        customer = np.random.randint(1,load+1)
        num = 0
        for j in network.keys():
            size=len(network[j][1])
            if customer<=num+size:
                
                custs=network[j][1]
                for k in custs[customer-num-1]:
                    network[k][0]=network[k][0]-1
                    load=load-1
                network[j][1]=custs[:customer-num-1]+custs[customer-num:]
                
                break
            num+=size
        cumulative[i]=cumulative[i-1]
        times[i]=times[i-1]-np.log(rands[i][1])/load
    else:
        link = random.choice(list(network.keys()))
        if network[link][0]<C:
            load+=1
            network[link][0]=network[link][0]+1
            network[link][1].append([link])
            cumulative[i]=cumulative[i-1]
        else:
            others = list(range(K))
            for j in link:
                others.remove(j)
            other = random.choice(others)
            isOpen = True
            links=[]
            for j in link:
                newLink = frozenset([other,j])
                links.append(newLink)
                if network[newLink][0]==C:
                    isOpen=False
                    
            if isOpen:
                load+=2
                
                for j in links:
                    network[j][0]=network[j][0]+1
                network[link][1].append(links)
                cumulative[i]=cumulative[i-1]
            else:
                cumulative[i]=cumulative[i-1]+1
        times[i]=times[i-1]-np.log(rands[i][1])/(K*(K-1)*nu/2)

plt.plot(times,cumulative,label='cumulative blocked calls')
plt.xlabel('time')
plt.legend()
plt.grid()
plt.show()
