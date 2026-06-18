class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        def wordBreak(s,words):
            n=len(s)
            m=len(words)
            dp=[False for _ in range(n+1)]
            dp[0]=True
            for i in range(n):
                for j in range(i+1):
                    if s[j:i+1] in words and dp[j] and s[j:i+1]!=s:
                        dp[i+1]|=dp[j]
            return dp[n]
        concat=[False]*(len(words))
        wordsSet=set(words)
        for i in range(len(words)):
            concat[i]=wordBreak(words[i],wordsSet)
        ans=[]
        for i in range(len(concat)):
            if concat[i]:
                ans.append(words[i])
        return ans



        