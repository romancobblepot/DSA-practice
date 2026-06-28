class Solution(object):
    def filterOccupiedIntervals(self, occupiedIntervals, freeStart, freeEnd):
        """
        :type occupiedIntervals: List[List[int]]
        :type freeStart: int
        :type freeEnd: int
        :rtype: List[List[int]]
        """
        def mergeIntervals(nums):
            nums.sort(key=lambda x:x[0])
            prev_start=nums[0][0]
            prev_end=nums[0][1]
            arr=[]
            for i in range(1,len(nums)):
                if nums[i][0]>prev_end+1:
                    arr.append([prev_start,prev_end])
                    prev_start=nums[i][0]
                prev_end=max(prev_end,nums[i][1])
            arr.append([prev_start,prev_end])
            return arr
        merged_intervals=mergeIntervals(occupiedIntervals)
        free_interval=[freeStart,freeEnd]
        def non_overlapping(nums,free_start,free_end):
            nums.sort()
            arr=[]
            for start, end in nums:
                if end < free_start:
                    arr.append([start, end])
                elif start > free_end:
                    arr.append([start, end])
                else:
                    if start < free_start:
                        arr.append([start, free_start-1])
                    if end > free_end:
                        arr.append([free_end+1, end])
                
            return arr
        return non_overlapping(merged_intervals,freeStart,freeEnd)
            
        
                    
        