class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def subsequenceCheck(word1,word2):
            n=len(word1)
            m=len(word2)
            if m!=(n+1):
                return False
            i=0
            for j in range(len(word2)):
                if i<n and word2[j]==word1[i]:
                    i+=1
            return (i==n)
        n=len(words)
        dp=[1]*n
        max_len=0
        words.sort(key=len)
        for i in range(n):
            for j in range(i):
                if subsequenceCheck(words[j],words[i]):
                    if dp[i]<=dp[j]+1:
                        dp[i]=dp[j]+1
            if dp[i]>max_len:
                max_len=dp[i]
        return max_len
        