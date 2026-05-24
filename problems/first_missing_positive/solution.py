class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        n=len(nums)
        while i<n:
            swapped_index=nums[i]-1
            if 0<=swapped_index<n and nums[swapped_index]!=nums[i]:
                nums[i],nums[swapped_index]=nums[swapped_index],nums[i]
            else:
                i+=1
        for i in range(n):
            if nums[i]!=i+1:
                return i+1
        return n+1
            

            

        