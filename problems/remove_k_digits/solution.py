class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack=[]
        cnt=0
        n=len(num)
        if k==n:
            return "0"
        for i in range(n):
            while stack and (stack[-1]>num[i]) and cnt<k:
                stack.pop()
                cnt+=1
            stack.append(num[i])
        arr=stack[:n-k]
        while len(arr)>1 and arr[0]=="0":
            arr.pop(0)
        return ''.join(arr)