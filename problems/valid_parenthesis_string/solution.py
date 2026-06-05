class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open_stack=[]
        star_stack=[]
        for i in range(len(s)):
            if s[i]=="(":
                open_stack.append(i)
            elif s[i]=="*":
                star_stack.append(i)
            else:
                if open_stack:
                    open_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
        while open_stack:
            if star_stack:
                if star_stack[-1]>open_stack[-1]:
                    open_stack.pop()
                    star_stack.pop()
                else:
                    return False
            else:
                return False
        return True



        