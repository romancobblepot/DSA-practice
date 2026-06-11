class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        n=len(prices)
        dp=[[0]*2 for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            for buy in range(2):
                if buy==0:
                    dp[i][0]=max(dp[i+1][0],-prices[i]+dp[i+1][1])
                else:
                    dp[i][1]=max(dp[i+1][1],prices[i]-fee+dp[i+1][0])
        return dp[0][0]
        