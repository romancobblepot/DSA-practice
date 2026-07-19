from collections import Counter
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        last_seen=defaultdict(int)
        visited=set()
        for i in range(len(s)):
            last_seen[s[i]]=i
        for i in range(len(s)):
            while stack and ord(stack[-1])>=ord(s[i]) and last_seen[stack[-1]]>i and s[i] not in visited:                 
                    visited.remove(stack.pop())
            if s[i] not in visited:                
                stack.append(s[i])
                visited.add(s[i])
        return ''.join(stack)

            


        

        