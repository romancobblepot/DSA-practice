class Solution(object):
    def minExtraChar(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: int
        """
        n=len(s)
        dp=[0]*(n+1)
        for i in range(len(s)):
            dp[i+1]=dp[i]+1
            for word in dictionary:
                start=i-len(word)+1
                if start>=0 and s[start:i+1] in dictionary:
                    dp[i+1]=min(dp[start],dp[i+1])
        return dp[n]
                    
        