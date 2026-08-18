from collections import Counter
class Solution(object):
    def stoneGameIX(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        if len(stones)==1:
            return False
        for i in range(len(stones)):
            stones[i]=stones[i]%3
        mapp1=Counter(stones)
        if mapp1[0]%2==0:
            if mapp1[1]>=1 and mapp1[1]<=mapp1[2]:
                return True
            elif mapp1[2]>=1 and mapp1[1]>=mapp1[2]:
                return True
            return False
        else:
            if mapp1[1]+2<mapp1[2] or  mapp1[1]>mapp1[2]+2:
                return True
            return False


        
         



        