class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num=n
        sum=0
        product=1
        while num>0:
            sum+=num%10
            product*=num%10
            num//=10
        return n%(sum+product)==0

        
        