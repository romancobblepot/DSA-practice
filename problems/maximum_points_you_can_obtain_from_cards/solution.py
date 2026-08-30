class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        l=0
        n=len(cardPoints)
        r=n-k-1
        score=0
        for i in range(r+1):
            score+=cardPoints[i]
        min_score=score
        while 0<=r<n-1:
            score-=cardPoints[l]
            l+=1
            r+=1
            score+=cardPoints[r]
            min_score=min(min_score,score)
        return sum(cardPoints)-min_score
            




        