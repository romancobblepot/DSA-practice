class Solution(object):
    def distinctSubseqII(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        dp=[0]*(n+1)
        mapp={}
        for i in range(n):
            if s[i] in mapp:
                dp[i+1]=2*dp[i]-dp[mapp[s[i]]]
            else:
                dp[i+1]=2*dp[i]+1
            mapp[s[i]]=i
        return dp[n]%(10**9 + 7)
        