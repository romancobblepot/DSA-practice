class Solution(object):
    def finishTime(self, n, edges, baseTime):
        """
        :type n: int
        :type edges: List[List[int]]
        :type baseTime: List[int]
        :rtype: int
        """
        adj=[[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
        def dfs(root):
            latest=0
            earliest=float('inf')
            if not adj[root]:
                return baseTime[root]
            for it in adj[root]:
                t=dfs(it)
                latest=max(latest,t)
                earliest=min(earliest,t)
            ownDuration=latest-earliest+baseTime[root]
            return latest+ownDuration
        return dfs(0)
                
            
            