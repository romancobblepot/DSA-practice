class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ind1=nums.index(min(nums))
        ind2=nums.index(max(nums))
        n=len(nums)
        left=min(ind1,ind2)
        right=max(ind1,ind2)
        choice1=right+1
        choice2=n-left
        choice3=left+1+n-right
        return min(choice1,choice2,choice3)
