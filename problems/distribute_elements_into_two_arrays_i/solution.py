class Solution(object):
    def resultArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res1=[nums[0]]
        res2=[nums[1]]
        for i in range(2,len(nums)):
            if res1[-1]>res2[-1]:
                res1.append(nums[i])
            else:
                res2.append(nums[i])
        return res1+res2



        