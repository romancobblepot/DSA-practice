class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        def longestcommonSubsequence(s,t):
            n=len(s)
            m=len(t)
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
        return longestcommonSubsequence(s,t)
        