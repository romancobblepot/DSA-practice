class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(idx,target,sum,arr,ans):
            if idx>=len(candidates) or sum>target:
                return
            if sum==target:
                ans.append(arr[:])
                return 
            sum+=candidates[idx]
            arr.append(candidates[idx])
            backtrack(idx,target,sum,arr,ans)
            arr.pop()
            sum-=candidates[idx]
            backtrack(idx+1,target,sum,arr,ans)
        ans=[]
        backtrack(0,target,0,[],ans)
        return ans
        