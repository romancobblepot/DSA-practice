class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def isCeil(num,k):
            if num%k==0:
                return num//k
            return num//k + 1
        low=1
        high=max(piles)
        while low<=high:
            mid=(low+high)//2
            count=0
            for i in range(len(piles)):
                count+=isCeil(piles[i],mid)
            if count<=h:
                high=mid-1
            elif count>h:
                low=mid+1
        return low



        