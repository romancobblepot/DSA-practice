class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        n=len(heights)
        m=len(heights[0])
        visited=[[False]*m for _ in range(n)]
        pacific=set()
        q=deque()
        for i in range(n):
            q.append((i,0))
            pacific.add((i,0))
            visited[i][0]=True
        for j in range(m):
            q.append((0,j))
            pacific.add((0,j))
            visited[0][j]=True
        def isValid(i,j):
            if i<0 or i>=n: return False
            if j<0 or j>=m: return False
            return True
        delRow=[0,-1,0,1]
        delCol=[-1,0,1,0]
        while q:
            row,col=q.popleft()
            for k in range(4):
                nrow=row+delRow[k]
                ncol=col+delCol[k]
                if isValid(nrow,ncol) and not visited[nrow][ncol]:
                    if heights[nrow][ncol]>=heights[row][col]:
                        pacific.add((nrow,ncol))
                        visited[nrow][ncol]=True
                        q.append((nrow,ncol))
        visited=[[False]*m for _ in range(n)]
        atlantic=set()
        q=deque()
        for i in range(n):
            q.append((i,m-1))
            atlantic.add((i,m-1))
            visited[i][m-1]=True
        for j in range(m):
            q.append((n-1,j))
            atlantic.add((n-1,j))
            visited[n-1][j]=True
        def isValid(i,j):
            if i<0 or i>=n: return False
            if j<0 or j>=m: return False
            return True
        delRow=[0,-1,0,1]
        delCol=[-1,0,1,0]
        while q:
            row,col=q.popleft()
            for k in range(4):
                nrow=row+delRow[k]
                ncol=col+delCol[k]
                if isValid(nrow,ncol) and not visited[nrow][ncol]:
                    if heights[nrow][ncol]>=heights[row][col]:
                        atlantic.add((nrow,ncol))
                        visited[nrow][ncol]=True
                        q.append((nrow,ncol))   
        common=pacific & atlantic
        res=[]
        for i,j in common:
            res.append([i,j])
        return res   




        



        