class Solution(object):
    def numWays(self, words, target):
        """
        :type words: List[str]
        :type target: str
        :rtype: int
        """
        m=len(target)
        n=len(words[0])
        arr=[]
        for i in range(n):
            freq=defaultdict(int)
            for j in range(len(words)):
                freq[words[j][i]]+=1
            arr.append(freq)
        dp=[[0]*(m+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0]=1
        for i in range(1,n+1):
            freq=arr[i-1]
            for j in range(1,m+1):
                if target[j-1] in freq:
                    dp[i][j]+=dp[i-1][j-1]*(freq[target[j-1]])+dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[n][m]%(10**9 + 7)


        