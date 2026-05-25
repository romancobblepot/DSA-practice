class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        mat=board
        def isValid(i,j,n,m):
            if i<0 or i>=n:
                return False
            if j<0 or j>=m:
                return False
            return True
        def isBoundary(i,j,n,m):
            if i==0 or i==n-1 or j==0 or j==m-1:
                return True
            return False
        n,m=len(mat),len(mat[0])
        q=deque()
        for i in range(n):
            for j in range(m):
                if isBoundary(i,j,n,m):
                    if mat[i][j]=="O":
                        q.append((i,j))
        delRow=[0,-1,0,1]
        delCol=[-1,0,1,0]
        while q:
            row,col=q.popleft()
            mat[row][col]="#"
            for k in range(4):
                nrow=row+delRow[k]
                ncol=col+delCol[k]
                if isValid(nrow,ncol,n,m) and mat[nrow][ncol]=="O":
                    q.append((nrow,ncol))
                    mat[nrow][ncol]="#"
        for i in range(n):
            for j in range(m):
                if mat[i][j]=="O":
                    mat[i][j]="X"
                elif mat[i][j]=="#":
                    mat[i][j]="O"
        