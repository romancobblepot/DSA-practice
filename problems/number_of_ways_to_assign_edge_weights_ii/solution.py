class Solution(object):
    def assignEdgeWeights(self, edges, queries):
        """
        :type edges: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n=len(edges)+1
        adj=[[] for _ in range(n+1)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        LOG=(n).bit_length()
        up=[[-1]*LOG for _ in range(n+1)]
        depth=[0]*(n+1)
        def dfs(node,parent):
            up[node][0]=parent
            for j in range(1,LOG):
                if up[node][j-1]!=-1:
                    up[node][j]=up[up[node][j-1]][j-1]
            for it in adj[node]:
                if it!=parent:
                    depth[it]=(depth[node]+1)
                    dfs(it,node)
        dfs(1,-1)
        def lca(u,v):
            if depth[u]<depth[v]:
                u,v=v,u
            diff=depth[u]-depth[v]
            for j in range(LOG):
                if diff & (1<<j):
                    u=up[u][j]
            if u==v:
                return u
            for j in range(LOG-1,-1,-1):
                if up[u][j]!=up[v][j]:
                    u=up[u][j]
                    v=up[v][j]
            return up[u][0]
        ans=[]
        for u,v in queries:
            l=lca(u,v)
            d=(depth[u]+depth[v]-2*depth[l])
            if d==0:
                ans.append(0)
            else:
                ans.append(pow(2,d-1,10**9+7))
        return ans

        