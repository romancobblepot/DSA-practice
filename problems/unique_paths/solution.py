from collections import deque
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def isValid(i,j):
            if i<0 or i>=m: return False
            if j<0 or j>=n: return False
            return True
        def bfs(i,j):
            ways=[[0]*n for _ in range(m)]
            ways[0][0]=1
            for i in range(m):
                for j in range(n):
                    if isValid(i-1,j):
                        ways[i][j]+=ways[i-1][j]
                    if isValid(i,j-1):
                        ways[i][j]+=ways[i][j-1]
            return ways
        return bfs(0,0)[m-1][n-1]

        