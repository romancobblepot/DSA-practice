class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numbers=set(nums)
        max_len=0
        for num in numbers:
            if num-1 not in numbers:
                start=num
                count=1
                while start+1 in numbers:
                    start+=1
                    count+=1
                max_len=max(max_len,count)
        return max_len
            