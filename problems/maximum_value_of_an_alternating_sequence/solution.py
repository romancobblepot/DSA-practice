class Solution(object):
    def maximumValue(self, n, s, m):
        """
        :type n: int
        :type s: int
        :type m: int
        :rtype: int
        """
        if n == 1:
            return s
        cycles = (n - 1) // 2
        remainder = (n - 1) % 2
        highest_base = s + m + (cycles - 1) * (m - 1)        
        if remainder == 1:
            highest_base = max(highest_base, s + (cycles + 1) * m - cycles)            
        return highest_base
        
        
        