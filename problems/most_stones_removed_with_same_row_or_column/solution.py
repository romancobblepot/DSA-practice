class DisjointSet:
    def __init__(self,n):
        self.size=[1]*n
        self.parent=[0]*n
        for i in range(n):
            self.parent[i]=i
    def UParent(self,node):
        if node==self.parent[node]:
            return node
        self.parent[node]=self.UParent(self.parent[node])
        return self.parent[node]
    def UnionBySize(self,u,v):
        p_u=self.UParent(u)
        p_v=self.UParent(v)
        if p_u==p_v: return 
        if self.size[p_u]<self.size[p_v]:
            self.parent[p_u]=p_v
            self.size[p_v]+=self.size[p_u]
        else:
            self.parent[p_v]=p_u
            self.size[p_u]+=self.size[p_v]
class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        n=len(stones)
        maxRow=0
        maxCol=0
        for it in stones:
            maxRow=max(maxRow,it[0])
            maxCol=max(maxCol,it[1])
        ds=DisjointSet(maxRow + maxCol +2)
        nodes={}
        for it in stones:
            row=it[0]
            col=maxRow+it[1]+1
            ds.UnionBySize(row,col)
            nodes[row]=1
            nodes[col]=1
        count=0
        for key in nodes:
            if ds.UParent(key)==key:
                count+=1
        return n-count
        