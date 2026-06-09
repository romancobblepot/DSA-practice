class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        arr=nums
        n=len(arr)
        sum_=sum(arr)
        if sum_%2!=0:
            return False
        target=sum_//2
        prev=[False]*(target+1)
        prev[0]=True
        if arr[0]<=target:
            prev[arr[0]]=True
        for ind in range(1,n):
            curr=[False]*(target+1)
            curr[0]=True
            for sum_ in range(1,target+1):
                non_taken=prev[sum_]
                taken=False
                if arr[ind]<=sum_:
                    taken=prev[sum_-arr[ind]]
                curr[sum_]=taken or non_taken
            prev=curr
        return prev[target]