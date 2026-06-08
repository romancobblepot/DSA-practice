class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        grid=obstacleGrid
        m=len(grid)
        n=len(grid[0])
        prev=[0]*n
        for i in range(m):
            temp=[0]*n
            for j in range(n):
                if grid[i][j]==1:
                    temp[j]=0
                    continue
                if i==0 and j==0:
                    temp[j]=1
                    continue
                up=prev[j] if i>0 else 0
                left=temp[j-1] if j>0 else 0
                temp[j]=up + left
            prev=temp
        return prev[n-1]
        


        