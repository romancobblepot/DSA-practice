class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapp={'a':-1,'b':-1,'c':-1}
        l=0
        n=len(s)
        r=0
        length=3
        total=0
        while r<n:
            if s[r] in mapp:
                mapp[s[r]]=r
                total+=1+min(mapp.values())
                r+=1
        return total





            



        