class Solution(object):

    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        def daystoship(weights,capacity,Days):
            count=0
            days=0
            for weight in weights:
                count+=weight
                if count==capacity:
                    days+=1
                    count=0
                elif count>capacity:
                    days+=1
                    count=weight
            if count>0:
                days+=1
            return days<=Days
        low=max(weights)
        high=sum(weights)
        ans=-1
        while low<=high:
            mid=low+(high-low)//2
            if not daystoship(weights,mid,days):
                low=mid+1
            else:
                ans=mid
                high=mid-1
        return ans



        