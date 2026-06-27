import math
class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ''
        mapp=defaultdict(int)
        elements=set()
        for i in range(len(nums)):
            mapp[nums[i]]+=1
            elements.add(nums[i])
        max_len=1
        length=0
        for key in elements:
            if key==1:
                continue
            if mapp[key]==1:
                continue
            else:
                length=1
            prev_value=key
            while prev_value**2 in mapp and mapp[prev_value**2]>=2:
                length+=2
                prev_value=prev_value**2
            if prev_value**2 in mapp and mapp[prev_value**2]==1:
                length+=2
            max_len=max(max_len,length)
            length=0
        count_ones=mapp.get(1,0) 
        count_ones=count_ones if count_ones%2!=0 else count_ones-1
        max_len=max(max_len,count_ones)
        return max_len
            




                



        