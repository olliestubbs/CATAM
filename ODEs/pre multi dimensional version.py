import numpy as np
import math
import matplotlib.pyplot as plt
import time
def forwardEuler(startx,starty,steps,interval,fxy,truth = None, log = False):
    #initialise array with correct start values
    output = np.zeros((2,steps+1))
    output[0][0]=startx
    output[1][0]=starty
    for i in range(1,steps+1):
        #use the forward euler method iteratively
        output[0][i]=startx+i*interval
        output[1][i]=output[1][i-1]+interval*fxy(output[0][i-1],output[1][i-1])
    if truth == None:
        pass
    else:
        #This section adds an array of true values and errors to the output
        correctOutput=np.zeros((2,steps+1))
        correctOutput[0][0]=startx
        for i in range(1,steps+1):
            correctOutput[0][i]=startx+i*interval
        correctOutput[1]=truth(correctOutput[0])
        vec = output[1]-correctOutput[1]
        
        matrix = np.vstack((correctOutput[1],vec))
       
        output =np.vstack((output,matrix))
        if log:
            #adds the log of the errors to the output
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
    #initialise correctly sized array with correct initial values
    output = np.zeros((2,steps+1))
    output[0][0]=startx
    output[1][0]=starty
    for i in range(1,steps+1):
        #perform Runge-Kutta iteration
        output[0][i]=startx+i*interval
        xn=output[0][i-1]
        yn = output[1][i-1]
        k1 = interval*fxy(xn,yn)
        k2 = interval*fxy(xn+(1/2)*interval,yn+(1/2)*k1)
        k3 = interval*fxy(xn+(1/2)*interval,yn+(1/2)*k2)
        k4 = interval*fxy(xn+interval,yn+k3)
        output[1][i]=yn+(1/6)*(k1+2*k2+2*k3+k4)
    return output
def rungeKuttaMulti(startx,starty,steps,interval,dimension,fxy,p,truth = None):
    #almost the same as Runge-Kutta with slight modifications to include
    #a dimension argument
    xoutput = np.zeros((steps +1))
    youtput = np.zeros((steps+1,dimension))
    xoutput[0]=startx
    youtput[0]=starty
    for i in range(1,steps+1):
        xoutput[i]=startx+i*interval
        xn=xoutput[i-1]
        yn = youtput[i-1]
        k1 = interval*fxy(xn,yn,p)
        k2 = interval*fxy(xn+(1/2)*interval,yn+(1/2)*k1,p)
        k3 = interval*fxy(xn+(1/2)*interval,yn+(1/2)*k2,p)
        k4 = interval*fxy(xn+interval,yn+k3,p)
        youtput[i]=yn+(1/6)*(k1+2*k2+2*k3+k4)
    if truth == None:
        return [xoutput,youtput]
    else:
        #this section is copied from the forwardEuler function
        #It adds the correct values and errors to the output
        correctOutput=np.zeros((2,steps+1))
        correctOutput[0][0]=startx
        for i in range(1,steps+1):
            correctOutput[0][i]=startx+i*interval
        correctOutput[1]=truth(correctOutput[0],p)
        vec = youtput[:,0]-correctOutput[1]
        
        matrix = np.vstack((correctOutput[1],vec))
       
        return [xoutput,youtput,matrix]
    return [xoutput,youtput]

def RK4estimate(p,n):
    return rungeKuttaMulti(0,np.array([0,1]),n,(1/n),2,func16,p)[1][n][0]
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
def func16(x,y,p):
    output=np.zeros(2)
    output[0]=y[1]
    output[1] = -p**2*(1+x)**(-8)*y[0]

    return output
def func16Truth(x,p):
    return -(1/p)*(1+x)*np.sin(p*(1+x)**(-1)-p)
def falsePosition(left,right,func,error,n):
    #starts by evaluating each boundary
    lefteval = func(left,n)
    righteval = func(right,n)
    iterates = []
    for i in range(100):
        #If more than 100 iterations have taken place stop
        #then check if either boundary is within the given error
        if abs(lefteval)<error:
            
            iterates.append(left)
            return(iterates)
        elif abs(righteval)<error:
            
            iterates.append(right)
            return(iterates)
        else:
            #calculate the 'middle' value p*
            middle = (righteval*left - lefteval*right)/(righteval-lefteval)
            iterates.append([middle,abs(middle-2*np.pi)])
            middleeval = func(middle,n)
            if middleeval*lefteval<0:
                #if sign difference is with left side set right boundary
                #to the middle value
                right = middle
                righteval = middleeval
            else:
                #otherwise set left boundary to middle value
                left = middle
                lefteval = middleeval
def eigenvalueFinder(func,error,number,spacing,roughn,precisen):
    #timer to ensure program does not run for too long
    start_time = time.time()
    finished = False
    #initialise array for values where sign changes
    lefts = np.zeros((number,2))
    #set initial left boundary to start point
    left = spacing
    lefteval = func(left,roughn)
    count = 0
    while not finished:
        #calculate right boundary and evaluate function there
        right = left+spacing
        righteval = func(right,roughn)
        if lefteval*righteval<=0:
            #check whether there is sign change
            #if yes, add left value to array
            grad = abs((righteval-lefteval)/spacing)
            lefts[count,0]=left
            lefts[count,1]=grad
            count+=1
            if count >=number:
                #check whether we have reached five
                #sign changes
                finished = True
            else:
                
                pass
        else:
            #otherwise keep looking
            pass
        #then make new left boundary previous
        #right boundary
        left = right
        lefteval = righteval
        
        if time.time() - start_time > 30:
            finished = True
        else:
            pass
    #now we have sign changes, perform false position search
    #with boundary at the values with the opposite sign
    results = np.zeros((5))
    for i in range(5):
        results[i] = falsePosition(lefts[i,0],lefts[i,0]+spacing,func,error*(0.1*lefts[i,1]),precisen)[-1]
    return results
"""eigenvalues = eigenvalueFinder(RK4estimate,5*10**(-6),5,1,100,10000)
print(eigenvalues)
print('found values, doing graphs now')
xaxis = np.zeros((101))
for i in range(101):
    x=i*0.01
    xaxis[i]=x
for i in range(5):
   yaxis=rungeKuttaMulti(0,np.array([0,1]),100,0.01,2,func16,eigenvalues[i])[1][:,0]
   squared = np.square(yaxis)
   integral = np.trapz(squared,x=xaxis)
   root = np.sqrt(integral)
   yaxis = yaxis*(1/root)
   plt.plot(xaxis,yaxis,label = 'eigenfunction for p='+"{:.2f}".format(eigenvalues[i]))
   print('done ',i)
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc = 'upper left')
plt.ylim(top = 3)
plt.show()"""

#first graph
"""
results1 = forwardEuler(0,0,15,0.4,func5a)
results2 = rungeKutta(0,0,15,0.4,func5a)
xaxis = np.linspace(0,6,1000)
yaxis = func5aTruth(xaxis)
plt.plot(xaxis,yaxis,color = 'black', label = 'true solution')
plt.plot(results1[0],results1[1],'--',color = 'red',marker = 'o',label = 'forward Euler')
plt.plot(results2[0],results2[1],'--',color = 'blue',marker = 'o', label = 'RK4')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
print(results2)
plt.show()"""
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
print(xaxis)
print(rkyaxis)
plt.loglog(xaxis,euleryaxis,marker='o', label = 'Euler method')
plt.loglog(xaxis,rkyaxis,marker='o',color = 'red', label = 'RK4 method')
plt.xlabel('h')
plt.ylabel('error at x=1.6')
plt.legend(loc = 'upper left')
plt.show()
"""
print(forwardEuler(0,1,10000,0.001,func8a,truth = func8aTruth,log=True)[:,:5])
"""for i in range(13):
    h = 0.1/(2**i)
    steps = 10*(2**i)
    values = rungeKuttaMulti(0,np.array([0,1]),steps,h,2,func16,7,truth = func16Truth)
    print(h,values[1][steps][0],values[2][1][steps])"""

"""xaxis = []
yaxis1 = []
yaxis2 = []
for i in range(13):
    h = 0.1/(2**i)
    steps = 10*(2**i)
    values6 = rungeKuttaMulti(0,np.array([0,1]),steps,h,2,func16,6,truth = func16Truth)
    values7 = rungeKuttaMulti(0,np.array([0,1]),steps,h,2,func16,7,truth = func16Truth)
    xaxis.append(h)
    yaxis1.append(abs(values6[2][1][steps]))
    yaxis2.append(abs(values7[2][1][steps]))
plt.loglog(xaxis,yaxis1,marker='o',label = 'p=6')
plt.loglog(xaxis,yaxis2,marker='o',color='red',label = 'p=7')
plt.xlabel('h')
plt.ylabel('absolute error at x=1')
plt.legend(loc = 'upper left')
plt.show()"""
#
"""xaxis = []
yaxis = []
for i in range(50):
    p = 0.1+i/5
    xaxis.append(p)
    y = rungeKuttaMulti(0,np.array([0,1]),1000,0.001,2,func16,p)[1][1000][0]
    yaxis.append(y)
plt.plot(xaxis,yaxis,marker = 'x')
plt.xlabel('value of p')
plt.ylabel('g(p) with h 0.001')
plt.grid()
plt.show()"""
#
"""
yvalues = []
y1 = rungeKuttaMulti(0,np.array([0,1]),160,0.00625,2,func16,6)[1][160][0]
for i in range(1000):
    p = 6+0.001*i
    y2 = rungeKuttaMulti(0,np.array([0,1]),160,0.00625,2,func16,p+0.001)[1][160][0]
    yvalues.append((y2-y1)*1000)
    y1=y2
print(max(yvalues),min(yvalues))"""
#q9 graph
"""
xaxis = []
yaxis = []
for i in range(300):
    xaxis.append(i*0.2)
    yaxis.append(RK4estimate(i*0.2,40))
plt.plot(xaxis,yaxis)
plt.xlabel('p')
plt.ylabel('g(p)')
plt.grid()
plt.show()"""
#
"""
xaxis =np.linspace(0.4,2.5)
yaxis = np.divide(np.log(4*xaxis-1),xaxis)
plt.plot(xaxis,yaxis,label = 'value of ln(4h-1)/h')
plt.plot([0.4,0.5,0.6,1,2],[-1.242,0.032,0.589,1.123,0.984],'o',color = 'black',label='observed value of ln|\u03B5|/x at x=12')
plt.xlabel('h')
plt.grid()
plt.legend(loc='lower right')
plt.show()"""
    
