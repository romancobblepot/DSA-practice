class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        intervals.sort()
        prev_start=intervals[0][0]
        prev_end=intervals[0][1]
        arr=[]
        for i in range(len(intervals)):
            if intervals[i][0]>prev_end:
                arr.append([prev_start,prev_end])
                prev_start=intervals[i][0]
            prev_end=max(prev_end,intervals[i][1])
        arr.append([prev_start,prev_end])
        return arr

        