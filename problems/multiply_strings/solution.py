class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n=len(num1)
        m=len(num2)
        int1=0
        int2=0
        i=0
        j=0
        while i<n:
            digit=ord(num1[i])-ord('0')
            int1+=(digit*10**(n-1-i))
            i+=1
        while j<m:
            digit=ord(num2[j])-ord('0')
            int2+=(digit*10**(m-1-j))
            j+=1   
        int3=int1*int2
        ans=[]
        if int3>0:
            while int3>0:
                rem=int3%10
                ans.append(rem)
                int3=int3//10
            ans.reverse()
        else:
            ans.append(0)
        string=""
        for i in range(len(ans)):
            character=chr(ans[i]+ord('0'))
            string+=character
        return string
        





        