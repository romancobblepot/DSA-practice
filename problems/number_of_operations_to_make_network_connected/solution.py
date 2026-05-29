class DisjointSet:
    def __init__(self,n):
        self.parent=list(range(n+1))
        self.size=[1]*(n+1)
    def Uparent(self,node):
        if node==self.parent[node]:
            return node
        self.parent[node]=self.Uparent(self.parent[node])
        return self.parent[node]
    def UnionBySize(self,u,v):
        up_u=self.Uparent(u)
        up_v=self.Uparent(v)
        if up_u==up_v:
            return 
        if self.size[up_u]<self.size[up_v]:
            self.parent[up_u]=up_v
            self.size[up_v]+=self.size[up_u]
        else:
            self.parent[up_v]=up_u
            self.size[up_u]+=self.size[up_v]
class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        ds=DisjointSet(n)
        if len(connections)<n-1:
            return -1
        for i in range(len(connections)):
            u=connections[i][0]
            v=connections[i][1]
            ds.UnionBySize(u,v)
        count=0
        for i in range(n):
            if ds.parent[i]==i:
                count+=1
        return count-1
        