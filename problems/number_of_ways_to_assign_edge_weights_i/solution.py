class Solution(object):
    def assignEdgeWeights(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        E=len(edges)
        V=E+1
        adj=[[] for _ in range(V+1)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        q=deque()
        visited=[False]*(V+1)
        q.append((1,0))
        visited[1]=True
        max_depth=0
        while q:
            node,depth=q.popleft()
            max_depth=max(depth,max_depth)
            for it in adj[node]:
                if not visited[it]:
                    q.append((it,depth+1))   
                    visited[it]=True     
        return (2**(max_depth-1))%(10**9 + 7)


        
        


        