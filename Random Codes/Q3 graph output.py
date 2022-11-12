import numpy as np
import matplotlib.pyplot as plt
import pickle
def H(p):
    return -p*np.log2(p)-(1-p)*np.log2(1-p)
with open('data1.p','rb') as in1:
    datapoints1 = pickle.load(in1)
with open('data2.p','rb') as in2:
    datapoints2 = pickle.load(in2)
length1 = len(datapoints1)
xaxis1=np.zeros((length1))
yaxis1=np.zeros((length1))

for i in range(length1):
    point=datapoints1[i]
    xaxis1[i]=(1/point[0])*np.log2(point[1])
    yaxis1[i]=(point[2]-1)/point[0]
    
    
length2 = len(datapoints2)
xaxis2=np.zeros((length2))
yaxis2=np.zeros((length2))

for i in range(length2):
    point=datapoints2[i]
    xaxis2[i]=(1/point[0])*np.log2(point[1])
    yaxis2[i]=(point[2]-1)/point[0]
    
print(len(xaxis1))
xaxis3=np.linspace(0.001,0.5,num=100)
yaxis3=1-H(xaxis3)
yaxis4=np.linspace(0.001,0.99,num=100)
xaxis4=1-H(yaxis4/2)
plt.scatter(xaxis1,yaxis1,label='method 1',alpha=0.3,marker='x')
plt.scatter(xaxis2,yaxis2,label='method 2',alpha=0.2)
plt.plot(yaxis3,xaxis3,color='#e092c6',label='1-H(e)',linestyle='-.')
plt.plot(xaxis4,yaxis4,color='#b8046d',label='1-H(e/2)',linestyle='--')
plt.xlabel('information rate')
plt.ylabel('error-control rate')
plt.grid()
plt.legend()
plt.show()
