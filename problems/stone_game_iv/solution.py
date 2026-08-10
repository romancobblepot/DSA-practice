class Solution(object):
    def winnerSquareGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        squares=[]
        m=1
        while m*m<=n:
            squares.append(m*m)
            m+=1
        squares_set=set(squares)
        dp=[[False]*2 for _ in range(n+1)]
        for i in range(n,-1,-1):
            for j in range(2):
                for k in squares:
                    if i+k<=n:
                        if j==0:
                            if not dp[i+k][1]:
                                dp[i][j]=True
                                break
                        else:   
                            if not dp[i+k][0]:
                                dp[i][j]=True
                                break
                    else:
                        break
        return dp[0][0]








        