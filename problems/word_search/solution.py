class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        n=len(board)
        m=len(board[0])
        def dfs(i,j,board,word,count):
            if count==len(word):
                return True
            if i<0 or i>=n or j<0 or j>=m or board[i][j]!=word[count]:
                return False
            char=board[i][j]
            board[i][j]="#"
            found=(dfs(i,j-1,board,word,count+1) or
            dfs(i-1,j,board,word,count+1) or
            dfs(i,j+1,board,word,count+1) or
            dfs(i+1,j,board,word,count+1)
            )
            board[i][j]=char
            return found
        for i in range(n):
            for j in range(m):
                if dfs(i,j,board,word,0):
                    return True
        return False




        