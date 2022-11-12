import numpy as np
import time
np.random.seed(1)
class G:
    def __init__(self,n,p,k=None,errors=True):
        self.n=n
        self.p=p
        self.k=k
        self.nodes ={}
        self.colours = {}
        self.nodecolours={}
        for i in range(n):
            self.colours[i]=None
            self.nodes[i]=set()
            self.nodecolours[i]=set()
        for i in range(n):
            for j in range(i):
                if i==j or (k and i%k==j%k):
                    pass
                elif np.random.binomial(1,p):
                    self.nodes[i].add(j)
                    self.nodes[j].add(i)
    def colour(self,node,c):
        self.colours[node]=c
        for i in self.nodes[node]:
            self.nodecolours[i].add(c)
    def clearColours(self):
        self.colours = {}
        self.nodecolours={}
        for i in range(self.n):
            self.colours[i]=None
            self.nodecolours[i]=set()
    def greedy(self, order = None):
        n = self.n
        if order == None:
            order = []
            for i in range(n):
                order.append(i)
        for i in order:
            if self.colours[i]!=None:
                pass
            else:
                cant=self.nodecolours[i]
                for j in range(n):
                    if j not in cant:
                        self.colour(i,j)
                        break
                
                    
def subgraph(graph,nodes):
    sub = {}
    for i in nodes:
        sub[i]=nodes.intersection(graph[i])
    return sub
def clique(graph,k):
    output = None
    if k<=0:
        output = {next(iter(graph.keys())):set()}
        k=1
    for node in graph:
        if len(graph[node])<=k-1:
            pass
        else:
            best = clique(subgraph(graph,graph[node]),k-1)
            if best[0]:
                output = subgraph(graph,set(best[0].keys()).union(set([node])))
                k=best[1]+1
    return [output,k]

graph = G(2000,0.75,k=3)
print(clique(graph.nodes,0)[1])


