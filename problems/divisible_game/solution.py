class Solution(object):
    def divisibleGame(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidates = set()
        for x in nums:
            d = 2
            while d * d <= x:
                if x % d == 0:
                    candidates.add(d)
                    candidates.add(x // d)
                d += 1
            if x > 1:
                candidates.add(x)
        best_score = -min(nums)
        best_k = 2
        for k in candidates:
            curr = None
            best = float('-inf')
            for x in nums:
                val = x if x % k == 0 else -x
                if curr is None:
                    curr = val
                else:
                    curr = max(val, curr + val)
                best = max(best, curr)
            if best > best_score or (best == best_score and k < best_k):
                best_score = best
                best_k = k
        return (best_score * best_k) % (10**9 + 7)
        
            
                
                
                    
                    
        