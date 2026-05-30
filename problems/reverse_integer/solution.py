class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s=str(x)
        arr=list(s)
        negative=False
        if '-' in arr:
            negative=True
        n=len(arr)
        reversed=0
        r=n-1
        if negative:
            end=1
            n-=1
        else:
            end=0
        while n>=0 and r>=end:
            reversed+=int(arr[r])*(10**(n-1))
            r-=1
            n-=1
        if negative:
            reversed*=-1
        if reversed>(2**31 - 1) or reversed<(-2**31):
            return 0
        return reversed

        