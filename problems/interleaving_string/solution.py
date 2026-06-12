class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        n=len(s1)
        m=len(s2)
        if n+m<len(s3):
            return False
        dp=[False for _ in range(m+1)]
        dp[0]=True
        for i in range(1,m+1):
            if (i-1)<len(s3) and s2[i-1]==s3[i-1]:
                dp[i]=dp[i-1]
        for i in range(1,n+1):
            curr=[False for _ in range(m+1)]
            for j in range(m+1):
                if (i+j-1)<len(s3) and j>0 and i>0 and s1[i-1]==s3[i+j-1] and s2[j-1]==s3[i+j-1]:
                    curr[j]=dp[j] or curr[j-1]
                elif (i+j-1)<len(s3) and s1[i-1]==s3[i+j-1]:
                    curr[j]=dp[j]
                elif (i+j-1)<len(s3) and j>0 and s2[j-1]==s3[i+j-1]:
                    curr[j]=curr[j-1]
                else:
                    curr[j]=False
            dp=curr
        return dp[m]


        