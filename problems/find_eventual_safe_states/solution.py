class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        def toposort(V,adj,outdegree,indegree):
            for i in range(V):
                for it in adj[i]:
                    outdegree[i]+=1
                    indegree[it]+=1
        V=len(graph)
        outdegree=[0]*V
        indegree=[0]*V 
        toposort(V,graph,outdegree,indegree)
        def dfs(i,visited,safe):
            if safe[i]!=-1:
                return safe[i]
            if outdegree[i]==0:
                visited[i]=False
                safe[i]=1
                return 1
            visited[i]=True
            for it in graph[i]:
                if visited[it]:
                    visited[i]=False
                    safe[i]=0
                    return 0
                elif not visited[it]:
                    res=dfs(it,visited,safe)
                if res==0:
                    safe[i]=0
                    visited[i]=False
                    return 0
            visited[i]=False
            safe[i]=1
            return 1
        ans=[]
        safe=[-1]*V
        visited=[False]*V
        for i in range(V):
            if dfs(i,visited,safe)==1:
                ans.append(i)
        return ans
        