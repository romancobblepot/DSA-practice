class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit=0
        mini=prices[0]
        for i in range(1,len(prices)):
            if prices[i]<mini:
                mini=prices[i]
            current_profit=prices[i]-mini
            if current_profit>max_profit:
                max_profit=current_profit
        return max_profit
        