class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        def backtrack(idx,candidates,target,sum,arr,ans):
            if sum==target:
                ans.append(arr[:])
                return 
            if sum>target:
                return
            for i in range(idx,len(candidates)):
                    if i>idx and candidates[i]==candidates[i-1]:
                        continue
                    sum+=candidates[i]
                    arr.append(candidates[i])
                    backtrack(i+1,candidates,target,sum,arr,ans)
                    sum-=candidates[i]
                    arr.pop()
        ans=[]
        arr=[]
        backtrack(0,candidates,target,0,arr,ans)
        return ans
