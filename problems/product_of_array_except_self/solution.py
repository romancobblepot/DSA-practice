class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix_product=[1]*len(nums)
        prefix=1
        suffix_product=[1]*len(nums)
        suffix=1
        for i in range(1,len(nums)):
            prefix*=nums[i-1]
            prefix_product[i]=prefix
        for i in range(len(nums)-2,-1,-1):
            suffix*=nums[i+1]
            suffix_product[i]=suffix
        for i in range(len(nums)):
            prefix_product[i]*=suffix_product[i]
        return prefix_product


        