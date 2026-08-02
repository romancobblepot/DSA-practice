class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        total_stones=sum(piles)
        least_needed=(total_stones)//2 +1
        l=0
        r=len(piles)-1
        dp=[[0]*2 for _ in range(len(piles)//2 +1)]
        for i in range(1,len(piles)//2 +1):
            for j in range(2):
                if j==0:
                    dp[i][j]=piles[r]+max(dp[i-1][0],dp[i-1][1])
                    r-=1
                else:
                     dp[i][j]=piles[l]+max(dp[i-1][0],dp[i-1][1])
                     l+=1
        return max(dp[-1][0],dp[-1][1])>=least_needed




        