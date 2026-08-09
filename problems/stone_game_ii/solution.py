class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        n=len(piles)
        dp=[[0]*(n+1) for _ in range(n+1)]
        score=0
        for i in range(n-1,-1,-1):
            score+=piles[i]
            for m in range(1,n+1):
                j_take=0
                for j in range(min(n-i,2*m)):
                    j_take=max(j_take,score-dp[i+j+1][max(m,j+1)])
                dp[i][m]=j_take
        return dp[0][1]

            



        