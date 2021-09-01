# Write your code here
import sys
sys.setrecursionlimit(10**6)
import queue
q = queue.Queue()
class Graph:
    def __init__(self,nVertices):
        self.nVertices = nVertices
        self.AdjacenyMatrix = [[0 for i in range(self.nVertices)] for j in range(self.nVertices)]
        self.visited = [False for i in range(self.nVertices)]
        
    def addentry(self,v1,v2):
        self.AdjacenyMatrix[v1][v2] = 1
        self.AdjacenyMatrix[v2][v1] = 1
        
    def deleteentry(self,v1,v2):
        if self.containedges(v1,v2) is False:
            return
        self.AdjacenyMatrix[v1][v2] = 0
        self.AdjacenyMatrix[v2][v1] = 0
        
    def __dfsHelper(self,sv,visited):
        
        print(sv)
        visited[sv] = True
        for i in range(self.nVertices):
            if self.AdjacenyMatrix[sv][i] > 0 and visited[i] == False:
                self.__dfsHelper(i,visited)
        
    def dfs(self):
        sv = 0
        visited = [False for i in range(self.nVertices)]
        self.__dfsHelper(sv,visited)
        
    def __bfsHelper(self,sv,visited): 
        q.put(sv)
        visited[sv] = True
        while q.empty() is False:
            vertex = q.get()
            print(vertex,end=' ')
            for i in range(self.nVertices):
                if self.AdjacenyMatrix[vertex][i] > 0 and visited[i] == False:
                    q.put(i)
                    visited[i] = True
    

    
    def bfs(self):
        sv = 0
        visited = [False for i in range(self.nVertices)]
        for i in range(self.nVertices):
            if visited[i] is False:
                self.__bfsHelper(i,visited)
        
    def getpath(self,v1,v2):
        parent_dict = {}
        q.put(v1)
        while q.empty() is False:
            front = q.get()
            self.visited[front] = True
            for i in range(self.nVertices):
                if self.AdjacenyMatrix[front][i] > 0 and self.visited[i] == False:
                    parent_dict[i] = front
                    if i == v2:
                        ans = []
                        key = i
                        while key!=v1:
                            ans.append(key)
                            key = parent_dict[key]
                        ans.append(v1)
                        return ans
                    else:
                        q.put(i)

    def containedges(self,v1,v2):
        return True if self.AdjacenyMatrix[v1][v2] == 1 else  False
        
    def __str__(self):
        return str(self.AdjacenyMatrix)
    
    

VE = [int(i) for i in input().split()]
n = VE[0]
# visited = [False for i in range(n)]
e = VE[1]
g = Graph(n)
while e > 0:
    edges = [int(i) for i in input().split()]
    g.addentry(edges[0],edges[1])
    e = e - 1
path = [int(i) for i in input().split()]
ans = g.getpath(path[0],path[1])
if ans is None:
    print()
else:
    for i in range(len(ans)):
        print(ans[i],end=' ')