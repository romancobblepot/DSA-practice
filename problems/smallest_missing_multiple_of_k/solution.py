class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hash_set=set(nums)
        max_multiple=max(nums)//k
        for m in range(1,max_multiple+1):
            if m*k not in hash_set:
                return m*k
        return max_multiple*k +k

