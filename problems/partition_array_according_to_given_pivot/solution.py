class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        small=[]
        big=[]
        count=0
        for i in range(len(nums)):
            if nums[i]<pivot:
                small.append(nums[i])
            elif nums[i]>pivot:
                big.append(nums[i])
            else:
                count+=1
        return small + [pivot]*count + big


        