class Solution(object):
    def shortestPath(self, n, edges, labels, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :type k: int
        :rtype: int
        """
        adj=[[] for _ in range(n)]
        for u,v,w in edges:
            adj[u].append((v,w))
        q=[]
        heapq.heappush(q,(0,0,k-1,labels[0]))
        distance={}
        distance[(0,labels[0],k-1)]=0
        while q:
            total_wt,node,count,character=heapq.heappop(q)
            if node==n-1:
                return total_wt
            for it,w in adj[node]:
                if labels[it]==character and count>0:
                    if w+total_wt<distance.get((it,labels[it],count-1),float('inf')):
                        distance[(it,labels[it],count-1)]=w+total_wt
                        heapq.heappush(q,(w+total_wt,it,count-1,labels[it]))
                elif labels[it]!=character:
                    if w+total_wt<distance.get((it,labels[it],k-1),float('inf')):
                        distance[(it,labels[it],k-1)]=w+total_wt
                        heapq.heappush(q,(w+total_wt,it,k-1,labels[it]))
        return -1
                        
                
            
        
        