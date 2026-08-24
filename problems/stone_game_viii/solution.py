class Solution(object):
    def stoneGameVIII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n=len(stones)
        prefix_arr=[0]*(n+1)
        for i in range(1,n+1):
            prefix_arr[i]=prefix_arr[i-1]+stones[i-1]
        dp=[0]*(n+1)
        dp[n]=prefix_arr[n]
        maxi=prefix_arr[n]
        for i in range(n-1,-1,-1):
            dp[i]=maxi
            if prefix_arr[i]-dp[i]>maxi:
                maxi=prefix_arr[i]-dp[i]
        return dp[1]


        