class Solution(object):
    def boxCheck(self,board,i,j):
        seen=set()
        for k in range(i,i+3):
            for l in range(j,j+3):
                if board[k][l] in seen:
                    return False
                if board[k][l]!=".":
                    seen.add(board[k][l])
        return True
    def columnCheck(self,board,j):
        seen=set()
        for i in range(len(board)):
            if board[i][j] in seen:
                return False
            if board[i][j]!=".":
                seen.add(board[i][j])
        return True
    def RowCheck(self,board,i):
        seen=set()
        for j in range(len(board)):
            if board[i][j] in seen:
                return False
            if board[i][j]!=".":
                seen.add(board[i][j])
        return True
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for j in range(len(board)):
            if not self.columnCheck(board,j):
                return False
        for i in range(len(board)):
            if not self.RowCheck(board,i):
                return False
        for i in range(0,len(board),3):
            for j in range(0,len(board),3):
                if not self.boxCheck(board,i,j):
                    return False
        return True



        