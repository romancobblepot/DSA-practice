import math
class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n<=2: return n
        num=1
        while num<=n:
            num*=2
        return num
        