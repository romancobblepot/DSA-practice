class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices)
        dp=[[[0]*(k+1) for _ in range(2)] for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            for buy in range(2):
                for j in range(1,k+1):
                    if buy==0:
                        dp[i][0][j]=max(dp[i+1][0][j],-prices[i]+dp[i+1][1][j])
                    else:
                        dp[i][1][j]=max(dp[i+1][1][j],prices[i]+dp[i+1][0][j-1])
        return dp[0][0][k]
        