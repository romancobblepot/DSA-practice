class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        arr=[]
        prev_end=intervals[0][1]
        prev_start=intervals[0][0]
        for i in range(1,len(intervals)):
            if intervals[i][0]>prev_end:
                arr.append([prev_start,prev_end])
                prev_start=intervals[i][0]
            prev_end=max(intervals[i][1],prev_end)
        arr.append([prev_start,prev_end])
        return arr

            
        