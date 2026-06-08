class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        m=len(triangle)
        if m==1:
            return triangle[0][0]
        prev=triangle[0]
        for i in range(1,m):
            temp=[0]*(i+1)
            for j in range(i+1):
                up=prev[j] if j<i else float('inf')
                up_left=prev[j-1] if j>0 else float('inf')
                temp[j]=min(triangle[i][j] + up, triangle[i][j] + up_left)
            prev=temp
        return min(prev)       