class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n=len(s)
        m=len(wordDict)
        dp=[False for _ in range(n+1)]
        dp[0]=True
        for i in range(n):
            for word in wordDict:
                start=i+1-len(word)
                if start>=0 and s[start:i+1] in wordDict and dp[start]:
                    dp[i+1]|=dp[start]
        return dp[n]



