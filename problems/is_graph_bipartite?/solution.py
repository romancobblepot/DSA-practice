class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        V=len(graph)
        visited=[False]*V
        color=[False]*V
        adj=graph
        def bfs(i):
            q=deque([i])
            visited[i]=True
            color[i]=True
            while q:
                node=q.popleft()
                for nodes in adj[node]:
                    if not visited[nodes]:
                        q.append(nodes)
                        visited[nodes]=True
                        color[nodes]= not color[node]
                    else:
                        if color[node]==color[nodes]:
                            return False
            return True
        for i in range(V):
            if not visited[i]:
                if not bfs(i):
                    return False
        return True   