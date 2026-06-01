class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(i,nums,arr,ans,used):
            if len(arr)==len(nums):
                ans.append(arr[:])
                return 
            for idx in range(len(nums)):
                if not used[idx]:
                    arr.append(nums[idx])
                    used[idx]=True
                    backtrack(idx+1,nums,arr,ans,used)
                    used[idx]=False
                    arr.pop()
        used=[False]*len(nums)
        ans=[]
        arr=[]
        backtrack(0,nums,arr,ans,used)
        return ans

        