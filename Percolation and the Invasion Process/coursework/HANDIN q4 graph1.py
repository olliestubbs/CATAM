import numpy as np
import matplotlib.pyplot as plt
class graph:
    def __init__(self,nodes=None,dimension = 2,lowestEdges=[],c=20):
        if nodes == None:
            nodes = {
        }
        self.nodes = nodes
        self.onedge = set()
        self.dimension = dimension
        self.c=c
    def addEdge(self,node1,node2):
        node1=tuple(node1)
        node2=tuple(node2)
        rand = np.random.random()
        
        if node1 not in self.nodes[node2]:
            
            self.nodes[node2].append([node1,rand])
            self.nodes[node1].append([node2,rand])
                
    def addNode(self,node):
        node = tuple(node)
        
            
        self.nodes[node]=[]
        for i in range(self.dimension):
            for j in [-1,1]:
                neighbour = list(node)
                neighbour[i]+=j
                neighbour = tuple(neighbour)
                if neighbour in self.nodes:
                    self.addEdge(neighbour,node)
n = 6
grid1 = graph()
grid2 = graph()
for i in range(n+1):
    for j in range(n):
        grid1.addNode(np.array([i,j]))
        grid2.addNode(np.array([j+0.5,i-0.5]))
fig = plt.figure(figsize = (10,10))
axis = fig.add_subplot(1,1,1)
plt.plot([],[],'o',color='#b80802',label='nodes')
plt.plot([],[],color = '#f5a958',label='edges')
plt.plot([],[],'o',color='#1d77a8',label='dual nodes')
plt.plot([],[],color = '#63d4b8',label='dual edges')
for i in grid1.nodes:    
    for j in grid1.nodes[i]:
        plt.plot(np.array([i[0],j[0][0]]),np.array([i[1],j[0][1]]),color = '#f5a958',alpha=0.5)        
    plt.plot(i[0],i[1],'o',color='#b80802')
for i in grid2.nodes:
    
    for j in grid2.nodes[i]:
        plt.plot(np.array([i[0],j[0][0]]),np.array([i[1],j[0][1]]),color = '#63d4b8',alpha =0.5)
    plt.plot(i[0],i[1],'o',color='#1d77a8')
plt.xlim(-1,n+1)
plt.ylim(-1,n)
plt.gca().set_aspect('equal', adjustable='box')
plt.axis('off')
plt.legend()
plt.show()
