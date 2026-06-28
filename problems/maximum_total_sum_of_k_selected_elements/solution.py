class Solution(object):
    def maxSum(self, nums, k, mul):
        """
        :type nums: List[int]
        :type k: int
        :type mul: int
        :rtype: int
        """
        nums.sort(reverse=True)
        total=0
        for i in range(k):
            if mul>0:
                total+=nums[i]*mul
                mul-=1
            elif mul<=0:
                total+=nums[i]
        return total
        
            

                
        