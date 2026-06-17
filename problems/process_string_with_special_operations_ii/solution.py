class Solution(object):
    def processStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        length=0
        for ch in s:
            if ch>='a' and ch<='z':
                length+=1
            elif ch=="#":
                length*=2
            elif ch=="*":
                if length:
                    length-=1
        if k>=length:
            return "."
        for ch in reversed(s):
            if ch=="#":
                length=length//2
                if length>0:
                    k=k%length
            elif ch=="%":
                k=length-k-1
            elif ch>='a' and ch<='z':
                length-=1
                if k==length:
                    return ch
            elif ch=="*":
                length+=1
        
            


        