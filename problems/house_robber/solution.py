class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=2:
            return max(nums)
        def dp(idx,nums,memo):
            if idx==len(nums)-1:
                return nums[idx]
            if idx>=len(nums):
                return 0
            if idx in memo:
                return memo[idx]
            pick=nums[idx]+dp(idx+2,nums,memo)
            non_pick=dp(idx+1,nums,memo)
            memo[idx]=max(pick,non_pick)
            return memo[idx]
        memo={}
        return dp(0,nums,memo)



                



        