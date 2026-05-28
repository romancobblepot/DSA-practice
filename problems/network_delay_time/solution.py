import heapq
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        adj=[[] for _ in range(n)]
        for i in range(len(times)):
            src,dst,time=times[i]
            adj[src-1].append((dst-1,time))
        q=[]
        heapq.heappush(q,(0,k-1))
        min_time=[float('inf') for _ in range(n)]
        min_time[k-1]=0
        while q:
            current_time,node=heapq.heappop(q)
            if current_time>min_time[node]:
                continue
            for it,co in adj[node]:
                if co+current_time<min_time[it]:
                    min_time[it]=co+current_time
                    heapq.heappush(q,(co+current_time,it))
        maximum_time=max(min_time)
        return -1 if maximum_time==float('inf') else  maximum_time
        