class Solution(object):
    def is_possible(self,nums,days,k,m):
      bouquets=0
      count=0
      for num in nums:
        if num<=days:
          count+=1
          if count==k:
            bouquets+=1
            count=0
        else:
          count=0
      return bouquets>=m
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        low=min(bloomDay)
        high=max(bloomDay)
        n=len(bloomDay)
        if n<(k*m):
            return -1
        ans=-1
        while low<=high:
            mid=(low+high)//2
            if self.is_possible(bloomDay,mid,k,m):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans    