class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort(key=lambda x:x[0])
        dp=[1]*(len(pairs)+1)
        dp[0]=0
        max_len=0
        for i in range(len(pairs)):
            for j in range(i):
                if pairs[i][0]>pairs[j][1]:
                    dp[i+1]=max(dp[i+1],dp[j+1]+1)
            max_len=max(max_len,dp[i+1])
        return max_len

        