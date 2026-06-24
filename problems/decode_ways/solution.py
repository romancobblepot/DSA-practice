class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        dp=[0 for _ in range(n+1)]
        if s[0]!="0":
            dp[1]=1
        dp[0]=1
        for i in range(1,n):
            if s[i]=="0":
                if s[i-1]=="0":
                    continue
                else:
                    if int(s[i-1]+s[i])<=26:
                        dp[i+1]=dp[i-1]
                continue            
            if s[i-1]=="0":
                dp[i+1]=dp[i]
                continue
            taken=0
            if int(s[i-1]+s[i])<=26:
                taken=dp[i-1]
            non_taken=dp[i]
            dp[i+1]+=taken+non_taken
        return dp[n]


        