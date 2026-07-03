class Solution(object):
    def findMaxPathScore(self, edges, online, k):
        """
        :type edges: List[List[int]]
        :type online: List[bool]
        :type k: int
        :rtype: int
        """
        n=len(online)
        adj=[[] for _ in range(n)]
        l,r=float('inf'),0
        for u,v,w in edges:
            l=min(l,w)
            r=max(r,w)
            adj[u].append((v,w))
        def check(limit):
            q=[]
            heapq.heappush(q,(0,0))
            min_distance=[float('inf') for _ in range(n)]
            min_distance[0]=0
            while q:
                cost_remaining,node=heapq.heappop(q)
                if node==n-1:
                    return True
                if cost_remaining!=min_distance[node]:
                    continue
                for it,w in adj[node]:
                    if cost_remaining+w>k or w<limit:
                        continue
                    next_cost=cost_remaining+w
                    if online[it]:
                        if next_cost<min_distance[it]:
                            min_distance[it]=next_cost
                            heapq.heappush(q,(min_distance[it],it))
            return False
        def bs(l,r):
            low=l
            high=r
            while low<=high:
                mid=low+((high-low)//2)
                if check(mid):
                    low=mid+1
                else:
                    high=mid-1
            return high
        if bs(l,r)<l:
            return -1
        res=bs(l,r)
        return res
        
        
        
            

                




            

                


        