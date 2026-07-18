class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a
        return gcd(min(nums),max(nums))
        