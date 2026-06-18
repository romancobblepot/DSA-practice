class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dp=[[0]*(len(nums)) for _ in range(len(nums))]
        for g in range(1,len(nums)+1):
            j=g-1
            i=0
            while j<len(nums):
                if g==1:
                    dp[i][j]=nums[i]
                elif g==2:
                    dp[i][j]=max(nums[i],nums[j])
                else:
                    dp[i][j]=max(nums[i]+min(dp[i+1][j-1],dp[i+2][j]),nums[j]+min(dp[i+1][j-1],dp[i][j-2]))
                i+=1
                j+=1
        return sum(nums)-2*dp[0][len(nums)-1]<=0

                


        