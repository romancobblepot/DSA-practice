from collections import Counter
class Solution(object):
    def group(self,s):
        ans=[]
        count=1
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                count+=1
            else:
                ans.append((count,s[i-1]))
                count=1
        if s:
            ans.append((count,s[-1]))
        return ans
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result="1"
        for i in range(n-1):
            mapp=self.group(result)
            ans=""
            for u,v in mapp:
                ans+=str(u)+(v)
            result=ans  
        return result
        
        