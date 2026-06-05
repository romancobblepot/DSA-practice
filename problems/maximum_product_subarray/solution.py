class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_prod=min_prod=ans=nums[0]
        for i in range(1,len(nums)):
            if nums[i]<0:
                min_prod,max_prod=max_prod,min_prod
            max_prod=max(nums[i],nums[i]*max_prod)
            min_prod=min(nums[i],nums[i]*min_prod)
            ans=max(ans,max_prod)
        return ans
        