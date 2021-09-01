from sys import setrecursionlimit
setrecursionlimit(10**6)
import queue
#class graph:
    
    #def __init__(self, nVertices):
        
        #self.nVertices = nVertices
        #self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]
        
    
    #def addEdge(self, v1, v2):
        
        #self.adjMatrix[v1][v2] = 1
        #self.adjMatrix[v2][v1] = 1
        
    
    #def __getPath(self, sv, ev, visited , s):
        
        #if sv == ev:
            #print(s)
            #how to return path
            #return  True
        
        #visited[sv]=True
        #for i in range(self.nVertices):
            #if self.adjMatrix[sv][i] == 1 and self.visited[i] is False:
                #ans=self.__getPath(i , ev , visited , s+" "+str(i))
                #if ans is True:
                    #return True
                
        #return False
 
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
    def __getpathdfs(self,sv,ev,visited):
        if sv==ev:
            return list([sv])
        visited[sv]=True
        for i in range(self.nvertices):
            if self.adjmatrix[sv][i]==1 and not visited[i]:
                li=self.__getpathdfs(i,ev,visited)
                if li!=None:
                    li.append(sv)
                    return li
        return None
    def getpathdfs(self,sv,ev):
        visited=[False for i in range(self.nvertices)]
        return self.__getpathdfs(sv,ev,visited)
## Read input as specified in the question.

li=input().strip().split()
v=int(li[0])
e=int(li[1])
g=graph(v)
for i in range(e):
    arr=input().strip().split()
    fv=int(arr[0])
    sv=int(arr[1])
    g.addedge(fv,sv)
li=input().strip().split()
sv=int(li[0])
ev=int(li[1])
li=g.getpathdfs(sv,ev)
if li!=None:
    for element in li:
        print(element,end=" ")
       