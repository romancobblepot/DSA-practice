class Solution(object):
    def subarrayslessKDistinct(self,nums,k):
        l=0
        r=0
        n=len(nums)
        numbers={}
        count=0
        while r<n:
            numbers[nums[r]]=numbers.get(nums[r],0)+1
            while len(numbers)>k:
                if nums[l] in numbers:
                    numbers[nums[l]]-=1
                    if numbers[nums[l]]==0:
                        del numbers[nums[l]]
                l+=1
            count+=r-l+1
            r+=1
        return count

    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        case1=self.subarrayslessKDistinct(nums,k)
        case2=self.subarrayslessKDistinct(nums,k-1)
        return case1-case2
        