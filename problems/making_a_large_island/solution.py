class DisjointSet:
    def __init__(self,n):
        self.parent=[0]*n
        self.size=[1]*n
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
        if p_u==p_v:
            return 
        if self.size[p_v]<self.size[p_u]:
            self.size[p_u]+=self.size[p_v]
            self.parent[p_v]=p_u
        else:
            self.size[p_v]+=self.size[p_u]
            self.parent[p_u]=p_v
class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n=len(grid)
        ds=DisjointSet(len(grid)**2)
        max_size=0
        row=[0,-1,0,1]
        col=[-1,0,1,0]
        def isValid(i,j):
            if i<0 or i>=n or j<0 or j>=n: return False
            return True
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j]==1:
                    node=i*n + j
                    for k in range(4):
                        nrow=i+row[k]
                        ncol=j+col[k]
                        if isValid(nrow,ncol) and grid[nrow][ncol]==1:
                            if ds.UParent(node)!=ds.UParent( nrow*n + ncol):
                                ds.UnionBySize(node,nrow*n + ncol)
        for i in range(n*n):
            if ds.parent[i] == i:
                max_size = max(max_size, ds.size[i])
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j]==0:
                    node=i*n + j
                    seen=set()
                    node_size=1
                    for k in range(4):
                        nrow=i+row[k]
                        ncol=j+col[k]
                        if isValid(nrow,ncol) and grid[nrow][ncol]==1:
                                parent=ds.UParent(nrow*n + ncol)
                                if parent not in seen:
                                    node_size+=ds.size[parent]
                                    seen.add(parent)
                    max_size=max(max_size,node_size)
        return max_size        