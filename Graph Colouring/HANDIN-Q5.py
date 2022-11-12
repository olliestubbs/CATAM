import numpy as np
import matplotlib.pyplot as plt
import time
import random
np.random.seed(1)
def subgraph(graph,nodes):
    sub = {}
    for i in nodes:
        sub[i]=nodes.intersection(graph[i])
    return sub
def clique(graph,k):
    output = None
    newGraph=graph.copy()
    if k<=0:
        output = {next(iter(newGraph.keys())):set()}
        k=1
    for node in graph.keys():
        if len(graph[node])<=k-1:
            pass
        else:
            best = clique(subgraph(newGraph,newGraph[node]),k-1)
            if best[0]:
                output = subgraph(newGraph,set(best[0].keys()).union(set([node])))
                k=best[1]+1
        newGraph = subgraph(newGraph,set(newGraph.keys())-set([node]))
    return [output,k]
def dual(graph):
    n = set(graph.keys())
    newGraph=graph.copy()
    for node in newGraph:
        newGraph[node]=(n-newGraph[node])-set([node])
    return newGraph
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
    def cliqueColour(self):           
        remaining = graph.nodes
        while remaining != {}:
            
            indep = clique(dual(remaining),0)[0]
            print(set(indep.keys()))
            colourSet=set()
            for i in indep:
                colourSet=colourSet.union(self.nodecolours[i])
            for i in range(self.n):
                if i not in colourSet:
                    for j in indep:
                        self.colour(j,i)
                    break
            
            remaining = subgraph(remaining,set(remaining.keys())-set(indep.keys()))
        

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
xaxis = np.arange(50,200,10)
yaxis = np.zeros(xaxis.shape)
for i in range(15):
    graph = G(xaxis[i],0.5)
    start = time.time()
    clique(graph.nodes,0)
    yaxis[i]=np.log(time.time()-start)
    print(i)
plt.plot(xaxis,yaxis)
plt.show()
"""
xaxis = np.linspace(0.3,0.7,20)
yaxis1 = np.zeros((20))
yaxis2=np.zeros((20))
for i in range(20):
    total1=0
    total2=0
    for j in range(10):
        order=[]
        graph = G(70,xaxis[i])
        sub = graph.nodes
        n=len(sub)
        for k in range(n):
            lowest = orderByDegree(sub)[-1]
            vertices = set(sub.keys())
            vertices.remove(lowest)
            order.append(lowest)
            sub = subgraph(graph.nodes,vertices)
        order.reverse()
        graph.greedyColour(order=order)
        total1+=max(set(graph.colours.values()))+1
        graph.clearColours()
        graph.cliqueColour()
        total2+=max(set(graph.colours.values()))+1
        graph.clearColours()
    yaxis1[i]=total1/10
    yaxis2[i]=total2/10
plt.plot(xaxis,yaxis1,label='minimum subgraph degree colouring')
plt.plot(xaxis,yaxis2,label='independent set colouring')
plt.grid()
plt.legend()
plt.xlabel('p')
plt.ylabel(r'Upper bound for $\chi(G)$')
plt.show()"""
"""
graphs = []
for i in range(10):
    graphs.append(G(70,0.5,k=7))
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
    indiv.append(max(set(graph.colours.values()))+1)
    graph.clearColours()
    graph.greedyColour(order = order3)
    indiv.append(max(set(graph.colours.values()))+1)
    graph.clearColours()
    graph.greedyColour(order = order4)
    indiv.append(max(set(graph.colours.values()))+1)
    graph.clearColours()
    print('cliquing')
    graph.cliqueColour()
    indiv.append(max(set(graph.colours.values()))+1)
    results.append(indiv)
    print('iterated')
total =[0]*4
for i in range(4):
    for j in range(10):
        total[i]+=results[j][i]
    total[i]=total[i]/10
results.append(total)
results=np.array(results)
for i in range(11):
    a = results[i]
    print(f'{i+1}&{a[0]}&{a[1]}&{a[2]}&{a[3]}\\\\')"""




