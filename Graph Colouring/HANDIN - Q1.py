import numpy as np
import matplotlib.pyplot as plt
import time
import random
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
    def greedyColour(self, order = None):
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
def orderByDegree(graph):
    order = []
    degrees = {}
    n=len(graph)
    for i in graph.keys():
        degree = len(graph[i])
        if degree in degrees:
            degrees[degree].add(i)
        else:
            degrees[degree]=set([i])
    for degree in range(n-1,-1,-1):
        if degree in degrees:
            for j in degrees[degree]:
                order.append(j)
        else:
            pass
    return order
graphs = []
for i in range(10):
    graphs.append(G(70,0.5))
results = []
for graph in graphs:
    indiv = []
    order1 = orderByDegree(graph.nodes)
    order2 = order1[::-1]
    order3 = []
    sub = graph.nodes
    n=len(sub)
    for i in range(n):
        lowest = orderByDegree(sub)[-1]
        vertices = set(sub.keys())
        vertices.remove(lowest)
        order3.append(lowest)
        sub = subgraph(graph.nodes,vertices)
    order3.reverse()
    order4 = random.shuffle(order1)
    graph.greedyColour(order = order1)
    indiv.append(max(set(graph.colours.values())))
    graph.clearColours()
    graph.greedyColour(order = order2)
    indiv.append(max(set(graph.colours.values())))
    graph.clearColours()
    graph.greedyColour(order = order3)
    indiv.append(max(set(graph.colours.values())))
    graph.clearColours()
    graph.greedyColour(order = order4)
    indiv.append(max(set(graph.colours.values())))
    graph.clearColours()
    results.append(indiv)
total =[0]*4
for i in range(4):
    for j in range(10):
        total[i]+=results[j][i]
    total[i]=total[i]/10
results.append(total)
results=np.array(results)+1
for i in range(10):
    print(str(i+1)+'&'+str(results[i][0])+'&'+str(results[i][1])+'&'+str(results[i][2])+'&'+str(results[i][3])+'\\\\')
print('average'+'&'+str(results[10][0])+'&'+str(results[10][1])+'&'+str(results[10][2])+'&'+str(results[10][3])+'\\\\')
plt.boxplot(results[0:10],usermedians=results[10])
plt.xlabel('Ordering for greedy colouring')
plt.ylabel('number of colours used')
plt.show()
