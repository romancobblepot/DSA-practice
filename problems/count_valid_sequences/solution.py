import math
class Solution(object):
    def count_sequences(self,n,k,mod):
        if k==0 or k==n:
            return 1
        num=1
        den=1
        for i in range(k):
            num=(num*(n-i))%mod
            den=(den*(i+1))%mod
        res=(num*pow(den,mod-2,mod))%mod
        return res
    def countValidSequences(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        mod=10**9 +7
        total_combinations=self.count_sequences(n-1,k-1,mod)
        odd_combinations=0
        if (n-k)%2==0:
            parity=(n-k)//2
            odd_combinations=self.count_sequences(parity+k-1,k-1,mod)
        return (total_combinations-odd_combinations)%mod
        
            
        