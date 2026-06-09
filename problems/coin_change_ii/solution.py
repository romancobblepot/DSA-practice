class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        n=len(coins)
        dp=[0]*(amount+1)
        for i in range(amount+1):
            if i%coins[0]==0:
                dp[i]=1
        for i in range(1,len(coins)):
            for sum_ in range(amount+1):
                taken=0
                if sum_>=coins[i]:
                    taken=dp[sum_-coins[i]]
                dp[sum_]+=taken
        return dp[amount]


            

        