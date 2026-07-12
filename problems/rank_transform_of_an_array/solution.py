class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        nums=arr[:]
        nums.sort()
        mapp={}
        rank=1
        for i in range(len(nums)):
            if nums[i] not in mapp:
                mapp[nums[i]]=rank
                rank+=1
        for i in range(len(arr)):
            arr[i]=mapp[arr[i]]
        return arr


        