class Solution(object):
    def remainingMethods(self, n, k, invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """
        visited=set()
        adj=[[] for _ in range(n)]
        indegree=[0]*n
        for u,v in invocations:
            adj[u].append(v)
            indegree[v]+=1
        q=deque()
        q.append(k)
        bug=set([k])
        while q:
            node=q.popleft()
            for it in adj[node]:
                if (node,it) not in visited:
                    indegree[it]-=1
                    bug.add(it)
                    q.append(it)
                    visited.add((node,it))
        for node in bug:
            if indegree[node]!=0:
                return list(range(n))
        ans=[]
        for i in range(n):
            if i not in bug:
                ans.append(i)
        return ans
        





        