class Solution(object):
    def largestInteger(self, n, s):
        """
        :type n: int
        :type s: int
        :rtype: int
        """
        if s>9*n:
            return -1
        ans=""
        count=0
        while s>0:
            maxi=min(9,s)
            ans+=str(maxi)
            s-=maxi
            count+=1
        while count<n:
            ans+="0"
            count+=1
        return int(ans)
            
        