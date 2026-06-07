class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def backtrack(idx,nums,sum,target,memo):
            if idx==len(nums) and sum==target:
                return 1
            elif idx==len(nums):
                return 0
            if (idx,sum) in memo:
                return memo[(idx,sum)]
            left=backtrack(idx+1,nums,sum+nums[idx],target,memo)
            right=backtrack(idx+1,nums,sum-nums[idx],target,memo)
            memo[(idx,sum)]=left+right
            return memo[(idx,sum)]
        memo={}
        if abs(target)>sum(nums):
            return 0
        res=backtrack(0,nums,0,target,memo)
        return res

        