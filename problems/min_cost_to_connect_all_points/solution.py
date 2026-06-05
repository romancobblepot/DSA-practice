class DisjointSet(object):
    def __init__(self,n):
        self.size=[1]*(n)
        self.parent=list(range(n+1))
    def Uparent(self,node):
        if node==self.parent[node]:
            return node
        self.parent[node]=self.Uparent(self.parent[node])
        return self.parent[node]
    def UnionbySize(self,u,v):
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
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        mapp=defaultdict(list)
        for i in range(len(points)):
            mapp[i]=points[i]
        ds=DisjointSet(len(points))
        edges=[]
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                distance=abs(points[j][0]-points[i][0])+abs(points[j][1]-points[i][1])
                edges.append((distance,i,j))
        edges.sort()
        sum=0
        for wt,u,v in edges:
            if ds.Uparent(u)!=ds.Uparent(v):
                sum+=wt
                ds.UnionbySize(u,v)
        return sum
        