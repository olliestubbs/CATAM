import numpy as np
import matplotlib.pyplot as plt
import time
np.random.seed(1)
start = time.time()
class graph:
    def __init__(self,nodes=None,dimension = 2,lowestEdges=[],c=20):
        if nodes == None:
            nodes = {
        }
        self.nodes = nodes
        self.onedge = set()
        self.dimension = dimension
        self.lowestEdges=lowestEdges
        self.c=c
    def addLowest(self,newNode,filling = False):
        if self.lowestEdges == []:
            if filling:
                self.lowestEdges = [newNode]
                return None
            else:
                return None
        newRand = newNode[1]
        length = len(self.lowestEdges)
        if length ==self.c:
            filling = False
        if newRand > self.lowestEdges[-1][1]:
            if not filling:
                pass
            else:
                self.lowestEdges= self.lowestEdges+[newNode]
                return None
        else:
            for i in range(length-2,-1,-1):
                if newRand >self.lowestEdges[i][1]:
                    self.lowestEdges = self.lowestEdges[0:i+1]+[newNode]+self.lowestEdges[i+1:self.c-1]
                    return None
            self.lowestEdges=[newNode]+self.lowestEdges[0:self.c-1]
            return None
    def addEdge(self,node1,node2):
        node1=tuple(node1)
        node2=tuple(node2)
        rand = np.random.random()
        if node1 not in self.nodes:
            if node2 in self.nodes:
                self.nodes[node2].append([node1,rand])
                self.addLowest([node1,rand],c)
                
            else:
                print('tried to make edge between non-existant nodes')
        else:
            if node2 in self.nodes:
                pass
            else:
                self.nodes[node1].append([node2,rand])
                self.addLowest([node2,rand])
    def removeEdge(self,node1,node2):
        node1=tuple(node1)
        node2=tuple(node2)
        for i in range(len(self.nodes[node1])):
            if self.nodes[node1][i][0]==node2:
                
                del self.nodes[node1][i]
                return None
            else:
                pass
    def addNode(self,node):
        node = tuple(node)
        if self.nodes.get(node,False):
            print('hm')
        else:
            unbound = False
            self.nodes[node]=[]
            for j in range(len(self.lowestEdges)-1,-1,-1):
                if self.lowestEdges[j][0]==node:
                    del self.lowestEdges[j]
            for i in range(self.dimension):
                for j in [-1,1]:
                    neighbour = list(node)
                    neighbour[i]+=j
                    neighbour = tuple(neighbour)
                    if neighbour in self.nodes:
                        self.removeEdge(neighbour,node)
                        if self.nodes[neighbour]==[]:
                            self.onedge.remove(neighbour)
                    else:
                        self.addEdge(node,neighbour)
                        unbound = True
            if unbound:
                self.onedge.add(node)
    

        

def invade(n):
    main = graph(c=100)
    main.addNode([0,0])
    rands = []

    checkcount=0
    i=0
    while i < n:
        if main.lowestEdges != []:
            i+=1
            newNode = list(main.lowestEdges)[0]
            rands.append(newNode[1])
            main.addNode(newNode[0])
        
        
        else:
        
            checkcount+=1
            for node in main.onedge:
                for edge in main.nodes[node]:
                    main.addLowest(edge,filling=True)
    return rands
results = []
hd = 1000
for i in range(30):
    print(i)
    rands = invade(10000)
    sup = np.amax(rands)
    template = np.zeros(hd)
    for j in range(hd):
        if j/hd<sup:
            pass
        else:
            template[j]=1
    results.append(np.array(template))
results = np.array(results)
yaxis = np.average(results, axis=0)
xaxis = np.linspace(0,1,len(yaxis))
plt.xticks(ticks = np.array([0,0.25,0.5,0.75,1]))
plt.xlabel('p')
plt.ylabel(r'$\theta_p$')
plt.grid()
plt.plot(xaxis,yaxis)
plt.show()
           
                
