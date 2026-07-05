class Solution(object):
    def pathsWithMaxScore(self, board):
        """
        :type board: List[str]
        :rtype: List[int]
        """
        n=len(board)
        m=len(board[0])
        max_sum=0
        for i in range(n):
            for j in range(m):
                if board[i][j] not in 'SEX':
                    max_sum+=int(board[i][j])
        dp=[[0]*(m) for _ in range(n)]
        dp2=[[0]*(m) for _ in range(n)]
        dp2[n-1][m-1]=1
        def isValid(i,j):
            if i<0 or i>=n: return False
            if j<0 or j>=m: return False
            return True
        delRow=[0,1,1]
        delCol=[1,1,0]
        mapp=defaultdict(int)
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                flag=False
                if board[i][j]!='X':
                    max_value=0
                    for k in range(3):
                        nrow=i+delRow[k]
                        ncol=j+delCol[k]
                        if isValid(nrow,ncol) and board[nrow][ncol]!='X' and dp[nrow][ncol]!=0:
                            flag=True
                            if dp[nrow][ncol]>max_value:
                                dp2[i][j]=dp2[nrow][ncol]
                            elif dp[nrow][ncol]==max_value:
                                dp2[i][j]+=dp2[nrow][ncol]
                            max_value=max(max_value,dp[nrow][ncol])
                        elif isValid(nrow,ncol) and board[nrow][ncol]=='S':
                            if dp[nrow][ncol]>max_value:
                                dp2[i][j]=dp2[nrow][ncol]
                            elif dp[nrow][ncol]==max_value:
                                dp2[i][j]+=dp2[nrow][ncol]
                            flag=True
                            max_value=max(max_value,dp[nrow][ncol])
                    if not flag:
                        continue
                    if board[i][j] in 'SE':
                        dp[i][j]=max(dp[i][j],max_value)
                    else: 
                        dp[i][j]=max(dp[i][j],max_value+int(board[i][j]))     
        if not flag:
            return [0,0]
        return dp[0][0],dp2[0][0]%(10**9+7)




        