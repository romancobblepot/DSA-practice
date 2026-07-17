from collections import Counter
class Solution(object):
    def gcdValues(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        mapp=Counter(nums)
        def no_divisible_by(mapp,k,arr,maxi):
            start=k
            multiplier=1
            count=0
            while start<=maxi:
                count+=mapp.get(start,0)
                multiplier+=1
                start=k*multiplier
            arr[k]=count*(count-1)/2
        maxi=max(nums)
        arr=[0]*(maxi+1)
        for k in range(1,maxi+1):
            no_divisible_by(mapp,k,arr,maxi)
        for k in range(maxi,0,-1):
            multiplier=2
            start=k*multiplier
            while start<=maxi:
                arr[k]-=(arr[start])
                multiplier+=1
                start=k*multiplier
        prefix_sum=[0]*(len(arr))
        for i in range(1,len(arr)):
            prefix_sum[i]=prefix_sum[i-1]+arr[i]
        def lowerBound(nums,target):
            low=0
            high=len(nums)-1
            while low<=high:
                mid=low+(high-low)//2
                if nums[mid]<=target:
                    low=mid+1
                else:
                    high=mid-1
            return low
        ans=[]
        for q in queries:
            ans.append(lowerBound(prefix_sum,q))
        return ans




        