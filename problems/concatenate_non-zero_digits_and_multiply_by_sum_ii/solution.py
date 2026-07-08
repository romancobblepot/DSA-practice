from math import pow
class Solution(object):
    def sumAndMultiply(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n=len(s)
        prefix=[0]*(n+1)
        prefix_num=[0]*(n+1)
        prefix_nonzeros=[0]*(n+1)
        prefix_pow=[1]*(n+1)
        for i in range(1,n+1):
            if s[i-1]=="0":
                prefix_num[i]=(prefix_num[i-1])%(10**9 +7)
                prefix_nonzeros[i]=prefix_nonzeros[i-1]
            else:
                prefix_num[i]=(prefix_num[i-1]*10 + int(s[i-1]))%(10**9 + 7)
                prefix_nonzeros[i]=prefix_nonzeros[i-1]+1
            prefix_pow[i]=prefix_pow[i-1]*10%(10**9 + 7)
            prefix[i]=(prefix[i-1] + int(s[i-1]))%(10**9 + 7)
        arr=[]
        for l,r in queries:
            length=prefix_nonzeros[r+1]-prefix_nonzeros[l]
            exp=prefix_pow[length]
            num1_int=((prefix_num[l])*exp)%(10**9 + 7)
            num2_int=(prefix_num[r+1])%(10**9 + 7)
            arr.append(((num2_int-num1_int)*(prefix[r+1]-prefix[l]))%(10**9 +7))
        return arr

        