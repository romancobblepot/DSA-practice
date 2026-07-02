class Solution(object):
    def findSafeWalk(self, grid, health):
        """
        :type grid: List[List[int]]
        :type health: int
        :rtype: bool
        """
        n=len(grid)
        m=len(grid[0])
        min_health=[[0]*m for _ in range(n)]
        q=[]
        if grid[0][0]==1:
            health=health-1
        if health<=0:
            return False
        heapq.heappush(q,(-health,0,0))
        min_health[0][0]=health
        delRow=[0,-1,0,1]
        delCol=[-1,0,1,0]
        def isValid(i,j):
            if i<0 or i>=n: return False
            if j<0 or j>=m: return False
            return True
        visited={}
        visited[(0,0)]=1
        while q:
            health_remaining,i,j=heapq.heappop(q)
            health_remaining*=-1
            if i==n-1 and j==m-1:
                return True
            for k in range(4):
                nrow=i+delRow[k]
                ncol=j+delCol[k]
                if isValid(nrow,ncol) and (nrow,ncol) not in visited:
                    if grid[nrow][ncol]==1 and health_remaining>1:
                        min_health[nrow][ncol]=max(min_health[nrow][ncol],health_remaining-1)
                        heapq.heappush(q,(-min_health[nrow][ncol],nrow,ncol))
                        visited[(nrow,ncol)]=1
                    elif grid[nrow][ncol]!=1:
                        min_health[nrow][ncol]=max(health_remaining,min_health[nrow][ncol])
                        heapq.heappush(q,(-min_health[nrow][ncol],nrow,ncol))
                        visited[(nrow,ncol)]=1
        return False
        




        