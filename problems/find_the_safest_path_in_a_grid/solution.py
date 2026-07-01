class Solution(object):
    def maximumSafenessFactor(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n=len(grid)
        m=len(grid[0])
        min_distance=[[float('inf')]*m for _ in range(n)]
        q=deque()
        visited={}
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    min_distance[i][j]=0
                    q.append((0,i,j))
        def isValid(i,j):
            if i<0 or i>=n: return False
            if j<0 or j>=m: return False
            return True
        delRow=[0,-1,0,1]
        delCol=[-1,0,1,0]
        def bfs(q,visited):
            while q:
                distance,row,col=q.popleft()
                visited[(row,col)]=1
                for k in range(4):
                    nrow=row+delRow[k]
                    ncol=col+delCol[k]
                    if isValid(nrow,ncol) and grid[nrow][ncol]!=1 and ((nrow,ncol) not in visited):
                        if distance+1<min_distance[nrow][ncol]:
                            min_distance[nrow][ncol]=1+distance
                        q.append((min_distance[nrow][ncol],nrow,ncol))
                        visited[(nrow,ncol)]=1
        bfs(q,visited)
        end=0
        for i in range(len(min_distance)):
            for j in range(len(min_distance[0])):
                end=max(end,min_distance[i][j])
        def check(v):
            if min_distance[0][0]<v or min_distance[n-1][m-1]<v:
                return False
            visited={}
            visited[(0,0)]=1
            q=deque()
            q.append([0,0])
            while q:
                row,col=q.popleft()
                if row==n-1 and col==m-1:
                    return True
                for k in range(4):
                    nrow=row+delRow[k]
                    ncol=col+delCol[k]
                    if isValid(nrow,ncol) and min_distance[nrow][ncol]>=v and ((nrow,ncol) not in visited):
                        q.append((nrow,ncol))
                        visited[(nrow,ncol)]=1
            return False
        start=0
        res=-1
        while start<=end:
            mid=start + (end-start)//2
            if check(mid):
                res=mid
                start=mid+1
            else:
                end=mid-1
        return res

        
        
                

        





        
        