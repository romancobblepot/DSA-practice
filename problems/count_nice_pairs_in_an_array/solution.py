class Solution(object):
    def countNicePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def reverse(n):
            if n<0:
                sign=-1
            else:
                sign=1
            reversed_sum=0
            N=abs(n)
            while N>0:
                last_digit=N%10
                reversed_sum=(reversed_sum)*10 + last_digit
                N=N//10
            return reversed_sum*sign
        n=len(nums)
        for i in range(len(nums)):
            nums[i]-=reverse(nums[i])
        count=0
        hash_map=defaultdict(int)
        for i in range(len(nums)):
            if nums[i] in hash_map:
                count+=hash_map[nums[i]]
            hash_map[nums[i]]+=1
        return count%(10**9 + 7)
        

            
        