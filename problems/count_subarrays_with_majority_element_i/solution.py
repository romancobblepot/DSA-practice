class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n=len(nums)
        count=0
        prefix_count=[0]*(n+1)
        for i in range(1,n+1):
            if nums[i-1]==target:
                prefix_count[i]=prefix_count[i-1]+1
            else:
                prefix_count[i]=prefix_count[i-1]
        for g in range(1,n+1):
            for i in range(n-g+1):
                j=g+i-1
                mapp=prefix_count[j+1]-prefix_count[i]
                if 2*mapp>(g):
                    count+=1
        return count 

        