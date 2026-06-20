from math import ceil
class Solution(object):
    def minLights(self, lights):
        """
        :type lights: List[int]
        :rtype: int
        """
        def merge(intervals):
            prev_start=intervals[0][0]
            prev_end=intervals[0][1]
            ans=[]
            for i in range(1,len(intervals)):
                if intervals[i][0]>prev_end:
                    ans.append([prev_start,prev_end])
                    prev_start=intervals[i][0]
                prev_end=max(intervals[i][1],prev_end)
            ans.append([prev_start,prev_end])
            return ans                  
        n=len(lights)
        covered=[]
        for i in range(len(lights)):
            power=lights[i]
            if power>0:
                covered.append((max(0,i-power),min(n-1,i+power)))
        covered.sort()
        ans=[]
        if len(covered):
            ans=merge(covered)
        ans.sort()
        total=0
        for i in range(len(ans)-1):
            curr_end=ans[i][1]
            next_start=ans[i+1][0]
            total+=(next_start-curr_end+1)//3
        if ans:
            total+=(ans[0][0]+2)//3 + (n+1-ans[-1][1])//3
        else:
            total+=(n+2)//3
        return total
            

            
        
        
        
        