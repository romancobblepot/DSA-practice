class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        def pivot(nums):
            low=0
            n=len(nums)
            high=len(nums)-1
            while low<=high:
                mid=(low+high)//2
                if mid>0 and nums[mid]<nums[mid-1]:
                    return mid
                if mid<n-1 and nums[mid]>nums[mid+1]:
                    return mid+1
                if nums[mid]==nums[low]==nums[high]:
                    low+=1
                elif nums[mid]>nums[high] or (nums[low]==nums[mid] and nums[mid]>nums[high]):
                    low=mid+1
                else:
                    high=mid-1
            return 0
        pivot=pivot(nums)
        low=0
        high=len(nums)-1
        if target==nums[pivot]:
            return True
        elif target<=nums[-1]:
            low=pivot+1
            high=len(nums)-1
            while low<=high:
                mid=(low+high)//2
                if target==nums[mid]:
                    return True
                elif target>nums[mid]:
                    low=mid+1
                else:
                    high=mid-1
        else:
            high=pivot
            low=0
            while low<=high:
                mid=(low+high)//2
                if target==nums[mid]:
                    return True
                elif target<nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
        return False

                

        
        



