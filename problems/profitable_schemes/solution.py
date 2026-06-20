class Solution(object):
    def profitableSchemes(self, n, minProfit, group, profit):
        """
        :type n: int
        :type minProfit: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        max_profit=sum(profit)
        m=len(profit)
        dp=[[[0]*(minProfit+1) for _ in range(n+1)] for _ in range(m+1)]
        dp[0][0][0]=1
        for i in range(1,m+1):
            for j in range(n+1):
                for k in range(minProfit+1):
                    next_profit=min(minProfit,profit[i-1]+k)
                    dp[i][j][k]+=dp[i-1][j][k]
                    if j+group[i-1]<=n:
                        dp[i][j+group[i-1]][next_profit]+=dp[i-1][j][k]
        total=0
        for j in range(n+1):
            total+=dp[m][j][minProfit]
        return total%(10**9 + 7)

        