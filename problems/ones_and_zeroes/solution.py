class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        l=len(strs)
        dp=[[[0]*(n+1) for _ in range(m+1)] for _ in range(len(strs)+1)]
        for g in range(len(strs)):
            zeros=strs[g].count('0')
            ones=strs[g].count('1')
            for i in range(m+1):
                for j in range(n+1):
                    if i==0 and j==0:
                        continue
                    non_pick=dp[g][i][j]
                    pick=0
                    if i>=zeros and j>=ones:
                        pick=dp[g][i-zeros][j-ones]+1
                    dp[g+1][i][j]=max(non_pick,pick)
        return dp[len(strs)][m][n]


        