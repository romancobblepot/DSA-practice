class Solution(object):
    def minimumMountainRemovals(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr=nums
        n=len(arr)
        dp=[1 for _ in range(n)]
        for i in range(n):
            for j in range(i):
                if arr[i]>arr[j]:
                    if dp[i]<dp[j]+1:
                        dp[i]=dp[j]+1
        dp1=[0]*n
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if arr[i]>arr[j]:
                    if dp1[i]<dp1[j]+1:
                        dp1[i]=dp1[j]+1
        max_len=0
        for i in range(n):
            if dp[i]!=1 and dp1[i]!=0:
                dp[i]+=dp1[i]
                max_len=max(dp[i],max_len)
        return n-max_len
        