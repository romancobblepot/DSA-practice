class Solution(object):
    def maxDigitRange(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq=defaultdict(list)
        for num in nums:
            n=num
            smallest=9
            largest=0
            while n>0:
                dig=n%10
                smallest=min(smallest,dig)
                largest=max(largest,dig)
                n=n//10
            diff=largest-smallest
            freq[diff].append(num)
        key=max(freq.keys())
        sum=0
        for i in freq[key]:
            sum+=i
        return sum
        
            
                
        