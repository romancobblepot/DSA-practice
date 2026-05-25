class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n=len(nums)
        if len(nums)==1:
            return False
        prefix_map={0:-1}
        prefix_sum=0
        for i in range(n):
            prefix_sum+=nums[i]
            if not prefix_sum%k in prefix_map:
                prefix_map[prefix_sum%k]=i
            else:
                if i-prefix_map[prefix_sum%k]>=2:
                    return True
        return False
        


        