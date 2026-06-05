class DisjointSet(object):
    def __init__(self,n):
        self.size=[1]*(n)
        self.parent=list(range(n+1))
    def Uparent(self,node):
        if node==self.parent[node]:
            return node
        self.parent[node]=self.Uparent(self.parent[node])
        return self.parent[node]
    def UnionbySize(self,u,v):
        ulp_u=self.Uparent(u)
        ulp_v=self.Uparent(v)
        if ulp_u==ulp_v:
            return
        if self.size[ulp_u]<self.size[ulp_v]:
            self.parent[ulp_u]=ulp_v
            self.size[ulp_v]+=self.size[ulp_u]
        else:
            self.parent[ulp_v]=ulp_u
            self.size[ulp_u]+=self.size[ulp_v]
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        ds=DisjointSet(len(edges)+1)
        for u,v in edges:
            if ds.Uparent(u)==ds.Uparent(v):
                return [u,v]
            ds.UnionbySize(u,v)
        


        