class Solution(object):
    def NSE(self,nums):
        stack=[]
        n=len(nums)
        ans=[n]*n
        for i in range(n-1,-1,-1):
            while stack and nums[stack[-1]]>=nums[i]:
                stack.pop()
            if stack:
                ans[i]=stack[-1]
            stack.append(i)
        return ans
    def PSE(self,nums):
        stack=[]
        n=len(nums)
        ans=[-1]*n
        for i in range(n):
            while stack and nums[stack[-1]]>=nums[i]:
                stack.pop()
            if stack:
                ans[i]=stack[-1]
            stack.append(i)
        return ans
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        nse=self.NSE(nums)
        pse=self.PSE(nums)
        max_score=float('-inf')
        for i in range(n):
            left_start=pse[i]
            right_end=nse[i]
            if left_start>=k or right_end<=k:
                continue
            max_score=max(max_score,nums[i]*(right_end-1-left_start))             
        return max_score

        

        