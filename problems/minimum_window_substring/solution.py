class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        n=len(s)
        m=len(t)
        char={}
        for i in range(m):
            char[t[i]]=char.get(t[i],0)+1
        min_length=float('inf')
        length=len(char)
        left=0
        right=0
        cnt=0
        start_index=-1
        while right<n:
            if s[right] in char:
                char[s[right]]-=1
                if  char[s[right]]==0:
                    cnt+=1
            while cnt==length:
                if s[left] in char:
                    char[s[left]]+=1
                    if  char[s[left]]>0:
                        cnt-=1
                if (right-left+1)<min_length:
                    start_index=left
                min_length=min(min_length,right-left+1)
                left+=1
            right+=1
        if start_index==-1:
            return ""
        return s[start_index:start_index+min_length]      