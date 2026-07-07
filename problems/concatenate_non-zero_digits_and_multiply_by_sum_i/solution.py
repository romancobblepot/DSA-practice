class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev=0
        num=n
        sum=0
        while num>0:
            dig=num%10
            num=num//10
            if dig>0:
                sum+=dig
                prev=prev*10 + dig
        prev=int(str(prev)[::-1])
        return prev*sum


        