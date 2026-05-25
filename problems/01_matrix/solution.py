class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        grid=mat
        n=len(grid)
        m=len(grid[0])
        def isValid(row,col,n,m):
            if row<0 or row>=n:
                return False
            if col<0 or col>=m:
                return False
            return True
        delRow=[0,-1,0,1]
        delCol=[-1,0,1,0]
        q=deque()
        distance=[[-1]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j]==0:
                    q.append((i,j))
                    distance[i][j]=0
        while q:
            row,col=q.popleft()
            for k in range(4):
                nrow=row+delRow[k]
                ncol=col+delCol[k]
                if isValid(nrow,ncol,n,m) and distance[nrow][ncol]==-1:
                    distance[nrow][ncol]=distance[row][col]+1
                    q.append((nrow,ncol))
        return distance
        