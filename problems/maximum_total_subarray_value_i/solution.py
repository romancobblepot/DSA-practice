class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_difference=max(nums)-min(nums)
        return max_difference*k
        
        