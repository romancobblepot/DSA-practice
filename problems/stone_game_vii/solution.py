class Solution(object):
    def stoneGameVII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n=len(stones)
        prefix_arr=[0]*(n+1)
        for i in range(1,n+1):
            prefix_arr[i]=stones[i-1]+prefix_arr[i-1]
        dp=[[0]*(n) for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                dp[i][j]=max(prefix_arr[j]-prefix_arr[i]-dp[i][j-1],prefix_arr[j+1]-prefix_arr[i+1]-dp[i+1][j])
        return dp[0][n-1]
        
        