class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x:x[0])
        prev_end=intervals[0][1]
        prev_start=intervals[0][0]
        count=1
        for start,end in intervals:
            if start>=prev_end:
                count+=1
                prev_start=start
            elif start>prev_start and end>prev_end:
                count+=1
                prev_start=start
            prev_end=max(prev_end,end)
        return count
        