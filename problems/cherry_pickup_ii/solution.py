class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        g=grid
        n=len(g)
        m=len(g[0])
        curr=[[0]*m for _ in range(m)]
        next=[[0]*m for _ in range(m)]
        for j1 in range(m):
            for j2 in range(m):
                next[j1][j2]=g[n-1][j1] if j1==j2 else g[n-1][j1]+g[n-1][j2]
        for i in range(n-2,-1,-1):
            for j1 in range(m):
                for j2 in range(m):
                    maxi=0
                    for d1 in [-1,0,1]:
                        for d2 in [-1,0,1]:
                            nj1=j1+d1
                            nj2=j2+d2
                            if 0<=nj1<m and 0<=nj2<m:
                                curr_val=g[i][j1] if j1==j2 else g[i][j1]+g[i][j2]
                                curr_val+=next[nj1][nj2]
                                if curr_val>maxi:
                                    maxi=curr_val
                    curr[j1][j2]=maxi
            next=[row[:] for row in curr]
        return next[0][m-1]
        