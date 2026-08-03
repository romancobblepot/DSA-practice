class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        n=len(stoneValue)
        dp=[0]*(n+3)
        for i in range(n-1,-1,-1):
            one_move=stoneValue[i]-dp[i+1]
            two_move=float('-inf')
            if i+1<n:
                two_move=stoneValue[i]+stoneValue[i+1]-dp[i+2]
            three_move=float('-inf')
            if i+2<n:
                three_move=stoneValue[i]+stoneValue[i+1]+stoneValue[i+2]-dp[i+3]
            dp[i]=max(one_move,two_move,three_move)
        if dp[0]==0:
            return "Tie"
        elif dp[0]>0:
            return "Alice"
        else:
            return "Bob"




        