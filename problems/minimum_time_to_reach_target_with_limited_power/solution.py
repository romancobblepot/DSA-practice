class Solution(object):
    def minTimeMaxPower(self, n, edges, power, cost, source, target):
        """
        :type n: int
        :type edges: List[List[int]]
        :type power: int
        :type cost: List[int]
        :type source: int
        :type target: int
        :rtype: List[int]
        """
        adj=[[] for _ in range(n)]
        for u,v,w in edges:
            adj[u].append((v,w))
        min_time_max_power={}
        min_time_max_power[(power,source)]=0
        visited={}
        visited[(power,source)]=1
        q=[]
        heapq.heappush(q,(0,-power,source))
        while q:
            time,power_remaining,node=heapq.heappop(q)
            power_remaining*=-1
            if node==target:
                return [time,power_remaining]
            if power_remaining<cost[node]:
                continue
            for it,w in adj[node]:
                power_next=power_remaining-cost[node]
                time_next=time+w
                if power_next<0:
                    continue
                if (power_next,it) not in visited:
                        min_time_max_power[(power_next,it)]=time_next
                        heapq.heappush(q,(min_time_max_power[(power_next,it)],-power_next,it))
                        visited[(power_next,it)]=1
                else:
                    if time_next<min_time_max_power.get((power_next,it),float('inf')):
                        min_time_max_power[(power_next,it)]=time_next
                        heapq.heappush(q,(min_time_max_power[(power_next,it)],-power_next,it))                        
        return [-1,-1]
        
                



        