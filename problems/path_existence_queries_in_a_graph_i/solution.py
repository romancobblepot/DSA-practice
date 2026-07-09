class DisJointSet(object):
    def __init__(self,n):
        self.parent=list(range(n+1))
        self.size=[1]*n
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
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        ans=[]
        ds=DisJointSet(n)
        for i in range(n-1):
            if abs(nums[i]-nums[i+1])<=maxDiff:
                if ds.parent[i]!=ds.parent[i+1]:
                    ds.UnionBySize(i,i+1)
        for l,r in queries:
            if ds.parent[l]==ds.parent[r]:
                ans.append(True)
            else:
                ans.append(False)
        return ans




        