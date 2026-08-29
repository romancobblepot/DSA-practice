from collections import defaultdict
class DisjointSet:
    def __init__(self,n):
        self.size=[1]*n
        self.parent=[0]*n
        for i in range(n):
            self.parent[i]=i
    def UParent(self,node):
        if node==self.parent[node]:
            return node
        self.parent[node]=self.UParent(self.parent[node])
        return self.parent[node]
    def UnionBySize(self,u,v):
        p_u=self.UParent(u)
        p_v=self.UParent(v)
        if p_u==p_v: return
        if self.size[p_u]<self.size[p_v]:
            self.size[p_v]+=self.size[p_u]
            self.parent[p_u]=p_v
        else:
            self.size[p_u]+=self.size[p_v]
            self.parent[p_v]=p_u
class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: List[int]
        """
        ds=DisjointSet(len(nums))
        arr = sorted((num, i) for i, num in enumerate(nums))
        for i in range(1,len(nums)):
            if abs(arr[i][0]-arr[i-1][0])<=limit:
                if ds.parent[arr[i][1]]!=ds.parent[arr[i-1][1]]:
                    ds.UnionBySize(arr[i-1][1],arr[i][1])
        group=ds.parent
        groups = defaultdict(list) 
        for i, g in enumerate(group):
            groups[g].append(i)
        for indices in groups.values():
            values = sorted(nums[i] for i in indices)
            for i, val in zip(indices, values):
                nums[i]=val
        return nums

        