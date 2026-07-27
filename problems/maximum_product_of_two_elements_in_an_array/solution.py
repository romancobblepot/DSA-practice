class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi=0
        second_maxi=0
        for num in nums:
            if num<=maxi:
                second_maxi=max(num,second_maxi)
            else:
                second_maxi=maxi
                maxi=num
        return (maxi-1)*(second_maxi-1)



        