class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        dp=[[0]*(n+1) for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            for j in range(i-1,-2,-1):
                non_take=dp[i+1][j+1]
                take=0
                if j==-1 or nums[i]>nums[j]:
                    take=1+dp[i+1][i+1]
                dp[i][j+1]=max(take,non_take)
        return dp[0][0]

        