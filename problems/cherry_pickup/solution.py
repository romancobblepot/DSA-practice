class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n=len(grid)
        m=len(grid[0])
        dp=[[[float('-inf')]*m for _ in range(n)] for _ in range(n)]
        nrow1=[0,1]
        ncol1=[1,0]
        dp[n-1][n-1][m-1]=grid[n-1][m-1]
        for i1 in range(n-1,-1,-1):
            for i2 in range(n-1,-1,-1):
                for j1 in range(m-1,-1,-1):
                    if i1==n-1 and j1==m-1 and i2==n-1:
                        continue
                    if grid[i1][j1]!=-1 and 0<=i1+j1-i2<m and grid[i2][i1+j1-i2]!=-1:
                        maxi=float('-inf')
                        for k in range(2):
                            for l in range(2):
                                ni1=i1+nrow1[k]
                                nj1=j1+ncol1[k]
                                ni2=i2+nrow1[l]
                                if 0<=nj1<m and 0<=ni1+nj1-ni2<m and 0<=ni1<n and 0<=ni2<n and grid[ni1][nj1]!=-1 and grid[ni2][nj1+ni1-ni2]!=-1:
                                        if dp[ni1][ni2][nj1]==float('-inf'):
                                            continue
                                        curr_val=grid[i1][j1] if i1==i2 else grid[i1][j1]+grid[i2][j1+i1-i2] 
                                        curr_val += dp[ni1][ni2][nj1]
                                        if curr_val>maxi:
                                            maxi=curr_val
                            dp[i1][i2][j1]=maxi
        return max(0,dp[0][0][0])

        

                
                    

        