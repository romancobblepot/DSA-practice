class Solution(object):
    def canMakeSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)>len(t):
            return False
        n=len(s)
        m=len(t)
        without_replacement=0
        with_replacement=0
        for i in range(m):
            if with_replacement<n:
                if s[with_replacement]==t[i]:
                    with_replacement+=1
                else:
                    with_replacement=max(with_replacement,without_replacement+1)
            if without_replacement<n:
                if s[without_replacement]==t[i]:
                    without_replacement+=1
        return with_replacement>=n



        
        
                    
                
                
        
        