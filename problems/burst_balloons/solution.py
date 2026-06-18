class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums1=[1]+nums+[1]
        n=len(nums1)
        dp=[[0]*(len(nums1)) for _ in range(len(nums1))]
        for g in range(2,n+1):
            for i in range(1,n-g+1):
                j=i+g-1
                for k in range(i,j):
                    dp[i][j]=max(dp[i][j],dp[i][k] + dp[k+1][j] + nums1[i-1]*nums1[k]*nums1[j])
        return dp[1][n-1]

        