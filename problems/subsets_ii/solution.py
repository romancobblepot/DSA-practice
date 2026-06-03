class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        def backtrack(idx,nums,ans,arr):
            if len(arr)==len(nums):
                return
            for i in range(idx,len(nums)):
                if i>idx and nums[i]==nums[i-1]:
                    continue
                arr.append(nums[i])
                ans.append(arr[:])
                backtrack(i+1,nums,ans,arr)
                arr.pop()
        ans=[[]]
        backtrack(0,nums,ans,[])
        return ans
        