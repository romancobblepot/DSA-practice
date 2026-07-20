class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m=len(grid)
        n=len(grid[0])
        k=k%(len(grid)*len(grid[0]))
        for _ in range(k):
            for i in range(m-1,0,-1):
                grid[i][n-1],grid[i-1][n-1]=grid[i-1][n-1],grid[i][n-1]
            for j in range(n-1,0,-1):
                for i in range(m):
                    grid[i][j],grid[i][j-1]=grid[i][j-1],grid[i][j]
        return grid


        