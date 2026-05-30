class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)
        max_l=0
        max_r=0
        max_length=0
        for i in range(n):
            even_odd=[(i,i),(i,i+1)]
            for x,y in even_odd:
                l=x
                r=y
                while l>=0 and r<n:
                    if s[l]==s[r]:
                        if (r-l+1)>max_length:
                            max_length=r-l+1
                            max_l=l
                            max_r=r
                    else:
                        break
                    r+=1
                    l-=1
        return s[max_l:max_r + 1]
            
        
        