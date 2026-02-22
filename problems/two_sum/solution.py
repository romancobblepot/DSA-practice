class Solution(object):
    def twoSum(self, nums, target):
        mpp = {}
        
        # Length of the nums list
        n = len(nums)
        
        for i in range(n):
            num = nums[i]
            
            more_needed = target - num
            if more_needed in mpp:
                return [mpp[more_needed], i]
            mpp[num] = i
        
        # If no such pair found, return [-1, -1]
        return [-1, -1]
        