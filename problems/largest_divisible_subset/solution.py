class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        parent=[0]*n
        dp=[1]*n
        max_len=0
        last_index=0
        nums.sort()
        for i in range(n):
            parent[i]=i
            for j in range(i):
                if nums[i]%nums[j]==0:
                    if dp[i]<=dp[j]+1:
                        dp[i]=dp[j]+1
                        parent[i]=j
            if dp[i]>max_len:
                max_len=dp[i]
                last_index=i
        i=last_index
        ans=[]
        while parent[i]!=i:
            ans.append(nums[i])
            i=parent[i]
        ans.append(nums[i])
        return ans
        