class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        def backtrack(idx,sum,target,arr,ans):            
            if sum>target:
                return
            if sum==target:
                ans.append(arr[:])
                return 
            for i in range(idx,len(candidates)):
                if candidates[i]==candidates[i-1] and i>idx:
                    continue
                if candidates[i]>target-sum:
                    continue
                sum+=candidates[i]
                arr.append(candidates[i])
                backtrack(i+1,sum,target,arr,ans)
                arr.pop()
                sum-=candidates[i]
        ans=[]
        backtrack(0,0,target,[],ans)
        return ans
        