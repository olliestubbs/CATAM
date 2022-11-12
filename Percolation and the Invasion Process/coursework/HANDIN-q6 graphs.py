import numpy as np
import time
import matplotlib.pyplot as plt
np.random.seed(1)

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
    

        
main = graph(c=3)
main.addNode([0,0])
rands = []
count = 1
while count < 14:
    
    if main.lowestEdges != []:
        count+=1
        newNode = list(main.lowestEdges)[0]
        rands.append(newNode[1])
        main.addNode(newNode[0])
    else:
        for node in main.onedge:
            for edge in main.nodes[node]:
                main.addLowest(edge,filling=True)
fig = plt.figure(figsize = (10,10))
axis = fig.add_subplot(1,1,1)
plt.plot([],[],'o',color='#b80802',label='invaded nodes')
plt.plot([],[],'o',color='#f7fa69',label='stored \'highest potential\' nodes')
plt.plot([],[],color = '#f5a958',label='potential edges')
for i in main.nodes:
    
    for j in main.nodes[i]:
        plt.plot(np.array([i[0],j[0][0]]),np.array([i[1],j[0][1]]),color = '#f5a958')
        plt.text((i[0]+j[0][0])/2-0.3,(i[1]+j[0][1])/2,str(j[1])[:4])
    plt.plot(i[0],i[1],'o',color='#b80802')
for i in main.lowestEdges:
    plt.plot(i[0][0],i[0][1],'o',color='#f7fa69')
plt.xlim(-4,4)
plt.ylim(-4,4)
plt.gca().set_aspect('equal', adjustable='box')
ticks = np.linspace(-3,3,1)
plt.grid()
plt.legend()
plt.show()

           
                
