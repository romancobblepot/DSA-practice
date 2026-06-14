class Solution(object):
    def maxPerformance(self, n, speed, efficiency, k):
        """
        :type n: int
        :type speed: List[int]
        :type efficiency: List[int]
        :type k: int
        :rtype: int
        """
        max_score=float('-inf')
        pairs = sorted(zip(efficiency, speed), reverse=True)
        heap=[]
        qsum=0
        for eff,speed in pairs:
            heapq.heappush(heap,speed)
            qsum+=speed
            if len(heap)>k:
                qsum-=heapq.heappop(heap)
            if len(heap)<=k:
                max_score=max(max_score,qsum*eff)
        return max_score%(10**9 + 7)

        

        