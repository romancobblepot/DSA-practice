from collections import deque
class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n=len(grid)
        m=len(grid[0])
        q=deque()
        delrow=[0,-1,0,1]
        delcol=[-1,0,1,0]
        count=0
        def isEdge(i,j):
            if i<=0 or i>=n-1:
                return True
            if j<=0 or j>=m-1:
                return True
            return False
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    if isEdge(i,j):
                        grid[i][j]=-1
                        q.append((i,j))
                    else:
                        count+=1
        while q:
            row,col=q.popleft()
            for k in range(4):
                nrow=row+delrow[k]
                ncol=col+delcol[k]
                if not isEdge(nrow,ncol) and grid[nrow][ncol]==1:
                    count-=1
                    grid[nrow][ncol]=-1
                    q.append((nrow,ncol))
        return count
        