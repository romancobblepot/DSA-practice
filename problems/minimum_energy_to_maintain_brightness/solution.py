class Solution(object):
    def minEnergy(self, n, brightness, intervals):
        """
        :type n: int
        :type brightness: int
        :type intervals: List[List[int]]
        :rtype: int
        """
        def mergeIntervals(intervals):
            intervals.sort()
            prev_start=intervals[0][0]
            prev_end=intervals[0][1]
            arr=[]
            for i in range(1,len(intervals)):
                if intervals[i][0]>prev_end:
                    arr.append([prev_start,prev_end])
                    prev_start=intervals[i][0]
                prev_end=max(prev_end,intervals[i][1])
            arr.append([prev_start,prev_end])
            return arr     
        merged_intervals=mergeIntervals(intervals)
        if brightness%3==0:
            lamps=brightness//3
        else:
            lamps=brightness//3 + 1
        sum=0
        for start,end in merged_intervals:
            sum+=lamps*(end-start+1)
        return sum
            
            
        
        
        
        