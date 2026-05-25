class Solution(object):
    def NSE(self,arr):
        n=len(arr)
        nse=[n]*n
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            if stack:
                nse[i]=stack[-1]
            stack.append(i)
        return nse        
    def PSEE(self,arr):
        n=len(arr)
        psee=[-1]*n
        stack=[]
        for i in range(n):
            while stack and arr[stack[-1]]>arr[i]:
                stack.pop()
            if stack:
                psee[i]=stack[-1]
            stack.append(i)
        return psee            
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n=len(arr)
        nse=self.NSE(arr)
        psee=self.PSEE(arr)
        sum=0
        for i in range(n):
            right_sub=nse[i]-i
            left_sub=i-psee[i]
            sum+=((left_sub*right_sub*arr[i]))
            sum=sum%(10**9 + 7)
        return sum

        