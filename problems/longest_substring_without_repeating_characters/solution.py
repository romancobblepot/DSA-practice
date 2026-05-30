class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen=set()
        l=0
        r=0
        n=len(s)
        max_length=0
        if len(s)==0:
            return 0
        while r<n:
            if s[r] not in seen:
                seen.add(s[r])
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l+=1
                seen.add(s[r])
            max_length=max(max_length,r-l+1)
            r+=1 
        return max_length

        