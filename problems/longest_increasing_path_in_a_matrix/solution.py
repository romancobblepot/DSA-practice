class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n=len(matrix)
        m=len(matrix[0])
        memo={}
        max_sum=0
        def isValid(i,j):
            if i<0 or i>=n: return False
            if j<0 or j>=m: return False
            return True
        delRow=[0,-1,0,1]
        delCol=[-1,0,1,0]
        def dfs(row,col):
            if (row,col) in memo:
                return memo[(row,col)]
            max_value=1
            for k in range(4):
                nrow=row+delRow[k]
                ncol=col+delCol[k]
                if isValid(nrow,ncol):
                    if matrix[nrow][ncol]>matrix[row][col]:
                        max_value=max(max_value,1+dfs(nrow,ncol))
            memo[(row,col)]=max_value
            return memo[(row,col)]
        res=1
        for i in range(n):
            for j in range(m):
                res=max(res,dfs(i,j))
        return res




        