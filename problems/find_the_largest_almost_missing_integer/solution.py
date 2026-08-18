from collections import Counter
class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cand1=nums[0]
        cand2=nums[-1]
        mapp=Counter(nums)
        if k==len(nums):
            return max(nums)
        if k==1:
            maxi=-1
            for key,value in mapp.items():
                if value==1:
                    maxi=max(maxi,key)
            return maxi
        if mapp[cand1]>1 and mapp[cand2]>1:
            return -1
        if mapp[cand2]>1:
            return cand1
        elif mapp[cand1]>1:
            return cand2
        return max(cand1,cand2)
            

        