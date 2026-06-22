class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        mapp1={}
        for t in text:
            mapp1[t]=mapp1.get(t,0)+1
        word="balloon"
        mapp2={}
        for w in word:
            mapp2[w]=mapp2.get(w,0)+1
        min_freq=float('inf')
        for key in mapp2:
            if key not in mapp1:
                return 0
            if mapp1[key]<mapp2[key]:
                return 0
            min_freq=min(min_freq,(mapp1[key]-mapp2[key])//mapp2[key] +1)
        return min_freq
            





        