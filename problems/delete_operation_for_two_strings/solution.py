class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        str1=word1
        str2=word2
        def longestCommonSubsequence(str1,str2):
            n=len(str1)
            m=len(str2)            
            if m>n:
                n,m=m,n
                str1,str2=str2,str1
            prev=[0]*(m+1)
            for i in range(1,n+1):
                curr=[0]*(m+1)
                for j in range(1,m+1):
                    if str1[i-1]==str2[j-1]:
                        curr[j]=1+prev[j-1]
                    else:
                        curr[j]=max(curr[j-1],prev[j])
                prev=curr
            return prev[m]
        return len(str1)+len(str2)-(2*longestCommonSubsequence(str1,str2))
        