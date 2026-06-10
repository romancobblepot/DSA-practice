class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        max_sum=sum(nums)
        min_sum=-sum(nums)
        if abs(target)>max_sum:
            return 0
        offset=max_sum
        prev=[0]*(max_sum-min_sum+1)
        prev[offset]=1
        for i in range(len(nums)):
            curr=[0]*(max_sum-min_sum+1)
            for sum_ in range(max_sum-min_sum+1):
                actual_sum=sum_-offset
                new_sum=actual_sum+offset
                if new_sum+nums[i]<max_sum-min_sum+1:
                    curr[new_sum+nums[i]]+=prev[sum_]
                curr[new_sum-nums[i]]+=prev[sum_]
            prev=curr
        return prev[offset+target]

        