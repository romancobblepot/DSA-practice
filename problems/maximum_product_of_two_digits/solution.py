class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        second_max=0
        maxi=0
        for num in str(n):
            if maxi>int(num):
                second_max=max(second_max,int(num))
            else:
                second_max=maxi
                maxi=int(num)
        return maxi*second_max

        