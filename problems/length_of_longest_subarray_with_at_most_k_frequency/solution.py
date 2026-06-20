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
        cnt=defaultdict(int)
        max_len=0
        max_freq=0
        while r<n:
            cnt[freq[nums[r]]]-=1
            freq[nums[r]]+=1
            cnt[freq[nums[r]]]+=1
            max_freq=max(max_freq,freq[nums[r]])
            if max_freq>k:
                while cnt[max_freq]>0:
                    cnt[freq[nums[l]]]-=1
                    freq[nums[l]]-=1
                    l+=1
            max_len=max(max_len,r-l+1)
            r+=1
        return max_len
        
                
        