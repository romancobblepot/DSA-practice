class Solution(object):
    def sumOfGoodIntegers(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        i=max(n-k,0)
        sum=0
        while True:
            if abs(n-i)<=k:
                if n & i ==0:
                    sum+=i
                i+=1
            else:
                break
        return sum
                
                
            
        