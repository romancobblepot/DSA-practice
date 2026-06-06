class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        freq={}
        l=0
        r=0
        n=len(s)
        max_length=0
        most_freq=0
        while r<n:
            freq[s[r]]=freq.get(s[r],0)+1
            most_freq=max(most_freq,freq[s[r]])
            while (r-l+1)-most_freq>k:
                freq[s[l]]-=1
                l+=1
            max_length=max(max_length,r-l+1)
            r+=1
        return max_length
            
        