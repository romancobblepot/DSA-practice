class Solution(object):
    def stoneGameVI(self, aliceValues, bobValues):
        """
        :type aliceValues: List[int]
        :type bobValues: List[int]
        :rtype: int
        """
        combined_arr=[0]*len(aliceValues)
        for i in range(len(aliceValues)):
            combined_arr[i]=aliceValues[i]+bobValues[i]
        sorted_pairs = sorted(zip(combined_arr,aliceValues, bobValues),reverse=True)
        combined_sort,sorted_scores, sorted_names = zip(*sorted_pairs)
        sorted_bob = list(sorted_names)
        sorted_alice = list(sorted_scores)
        score=0
        for i in range(len(aliceValues)):
            if i%2==0:
                score+=sorted_alice[i]
            else:
                score-=sorted_bob[i]
        if score==0:
            return score
        return 1 if score>0 else -1



        