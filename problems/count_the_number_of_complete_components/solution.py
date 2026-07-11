class DisJointSet(object):
    def __init__(self,n):
        self.size=[1]*n
        self.parent=list(range(n+1))
    def Uparent(self,node):
        if self.parent[node]==node:
            return node
        self.parent[node]=self.Uparent(self.parent[node])
        return self.parent[node]
    def UnionBySize(self,u,v):
        ulp_u=self.Uparent(u)
        ulp_v=self.Uparent(v)
        if ulp_u==ulp_v:
            return 
        if self.size[ulp_u]<self.size[ulp_v]:
            self.parent[ulp_u]=ulp_v
            self.size[ulp_v]+=self.size[ulp_u]
        else:
            self.parent[ulp_v]=ulp_u
            self.size[ulp_u]+=self.size[ulp_v]
class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        ds=DisJointSet(n)
        def bfs(i):
                visited={}
                q=deque()
                q.append((i,-1))
                visited[(i,-1)]=1
                visited[(-1,i)]=1
                count=0
                while q:
                    node,parent=q.popleft()
                    for it in adj[node]:
                        if (node,it) not in visited or (it,node) not in visited:
                            visited[(node,it)]=1
                            visited[(it,node)]=1
                            count+=1
                            q.append((it,node))
                return count
        for u,v in edges:
            if ds.parent[u]!=ds.parent[v]:
                ds.UnionBySize(u,v)
        adj=[[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        total=0
        for i in range(n):
            if ds.parent[i]==i:
                count=bfs(i)
                if count==(ds.size[i]*(ds.size[i]-1)/2):
                    total+=1
        return total






        