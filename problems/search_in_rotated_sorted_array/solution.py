class Solution(object):
    def lowest(self,nums):
            low=0
            high=len(nums)-1
            while low<high:
                mid=(low+high)//2
                if nums[mid]>nums[high]:
                    low=mid+1
                else:
                    high=mid
            return low+(high-low)//2
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        smallest=self.lowest(nums)
        highest=smallest-1
        if target>nums[highest] or target<nums[smallest]:
            return -1
        low=0
        high=len(nums)-1
        if nums[0]<=target<=nums[highest]:
            low=0
            high=highest
        if nums[smallest]<=target<=nums[-1]:
            low=smallest
            high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return -1


