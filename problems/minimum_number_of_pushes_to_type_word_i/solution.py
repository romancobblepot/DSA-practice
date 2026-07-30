class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        n=len(word)
        total=0
        i=1
        while n>0:
            if n>=8:
                total+=(i*8)
                n-=8
            else:
                total+=(i*n)
                n-=n
            i+=1
        return total
        