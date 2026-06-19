class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        dp=[[float('inf')]*(n) for _ in range(n)]
        for i in range(n):
            dp[i][i]=1
        for g in range(2,len(s)+1):
            for i in range(len(s)-g+1):
                j=i+g-1
                for k in range(i,j):
                    if s[i]==s[j]:
                        if s[k]!=s[i]:
                            dp[i][j]=min(dp[i][k]+dp[k+1][j],dp[i][j])
                        else:
                            dp[i][j]=dp[i][j-1]
                    else:
                        dp[i][j]=min(dp[i][k]+dp[k+1][j],dp[i][j])
        return dp[0][len(s)-1]


        