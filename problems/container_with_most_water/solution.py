
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)
        l=0
        r=n-1
        max_water=0
        while l<r:
            if height[r]>height[l]:
                max_water=max(max_water,(r-l)*height[l])
                l+=1
            else:
                max_water=max(max_water,(r-l)*height[r])
                r-=1
        return max_water

        