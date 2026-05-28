class Solution(object):
    def countPaths(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        adj=[[] for _ in range(n)]
        q=[]
        for i in range(len(roads)):
            src,dst,time=roads[i]
            adj[src].append((dst,time))
            adj[dst].append((src,time))
        min_time=[float('inf') for _ in range(n)]
        min_time[0]=0
        ways=[0 for _ in range(n)]
        ways[0]=1
        heapq.heappush(q,(0,0))
        while q:
            current_time,node=heapq.heappop(q)

            for it,time in adj[node]:
                if time+current_time<min_time[it]:
                    min_time[it]=time+current_time
                    heapq.heappush(q,(min_time[it],it))
                    ways[it]=ways[node]
                elif time+current_time==min_time[it]:
                    ways[it]+=ways[node]
        return ways[n-1]%(10**9 + 7)
        