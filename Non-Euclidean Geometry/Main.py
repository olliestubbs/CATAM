import numpy as np
import matplotlib.pyplot as plt
import csv
def findCentre(z1,z2):
    #This function assumes checks have been made to ensure points are not
    #colinear with zero
    numer = (abs(z1)**2-1)*z2-(abs(z2)**2-1)*z1
   
    denom = np.conj(z1)*z2-np.conj(z2)*z1
    
    return numer/denom

def connect(z1,z2,points):
    #produces a vector of complex numbers along the great circle
    #starts from z1 and finishes at z2
    connection = np.zeros((points+1),dtype = complex)
    if z1==0 or abs(np.imag(z2/z1))<10**(-5):
        for i in range(points+1):
            connection[i]=z1+(z2-z1)*i/points
        return connection
    else:
        a = findCentre(z1,z2)
        arg = np.angle((z2-a)/(z1-a))
        anti1 = -1/np.conj(z1)
        anti2 = -1/np.conj(z2)
        antia= findCentre(anti1,anti2)
        antiarg = np.angle((anti2-antia)/(anti1-antia))
        if abs(arg)<=abs(antiarg):
            for i in range(points+1):
                connection[i]=a+(z1-a)*np.exp(1j*i*arg/points)
            return connection
        else:
            
            for i in range(points+1):
                connection[i]=antia+(anti1-antia)*np.exp(1j*i*(antiarg)/points)
            connection = np.conj(connection)
            connection = -np.reciprocal(connection)
            return connection
def polygon(vertices,points):
    number = len(vertices)
    output = np.zeros((points*number),dtype = 'complex')
    for i in range(number):
        output[i*1000:(i+1)*1000]=connect(vertices[i],vertices[(i+1)%number],points)[:points]
    return output
   
def findHypCentre(z1,z2):
    #This function assumes checks have been made to ensure points are not
    #colinear with zero
    numer = (abs(z1)**2+1)*z2-(abs(z2)**2+1)*z1
   
    denom = np.conj(z1)*z2-np.conj(z2)*z1
    
    return numer/denom
def hypConnect(z1,z2,points):
    #produces a vector of complex numbers along the great circle
    #starts from z1 and finishes at z2
    connection = np.zeros((points+1),dtype = complex)
    if z1==0 or abs(np.imag(z2/z1))<10**(-5):
        for i in range(points+1):
            connection[i]=z1+(z2-z1)*i/points
        return connection
    else:
        a = findHypCentre(z1,z2)
        arg = np.angle((z2-a)/(z1-a))
        for i in range(points+1):
            connection[i]=a+(z1-a)*np.exp(1j*i*arg/points)
        return connection
def hypPolygon(vertices,points):
    number = len(vertices)
    output = np.zeros((points*number),dtype = 'complex')
    for i in range(number):
        output[i*1000:(i+1)*1000]=hypConnect(vertices[i],vertices[(i+1)%number],points)[:points]
    return output
def divider(n,points):
    cosa= np.cos(np.pi/3)*np.cos(np.pi/n)/(np.sin(np.pi/3)*np.sin(np.pi/n))
    r = np.tan((1/2)*np.arccos(cosa))
    vertices = np.zeros((n),dtype = 'complex')
    todraw = []
    for i in range(n):
        vertices[i]=r*np.exp(2j*np.pi*i/n)
    midvertices = np.zeros((n),dtype='complex')
    for i in range(n):
        nexti = (i+1)%n
        midvertices[i]=connect(vertices[i],vertices[nexti],2*points)[points]
    todraw.append(polygon(vertices,points))
    for i in range(n):
        todraw.append(connect(0,vertices[i],points))
        todraw.append(connect(0,midvertices[i],points))
    return todraw
def hypDivider(n,points):
    cosha= np.cos(np.pi/3)*np.cos(np.pi/n)/(np.sin(np.pi/3)*np.sin(np.pi/n))
    r = np.tanh((1/2)*np.arccosh(cosha))
    vertices = np.zeros((n),dtype = 'complex')
    todraw = []
    for i in range(n):
        vertices[i]=r*np.exp(2j*np.pi*i/n)
    midvertices = np.zeros((n),dtype='complex')
    for i in range(n):
        nexti = (i+1)%n
        midvertices[i]=hypConnect(vertices[i],vertices[nexti],2*points)[points]
    todraw.append(hypPolygon(vertices,points))
    for i in range(n):
        todraw.append(hypConnect(0,vertices[i],points))
        todraw.append(hypConnect(0,midvertices[i],points))
    return todraw
def pmultiply(M1,M2,p):
    M = np.matmul(M1,M2)
    Mprime = np.mod(M,p)
    return Mprime
def PSLequal(M1,M2,p):
    M1= np.mod(M1,p)
    M2 = np.mod(M2,p)
    if np.all(M1==M2):
        return True
    elif np.all(M1==np.mod(-M2,p)):
        return True
    else:
        return False
def lineInvert(z,theta):
    return(np.exp(2*1j*theta)*np.conj(z))
def circleInvert(z,a,r):
    return(a+r**2*np.reciprocal(np.conj(z)-np.conj(a)))
def rotator(z,z1,a,index,p):
    if index == 0:
        return lineInvert(circleInvert(z,a,abs(z1-a)),np.pi/p)
    elif index == 1:
        return circleInvert(lineInvert(z,0),a,abs(z1-a))
    elif index == 2:
        return lineInvert(lineInvert(z,np.pi/p),0)
    else:
        print('index not in range')
        return False
def triangulator(p,points):
    PSL = [[np.array([[1,0],[0,1]]),[]]]
    operations = [np.array([[0,1],[-1,0]]),np.array([[0,-1],[1,-1]]),np.array([[1,1],[0,1]])]
    for i in range(1000):
        print(len(PSL))
        newPSL=list(PSL)
        finished = True
        for M in PSL:
            for R in range(3):
                inPSL=False
                for K in PSL:
                    if PSLequal(pmultiply(operations[R],M[0],p),K[0],p):
                        inPSL=True
                    else:
                        pass
                if not inPSL and finished:
                    new = [pmultiply(operations[R],M[0],p),list(M[1])]
                    new[1].append(R)
                    newPSL.append(new)
                    finished = False
                    break
            if not finished:
                break
            
        PSL=list(newPSL)
        if finished:
            break
    triangles = []
    if p<6:
        cosa1= np.cos(np.pi/3)*np.cos(np.pi/p)/(np.sin(np.pi/3)*np.sin(np.pi/p))
        r1 = np.tan((1/2)*np.arccos(cosa1))
        cosa2 = (np.cos(np.pi/3)+np.cos(np.pi/2)*np.cos(np.pi/p))/(np.sin(np.pi/2)*np.sin(np.pi/p))
        r2 = np.tan((1/2)*np.arccos(cosa2))
        z1=r1
        z2=r2*np.exp(1j*np.pi/p)
        triangle0=polygon([0,z1,z2],points)
        a = findCentre(z1,z2)
    else:
        cosha1= np.cos(np.pi/3)*np.cos(np.pi/p)/(np.sin(np.pi/3)*np.sin(np.pi/p))
        r1 = np.tanh((1/2)*np.arccosh(cosha1))
        cosha2 = (np.cos(np.pi/3)+np.cos(np.pi/2)*np.cos(np.pi/p))/(np.sin(np.pi/2)*np.sin(np.pi/p))
        r2 = np.tanh((1/2)*np.arccosh(cosha2))
        z1=r1
        z2=r2*np.exp(1j*np.pi/p)
        triangle0=hypPolygon([0,z1,z2],points)
        a = findHypCentre(z1,z2)
    for i in PSL:
        newtriangle = np.array(triangle0)
        
        for k in i[1]:
            
            newtriangle = rotator(newtriangle,z1,a,k,p)
        triangles.append(newtriangle)
        
    return [triangles,PSL]
    



#vector = hypPolygon([-0.8j,0.75,-0.8],1000)
#all the following code is to plot a nice argand diagram
#todraw = hypDivider(24,1000)

fig = plt.figure(figsize = (10,10))
axis = fig.add_subplot(1,1,1)
axis.spines['left'].set_position('zero')
axis.spines['bottom'].set_position('zero')
axis.spines['top'].set_color('none')
axis.spines['right'].set_color('none')
#plt.plot(np.real(vector),np.imag(vector))
triang = triangulator(5,1000)
print(triang[1])
triangles=triang[0]
for i in range(len(triangles)):
    centrex=np.mean(np.real(triangles[i]))
    centrey=np.mean(np.imag(triangles[i]))
    plt.text(centrex-0.01,centrey-0.01,str(i+1),size = 'xx-small')
    
    if i<167:
        plt.plot(np.real(triangles[i]),np.imag(triangles[i]),color='b')
        plt.fill(np.real(triangles[i]),np.imag(triangles[i]),color='#add8e6')
    else:
        plt.plot(np.real(triangles[i]),np.imag(triangles[i]),color='r')
        plt.fill(np.real(triangles[i]),np.imag(triangles[i]),color='r')
#plt.plot(np.real(newvec),np.imag(newvec))
#for i in todraw:
    #plt.plot(np.real(i),np.imag(i),color = 'b')
autox = plt.xlim()
autoy = plt.ylim()


most = min(max(abs(autox[0]),abs(autox[1]),abs(autoy[0]),abs(autoy[1])),5)

plt.xlim(-most,most)
plt.ylim(-most,most)
majorticks = np.arange(-np.floor(most),np.floor(most)+1,1)
majorticks=majorticks[majorticks!=0]
minorticks = np.arange(-np.floor(most),np.floor(most)+0.25,0.25)
minorticks=minorticks[minorticks!=0]
plt.gca().set_aspect('equal', adjustable='box')

axis.set_yticks(minorticks,minor=True)
axis.set_xticks(minorticks,minor=True)
axis.set_yticks(majorticks)
axis.set_axisbelow(True)
axis.set_xticks(majorticks)
axis.grid(which='minor',color = '#EEEEEE')
axis.grid()

#adds circle for hyperbolic disc
ticks = np.linspace(0.01,2*np.pi,1000)
#circle = np.exp(1j*ticks)
#plt.plot(np.real(circle),np.imag(circle),color='black')
#plt.fill(np.real(vector),np.imag(vector),color='#add8e6')
plt.show()
