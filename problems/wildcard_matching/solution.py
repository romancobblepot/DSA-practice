class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        t=p
        n=len(s)
        m=len(t)
        dp=[[False]*(m+1) for _ in range(n+1)]
        dp[0][0]=True
        for i in range(1,m+1):
            dp[0][i]=(t[i-1]=="*") and dp[0][i-1]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s[i-1]==t[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                elif t[j-1]=="?":
                    dp[i][j]=dp[i-1][j-1]
                elif t[j-1]=="*":
                    dp[i][j]=dp[i][j-1] or dp[i-1][j]
                else:
                    dp[i][j]=False
        return dp[n][m]
        