class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack=[]
        ans=[0]*len(temperatures)
        for i in range(len(temperatures)-1,-1,-1):
            current_element=temperatures[i]
            while stack and temperatures[stack[-1]]<=current_element:
                stack.pop()
            if stack:
                ans[i]=stack[-1]-i
            stack.append(i)
        return ans
        