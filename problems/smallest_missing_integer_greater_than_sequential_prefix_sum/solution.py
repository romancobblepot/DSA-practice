class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total=nums[0]
        max_total=nums[0]
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]==1:
                total+=nums[i]
                max_total=max(max_total,total)
            else:
                break
        ans=max_total
        for i in range(max_total,max(nums)+1):
            if i not in nums:
                return i
            else:
                ans+=1
        return ans



        



        