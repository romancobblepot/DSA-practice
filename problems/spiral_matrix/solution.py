class Solution(object):
    def Clockwise(self,i,j,m,n,arr,visited,matrix):
        for k in range(j,n):
            if not visited[i][k]:
                arr.append(matrix[i][k])
                visited[i][k]=True
        for l in range(i+1,m):
            if not visited[l][n-1]:
                arr.append(matrix[l][n-1])
                visited[l][n-1]=True
        for p in range(n-1,j-1,-1):
            if not visited[m-1][p]:
                arr.append(matrix[m-1][p])
                visited[m-1][p]=True
        for q in range(m-1,i-1,-1):
            if not visited[q][j]:
                arr.append(matrix[q][j])
                visited[q][j]=True
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        arr=[]
        m=len(matrix)
        n=len(matrix[0])
        visited=[[False]*n for _ in range(m)]
        row=m
        col=n
        arr=[]
        i=0
        j=0
        while i<len(matrix) and j<len(matrix[0]):
            if row>0 and col>0 and not visited[i][j] :
                self.Clockwise(i,j,row,col,arr,visited,matrix)
                row-=1
                col-=1
            i+=1
            j+=1
        return arr
        