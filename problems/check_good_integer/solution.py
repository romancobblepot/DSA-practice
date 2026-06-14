class Solution(object):
    def checkGoodInteger(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num=n
        length=len(str(num))
        sqSum=0
        digSum=0
        for i in range(length):
            dig1=num%10
            num=num//10
            sqSum+=(dig1)*(dig1)
            digSum+=dig1
        return (sqSum-digSum)>=50
            
            