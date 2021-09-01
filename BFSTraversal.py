import queue
from sys import setrecursionlimit
setrecursionlimit(10**6)
class graph:
    def __init__(self,nvertices):
        self.nvertices=nvertices
        self.adjmatrix=[[0 for i in range(nvertices)] for j in range(nvertices)]
        
    def addedge(self,v1,v2):
        self.adjmatrix[v1][v2]=1
        self.adjmatrix[v2][v1]=1
        
    def removeedge(self):
        if self.containsedge(v1,v2) is False:
            return
        self.adjmatrix[v1][v2]=0
        self.adjmatrix[v2][v1]=0
        
    def containsedge(self,v1,v2):
        if self.adjmatrix[v1][v2]>0:
            return True
        else:
            return False
        
    def __str__(self):
        return str(self.adjmatrix)
    
    def __bfs(self,sv,visited):
        q=queue.Queue()
        q.put(sv)
        visited[sv]=True
        while q.empty() is False:
            u=q.get()
            print(u,end=" ")
            for i in range(self.nvertices):
                if self.adjmatrix[u][i]>0 and visited[i] is False:
                    q.put(i)
                    visited[i]=True
                    
    def bfs(self):
        visited=[False for i in range(self.nvertices)]
        for i in range(self.nvertices):
            if visited[i] is False:
                self.__bfs(i,visited)
                
                
    def __connectedComponentsHelper(self,v1,visited):
        q = queue.Queue()
        arr=[]
        q.put(v1)
        visited[v1] = True
        while q.empty() is False:
            sv = q.get()
            arr.append(sv)
            for i in range (self.nvertices):
                if self.adjmatrix[sv][i]>0 and visited[i] is False:
                    q.put(i)
                    visited[i] = True
                    
        return arr
    
    def connectedComponents(self):
        if self.nvertices == 0:
            return [[]]
        visited = [False for i in range (self.nvertices)]
        result = []
        for i in range(self.nvertices):
            if visited[i] is False:
                smallOutput = self.__connectedComponentsHelper(i,visited)
                result.append(smallOutput)
        return result
        

        
                
li=input().strip().split()
v=int(li[0])
e=int(li[1])
g=graph(v)
for i in range(e):
    arr=input().strip().split()
    fv=int(arr[0])
    sv=int(arr[1])
    g.addedge(fv,sv)
    
result = g.connectedComponents()
for i in result:
    i.sort()
    for j in i:
        print(j,end=" ")
        
    print()
