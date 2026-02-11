class Solution(object):
    def lowBound(self,nums,target):
        low=0
        high=len(nums)-1
        temp=0
        while low<=high:
            mid=(low+high)//2
            if nums[mid]<target:
                temp=mid
                low=mid+1
            else:
                high=mid-1
        if 0<=temp<len(nums) and nums[temp]==target:
            return temp
        if 1<=temp+1<len(nums) and nums[temp+1]==target:
            return temp+1
        return -1
    def HighBound(self,nums,target):
        low=0
        high=len(nums)-1
        temp=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>target:
                temp=mid
                high=mid-1
            else:
                low=mid+1
        if 0<=temp<len(nums) and nums[temp]==target:
            return temp
        if 0<=temp-1<len(nums) and nums[temp-1]==target:
            return temp-1
        return -1    
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        low=self.lowBound(nums,target)
        high=self.HighBound(nums,target)
        return [low,high]

        