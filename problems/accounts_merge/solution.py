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
class Solution:
    def accountsMerge(self, accounts):
        email_map={}
        ds=DisjointSet(len(accounts))
        for i in range(len(accounts)):
            for j in range(1,len(accounts[i])):
                if accounts[i][j] not in email_map:
                    email_map[accounts[i][j]]=i
                else:
                    ds.UnionBySize(i,email_map[accounts[i][j]])
        parents_to_email=defaultdict(set)
        for i in range(len(accounts)):
            root=ds.UParent(i)
            for j in range(1,len(accounts[i])):
                parents_to_email[root].add(accounts[i][j])
        res=[]
        for root in parents_to_email:
            name=accounts[root][0]
            ind=[name]+list(sorted(parents_to_email[root]))
            res.append(ind)
        return res

                




                


        