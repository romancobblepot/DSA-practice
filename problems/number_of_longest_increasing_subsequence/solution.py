class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        dp=[1]*n 
        max_len=0
        total=0
        count=[1]*n
        for i in range(n):
            for j in range(i):
                if nums[i]>nums[j]:
                    if dp[i]<dp[j]+1:
                        dp[i]=dp[j]+1
                        count[i]=count[j]
                    elif dp[i]==dp[j]+1:
                        dp[i]=dp[j]+1
                        count[i]+=count[j]
            if dp[i]>max_len:
                max_len=dp[i]
                total=count[i]
            elif dp[i]==max_len:
                total+=count[i]
        return total