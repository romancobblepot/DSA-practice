class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(idx,arr,ans):
            if len(arr)==len(nums):
                return
            for i in range(idx,len(nums)):
                arr.append(nums[i])
                ans.append(arr[:])
                backtrack(i+1,arr,ans)
                arr.pop()
        ans=[[]]
        backtrack(0,[],ans)
        return ans
            
        