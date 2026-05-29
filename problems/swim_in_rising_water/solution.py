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
    def UnionBysize(self,u,v):
        p_u=self.UParent(u)
        p_v=self.UParent(v)
        if p_u==p_v: return
        if self.size[p_u]<self.size[p_v]:
            self.size[p_v]+=self.size[p_u]
            self.parent[p_u]=p_v
        else:
            self.size[p_u]+=self.size[p_v]
            self.parent[p_v]=p_u
class Solution(object):
    def swimInWater(self, grid):
        # Your code goes here
        n=len(grid)
        ds=DisjointSet(n*n)
        def isValid(i,j):
            if 0<=i<n and 0<=j<n: return True
            return False
        time=0
        delRow=[0,-1,0,1]
        delCol=[-1,0,1,0]
        cells = []
        for i in range(n):
            for j in range(n):
                cells.append((grid[i][j], i, j))
        cells.sort()
        time=0
        active=[False]*(n*n)
        for k in range(len(cells)):
                height,i,j=cells[k]
                node=i*n + j
                active[node]=True
                for k in range(4):
                    nrow=i+delRow[k]
                    ncol=j+delCol[k]
                    if isValid(nrow,ncol):
                        if ds.UParent(node)!=ds.UParent(nrow*n + ncol) and active[nrow*n + ncol]:
                            ds.UnionBysize(node,nrow*n + ncol)
                if ds.UParent(0)==ds.UParent(n*n -1):
                    return height
        