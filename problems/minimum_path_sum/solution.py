class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        matrix=grid
        m=len(matrix)
        n=len(matrix[0])
        prev=[0]*n
        for i in range(m):
            temp=[0]*n
            for j in range(n):
                if i==0 and j==0:
                    temp[j]=matrix[i][j]
                    continue
                up=prev[j] if i>0 else float('inf')
                left=temp[j-1] if j>0 else float('inf')
                temp[j]=min(matrix[i][j]+up,matrix[i][j]+left)
            prev=temp
        return prev[n-1]
        