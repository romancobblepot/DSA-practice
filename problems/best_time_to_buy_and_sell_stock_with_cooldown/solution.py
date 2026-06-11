class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices)
        dp=[[0]*2 for _ in range(n+2)]
        for i in range(n-1,-1,-1):
            for buy in range(2):
                if buy==0:
                    dp[i][0]=max(dp[i+1][0],-prices[i]+dp[i+1][1])
                else:
                    dp[i][1]=max(dp[i+1][1],prices[i]+dp[i+2][0])
        return dp[0][0]
        