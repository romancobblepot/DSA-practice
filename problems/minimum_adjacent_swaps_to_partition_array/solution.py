class Solution(object):
    def minAdjacentSwaps(self, nums, a, b):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :rtype: int
        """
        less_than_a=0
        less_than_b=0
        greater_than_b=0
        ans=0
        for num in nums:
            if num<a:
                ans+=less_than_b+greater_than_b
                less_than_a+=1
            elif num<=b:
                ans+=greater_than_b
                less_than_b+=1
            else:
                greater_than_b+=1
        return ans%(10**9+7)


                
        
                
        