import heapq
class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        q=[]
        n=len(heights)
        m=len(heights[0])
        def isValid(i,j,n,m):
            if i<0 or i>=n: return False
            if j<0 or j>=m: return False
            return True
        distance=[[float('inf')]*m for _ in range(n)]
        distance[0][0]=0
        heapq.heappush(q,(0,0,0))
        delRow=[0,-1,0,1]
        delCol=[-1,0,1,0]
        while q:
            max_difference,row,col=heapq.heappop(q)
            if row==n-1 and col==m-1:
                return max_difference
            for k in range(4):
                nrow=row+delRow[k]
                ncol=col+delCol[k]
                if isValid(nrow,ncol,n,m) and max(max_difference,abs(heights[row][col]-heights[nrow][ncol]))<distance[nrow][ncol]:
                    distance[nrow][ncol]=max(max_difference,abs(heights[row][col]-heights[nrow][ncol]))
                    heapq.heappush(q,(distance[nrow][ncol],nrow,ncol))
        return 0

        