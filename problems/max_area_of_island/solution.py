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
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        ds=DisjointSet(m*n + 1)
        def isValid(i,j):
            if i<0 or i>=m: return False
            if j<0 or j>=n: return False
            return True
        delRow=[0,-1,0,1]
        delCol=[-1,0,1,0]
        q=deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    q.append((i,j))
        max_area=0
        k=len(q)
        while q:
            row,col=q.popleft()
            node=col +(row)*n
            for k in range(4):
                nrow=row+delRow[k]
                ncol=col+delCol[k]
                if isValid(nrow,ncol) and grid[nrow][ncol]==1:
                    node_new=ncol + (n*nrow)
                    if ds.Uparent(node)!=ds.Uparent(node_new):
                        ds.UnionbySize(node,node_new)
        if k>0:
            for i in range(m*n + 1):
                if ds.parent[i]==i:
                    max_area=max(max_area,ds.size[i])
        return max_area
        
        
        

        