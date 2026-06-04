class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def palindromeCheck(l,r,s):
            count=0
            while l>=0 and r<len(s) and s[l]==s[r]:
                count+=1
                l-=1
                r+=1
            return count
        count_odd=0
        count_even=0
        for i in range(len(s)):
            count_odd+=palindromeCheck(i,i,s)
            count_even+=palindromeCheck(i,i+1,s)
        return count_odd+count_even
        