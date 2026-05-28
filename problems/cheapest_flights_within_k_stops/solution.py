class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        amount=[[float('inf')]*(k+2) for _ in range(n)]
        q=deque()
        q.append((0,0,src))
        if src==dst:
            return 0
        adj=[[] for _ in range(n)]
        for i in range(len(flights)):
            sorc,dest,cost=flights[i]
            adj[sorc].append((dest,cost))
        amount[src][0]=0
        while q:
            cost,edges,node=q.popleft()
            if cost>amount[node][edges]:
                continue
            edges+=1
            for it,co in adj[node]:
                if edges<k+2:
                    if cost+co<amount[it][edges]: 
                        amount[it][edges]=cost+co
                        q.append((cost+co,edges,it))
        cheapest=min(amount[dst])
        if cheapest==float('inf'):
            return -1
        return cheapest
        