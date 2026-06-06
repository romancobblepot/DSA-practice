class Solution(object):
    def NSE(self,nums):
        stack=[]
        ans=[len(nums)]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            current_element=nums[i]
            while stack and nums[stack[-1]]>=current_element:
                stack.pop()
            if stack:
                ans[i]=stack[-1]
            stack.append(i)
        return ans
    def PSE(self,nums):
        stack=[]
        ans=[-1]*len(nums)
        for i in range(len(nums)):
            current_element=nums[i]
            while stack and nums[stack[-1]]>=current_element:
                stack.pop()
            if stack:
                ans[i]=stack[-1]
            stack.append(i)
        return ans
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        nse=self.NSE(heights)
        pse=self.PSE(heights)
        max_area=0
        for i in range(len(heights)):
            if pse[i]!=-1:
                max_area=max(max_area,heights[i]*(nse[i]-pse[i]-1))
            else:
                max_area=max(max_area,heights[i]*(nse[i]))
        return max_area
        