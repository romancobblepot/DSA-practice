from collections import deque
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        delRow=[0,-1,-1,-1,0,1,1,1]
        delCol=[-1,-1,0,1,1,1,0,-1]
        q=deque()
        n=len(grid)
        def isvalid(i,j,n):
            if i<0 or i>=n: return False
            if j<0 or j>=n: return False
            return True
        distance=[[float('inf')]*n for _ in range(n)]
        distance[0][0]=1  
        q.append((0,0,1))
        if grid[0][0]!=0:
            return -1
        if n==1:
            return 1
        while q:
            row,col,length=q.popleft()
            for k in range(8):
                nrow=row+delRow[k]
                ncol=col+delCol[k]
                if isvalid(nrow,ncol,n) and grid[nrow][ncol]==0:
                    if length+1<distance[nrow][ncol]:
                        distance[nrow][ncol]=length+1
                        q.append((nrow,ncol,distance[nrow][ncol]))
                    if nrow==n-1 and ncol==n-1:
                        return distance[nrow][ncol]
        return -1
        