class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n=len(points)
        ans=1
        for i in range(n):
            slopes={}
            for j in range(i+1,n):
                    dy=points[j][1]-points[i][1]
                    dx=points[j][0]-points[i][0]
                    if dx==0:
                        slope=float('inf')
                    else:
                        slope=float(dy)/dx
                    slopes[slope]=slopes.get(slope,0)+1
            if slopes:
                ans= max(ans,max(slopes.values())+1)
        return ans

        