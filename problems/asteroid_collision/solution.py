class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack=[]
        n=len(asteroids)
        for i in range(n-1,-1,-1):
            if asteroids[i]>0:
                while stack and stack[-1]<0 and abs(asteroids[i])>abs(stack[-1]):
                    stack.pop()
                if stack and stack[-1]<0 and abs(asteroids[i])==abs(stack[-1]):
                    stack.pop()
                    continue
            else:
                stack.append(asteroids[i])
            if not stack or stack[-1]>0:
                stack.append(asteroids[i])
        stack.reverse()
        return stack
        