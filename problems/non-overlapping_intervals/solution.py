class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x:(x[1],x[0]))
        def mergeIntervals(intervals):
            count=0
            prev_end=intervals[0][1]
            for i in range(1,len(intervals)):
                if intervals[i][0]<prev_end:
                    count+=1
                else:
                    prev_end=intervals[i][1]                            
            return count
        return mergeIntervals(intervals)
                    
                        