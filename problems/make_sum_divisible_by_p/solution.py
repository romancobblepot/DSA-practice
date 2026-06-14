class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        n=len(nums)
        prefix=[0]*(n+1)
        for i in range(1,n+1):
            prefix[i]=prefix[i-1]+nums[i-1]
        hash_map={0:0}
        min_len=float('inf')
        need=prefix[-1]%p
        if need==0:
            return 0
        for i in range(1,len(prefix)):
            prefix_num=prefix[i]
            if ((-need+prefix_num)%p) in hash_map:
                min_len=min(min_len,i-hash_map[(-need+prefix_num)%p])
            hash_map[prefix_num%p]=i
        if min_len==float('inf') or min_len==n:
            return -1
        return min_len
            

        
        