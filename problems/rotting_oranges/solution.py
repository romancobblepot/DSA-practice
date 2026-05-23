from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        total=0
        count=0
        time=0
        q=deque()
        n=len(grid)
        m=len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]!=0:
                    count+=1
                if grid[i][j]==2:
                    q.append((i,j))
        def isValid(i,j,n,m):
            if i<0 or i>=n:
                return False
            if j<0 or j>=m:
                return False
            return True
        delRow=[0,-1,0,1]
        delCol=[-1,0,1,0]
        while q:
            k=len(q)
            total+=k
            for _ in range(k):
                row,col=q.popleft()
                for i in range(4):
                    nrow=row+delRow[i]
                    ncol=col+delCol[i]
                    if isValid(nrow,ncol,n,m) and grid[nrow][ncol]==1:
                        grid[nrow][ncol]=2
                        q.append((nrow,ncol))
            if q:
                time+=1        
        if total==count:
            return time
        return -1     