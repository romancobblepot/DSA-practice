class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        freq=defaultdict(int)
        l=0
        r=0
        max_len=0
        while r<n:
            freq[s[r]]+=1
            while freq[s[r]]>2:
                freq[s[l]]-=1
                l+=1
            max_len=max(max_len,r-l+1)
            r+=1
        return max_len
            

        