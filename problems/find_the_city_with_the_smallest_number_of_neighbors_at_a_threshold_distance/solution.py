class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        adj=[[] for _ in range(n)]
        for u,v,w in edges:
            adj[u].append((v,w))
            adj[v].append((u,w))
        distance=[[float('inf')]*(n) for _ in range(n)]
        minCount=float('inf')
        ans=-1
        for i in range(n):
            q=[]
            heapq.heappush(q,(0,i))
            distance[i][i]=0
            while q:
                length,node=heapq.heappop(q)
                if length>=distanceThreshold:
                    continue
                for it,wt in adj[node]:
                    if length+wt<distance[i][it]:
                        distance[i][it]=length+wt
                        heapq.heappush(q,(distance[i][it],it))
            count=0
            for j in range(len(distance)):
                if j!=i and distance[i][j]<=distanceThreshold:
                    count+=1
            if count<=minCount:
                minCount=count
                ans=i
        return ans
        