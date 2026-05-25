class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        n=len(grid)
        m=len(grid[0])
        visited=[[False]*m for _ in range(n)]
        count=0
        def isvalid(i,j):
            if i<0 or i>=n:
                return False
            if j<0 or j>=m:
                return False
            return True
        delrow=[0,-1,0,1]
        delcol=[-1,0,1,0]
        def dfs(row,col,n,m,visited):
            visited[row][col]=True
            for k in range(4):
                nrow=row+delrow[k]
                ncol=col+delcol[k]
                if isvalid(nrow,ncol) and grid[nrow][ncol]=="1" and not visited[nrow][ncol]:
                    dfs(nrow,ncol,n,m,visited)
        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1" and not visited[i][j]:
                    count+=1
                    dfs(i,j,n,m,visited)
        return count
