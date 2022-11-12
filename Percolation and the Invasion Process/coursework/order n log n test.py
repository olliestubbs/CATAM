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
    

        

def runTest(nodes):
    main = graph(c=100)
    main.addNode([0,0])
    rands = []
    count = 1
    checkcount=0
    while count < nodes:
        if main.lowestEdges != []:
            count+=1
            newNode = list(main.lowestEdges)[0]
            rands.append(newNode[1])
            main.addNode(newNode[0])
        else:
            checkcount+=1
            for node in main.onedge:
                for edge in main.nodes[node]:
                    main.addLowest(edge,filling=True)
    return checkcount
xaxis=[]
ylist=[]
for i in range(1,16):
    xaxis.append(i*10000)
    yaxis=[]
    for j in range(12):
        start = time.time()
        print(runTest(i*10000))
        end = time.time()
        yaxis.append(end-start)
    ylist.append(list(yaxis))
fig, ax = plt.subplots()
ax.boxplot(ylist)
ax.set_xticklabels(xaxis)
ax.set_xlabel('Number of vertices invaded')
ax.set_ylabel('Time')
plt.show()
    

           
                
