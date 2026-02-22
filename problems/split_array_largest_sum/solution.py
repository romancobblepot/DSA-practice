class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        low=max(nums)
        high=sum(nums)
        while low<=high:
            sum1=0
            count=0
            mid=(low+high)//2
            for num in nums:
                sum1+=num
                if sum1>mid:
                    count+=1
                    sum1=num
            if sum1>0:
                count+=1
            if count<=k:
                high=mid-1
            else:
                low=mid+1
        return low


                    


               