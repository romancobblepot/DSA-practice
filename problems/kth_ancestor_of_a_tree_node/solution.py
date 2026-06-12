class TreeAncestor(object):

    def __init__(self, n, parent):
        """
        :type n: int
        :type parent: List[int]
        """
        adj=[[] for _ in range(n)]
        LOG=(n).bit_length()
        self.up=[[-1]*LOG for _ in range(n)]
        self.up[0][0]=-1
        for i in range(1,len(parent)):
            adj[i].append(parent[i])
            adj[parent[i]].append(i)
            self.up[i][0]=parent[i]
        visited=[False]*n
        visited[0]=True
        q=deque()
        q.append((0,-1))
        while q:
            node,parent=q.popleft()
            for j in range(1,LOG):
                if self.up[node][j-1]!=-1:
                    self.up[node][j]=self.up[self.up[node][j-1]][j-1]
            for it in adj[node]:
                if not visited[it]:
                    q.append((it,node))
                    visited[it]=True      
    def getKthAncestor(self, node, k):
        """
        :type node: int
        :type k: int
        :rtype: int
        """
        j=0
        while k and node!=-1:
            if k & 1:
                node=self.up[node][j]
            k>>=1
            j+=1
        return node


        


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)