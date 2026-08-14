class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l=0
        r=0
        n=len(nums)
        freq=defaultdict(int)
        max_len=0
        while r<n:
            freq[nums[r]]+=1
            while freq[nums[r]]>k:
                freq[nums[l]]-=1
                l+=1
            max_len=max(max_len,r-l+1)
            r+=1
        return max_len
        
                
        