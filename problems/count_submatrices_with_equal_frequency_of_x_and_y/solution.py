class Solution(object):
    def numberOfSubmatrices(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        x=0
        y=0
        n=len(grid)
        m=len(grid[0])
        prev_x=[0]*(m+1)
        prev_y=[0]*(m+1)
        curr_x=[0]*(m+1)
        curr_y=[0]*(m+1)
        count=0
        for r in range(n):
            runing_x=0
            runing_y=0
            for c in range(m):
                if grid[r][c]=="X":
                    runing_x+=1
                elif grid[r][c]=="Y":
                    runing_y+=1
                curr_x[c+1]+=runing_x
                curr_y[c+1]+=runing_y
                if curr_x[c+1]>=1 and curr_x[c+1]==curr_y[c+1]:
                    count+=1
        return count

        