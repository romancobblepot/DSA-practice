import math
class Solution(object):
    def subsequencePairCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        n=len(nums)
        max_element=max(nums)
        dp=[[[0]*(max_element+1) for _ in range(max_element+1)] for _ in range(n+1)]
        dp[0][0][0]=1
        for i in range(1,n+1):
            for gcd1 in range(max_element+1):
                new_gcd1=gcd(gcd1,nums[i-1])
                for gcd2 in range(max_element+1):
                    if dp[i-1][gcd1][gcd2]==0:
                        continue
                    new_gcd2=gcd(gcd2,nums[i-1])
                    dp[i][gcd1][gcd2]+=dp[i-1][gcd1][gcd2]
                    dp[i][new_gcd1][gcd2]+=dp[i-1][gcd1][gcd2]
                    dp[i][gcd1][new_gcd2]+=dp[i-1][gcd1][gcd2]
        total=0
        for gcd in range(1,max_element+1):
            total+=dp[n][gcd][gcd]
        return total%(10**9 + 7)




        