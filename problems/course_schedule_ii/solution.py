class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        N=numCourses
        arr=prerequisites
        adj=[[] for _ in range(N)]
        for u,v in arr:
            adj[v].append(u)
        def toposort(N,adj):
            indegree=[0]*N
            ans=[]
            q=deque()
            for i in range(N):
                for it in adj[i]:
                    indegree[it]+=1
            for i in range(N):
                if indegree[i]==0:
                    q.append(i)
            while q:
                node=q.popleft()
                ans.append(node)
                for it in adj[node]:
                    indegree[it]-=1
                    if indegree[it]==0:
                        q.append(it)
            return ans
        ans=toposort(N,adj)
        if len(ans)<N:
            return []
        return ans
        