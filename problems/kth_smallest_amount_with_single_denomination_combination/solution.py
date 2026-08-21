class Solution(object):
    def gcd(self,a,b):
        while b:
            a,b=b,a%b
        return a
    def lcm(self,a,b):
        if a==0 or b==0:
            return 0
        return a*b//(self.gcd(a,b))
    def count_nums(self,num,coins):
        n=len(coins)
        ans=0
        for mask in range(1,1<<n):
            l=1
            count=0
            for i in range(n):
                if mask & 1<<i:
                    l=self.lcm(l,coins[i])
                    count+=1
                if l>num:
                    break
            if l>num:
                continue
            if count%2==0:
                ans-=num//l
            else:
                ans+=num//l
        return ans
    def findKthSmallest(self, coins, k):
        """
        :type coins: List[int]
        :type k: int
        :rtype: int
        """
        low=min(coins)
        high=min(coins)*(k)
        while low<high:
            mid=low+(high-low)//2
            if self.count_nums(mid,coins)<k:
                low=mid+1
            else:
                high=mid
        return low


        