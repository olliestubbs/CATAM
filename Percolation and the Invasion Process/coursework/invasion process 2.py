import numpy as np
import time
start = time.time()
class graph:
    def __init__(self,nodes=None,dimension = 2):
        if nodes == None:
            nodes = {
        }
        self.nodes = nodes
        self.onedge = []
        self.dimension = dimension
    def addEdge(self,node1,node2):
        node1=tuple(node1)
        node2=tuple(node2)
        rand = np.random.random()
        if node1 not in self.nodes:
            if node2 in self.nodes:
                self.nodes[node2].append([node1,rand])
            else:
                print('tried to make edge between non-existant nodes')
        else:
            if node2 in self.nodes:
                pass
            else:
                self.nodes[node1].append([node2,rand])
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
        if node in self.nodes:
            pass
        else:
            unbound = False
            self.nodes[node]=[]
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
                self.onedge.append(node)
    
def addLowest(lowestNodes,newNode,c,filling = False):
    if lowestNodes == [] and filling:
        return [newNode]
    newRand = newNode[1]
    length = len(lowestNodes)
    if length ==c:
        filling = False
    if newRand > lowestNodes[-1][1]:
        if not filling:
            return lowestNodes
        else:
            return lowestNodes+[newNode]
    else:
        for i in range(length-2,-1,-1):
            if newRand >lowestNodes[i][1]:
                newLowest = lowestNodes[0:i+1]+[newNode]+lowestNodes[i+1:c-1]
                return newLowest
        return [newNode]+lowestNodes[0:c-1]

        
main = graph()
main.addNode([0,0])
rands = []
c = 100
checkcount=0
lowestNodes = []
for i in range(70000):
    if lowestNodes != []:
        newNode = list(lowestNodes)[0]
        rands.append(newNode[1])
        main.addNode(newNode[0])
        for node in main.nodes[newNode[0]]:
            lowestNodes = addLowest(lowestNodes,node,c)
        lowestNodes.remove(newNode)
        
    else:
        
        checkcount+=1
        for node in main.onedge:
            for edge in main.nodes[node]:
                lowestNodes = addLowest(lowestNodes,edge,c,filling=True)
end=time.time()
print(max(rands[2000:]))
print(checkcount)
print(end-start)            
                
