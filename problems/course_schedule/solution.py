from collections import deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adj=[[] for _ in range(numCourses)]
        for u,v in prerequisites:
            adj[v].append(u)
        def topoSort(adj,V):
            indegree=[0]*V
            ans=[]
            q=deque()
            for i in range(V):
                for u in adj[i]:
                    indegree[u]+=1
            for i in range(V):
                if indegree[i]==0:
                    q.append(i)
            while q:
                node=q.popleft()
                ans.append(node)
                for nodes in adj[node]:
                    indegree[nodes]-=1
                    if indegree[nodes]==0:
                        q.append(nodes)
            return ans  
        arr=topoSort(adj,numCourses)   
        if len(arr)<numCourses:
            return False
        return True   