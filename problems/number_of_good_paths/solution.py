class DisjointSet(object):
    def __init__(self,n):
        self.parent=list(range(n+1))
        self.size=[1]*n
    def UParent(self,node):
        if self.parent[node]==node:
            return node
        self.parent[node]=self.UParent(self.parent[node])
        return self.parent[node]
    def UnionByValue(self,u,v):
        ulp_u=self.UParent(u)
        ulp_v=self.UParent(v)
        if ulp_u==ulp_v:
            return 
        if self.size[ulp_u]<self.size[ulp_v]:
            self.size[ulp_v]+=self.size[ulp_u]
            self.parent[ulp_u]=ulp_v
        else:
            self.size[ulp_u]+=self.size[ulp_v]
            self.parent[ulp_v]=ulp_u
class Solution(object):
    def numberOfGoodPaths(self, vals, edges):
        """
        :type vals: List[int]
        :type edges: List[List[int]]
        :rtype: int
        """
        n=len(vals)
        ds=DisjointSet(n)
        adj=[[] for _ in range(n)]
        value_nodes=defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        for i,value in enumerate(vals):
            value_nodes[value].append(i)
        total=n
        for j in sorted(value_nodes.keys()):
            for u in value_nodes[j]:
                for v in adj[u]:
                    if vals[v]<=vals[u]:
                        ds.UnionByValue(u,v)
            root_count=defaultdict(int)
            for u in value_nodes[j]:
                root_count[ds.UParent(u)]+=1
            for k,count in root_count.items():
                if count>1:
                    total+=(count*(count-1)//2)
        return total








        