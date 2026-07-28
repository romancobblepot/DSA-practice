class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        mid=len(s)//2
        if len(s)%2!=0:
            s1="".join(sorted(s[:mid]))
            return s1+s[mid]+s1[::-1]
        else:
            s1="".join(sorted(s[:mid]))
            return s1+s1[::-1]


        