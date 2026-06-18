class Solution(object):
    def minCost(self, n, cuts):
        """
        :type n: int
        :type cuts: List[int]
        :rtype: int
        """
        cuts1=[0]+cuts+[n]
        cuts1.sort()
        dp=[[float('inf')]*(len(cuts1)) for _ in range(len(cuts1))]
        for i in range(len(cuts1)):
            dp[i][i]=0
        for g in range(1,len(cuts1)+1):
            for i in range(1,len(cuts1)-g+1):
                j=i+g-1
                for k in range(i,j):
                    dp[i][j]=min(dp[i][k]+dp[k+1][j]+abs(cuts1[j]-cuts1[i-1]),dp[i][j])
        return dp[1][len(cuts1)-1]

        