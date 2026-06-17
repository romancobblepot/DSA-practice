class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        half_sum=sum(stones)//2
        diff=sum(stones)-2*half_sum
        dp=[[False]*(half_sum+1) for _ in range(len(stones)+1)]
        dp[0][0]=True
        for i in range(1,len(stones)+1):
            for j in range(half_sum+1):
                non_taken=dp[i-1][j]
                taken=False
                if j>=stones[i-1]:
                    taken=dp[i-1][j-stones[i-1]]
                dp[i][j]=taken or non_taken
        arr=dp[-1]
        m=len(arr)
        for i in range(m-1,-1,-1):
            if arr[i]:
                return sum(stones)-2*i
        