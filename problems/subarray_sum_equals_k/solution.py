class Solution:
    def subarraySum(self, nums, k):
        sum1 = 0
        count = 0
        freq = {0: 1}          # prefix sum 0 appears once (before starting)

        for num in nums:
            sum1 += num

        # If we previously saw (sum1 - k), then subarray sum = k
            if (sum1 - k) in freq:
                count += freq[ (sum1 - k) ]

        # Record current prefix sum
            freq[sum1] = freq.get(sum1, 0) + 1

        return count

      