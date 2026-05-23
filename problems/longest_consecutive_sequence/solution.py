class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numbers=set()
        for i in range(len(nums)):
            numbers.add(nums[i])
        max_count=0
        for num in numbers:
            if num-1 not in numbers:
                    start=num
                    count=1
                    while start+1 in numbers:
                        count+=1
                        start=start+1
                    max_count=max(count,max_count)
        return max_count