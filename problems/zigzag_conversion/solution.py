class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s
        arr=[['#']*len(s) for _ in range(numRows)]
        i=0
        j=0
        goingDown=True
        for idx in range(len(s)):
            arr[i][j]=s[idx]
            if i == numRows - 1:
                goingDown = False
            elif i == 0:
                goingDown = True
            if goingDown:
                i+=1
            else:
                i-=1
                j+=1
        ans=""
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if arr[i][j]!="#":
                    ans+=arr[i][j]
        return ans



        