class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s
        arr=[[] for _ in range(numRows)]
        i=0
        d=1
        for idx in range(len(s)):
            arr[i].append(s[idx])
            if i == numRows - 1:
                d=-1
            elif i == 0:
                d=1
            i+=d
        ans=""
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                ans+=arr[i][j]
        return ans



        