# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        adj=defaultdict(list)
        def dfs(root,adj):
            if not root:
                return 
            if root.left:
                adj[root.val].append(root.left.val)
                adj[root.left.val].append(root.val)
            if root.right:
                adj[root.val].append(root.right.val)
                adj[root.right.val].append(root.val)
            dfs(root.left,adj)
            dfs(root.right,adj)
        dfs(root,adj)
        q=deque()
        q.append((target.val,0))
        ans=[]
        visited=set()
        visited.add(target.val)
        while q:
            node,distance=q.popleft()
            if distance==k:
                ans.append(node)
            if distance>k:
                continue
            for it in adj[node]:
                if it not in  visited:
                    q.append((it,distance+1))
                    visited.add(it)
        return ans


