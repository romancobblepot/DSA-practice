class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        def backtrack(idx,s,wordDict,memo):
            if idx==len(s):
                return True
            for i in range(idx,len(s)):
                if idx not in memo:
                    s2=s[idx:i+1]
                    if s2 in wordDict:
                        l=backtrack(i+1,s,wordDict,memo)
                        if l:
                            memo[idx]=True
                            return True
                else:
                    return memo[idx]
            if idx not in memo:
                memo[idx]=False
            return False
        memo={}
        wordSet=set(wordDict)
        return backtrack(0,s,wordSet,memo)
                
        