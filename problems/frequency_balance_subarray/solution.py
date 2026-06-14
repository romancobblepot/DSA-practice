class Solution(object):
    def getLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 1
        for l in range(n):
            freq = defaultdict(int)
            cnt = defaultdict(int)
            for r in range(l, n):
                x = nums[r]
                old = freq[x]
                if old:
                    cnt[old] -= 1
                    if cnt[old] == 0:
                        del cnt[old]
                freq[x] += 1
                new = freq[x]
                cnt[new] += 1
                freqs = sorted(cnt.keys())
                balanced = False
                if len(freqs) == 1:
                    f=freqs[0]
                    if cnt[f] == 1:
                        balanced = True
                elif len(freqs) == 2:
                    a, b = freqs
                    if b == 2 * a:
                        balanced = True
                if balanced:
                    ans = max(ans, r - l + 1)
        return ans
                    
                    
                    
                    
                        
                        
                        
            
            