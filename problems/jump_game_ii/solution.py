class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return 0
        max_index=list(range(len(nums)))
        for i in range(len(max_index)):
            max_index[i]+=nums[i]
        i=0
        jump=0
        while i<len(nums):
            if i==len(nums)-1:
                return jump
            if max_index[i]>=len(nums)-1:
                return jump+1
            maxi=i
            for idx in range(i+1,max_index[i]+1):
                if max_index[idx]>max_index[maxi]:
                    maxi=idx
            jump+=1
            i=maxi
        return jump



        
        