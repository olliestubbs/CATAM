import numpy as np
import math
import matplotlib.pyplot as plt
np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})
def forwardEuler(startx,starty,steps,interval,fxy,truth = None, log = False):
    output = np.zeros((2,steps+1))
    output[0][0]=startx
    output[1][0]=starty
    for i in range(1,steps+1):
        output[0][i]=startx+i*interval
        output[1][i]=output[1][i-1]+interval*fxy(output[0][i-1],output[1][i-1])
    if truth == None:
        pass
    else:
        correctOutput=np.zeros((2,steps+1))
        correctOutput[0][0]=startx
        for i in range(1,steps+1):
            correctOutput[0][i]=startx+i*interval
        correctOutput[1]=truth(correctOutput[0])
        vec = output[1]-correctOutput[1]
        
        matrix = np.vstack((correctOutput[1],vec))
       
        output =np.vstack((output,matrix))
        if log:
            logged = np.zeros((1,steps+1))
            for i in range(steps+1):
                if vec[i]==0:
                    logged[0,i]=13
            
                elif i ==0:
                    pass
                else:
                    logged[0,i]=np.log(abs(vec[i]))/(i*interval)
            output = np.vstack((output,logged))
                    
    
    return output
def rungeKutta(startx,starty,steps,interval,fxy):
    output = np.zeros((2,steps+1))
    output[0][0]=startx
    output[1][0]=starty
    for i in range(1,steps+1):
        output[0][i]=startx+i*interval
        xn=output[0][i-1]
        yn = output[1][i-1]
        k1 = interval*fxy(xn,yn)
        k2 = interval*fxy(xn+(1/2)*interval,yn+(1/2)*k1)
        k3 = interval*fxy(xn+(1/2)*interval,yn+(1/2)*k2)
        k4 = interval*fxy(xn+interval,yn+k3)
        output[1][i]=yn+(1/6)*(k1+2*k2+2*k3+k4)
    return output
    
def func5a(x,y):
    output = -4*y+4*np.exp(-2*x)
    return output
def func5aTruth(x):
    return (-2*np.exp(-4*x)+2*np.exp(-2*x))
def func8a(x,y):
    output = 4*y-5*np.exp(-x)
    return output
def func8aTruth(x):
    return np.exp(-x)
#first graph
"""results1 = forwardEuler(0,0,15,0.4,func5a)
results2 = rungeKutta(0,0,15,0.4,func5a)
xaxis = np.linspace(0,6,1000)
yaxis = func5aTruth(xaxis)
plt.plot(xaxis,yaxis,color = 'black')
plt.plot(results1[0],results1[1],'--',color = 'red',marker = 'o')
plt.plot(results2[0],results2[1],'--',color = 'blue',marker = 'o')"""

#second graph
"""
xaxis = np.zeros(16)
euleryaxis=np.zeros(16)
rkyaxis = np.zeros(16)
correct = func5aTruth(1.6)
for i in range(16):
    h=1.6/(2**(15-i))
    xaxis[i]=h
    euleryaxis[i]=abs(forwardEuler(0,0,2**(15-i),h,func5a)[1,-1]-correct)
    rkyaxis[i]=abs(rungeKutta(0,0,2**(15-i),h,func5a)[1,-1]-correct)

plt.loglog(xaxis,euleryaxis,marker='o')
plt.loglog(xaxis,rkyaxis,marker='o',color = 'red')
plt.xlabel('h')
plt.ylabel('error at x=1.6')
plt.show()
"""
print(forwardEuler(0,1,1000000,0.00001,func8a,truth = func8aTruth,log=True))
