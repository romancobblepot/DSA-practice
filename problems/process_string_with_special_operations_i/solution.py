class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=[]
        for ch in s:
            if ch<='z' and ch>='a':
                res.append(ch)
            elif ch=="*":
                if res:
                    res.pop()
            elif ch=="#":
                temp=res[:]
                for t in temp:
                    res.append(t)
            else:
                res.reverse()
        return ''.join(res)

        