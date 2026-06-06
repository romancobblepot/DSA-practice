from collections import defaultdict
class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        mapp=defaultdict(list)
        for i in range(len(s)):
            if s[i] not in mapp:
                mapp[s[i]].append(i)
                mapp[s[i]].append(i)
            else:
                mapp[s[i]][1]=i
        intervals=list(mapp.values())
        intervals.sort()
        arr=[]
        prev_start=intervals[0][0]
        prev_end=intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0]>prev_end:
                arr.append([prev_start,prev_end])
                prev_start=intervals[i][0]
            prev_end=max(prev_end,intervals[i][1])
        arr.append([prev_start,prev_end])
        ans=[]
        for i in range(len(arr)):
            ans.append(arr[i][1]-arr[i][0]+1)
        return ans



        
        