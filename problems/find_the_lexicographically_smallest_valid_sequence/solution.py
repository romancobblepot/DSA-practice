class Solution(object):
    def validSequence(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: List[int]
        """
        n=len(word1)
        m=len(word2)
        dp=[0]*(n+1)
        for i in range(n-1,-1,-1):
            if dp[i+1]<m and word1[i]==word2[m-dp[i+1]-1]:
                dp[i]=dp[i+1]+1
            else:
                dp[i]=dp[i+1]
        ans=[]
        flag=False
        with_replacement=0
        for i in range(n):
            if with_replacement<m:
                if word1[i]==word2[with_replacement]:
                    ans.append(i)
                    with_replacement+=1
                else:
                    if not flag and dp[i+1]>=(m-with_replacement-1):
                        flag=True
                        ans.append(i)
                        with_replacement+=1
        if len(ans)<len(word2):
            return []
        return ans







        