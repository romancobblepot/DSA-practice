class Solution(object):
    def numTilings(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        if n==2:
            return 2
        full=[0]*(n+1)
        not_full=[0]*(n+1)
        full[1]=1
        full[2]=2
        not_full[2]=1
        for i in range(3,n+1):
            full[i]=(full[i-1]+full[i-2]+2*not_full[i-1])
            not_full[i]=(full[i-2]+not_full[i-1])
        return full[n]%(10**9 + 7)
        