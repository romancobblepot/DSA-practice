class Solution(object):
    def consecutiveSetBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        binary=bin(n)[2:]
        start=False
        n=len(binary)
        count=0
        i=1
        while i<n:
            if binary[i]=="1" and binary[i-1]=="1":
                count+=1
            i+=1
        return count==1
            
        