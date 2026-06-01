class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def pos_pow(x,n):
            if n==0:
                return 1
            return float(x*pow(x,n-1))
        def neg_pow(x,n):
            if n==0:
                return 1
            return float(pow(x,n+1))/x
        if x==0:
            return x
        if n>0:
            return pos_pow(x,n)
        else:
            return neg_pow(x,n)
        
        