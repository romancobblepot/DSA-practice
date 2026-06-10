class Solution(object):
    def longestPalindromicSubsequence(self,s):
        def longestCommonSubsequence(s,t):
            n=len(s)
            m=len(t)
            if m>n:
                n,m=m,n
                s,t=t,s
            prev=[0]*(m+1)
            for i in range(1,n+1):
                curr=[0]*(m+1)
                for j in range(1,m+1):
                    if s[i-1]==t[j-1]:
                        curr[j]=1+prev[j-1]
                    else:
                        curr[j]=max(prev[j],curr[j-1])
                prev=curr
            return prev[m]
        t=s[::-1]
        return longestCommonSubsequence(s,t)   
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        k=self.longestPalindromicSubsequence(s)
        n=len(s)
        return n-k
        