class Solution(object):
    def minScore(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        adj=[[] for _ in range(n+1)]
        for u,v,d in roads:
            adj[u].append((v,d))
            adj[v].append((u,d))
        def bfs(True):
            q=deque()
            q.append(1)
            res=float('inf')
            visited={}
            visited[1]=1
            while q:
                node=q.popleft()
                for it,d in adj[node]:
                    res=min(res,d)
                    if it not in visited:
                        q.append(it)
                        visited[it]=1
            return res
        return bfs(True)

        
        