class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mid=0
        for i in range(1,len(nums)-1):
            if nums[i-1]>nums[i] and nums[i]<=nums[i+1]:
                mid=i
        if nums[-1]<nums[len(nums)-2]:
            mid=len(nums)-1
        arr=[101]*len(nums)
        for i in range(len(nums)):
            arr[i]=nums[(i+mid)%(len(nums))]
        for i in range(1,len(arr)):
            if arr[i]<arr[i-1]:
                return False
        return True
        

        