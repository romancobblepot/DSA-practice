class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        prev=[float('inf')]*(amount+1)
        for i in range(amount+1):
            if i%coins[0]==0:
                prev[i]=i//coins[0]
        for i in range(1,len(coins)):
            curr=[float('inf')]*(amount+1)
            for sum_ in range(amount+1):
                non_take=prev[sum_]
                take=float('inf')
                if sum_>=coins[i]:
                    take=1+curr[sum_-coins[i]]
                curr[sum_]=min(take,non_take)
            prev=curr
        return prev[amount] if prev[amount]<float('inf') else -1
        