class Solution(object):
    def longestArithSeqLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp=[[0]*(2*(max(nums)-min(nums))+1) for _ in range(len(nums)+1)]
        offset=max(nums)-min(nums)
        dp[1][offset]=1
        max_len=0
        for i in range(len(nums)):
            for j in range(i):
                diff=nums[i]-nums[j]
                dp[i+1][diff+offset]=max(dp[j+1][diff+offset],1)+1
                max_len=max(max_len,dp[i+1][diff+offset])
        return max_len
        