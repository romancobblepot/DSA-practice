class Solution(object):
    def stoneGameV(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: int
        """
        n=len(stoneValue)
        prefix=[0]*(n+1)
        for i in range(1,n+1):
            prefix[i]=prefix[i-1]+stoneValue[i-1]
        dp=[[0]*n for _ in range(n)]
        max_left=[[0]*n for _ in range(n)]
        max_right=[[0]*n for _ in range(n)]
        for i in range(n):
            max_left[i][i]=stoneValue[i]
            max_right[i][i]=stoneValue[i]
        for g in range(2,n+1):
            for i in range(n-g+1):
                mid=i
                j=i+g-1
                while mid<j and prefix[mid+1]-prefix[i]<prefix[j+1]-prefix[mid+1]:
                    mid+=1
                res=max_left[i][mid-1] if mid>i else 0
                if mid<j and prefix[mid+1]-prefix[i]>prefix[j+1]-prefix[mid+1]:
                     res=max(res,max_right[mid+1][j])
                elif mid<j:
                    res=max(res,max_left[i][mid],max_right[mid+1][j])
                dp[i][j]=res
                max_left[i][j]=max(max_left[i][j-1],dp[i][j]+prefix[j+1]-prefix[i])
                max_right[i][j]=max(max_right[i+1][j],dp[i][j]+prefix[j+1]-prefix[i])
        return dp[0][n-1]

        