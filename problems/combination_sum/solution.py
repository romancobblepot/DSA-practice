class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(i,candidates,target,sum,ans,arr):
            if sum==target:
                ans.append(arr[:])
                return
            if i>=len(candidates) or sum>target:
                return
            sum+=candidates[i]
            arr.append(candidates[i])
            backtrack(i,candidates,target,sum,ans,arr)
            sum-=candidates[i]
            arr.pop()
            backtrack(i+1,candidates,target,sum,ans,arr)
        ans=[]
        backtrack(0,candidates,target,0,ans,[])
        return ans


        