class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        prefix_sum=0
        for i in range(len(gain)):
            gain[i]=prefix_sum+gain[i]
            prefix_sum=gain[i]
        return max(max(gain),0)
        