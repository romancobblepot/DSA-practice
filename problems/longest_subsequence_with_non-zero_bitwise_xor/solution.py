class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor=nums[0]
        non_zero=False
        for num in nums:
            if num!=0:
                non_zero=True
                break
        if not non_zero: return 0
        for num in nums[1:]:
            xor=xor^num
        return len(nums) if xor!=0 else len(nums)-1



                        
        